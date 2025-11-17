# I took this from: https://github.com/ManimCommunity/manim/discussions/4261#discussioncomment-14765744

from manim import *
import cv2  # requires: pip install opencv-python
from PIL import Image, ImageOps
from dataclasses import dataclass
import numpy as np

@dataclass
class VideoStatus:
    time: float = 0
    videoObject: cv2.VideoCapture = None
    
    def __deepcopy__(self, memo):
        return self

class VideoMobject(ImageMobject):
    '''
    Custom VideoMobject for Manim using OpenCV
    
    Parameters
    ----------
    filename : str
        Path to the video file
    imageops : function (optional)
        PIL.ImageOps operation (e.g., PIL.ImageOps.mirror)
    speed : float (optional)
        Speed multiplier for playback (default: 1.0)
    loop : bool (optional)
        Whether to loop the video (default: False)
    '''
    def __init__(self, filename=None, imageops=None, speed=1.0, loop=False, **kwargs):
        self.filename = filename
        self.imageops = imageops
        self.speed = speed
        self.loop = loop
        self._id = id(self)
        
        # Initialize video capture
        self.status = VideoStatus()
        self.status.videoObject = cv2.VideoCapture(filename)
        
        # Get video properties
        self.fps = self.status.videoObject.get(cv2.CAP_PROP_FPS)
        self.frame_count = int(self.status.videoObject.get(cv2.CAP_PROP_FRAME_COUNT))
        self.duration = self.frame_count / self.fps if self.fps > 0 else 0
        
        print(f"Video loaded: {filename}")
        print(f"FPS: {self.fps}, Frames: {self.frame_count}, Duration: {self.duration:.2f}s")
        
        # Start from frame 0
        self.status.videoObject.set(cv2.CAP_PROP_POS_FRAMES, 0)
        
        # Read first frame
        ret, frame = self.status.videoObject.read()
        
        if ret:
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            img = Image.fromarray(frame)
            if imageops != None:
                img = imageops(img)
        else:
            # Fallback image if video fails to load
            print("WARNING: Could not read video file!")
            img = Image.fromarray(np.uint8([[63, 0, 0, 0],
                                            [0, 127, 0, 0],
                                            [0, 0, 191, 0],
                                            [0, 0, 0, 255]]))
        
        super().__init__(img, **kwargs)
        
        if ret:
            self.add_updater(self.videoUpdater)
    
    def videoUpdater(self, mobj, dt):
        if dt == 0:
            return
        
        status = self.status
        status.time += 1000 * dt * mobj.speed
        
        # Set position in milliseconds
        self.status.videoObject.set(cv2.CAP_PROP_POS_MSEC, status.time)
        ret, frame = self.status.videoObject.read()
        
        # Handle looping
        if not ret and self.loop:
            status.time = 0
            self.status.videoObject.set(cv2.CAP_PROP_POS_MSEC, 0)
            ret, frame = self.status.videoObject.read()
        
        if ret:
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            img = Image.fromarray(frame)
            if mobj.imageops != None:
                img = mobj.imageops(img)
            mobj.pixel_array = change_to_rgba_array(
                np.asarray(img), mobj.pixel_array_dtype
            )
    
    def get_duration(self):
        """Returns video duration in seconds"""
        return self.duration