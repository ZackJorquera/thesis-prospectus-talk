from manim import *
import cv2  # requires: pip install opencv-python
from PIL import Image, ImageOps
from dataclasses import dataclass
import numpy as np
import re


@dataclass
class VideoStatus:
    time: float = 0
    videoObject: cv2.VideoCapture = None
    
    def __deepcopy__(self, memo):
        return self


# I took this from: https://github.com/ManimCommunity/manim/discussions/4261#discussioncomment-14765744
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


# The built-in Title Mobject is centered and I dont want that.
class FancyTitle(VGroup):
    def __init__(self,text,**kwargs):
        for keyword in [r"Quantum Max-Cut", r"Max-Cut", r"Quantum Max-\(d\)-Cut", r"Max-\(d\)-Cut", r"Maximal Entanglement"]:
            text = text.replace(keyword, rf"\algprobm{{{keyword}}}")

        self.title_text = text
        
        # self.title = Text(text, font_size=36)
        self.title = Tex(text, font_size=48)
        self.title.to_corner(UL, buff=0.5)
        self.line = Line(4*LEFT, 6*RIGHT)
        self.line.next_to(self.title, DOWN, aligned_edge=LEFT, buff=0.15).shift(LEFT*0.25)
        super().__init__(self.title,self.line,**kwargs)

    def create(self):
        return LaggedStart(Write(self.title), Create(self.line), lag_ratio=0.5)

    def anim(self,run_time=0.75):
        return LaggedStart(Write(self.title,run_time=run_time/1.5), Create(self.line,run_time=run_time/1.5), lag_ratio=0.5)
    

class LeftRightArrows(VGroup):
    def __init__(self,start=LEFT,end=RIGHT,buff=0.25,tip_length=0.2,**kwargs):
        self.right = Arrow(start=start+UP*(buff/2),end=end+UP*(buff/2),tip_length=tip_length,**kwargs)
        self.left = Arrow(start=end+DOWN*(buff/2),end=start+DOWN*(buff/2),tip_length=tip_length,**kwargs)
        super().__init__(self.right,self.left,**kwargs)

    def create(self):
        return LaggedStart(Create(self.right), Create(self.left), lag_ratio=0.75)


# maybe I should have looked into BulletedList before making this, idk
class Bullets(VGroup):
    def __init__(self, *lines, minipage_size=16, indent_size=0.25, font_size=28, vspace=0.25, bullet_hspace=0.15, align_ref=None, double_space_for_new_sections=False, bullet_aligned_edge=UP, **kwargs):
        super().__init__(**kwargs)
        self._lines = []
        self._indent_level_list = []
        self._next_line = 0
        self._minipage_size = minipage_size
        self._indent_size = indent_size
        self._font_size = font_size
        self._vspace = vspace
        self._bullet_hspace = bullet_hspace
        self._align_ref = align_ref
        self._ds_for_new_sec = double_space_for_new_sections # a new section is a line with about any indentation.
        self._bullet_ae = bullet_aligned_edge

        for line in lines:
            self.add_line(line)

    def add_line(self, line, indent_level=None, bullet=None):
        if isinstance(line, str):
            dots_match = re.match(r'^(\.*)\s+(.*)', line)
            bullet_match = re.match(r'^(\.*)\*\s+(.*)', line)
            circ_match = re.match(r'^(\.*)O\s+(.*)', line)  # we do capital O to avoid conflicting with let_match
            arrow_match = re.match(r'^(\.*)->\s+(.*)', line)
            num_match = re.match(r'^(\.*)([1-9]+)\s+(.*)', line)
            let_match = re.match(r'^(\.*)([a-z]+)\s+(.*)', line)
            textbf_match = re.match(r'^(\.*)\\textbf\{(.*)\}\s+(.*)', line)
            
            space_size = self._bullet_hspace

            if dots_match is not None:
                indent_level = len(dots_match.group(1))
                line_text = dots_match.group(2)
                bullet_mo = None
                bullet_width = 0
                space_size = 0
                basic_bullet = True
            elif circ_match is not None:
                indent_level = len(circ_match.group(1))
                line_text = circ_match.group(2)
                bullet_mo = MathTex(r"\circ", font_size=self._font_size)
                bullet_width = bullet_mo.width
                basic_bullet = True
            elif bullet_match is not None:
                indent_level = len(bullet_match.group(1))
                line_text = bullet_match.group(2)
                bullet_mo = MathTex(r"\bullet", font_size=self._font_size)
                bullet_width = bullet_mo.width
                basic_bullet = True
            elif arrow_match is not None:
                indent_level = len(arrow_match.group(1))
                line_text = arrow_match.group(2)
                bullet_mo = MathTex(r"\rightarrow", font_size=self._font_size)
                bullet_width = bullet_mo.width
                basic_bullet = True
            elif num_match is not None:
                indent_level = len(num_match.group(1))
                num = num_match.group(2)
                line_text = num_match.group(3)
                bullet_mo = MathTex(f"{num}.", font_size=self._font_size)
                bullet_width = bullet_mo.width
                basic_bullet = False
            elif let_match is not None:
                indent_level = len(let_match.group(1))
                let = let_match.group(2)
                line_text = let_match.group(3)
                bullet_mo = MathTex(f"({let})", font_size=self._font_size)
                bullet_width = bullet_mo.width
                basic_bullet = False
            elif textbf_match is not None:
                indent_level = len(textbf_match.group(1))
                bf_text = textbf_match.group(2)
                line_text = textbf_match.group(3)
                bullet_mo = Tex(fr"\textbf{{{bf_text}}}", font_size=self._font_size)
                bullet_width = bullet_mo.width
                basic_bullet = False
            else:
                raise "Something didn't work. Maybe add a space to the start of your string."

            if self._minipage_size is not None:
                render_width = self._minipage_size - indent_level*self._indent_size - bullet_width - space_size
                line_text_mo = Tex(fr"{{{render_width}cm}}\RaggedRight{{{line_text}}}",
                    font_size = self._font_size, tex_environment="minipage")
                if bullet_mo is not None:
                    if basic_bullet:
                        if self._bullet_ae is not None:
                            bullet_and_line = VGroup(bullet_mo,line_text_mo).arrange(RIGHT,buff=self._bullet_hspace,aligned_edge=self._bullet_ae)
                        else:
                            bullet_and_line = VGroup(bullet_mo,line_text_mo).arrange(RIGHT,buff=self._bullet_hspace)
                    else:
                        bullet_and_line = VGroup(bullet_mo,line_text_mo).arrange(RIGHT,buff=self._bullet_hspace,aligned_edge=UP)
                    # TODO: when the bullet is * or -> then arrange aligned_edge=UP gives the wrong spacing.
                    # Really is is wrong all the time, but idk how to tap into latex to get the right spacing
                    # the basic_bullet fix is sort of hacky but it works for most cases
                else:
                    bullet_and_line = line_text_mo
            else:
                raise "I didn't write the code for this part"
                
            if len(self._lines) == 0:
                if self._align_ref is not None:
                    raise "I didn't write the code for this part"
                else:
                    bullet_and_line.to_corner(UL, buff=0.5).shift(DOWN).shift(RIGHT * indent_level * self._indent_size)
            else:
                bullet_and_line.next_to(self._lines[-1], DOWN, aligned_edge=LEFT, buff=self._vspace).shift(RIGHT * (indent_level - self._indent_level_list[-1]) * self._indent_size)
                if self._ds_for_new_sec and indent_level == 0:
                    bullet_and_line.shift(DOWN*self._vspace)

            self._lines.append(bullet_and_line)
            self._indent_level_list.append(indent_level)
            self.add(bullet_and_line)

        elif isinstance(line, Mobject):
            raise "I didn't write the code for this part"
        else:
            raise ValueError("line can only be str or Mobject")
        
    def write_next_line(self, run_time=None):
        if run_time is not None:
            anim = Write(self._lines[self._next_line], run_time=run_time)
        else:
            anim = Write(self._lines[self._next_line])
        self._next_line += 1
        if self._next_line == len(self._lines):
            self._next_line == 0
        return anim
        
    def get_num_lines(self):
        return len(self._lines)
    
    def get_lines(self):
        return self._lines
