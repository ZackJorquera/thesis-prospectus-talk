# Render everything: 
# manim talk.py TitleSlide MaxCutExampleVideo ALittleQuantumVideo ALittleMoreQuantum2Video AnAlgorithmForMEVideo ALittleSOSVideo Overview IntroToCSPs MaxCutExample ALittleQuantum IntroToLHPs QuantumMaxCut WhyCare ALittleMoreQuantum ALittleMoreQuantum2 BabysFirstProofTheStarBound AnAlgorithmForME CSPsOverDistributions ALittleSOS ALittleMoreSOS TheFinalSOSSlide QMdCIntro QMdCStarBound QMdCPartialResults FutureWork Thanks

# Render everything except Overview: 
# manim talk.py TitleSlide IntroToCSPs MaxCutExample ALittleQuantum IntroToLHPs QuantumMaxCut ALittleMoreQuantum ALittleMoreQuantum2 BabysFirstProofTheStarBound AnAlgorithmForME CSPsOverDistributions ALittleSOS ALittleMoreSOS TheFinalSOSSlide QMdCIntro QMdCStarBound QMdCPartialResults FutureWork Thanks

# Only render overview slide
# manim talk.py MaxCutExampleVideo ALittleQuantumVideo ALittleMoreQuantum2Video AnAlgorithmForMEVideo ALittleSOSVideo Overview

# Convert whole slideshow to HTML
# manim-slides convert --use-template template.html --config one_file=true TitleSlide Overview IntroToCSPs MaxCutExample ALittleQuantum IntroToLHPs QuantumMaxCut WhyCare ALittleMoreQuantum ALittleMoreQuantum2 BabysFirstProofTheStarBound AnAlgorithmForME CSPsOverDistributions ALittleSOS ALittleMoreSOS TheFinalSOSSlide QMdCIntro QMdCStarBound QMdCPartialResults FutureWork Thanks talk.html


import manim as mn
from manim import *
from helpermobjects import VideoMobject, Bullets, FancyTitle, LeftRightArrows

from manim_slides import Slide

from manim_themes.manim_theme import apply_theme

import networkx as nx

config.frame_width = 16
config.frame_height = 9

my_template = TexTemplate()
my_template.add_to_preamble(r"\usepackage{jorqu}")
Tex.set_default(tex_template=my_template)
MathTex.set_default(tex_template=my_template)

manim_video_output_dir = r"media\videos\talk\1080p60"


class TitleSlide(Slide):
    def setup(self):
        theme = "Monokai Pro Light" # select a theme from https://iterm2colorschemes.com
        apply_theme(manim_scene=self, theme_name=theme, light_theme=True) # use the theme


    def construct(self):
        title_text = Text("Entanglement Bounds and the Algorithms That Use Them", font_size=36)
        author_text = Text("Thesis Prospectus of: Zackary Jorquera", font_size=28, slant=ITALIC)
        line = Line(LEFT*5,RIGHT*5)

        title_and_author = VGroup(title_text, line, author_text).arrange(DOWN, buff=0.15)

        self.play(LaggedStart(Write(title_text),Create(line),Write(author_text),lag_ratio=0.5))

        self.wait(0.1)
        self.next_slide(notes="These are some notes.")
        self.clear()

        ack_title = FancyTitle(r"Acknowledgement")
        
        slide_text_1 = Tex(r"{16cm}The work in this presentation was done in collaboration with Alexandra Kolla, Steven Kordonowy, Juspreet Singh Sandhu, Stuart Wayland, and Ojas Parekh. The work on Quantum Max-\(d\)-Cut was done, in part, while I was interning at Sandia National Labs.", 
                           font_size=28,tex_environment="minipage")
        slide_text_1.to_corner(UL, buff=0.5).shift(DOWN)
        self.play(ack_title.anim())
        self.play(Write(slide_text_1), run_time=1)
        self.wait(0.1)


class Overview(Slide):
    def setup(self):
        theme = "Monokai Pro Light" # select a theme from https://iterm2colorschemes.com
        apply_theme(manim_scene=self, theme_name=theme, light_theme=True) # use the theme


    def construct(self):
        title = FancyTitle("Overview")
        self.play(title.anim())

        self.wait(0.1)
        self.next_slide(auto_next=True)

        slide_text_1 = r"1. Classical Optimization"
        slide_text_2 = r"2. Quantum 101"
        slide_text_3 = r"3. An Entanglement Bound"
        slide_text_4 = r"4. An Algorithm That Uses It"
        slide_text_5 = r"5. Semidefinite Programming"

        slide_text_1_mo = Tex(fr"{{16cm}}{slide_text_1}", 
                           font_size=28, tex_environment="minipage").to_corner(UL, buff=0.5).shift(DOWN*1.5)
        slide_text_2_mo = Tex(fr"{{16cm}}{slide_text_2}", 
                           font_size=28, tex_environment="minipage").next_to(slide_text_1_mo, DOWN, aligned_edge=LEFT, buff=1.2)
        slide_text_3_mo = Tex(fr"{{16cm}}{slide_text_3}", 
                           font_size=28, tex_environment="minipage").next_to(slide_text_2_mo, DOWN, aligned_edge=LEFT, buff=1.2)
        slide_text_4_mo = Tex(fr"{{16cm}}{slide_text_4}", 
                           font_size=28, tex_environment="minipage").next_to(slide_text_3_mo, DOWN, aligned_edge=LEFT, buff=1.2)
        slide_text_5_mo = Tex(fr"{{16cm}}{slide_text_5}", 
                           font_size=28, tex_environment="minipage").next_to(slide_text_4_mo, DOWN, aligned_edge=LEFT, buff=1.2)

        vid1 = VideoMobject(rf"{manim_video_output_dir}\MaxCutExampleVideo.mp4",loop=False).scale(0.2).move_to(slide_text_1_mo,aligned_edge=LEFT).shift(RIGHT*7)
        vid2 = VideoMobject(rf"{manim_video_output_dir}\ALittleQuantumVideo.mp4",loop=False).scale(0.2).move_to(slide_text_2_mo,aligned_edge=LEFT).shift(RIGHT*11)
        vid3 = VideoMobject(rf"{manim_video_output_dir}\ALittleMoreQuantum2Video.mp4",loop=False).scale(0.2).move_to(slide_text_3_mo,aligned_edge=LEFT).shift(RIGHT*7)
        vid4 = VideoMobject(rf"{manim_video_output_dir}\AnAlgorithmForMEVideo.mp4",loop=False).scale(0.2).move_to(slide_text_4_mo,aligned_edge=LEFT).shift(RIGHT*11)
        vid5 = VideoMobject(rf"{manim_video_output_dir}\ALittleSOSVideo.mp4",loop=False).scale(0.2).move_to(slide_text_5_mo,aligned_edge=LEFT).shift(RIGHT*7)

        surrbox1 = SurroundingRectangle(vid1,color=BLACK,buff=0.01,corner_radius=0.2)
        surrbox2 = SurroundingRectangle(vid2,color=BLACK,buff=0.01,corner_radius=0.2)
        surrbox3 = SurroundingRectangle(vid3,color=BLACK,buff=0.01,corner_radius=0.2)
        surrbox4 = SurroundingRectangle(vid4,color=BLACK,buff=0.01,corner_radius=0.2)
        surrbox5 = SurroundingRectangle(vid5,color=BLACK,buff=0.01,corner_radius=0.2)

        line1 = DashedLine(start=slide_text_1_mo.get_edge_center(RIGHT)+RIGHT*0.25,
                           end=surrbox1.get_edge_center(LEFT)+LEFT*0.25,dash_length=0.2,color=GRAY_C)
        line2 = DashedLine(start=slide_text_2_mo.get_edge_center(RIGHT)+RIGHT*0.25,
                           end=surrbox2.get_edge_center(LEFT)+LEFT*0.25,dash_length=0.2,color=GRAY_C)
        line3 = DashedLine(start=slide_text_3_mo.get_edge_center(RIGHT)+RIGHT*0.25,
                           end=surrbox3.get_edge_center(LEFT)+LEFT*0.25,dash_length=0.2,color=GRAY_C)
        line4 = DashedLine(start=slide_text_4_mo.get_edge_center(RIGHT)+RIGHT*0.25,
                           end=surrbox4.get_edge_center(LEFT)+LEFT*0.25,dash_length=0.2,color=GRAY_C)
        line5 = DashedLine(start=slide_text_5_mo.get_edge_center(RIGHT)+RIGHT*0.25,
                           end=surrbox5.get_edge_center(LEFT)+LEFT*0.25,dash_length=0.2,color=GRAY_C)

        self.play(LaggedStart(Write(slide_text_1_mo, run_time=0.5),
                              Create(line1, run_time=0.25),
                              Create(surrbox1, run_time=0.5), lag_ratio=0.5))
        
        self.wait(0.1)
        self.next_slide(loop=True)
        
        self.add(vid1)
        self.bring_to_back(vid1)

        self.wait(vid1.get_duration())
        self.next_slide(auto_next=True)

        self.play(LaggedStart(Write(slide_text_2_mo, run_time=0.5),
                              Create(line2, run_time=0.25),
                              Create(surrbox2, run_time=0.5), lag_ratio=0.5))
        
        self.wait(0.1)
        self.next_slide(loop=True)

        self.add(vid2)
        self.bring_to_back(vid2)

        self.wait(vid2.get_duration())
        self.next_slide(auto_next=True)

        self.play(LaggedStart(Write(slide_text_3_mo, run_time=0.5),
                              Create(line3, run_time=0.25),
                              Create(surrbox3, run_time=0.5), lag_ratio=0.5))
        
        self.wait(0.1)
        self.next_slide(loop=True)

        self.add(vid3)
        self.bring_to_back(vid3)

        self.wait(vid3.get_duration())
        self.next_slide(auto_next=True)

        self.play(LaggedStart(Write(slide_text_4_mo, run_time=0.5),
                              Create(line4, run_time=0.25),
                              Create(surrbox4, run_time=0.5), lag_ratio=0.5))
        
        self.wait(0.1)
        self.next_slide(loop=True)

        self.add(vid4)
        self.bring_to_back(vid4)

        self.wait(vid4.get_duration())
        self.next_slide(auto_next=True)

        self.play(LaggedStart(Write(slide_text_5_mo, run_time=0.5),
                              Create(line5, run_time=0.25),
                              Create(surrbox5, run_time=0.5), lag_ratio=0.5))
        
        self.wait(0.1)
        self.next_slide(loop=True)

        self.add(vid5)
        self.bring_to_back(vid5)

        self.wait(vid5.get_duration())


class ALittleQuantum(Slide):
    def setup(self):
        theme = "Monokai Pro Light" # select a theme from https://iterm2colorschemes.com
        apply_theme(manim_scene=self, theme_name=theme, light_theme=True) # use the theme


    def construct(self):
        title = FancyTitle("First, A Little Quantum")
        self.play(title.anim())

        self.wait(0.1)
        self.next_slide(notes="Even before we talk about quantum we look at the most basic unit of information. It can take one of two values: typically, 0 or 1.")
        
        slide_text_1 = Tex(r"{16cm}\textbf{Bit:} a \emph{bit}, \(x \in \{0,1\}\), takes one of two values.", 
                           font_size=28, tex_environment="minipage")
        slide_text_2a = Tex(r"{16cm}\textbf{Qubit:} A \emph{qubit} is a ``superposition'' of \(\ket{0}\) and \(\ket{1}\).", 
                           font_size=28, tex_environment="minipage")
        slide_text_2b = Tex(r"{16cm}\textbf{Qubit:} A \emph{qubit} is represented as a unit vector, \(\ket{\psi} \in \C^2\).", 
                           font_size=28, tex_environment="minipage")
        slide_text_1.to_corner(UL, buff=0.5).shift(DOWN)
        slide_text_2a.next_to(slide_text_1, DOWN, aligned_edge=LEFT, buff=0.25)
        slide_text_2b.next_to(slide_text_1, DOWN, aligned_edge=LEFT, buff=0.25)
        self.play(Write(slide_text_1), run_time=1)

        self.wait(0.1)
        self.next_slide(notes="We can quantumize a bit into qubit. In short, it is a superposition of 0 and 1. Lets break that down.")

        self.play(Write(slide_text_2a), run_time=1)

        self.wait(0.1)
        self.next_slide(notes="We have our bits. We turn them into ...")

        zero = MathTex(r"0").shift(LEFT*7)
        zero_copy = zero.copy()
        ket_zero = MathTex(r"\ket{0}").next_to(zero, RIGHT, buff=3)
        ket_zero_copy = ket_zero.copy()
        bmat_ket_zero = MathTex(r"= \begin{bmatrix}1\\0\end{bmatrix}").next_to(ket_zero, RIGHT, buff=2)

        one = MathTex(r"1").next_to(zero, DOWN, buff=1)
        one_copy = one.copy()
        ket_one = MathTex(r"\ket{1}").next_to(one, RIGHT, buff=3)
        ket_one_copy = ket_one.copy()
        bmat_ket_one = MathTex(r"= \begin{bmatrix}0\\1\end{bmatrix}").next_to(ket_one, RIGHT, buff=2)

        lin_comb = MathTex(r"\ket{\psi} = \alpha \ket{0} + \beta \ket{1} \in \C^2").next_to(bmat_ket_zero, RIGHT, buff=2.5).shift(DOWN * 0.5)
        unit_vec_const = MathTex(r"1 = \bra{\psi}\ket{\psi} = \abs{\alpha}^2 + \abs{\beta}^2").next_to(lin_comb, DOWN, buff=0.6)

        bit_text = Tex("Bits",font_size=28).next_to(zero, UP, buff=0.5)
        comp_basis_text = Tex(r"Computational\\Basis",font_size=28).next_to(ket_zero, UP, buff=0.5)
        vec_rep_text = Tex(r"Vector\\Representation",font_size=28).next_to(bmat_ket_zero, UP, buff=0.3)
        lin_comb_text = Tex(r"Linear\\Combination",font_size=28).next_to(lin_comb, UP, buff=1)
        unit_vec_text = Tex(r"Unit Vector",font_size=28).next_to(lin_comb, DOWN, buff=0.1)

        ast_text = MathTex(r"\ast", font_size=28,color=TEAL_D).move_to(unit_vec_const,aligned_edge=LEFT).shift(RIGHT*2+UP*0.25)
        footnote_text = Tex(r"\(^\ast\bra{\psi}\ket{\varphi}\) is the inner product.",font_size=28,color=TEAL_D).to_corner(DR, buff=0.5)

        self.play(Write(zero), Write(one), Write(bit_text), run_time=0.5)

        self.wait(0.1)
        self.next_slide(notes="We turn them into the so called computational basis vectors.")

        self.add(zero_copy,one_copy)
        self.play(TransformMatchingShapes(zero_copy,ket_zero),TransformMatchingShapes(one_copy,ket_one), Write(comp_basis_text), run_time=0.5)

        self.wait(0.1)
        self.next_slide(notes="Which can be understood as vectors. Indeed we will use the bra-ket notation, where a ket, |v>, is a vectors.")

        self.add(ket_zero_copy,ket_one_copy)
        self.play(TransformMatchingShapes(ket_zero_copy,bmat_ket_zero), TransformMatchingShapes(ket_one_copy,bmat_ket_one), Write(vec_rep_text), run_time=0.5)

        self.wait(0.1)
        self.next_slide(notes="A general quantum state takes the form of a linear combination. Here, we think of a superposition as represented by a linear combination.")

        self.play(Write(lin_comb), Write(lin_comb_text), run_time=0.5)

        self.wait(0.1)
        self.next_slide(notes=r"that is a unit vector. Note the the <\psi| is called a bra, which is the same as a row vectors, or the conjugate transpose of the ket version (or, rather, a dual vector). Putting a bra and a ket together like this gives an inner product.")

        self.play(lin_comb.animate.shift(UP * 0.5), Write(unit_vec_const), Write(unit_vec_text), run_time=1)
        self.play(Write(ast_text), Write(footnote_text))

        self.wait(0.1)
        self.next_slide(notes="This gives us the following definition for a qubit.")

        qubit_stuff = [one,ket_one,bmat_ket_one,zero,ket_zero,bmat_ket_zero,lin_comb,unit_vec_const,bit_text,comp_basis_text,vec_rep_text,lin_comb_text,unit_vec_text,ast_text,footnote_text]
        animations = [
            AnimationGroup(
                item.animate.scale(0.1).move_to(slide_text_2a).set_opacity(0),
                # FadeOut(item),
            )
            for item in qubit_stuff
        ]
        self.play(*animations,TransformMatchingTex(slide_text_2a,slide_text_2b))
        self.remove(*qubit_stuff)

        self.wait(0.1)

        ################# Tensor Product #########################

        self.next_slide(notes="Lets break that down.")

        slide_text_3 = Tex(r"{16cm}\textbf{Multiple Qubits:} We represent two qubits with a \emph{tensor product}, \(\ket{\psi} \in \C^2 \otimes \C^2 \cong \C^4\).", 
                           font_size=28, tex_environment="minipage")
        slide_text_3_2 = Tex(r"{15.75cm} \(\rightarrow\) A two qubit state of the form \(\ket{\psi_1} \otimes \ket{\psi_2}\) is said to be a product state.", 
                           font_size=28, tex_environment="minipage")
        slide_text_3_3 = Tex(r"{15.75cm} \(\rightarrow\) Any state that cannot be written as a product state is said to be entangled.", 
                           font_size=28, tex_environment="minipage")
        slide_text_4 = Tex(r"{15.75cm}\textbf{Notation:} We use \((\C^2)^{\otimes n}\) to denote the space where \(n\) qubits live.\\\phantom{\textbf{Notation:}} The \emph{computations basis} is identified by bit-strings \(\{\ket{x}\}_{x \in \{0,1\}^n}\).", 
                           font_size=26, tex_environment="minipage")
        slide_text_3.next_to(slide_text_2a, DOWN, aligned_edge=LEFT, buff=0.25)
        slide_text_3_2.next_to(slide_text_3, DOWN, aligned_edge=LEFT, buff=0.25).shift(RIGHT * 0.25)
        slide_text_3_3.next_to(slide_text_3_2, DOWN, aligned_edge=LEFT, buff=0.25)
        slide_text_4.next_to(slide_text_3_3, DOWN, aligned_edge=LEFT, buff=0.25)
        self.play(Write(slide_text_3), run_time=0.5)

        cart_prod = MathTex(r"\{0,1\} \times \{0,1\}").shift(LEFT*5)
        cart_prod_copy = cart_prod.copy()
        cart_prod2 = MathTex(r"=\{00,01,10,11\}").next_to(cart_prod, RIGHT, buff=0.2)
        cart_prod2_copy = cart_prod2.copy()

        tensor_prod = MathTex(r"\{\ket{00},\ket{01},",r"\ket{10},",r"\ket{11}\}").next_to(cart_prod2, RIGHT, buff=1)
        tensor_prod_part2_copy = tensor_prod[1].copy()
        tensor_prod_part2_exp = MathTex(r"\overbrace{\ket{10} = \ket{1} \otimes \ket{0}}").next_to(tensor_prod[1],DOWN,buff=0.25)

        ent_state = MathTex(r"\ket{\psi}", r"= \alpha_{00} \ket{00}", r"+ \alpha_{01} \ket{01}", r"+ \alpha_{10} \ket{10}", r"+ \alpha_{11} \ket{11}").shift(DOWN * 3)
        ent_state_1_copy = ent_state[0].copy()
        unit_vec_const_2 = MathTex(r"\bra{\psi}\ket{\psi} = 1").next_to(ent_state[0],DOWN,buff=0.5).shift(RIGHT)

        two_strings_text = Tex(r"Classical (2-Bit) Strings",font_size=28).next_to(cart_prod, UP, buff=0.5)
        comp_basis_2qubits_text = Tex(r"Computational Basis",font_size=28).next_to(tensor_prod, UP, buff=0.5)
        abr_2qubit_state_text = Tex(r"Two-Qubit State",font_size=28).next_to(ent_state, UP, buff=0.5)

        self.wait(0.1)
        self.next_slide(notes="classically, we understand multiple bits with the cartesian product. That is, the cartesian product gives us the set of all length 2 bit strings. As with the single qubit case, we assign to each string a computation basis vectors...")

        self.play(Write(cart_prod), Write(two_strings_text), run_time=0.5)
        self.add(cart_prod_copy)
        self.wait(0.5)
        self.play(TransformMatchingShapes(cart_prod_copy,cart_prod2),two_strings_text.animate.shift(RIGHT*2), run_time=0.5)

        self.wait(0.1)
        self.next_slide(notes="As with the single qubit case, we assign to each string a computation basis vectors. We can decompose each computation basis vector into the tensor product of the individual computation basis vectors.")

        self.play(TransformMatchingShapes(cart_prod2_copy,tensor_prod), Write(comp_basis_2qubits_text), run_time=0.5)
        self.add(tensor_prod_part2_copy)
        self.wait()
        self.play(TransformMatchingShapes(tensor_prod_part2_copy,tensor_prod_part2_exp), run_time=0.5)

        self.wait(0.1)
        self.next_slide(notes="All together, a state on two qubits is just a linear combination of the computation basis vectors.")

        self.play(Write(ent_state), Write(abr_2qubit_state_text), run_time=0.5)
        self.add(ent_state_1_copy)
        self.wait()
        self.play(TransformMatchingShapes(ent_state_1_copy,unit_vec_const_2))

        self.wait(0.1)
        self.next_slide(notes = "lets break this down and look at a special case.")

        tensor_prod_stuff_1 = [
            cart_prod,
            cart_prod2,
            tensor_prod,
            tensor_prod_part2_exp,
            unit_vec_const_2,
            two_strings_text,
            comp_basis_2qubits_text,
            abr_2qubit_state_text]
        animations2 = [item.animate.shift(RIGHT*2).set_opacity(0) for item in tensor_prod_stuff_1]
        self.play(LaggedStart(AnimationGroup(*animations2, run_time=0.5), ent_state.animate.move_to(cart_prod,aligned_edge=LEFT).shift(DOWN*0.5).scale(0.75),lag_ratio=0.5))
        self.remove(*tensor_prod_stuff_1)

        self.wait(0.1)
        self.next_slide(notes="If I change the scalars to be the following, we get something interesting.")

        ent_state1b = MathTex(r"\ket{\psi}", r"= \alpha^{(1)}_{0}\alpha^{(2)}_{0} \ket{00}", r"+ \alpha^{(1)}_{0}\alpha^{(2)}_{1} \ket{01}", r"+ \alpha^{(1)}_{1}\alpha^{(2)}_{0} \ket{10}", r"+ \alpha^{(1)}_{1}\alpha^{(2)}_{1} \ket{11}",
                             font_size=28).move_to(ent_state,aligned_edge=LEFT)
        ent_state2 = MathTex(r"= \alpha^{(1)}_{0}\alpha^{(2)}_{0} \ket{0} \otimes \ket{0}", r"+ \alpha^{(1)}_{0}\alpha^{(2)}_{1} \ket{0} \otimes \ket{1}", r"+  \alpha^{(1)}_{1}\alpha^{(2)}_{0} \ket{1} \otimes \ket{0}", r"+ \alpha^{(1)}_{1}\alpha^{(2)}_{1} \ket{1} \otimes \ket{1}",
                            font_size=28).move_to(ent_state1b[1],aligned_edge=LEFT)
        # ent_state3 =MathTex(r"\ket{\psi}", r"= \ket{0} \otimes \left(\alpha_{00} \ket{0} + \alpha_{01} \ket{1}\right)", r"+ \ket{1} \otimes \left(\alpha_{10} \ket{0} + \alpha_{11} \ket{1}\right)").next_to(ent_state2,DOWN,aligned_edge=LEFT,buff=0.25)
        prod_state_0 = MathTex(r"= \alpha^{(1)}_{0} \ket{0} \otimes \left(\alpha^{(2)}_{0} \ket{0} + \alpha^{(2)}_{1} \ket{1}\right)", r"+ \alpha^{(1)}_{1} \ket{1} \otimes \left(\alpha^{(2)}_{0} \ket{0} + \alpha^{(2)}_{1} \ket{1}\right)",
                               font_size=28).next_to(ent_state2,DOWN,aligned_edge=LEFT,buff=0.25)
        prod_state_0b = MathTex(r"{{=}} {{\alpha^{(1)}_{0} \ket{0} }} \otimes {{\left(\alpha^{(2)}_{0} \ket{0} + \alpha^{(2)}_{1} \ket{1}\right)}} + {{\alpha^{(1)}_{1} \ket{1} }} \otimes {{\left(\alpha^{(2)}_{0} \ket{0} + \alpha^{(2)}_{1} \ket{1}\right)}}",
                                font_size=28).next_to(ent_state2,DOWN,aligned_edge=LEFT,buff=0.25)
        prod_state = MathTex(r"{{=}} \left({{\alpha^{(1)}_{0} \ket{0} }} + {{\alpha^{(1)}_{1} \ket{1} }}\right) \otimes {{\left(\alpha^{(2)}_{0} \ket{0} + \alpha^{(2)}_{1} \ket{1}\right)}}",
                             font_size=28).move_to(prod_state_0,aligned_edge=LEFT)
        prod_state_2 = MathTex(r"= \underbrace{\left(\alpha^{(1)}_{0} \ket{0} + \alpha^{(1)}_{1} \ket{1}\right)}_{\ket{\psi_1} } \otimes \underbrace{\left(\alpha^{(2)}_{0} \ket{0} + \alpha^{(2)}_{1} \ket{1}\right)}_{\ket{\psi_2} }",
                             font_size=28).move_to(prod_state,aligned_edge=UP)

        self.play(LaggedStart(*[TransformMatchingShapes(ent_state[i], ent_state1b[i]) for i in range(5)], lag_ratio=0.25))

        self.wait(0.1)
        self.next_slide(notes="Lets expand it out.")

        self.play(LaggedStart(*[TransformMatchingShapes(ent_state1b[i+1], ent_state2[i]) for i in range(4)], lag_ratio=0.25))

        self.wait(0.1)
        self.next_slide(notes="re-group.")
        
        ent_state2_copy = ent_state2.copy()

        self.play(LaggedStart(TransformMatchingShapes(VGroup(ent_state2_copy[0],ent_state2_copy[1]),prod_state_0[0]),
                              TransformMatchingShapes(VGroup(ent_state2_copy[2],ent_state2_copy[3]),prod_state_0[1]),
                              lag_ratio=0.25))
        
        # self.next_slide()

        # ent_state3_copy = ent_state3.copy()

        # self.play(LaggedStart(*[TransformMatchingShapes(ent_state3_copy[i], prod_state_0[i]) for i in range(3)], lag_ratio=0.25))

        self.wait(0.1)
        self.next_slide(notes="re-group again.\nHere we notices something interesting. This is just a tensor product of two single qubit states.")
        self.remove(prod_state_0, ent_state2_copy, *[prod_state_0[i] for i in range(2)], *[ent_state2_copy[i] for i in range(2)])
        self.add(prod_state_0b)

        self.play(TransformMatchingTex(prod_state_0b,prod_state))
        self.play(TransformMatchingShapes(prod_state,prod_state_2))

        self.wait(0.1)
        self.next_slide()

        self.play(Write(slide_text_3_2), run_time=0.5)

        self.wait(0.1)
        self.next_slide(notes="So, in a sense, entanglement is a result of superpositions over multiple qubits/states.")

        self.play(Write(slide_text_3_3), run_time=0.5)

        self.wait(0.1)
        self.next_slide()

        tensor_prod_stuff_2 = [
            # ent_state,
            # ent_state1b,
            ent_state1b[0],
            ent_state2,
            prod_state,
            prod_state_2]
        animations3 = [item.animate.shift(RIGHT*2).set_opacity(0) for item in tensor_prod_stuff_2]
        self.play(LaggedStart(AnimationGroup(*animations3, run_time=0.5), Write(slide_text_4,run_time = 0.5),lag_ratio=0.5))
        self.remove(*tensor_prod_stuff_1)

        self.wait(0.1)
        self.next_slide()

        ############# dits ############

        slide_text_5 = Tex(r"{16cm}\textbf{Dit:} A \emph{base-\(d\) dit}, \(x \in [d] = \{1,2,\dotsc,d\}\), takes \(d\) possible values.", 
                           font_size=28, tex_environment="minipage")
        slide_text_6 = Tex(r"{16cm}\textbf{Qudit:} A \(d\)-dimensional \emph{qudit} is represented as a unit vector, \(\ket{\psi} \in \C^d\).", 
                           font_size=28, tex_environment="minipage")
        slide_text_7 = Tex(r"{16cm}\textbf{Notation:} We use \((\C^d)^{\otimes n}\) to denote the space where \(n\), \(d\)-dimensional qudits live.\\\phantom{\textbf{Notation:}} The \emph{computations basis} is identified by strings \(\{\ket{x}\}_{x \in [d]^n}\).", 
                           font_size=26, tex_environment="minipage")
        slide_text_5.next_to(slide_text_4, DOWN, aligned_edge=LEFT, buff=0.25).shift(LEFT * 0.25)
        slide_text_6.next_to(slide_text_5, DOWN, aligned_edge=LEFT, buff=0.25)
        slide_text_7.next_to(slide_text_6, DOWN, aligned_edge=LEFT, buff=0.25).shift(RIGHT * 0.25)
        self.play(Write(slide_text_5), run_time=0.5)

        self.wait(0.1)
        self.next_slide()

        self.play(Write(slide_text_6), run_time=0.5)
        self.wait(0.1)
        
        self.next_slide()
        self.play(Write(slide_text_7), run_time=0.5)
        self.wait(0.1)


class ALittleQuantumVideo(Scene):
    def setup(self):
        theme = "Monokai Pro Light" # select a theme from https://iterm2colorschemes.com
        apply_theme(manim_scene=self, theme_name=theme, light_theme=True) # use the theme


    def construct(self):
        cart_prod = MathTex(r"\{0,1\} \times \{0,1\}").shift(LEFT*5+UP*1.5)
        cart_prod_copy = cart_prod.copy()
        cart_prod2 = MathTex(r"=\{00,01,10,11\}").next_to(cart_prod, RIGHT, buff=0.2)
        cart_prod2_copy = cart_prod2.copy()

        tensor_prod = MathTex(r"\{\ket{00},\ket{01},",r"\ket{10},",r"\ket{11}\}").next_to(cart_prod2, RIGHT, buff=1)
        tensor_prod_part2_copy = tensor_prod[1].copy()
        tensor_prod_part2_exp = MathTex(r"\overbrace{\ket{10} = \ket{1} \otimes \ket{0}}").next_to(tensor_prod[1],DOWN,buff=0.25)

        ent_state = MathTex(r"\ket{\psi}", r"= \alpha_{00} \ket{00}", r"+ \alpha_{01} \ket{01}", r"+ \alpha_{10} \ket{10}", r"+ \alpha_{11} \ket{11}").shift(DOWN * 1.5)
        ent_state_1_copy = ent_state[0].copy()
        unit_vec_const_2 = MathTex(r"\bra{\psi}\ket{\psi} = 1").next_to(ent_state[0],DOWN,buff=0.5).shift(RIGHT)

        two_strings_text = Tex(r"Classical (2-Bit) Strings",font_size=28).next_to(cart_prod, UP, buff=0.5)
        comp_basis_2qubits_text = Tex(r"Computational Basis",font_size=28).next_to(tensor_prod, UP, buff=0.5)
        abr_2qubit_state_text = Tex(r"Two-Qubit State",font_size=28).next_to(ent_state, UP, buff=0.5)

        self.play(Write(cart_prod), Write(two_strings_text), run_time=0.5)
        self.add(cart_prod_copy)
        self.wait(0.25)
        self.play(TransformMatchingShapes(cart_prod_copy,cart_prod2),two_strings_text.animate.shift(RIGHT*2), run_time=0.5)

        self.wait(0.25)

        self.play(TransformMatchingShapes(cart_prod2_copy,tensor_prod), Write(comp_basis_2qubits_text), run_time=0.5)
        self.add(tensor_prod_part2_copy)
        self.play(TransformMatchingShapes(tensor_prod_part2_copy,tensor_prod_part2_exp), run_time=0.5)

        self.play(Write(ent_state), Write(abr_2qubit_state_text), run_time=0.5)
        self.add(ent_state_1_copy)
        self.play(TransformMatchingShapes(ent_state_1_copy,unit_vec_const_2))

        self.wait(1)


class IntroToCSPs(Slide):
    def setup(self):
        theme = "Monokai Pro Light" # select a theme from https://iterm2colorschemes.com
        apply_theme(manim_scene=self, theme_name=theme, light_theme=True) # use the theme


    def construct(self):
        title = FancyTitle("Classical Optimization Problems")
        self.play(title.anim())

        self.wait(0.1)
        self.next_slide()
        
        slide_text_1 = Tex(r"{{Find a}} binary {{string,}} {{\(x \in \{0,1\}^n\),}} {{that maximizes some objective:}} {{$\operatorname{max}_x(\mathcal{C}(x))$ (for $\calC: \{0,1\}^n \to \R$).}}", 
                           font_size=28)
        slide_text_1b = Tex(r"{{Find a}} {{string,}} {{\(x \in [d]^n\),}} {{that maximizes some objective:}} {{$\operatorname{max}_x(\mathcal{C}(x))$ (for $\mathcal{C}: [d]^n \to \mathbb{R}$).}}", 
                           font_size=28)
        slide_text_1.to_corner(UL, buff=0.5).shift(DOWN)
        slide_text_1b.to_corner(UL, buff=0.5).shift(DOWN)
        self.play(Write(slide_text_1), run_time=0.5)

        self.wait(0.1)
        self.next_slide()

        slide_text_2 = Tex(r"More generally, we let {{\(x \in [d]^n\),}} where \([d] = \{1,2,\dotsc,d\}\), and $\calC: [d]^n \to \mathbb{R}$.", 
                           font_size=28)
        slide_text_2.next_to(slide_text_1, DOWN, aligned_edge=LEFT, buff=0.25)
        self.play(Write(slide_text_2), run_time=0.5)

        self.wait(0.1)
        self.next_slide()

        self.play(TransformMatchingTex(VGroup(slide_text_1,slide_text_2), slide_text_1b, transform_mismatches=True), run_time=0.5)

        self.wait(0.1)
        self.next_slide()

        slide_text_3 = Tex(r"{16cm}Typically, we might write \(\calC(x) = \sum_\alpha \calC_\alpha(x)\).", 
                           font_size=28, tex_environment="minipage")
        slide_text_4 = Tex(r"{15cm}\(\rightarrow\) \(\calC\) is said to be \emph{\(k\)-local} if each \(\calC_\alpha\) depends on at most \(k\) variables.", 
                           font_size=28, tex_environment="minipage")
        slide_text_3.next_to(slide_text_1b, DOWN, aligned_edge=LEFT, buff=0.25)
        slide_text_4.next_to(slide_text_3, DOWN, aligned_edge=LEFT, buff=0.25).shift(RIGHT * 0.25)
        self.play(Write(slide_text_3), run_time=0.5)

        self.wait(0.1)
        self.next_slide()

        self.play(Write(slide_text_4), run_time=0.5)
        self.wait(0.1)


class MaxCutExample(Slide):
    def setup(self):
        theme = "Monokai Pro Light" # select a theme from https://iterm2colorschemes.com
        apply_theme(manim_scene=self, theme_name=theme, light_theme=True) # use the theme


    def construct(self):
        title = FancyTitle("Motivating Example: Max-Cut")
        self.play(title.anim())

        self.wait(0.1)
        self.next_slide(notes="There is a local term for each edge that is the indicator function on whether the assignments to the two vertices are different.")

        slide_text_5 = Tex(r"{8cm}Max-Cut is a 2-local optimization problem defined over a graph, \(G = (V,E,w)\).", 
                           font_size=28, tex_environment="minipage")
        slide_text_6 = MathTex(r"\calC(x)", r"= \sum_{(a,b) \in E} w_{(a,b)}", r"\overbrace{\mathbbm{1}(x_a \neq x_b)}^{\calC_{(a,b)}}",font_size=28)
        slide_text_5.to_corner(UL, buff=0.5).shift(DOWN)
        slide_text_6.next_to(slide_text_5, DOWN, buff=1)

        nxG = nx.Graph()
        nxG.add_edges_from([(1,2),(2,3),(3,4),(1,4),(3,5),(4,5)])
        sl = nx.spring_layout(nxG, seed=1, scale=2.5)
        sl2 = {k: [x, y, 0] for k, (x, y) in sl.items()}
        G = Graph.from_networkx(nxG, layout=sl2,vertex_config={
                "radius": 0.15,
            }).shift(RIGHT * 4).shift(UP)

        vertex_labels = VGroup(*[
            MathTex(str(v)).next_to(G[v], RIGHT*0.1).shift(UP * 0.1 if str(v) == "3" else UP * 0.0).scale(0.5)
            for v in G.vertices
        ])


        self.play(LaggedStart(Write(slide_text_5,run_time=1), Write(slide_text_6,run_time=1), Create(G,run_time=1), lag_ratio=0.5))
        self.play(*[Write(item) for item in vertex_labels], run_time=0.25)

        self.wait(0.1)
        self.next_slide(notes="We consider the following example.")

        cut = [1,3,5]

        # cut_vec_x = MathTex(r"\begin{bmatrix}", "1", r" \\ ", "0", r" \\ ", "1", r" \\ ", "0", r" \\ ", "1", r"\end{bmatrix}")
        cut_vec_x = Matrix([[1],[0],[1],[0],[1]]).scale(0.5).next_to(G,DOWN,buff=0.25)
        x_eq_text = MathTex("x", "=").next_to(cut_vec_x, LEFT, buff = 0.2)
        for i, row in enumerate(cut_vec_x.get_entries()):
            row.set_color(GREEN if i%2 == 0 else BLUE)


        self.play(Write(cut_vec_x),Write(x_eq_text),run_time=0.5)
        for v in G.vertices:
            self.play(G[v].animate.set_color(GREEN if v in cut else BLUE), run_time=(0.2))

        self.wait(0.1)
        self.next_slide()

        x_eq_text_copy = x_eq_text[0].copy()
        Cx_eq_copy = slide_text_6[0].copy()
        self.add(x_eq_text_copy,Cx_eq_copy)
        Candx_copies = VGroup(x_eq_text_copy,Cx_eq_copy)
        eval_example = MathTex(r"\calC(x)", "= 5").next_to(slide_text_6[0],DOWN,buff=2.5).shift(RIGHT*2)
        eval_example[1].set_color(RED)

        self.play(TransformMatchingShapes(Candx_copies,eval_example[0]))

        for e, emob in G.edges.items():
            if (e[0] in cut and e[1] not in cut) or (e[0] not in cut and e[1] in cut):
                self.play(emob.animate.set_color(RED), run_time=(0.2))

        edges_vgroup = VGroup(*[emob for e, emob in G.edges.items() if (e[0] in cut and e[1] not in cut) or (e[0] not in cut and e[1] in cut)])
        edges_vgroup_copy = edges_vgroup.copy()

        self.play(Transform(edges_vgroup_copy,eval_example[1]))

        self.wait(0.1)
        self.next_slide()
        self.remove(edges_vgroup_copy) # this is a bit annoying but necessary

        self.play(eval_example.animate.next_to(cut_vec_x, RIGHT, buff=0.5))

        slide_text_7 = Tex(r"{8cm}Key take away: each \(\calC_e\) is an observable property of the assignment \(x\): whether the edge \(e\) is cut or not.", 
                           font_size=28, tex_environment="minipage")
        slide_text_7.next_to(slide_text_5, DOWN, aligned_edge=LEFT, buff=3)     

        self.play(Write(slide_text_7)) 
        self.wait(0.1)


class MaxCutExampleVideo(Scene):
    def setup(self):
        theme = "Monokai Pro Light" # select a theme from https://iterm2colorschemes.com
        apply_theme(manim_scene=self, theme_name=theme, light_theme=True) # use the theme


    def construct(self):
        MC_eq = MathTex(r"\calC(x)", r"= \sum_{(a,b) \in E} w_{(a,b)}", r"\overbrace{\mathbbm{1}(x_a \neq x_b)}^{\calC_{(a,b)}}", font_size=28)

        nxG = nx.Graph()
        nxG.add_edges_from([(1,2),(2,3),(3,4),(1,4),(3,5),(4,5)])
        sl = nx.spring_layout(nxG, seed=1, scale=2.5)
        sl2 = {k: [x, y, 0] for k, (x, y) in sl.items()}
        G = Graph.from_networkx(nxG, layout=sl2,vertex_config={
                "radius": 0.15,
            })

        vertex_labels = VGroup(*[
            MathTex(str(v)).next_to(G[v], RIGHT*0.1).shift(UP * 0.1 if str(v) == "3" else UP * 0.0).scale(0.5)
            for v in G.vertices
        ])

        G_vg = VGroup(G,vertex_labels)

        eq_G_vg = VGroup(VGroup(G,vertex_labels),MC_eq).arrange(RIGHT,buff=1).shift(UP*1.75)


        self.play(LaggedStart(Create(G,run_time=1), AnimationGroup(*[Write(item) for item in vertex_labels], run_time=0.25), Write(MC_eq,run_time=1), lag_ratio=0.25))

        cut = [1,3,5]

        # cut_vec_x = MathTex(r"\begin{bmatrix}", "1", r" \\ ", "0", r" \\ ", "1", r" \\ ", "0", r" \\ ", "1", r"\end{bmatrix}")
        cut_vec_x = Matrix([[1],[0],[1],[0],[1]]).scale(0.5).next_to(G,DOWN,buff=1)
        x_eq_text = MathTex("x", "=").next_to(cut_vec_x, LEFT, buff = 0.2)
        for i, row in enumerate(cut_vec_x.get_entries()):
            row.set_color(GREEN if i%2 == 0 else BLUE)


        self.play(Write(cut_vec_x),Write(x_eq_text),run_time=0.5)
        for v in G.vertices:
            self.play(G[v].animate.set_color(GREEN if v in cut else BLUE), run_time=0.1)

        x_eq_text_copy = x_eq_text[0].copy()
        Cx_eq_copy = MC_eq[0].copy()
        self.add(x_eq_text_copy,Cx_eq_copy)
        Candx_copies = VGroup(x_eq_text_copy,Cx_eq_copy)
        eval_example = MathTex(r"\calC(x)", "= 5").next_to(cut_vec_x,RIGHT,buff=3)
        eval_example[1].set_color(RED)

        self.play(TransformMatchingShapes(Candx_copies,eval_example[0]))

        for e, emob in G.edges.items():
            if (e[0] in cut and e[1] not in cut) or (e[0] not in cut and e[1] in cut):
                self.play(emob.animate.set_color(RED), run_time=0.1)

        edges_vgroup = VGroup(*[emob for e, emob in G.edges.items() if  (e[0] in cut and e[1] not in cut) or (e[0] not in cut and e[1] in cut)])
        edges_vgroup_copy = edges_vgroup.copy()

        self.play(Transform(edges_vgroup_copy,eval_example[1]))

        self.wait(1)


# IDK how to fix it, but this is a bad slide. 
class IntroToLHPs(Slide):
    def setup(self):
        theme = "Monokai Pro Light" # select a theme from https://iterm2colorschemes.com
        apply_theme(manim_scene=self, theme_name=theme, light_theme=True) # use the theme


    def construct(self):
        title = FancyTitle("Classical Optimization Problems (Again)")

        slide_text_1 = r"Find a string, \(x \in [d]^n\), that maximizes some \(k\)-local objective: $\calC(x) = \sum_\alpha \mathcal{C}_\alpha(x)$."
        slide_text_2 = r"\(\rightarrow\) Each \(\calC_\alpha: [d]^n \to \R\) encodes some observable property of the string, \(x \in [d]^n\)."
        slide_text_3 = r"We can represent \(\calC_\alpha: [d]^n \to \R\) as a diagonal matrix, \(\calC_\alpha \in M_{d^n}(\C)\) (moreover, \(\calC = \sum_\alpha \calC_\alpha\))."
        slide_text_4 = r"\(\rightarrow\) We then have that \(\calC(x) = \bra{x}\calC\ket{x}\) and \(\max_x(\calC(x)) = \eig_{\max}(\calC)\)."
        slide_text_5 = fr"\(\rightarrow\) {{\color[HTML]{{{GREEN_E.to_hex()[1:]}}}Goal}}: Find a string, \(x \in [d]^n\), that optimizes: \(\bra{{x}}\calC \ket{{x}}\)."
        
        slide_text_1_mo = Tex(f"{{16cm}}{slide_text_1}", 
                           font_size=28, tex_environment="minipage")
        slide_text_2_mo = Tex(f"{{15cm}}{slide_text_2}", 
                           font_size=28, tex_environment="minipage")
        slide_text_1_mo.to_corner(UL, buff=0.5).shift(DOWN)
        slide_text_2_mo.next_to(slide_text_1_mo, DOWN, aligned_edge=LEFT, buff=0.25).shift(RIGHT * 0.25)

        slide_text_3_mo = Tex(f"{{16cm}}{slide_text_3}", 
                           font_size=28, tex_environment="minipage")
        slide_text_3_mo.next_to(slide_text_2_mo, DOWN, aligned_edge=LEFT, buff=0.25).shift(LEFT * 0.25+DOWN*0.25)

        slide_text_4_mo = Tex(f"{{15cm}}{slide_text_4}", 
                           font_size=28, tex_environment="minipage")
        slide_text_4_mo.next_to(slide_text_3_mo, DOWN, aligned_edge=LEFT, buff=0.25).shift(RIGHT * 0.25)

        slide_text_5_mo = Tex(f"{{15cm}}{slide_text_5}", 
                           font_size=28, tex_environment="minipage")
        slide_text_5_mo.next_to(slide_text_4_mo, DOWN, aligned_edge=LEFT, buff=0.25)
        
        self.play(title.anim())

        self.wait(0.1)
        self.next_slide(notes="Recall where we left off with classical optimization.")

        self.play(Write(slide_text_1_mo), run_time=0.5)
        self.play(Write(slide_text_2_mo), run_time=0.5)

        self.wait(0.1)
        self.next_slide(notes="we just put the value into the diagonal entry indexed by the strings.")

        self.play(Write(slide_text_3_mo), run_time = 0.5)

        # C_alpha_diag_mat = MathTex(r"\calC_\alpha = \begin{bmatrix}\calC_\alpha(111\cdots 1)\end{bmatrix}").shift(LEFT*5)
        C_alpha_diag_mat = MathTex(r"""
            C_\alpha = \begin{blockarray}{ccccccc}
                & \vcenter{\hbox{\scriptsize $1\cdots 11$}} & \vcenter{\hbox{\scriptsize $1\cdots 12$}} & \vcenter{\hbox{\scriptsize $\cdots$}} & \vcenter{\hbox{\scriptsize $x$}} & \vcenter{\hbox{\scriptsize $\cdots$}} & \vcenter{\hbox{\scriptsize $d \cdots dd$}} \\
                \begin{block}{c[cccccc]}
                    \vcenter{\hbox{\scriptsize $1\cdots 11$}} & \calC_\alpha(111\cdots 111) \tstrut\bstrut & 0                          & \cdots & 0               & \cdots & 0 \\
                    \vcenter{\hbox{\scriptsize $1\cdots 12$}} & 0                           & \calC_\alpha(1 \cdots 112) & \cdots & 0               & \cdots & 0\\
                    \vcenter{\hbox{\scriptsize $\vdots$}}     & \vdots                      & \vdots                     & \ddots & \vdots          &        & \vdots \\
                    \vcenter{\hbox{\scriptsize $x$}}          & 0                           & 0                          & \cdots & \calC_\alpha(x) & \cdots & 0 \\
                    \vcenter{\hbox{\scriptsize $\vdots$}}     & \vdots                      & \vdots                     &        & \vdots          & \ddots & \vdots \\
                    \vcenter{\hbox{\scriptsize $d\cdots dd$}} & 0                           & 0                          & \cdots & 0               & \cdots & \calC_\alpha(d \cdots dd)\tstrut\bstrut \\
                \end{block}
            \end{blockarray}
        """,font_size=28).next_to(slide_text_3_mo, DOWN, buff=2)

        self.play(Write(C_alpha_diag_mat))

        self.wait(0.1)
        self.next_slide(notes="Indeed, this means the value is just quadratic form of the computation basis vector. Moreover, we have turned this optimization problem into an eigenvalue problem.")

        self.play(Write(slide_text_4_mo), run_time=0.5)

        self.wait(0.1)
        self.next_slide()

        self.play(Write(slide_text_5_mo), run_time=0.5)

        self.wait(0.1)
        self.next_slide("We can note introduce the LHP, the quantum version of optimization")

        self.play(Unwrite(C_alpha_diag_mat), run_time=0.5)

        slide_text_1b_mo = Tex(fr"{{8cm}}\RaggedRight{{{slide_text_1}}}", 
                           font_size=28, tex_environment="minipage")
        slide_text_2b_mo = Tex(fr"{{7.75cm}}\RaggedRight{{{slide_text_2}}}", 
                           font_size=28, tex_environment="minipage")
        slide_text_3b_mo = Tex(fr"{{8cm}}\RaggedRight{{{slide_text_3}}}", 
                           font_size=28, tex_environment="minipage")
        slide_text_4b_mo = Tex(fr"{{7.75cm}}\RaggedRight{{{slide_text_4}}}", 
                           font_size=28, tex_environment="minipage")
        slide_text_5b_mo = Tex(fr"{{7.75cm}}\RaggedRight{{{slide_text_5}}}", 
                           font_size=28, tex_environment="minipage")
        slide_text_1b_mo.to_corner(UL, buff=0.5).shift(DOWN)
        slide_text_2b_mo.next_to(slide_text_1b_mo, DOWN, aligned_edge=LEFT, buff=0.25).shift(RIGHT * 0.25)
        slide_text_3b_mo.next_to(slide_text_2b_mo, DOWN, aligned_edge=LEFT, buff=0.25).shift(LEFT * 0.25+DOWN*0.25)
        slide_text_4b_mo.next_to(slide_text_3b_mo, DOWN, aligned_edge=LEFT, buff=0.25).shift(RIGHT * 0.25)
        slide_text_5b_mo.next_to(slide_text_4b_mo, DOWN, aligned_edge=LEFT, buff=0.25)

        slide_title_1b = Text("Classical Optimization Problems", font_size=34)
        slide_title_1b.to_corner(UL, buff=0.5)

        self.play(TransformMatchingShapes(slide_text_1_mo,slide_text_1b_mo),
                  TransformMatchingShapes(slide_text_2_mo,slide_text_2b_mo),
                  TransformMatchingShapes(slide_text_3_mo,slide_text_3b_mo),
                  TransformMatchingShapes(slide_text_4_mo,slide_text_4b_mo),
                  TransformMatchingShapes(slide_text_5_mo,slide_text_5b_mo),
                  TransformMatchingShapes(title.title,slide_title_1b), run_time=0.5)
        
        line = Line(
            start=UP * (config.frame_y_radius-1.25),      # top edge of frame
            end=DOWN * config.frame_y_radius,      # bottom edge of frame
        )
        
        slide_title_1b = Text("Local Hamiltonian Problem", font_size=34)
        slide_title_1b.to_corner(UL, buff=0.5).shift(RIGHT*8)

        self.play(title.line.animate.put_start_and_end_on(title.line.get_start(),title.line.get_end()+RIGHT*5.5), Create(line), Write(slide_title_1b), run_time=0.5)

        self.wait(0.1)
        self.next_slide(notes="Here we generalize the notion on the left, that observables are represented by diagonal matrices, with the full quantum version that they need only be diagonalizable or rather self-adjoint.")

        box1 = SurroundingRectangle(slide_text_3b_mo, color=GOLD, buff=0.1)
        box2 = SurroundingRectangle(slide_text_4b_mo, color=GOLD, buff=0.1)
        box3 = SurroundingRectangle(slide_text_5b_mo, color=GOLD, buff=0.1)

        slide_text_5 = r"We represent local terms as matrices with real eigenvalues, \(H_\alpha \in M_{d^n}(\C)\), called \emph{quantum observables} (or \emph{Hamiltonians})."
        slide_text_6 = r"\(\rightarrow\) The full problem Hamiltonian is: \(H = \sum_{\alpha} H_\alpha\)."
        slide_text_7 = r"\(\rightarrow\) For a state, \(\ket{\psi} \in (\C^d)^{\otimes n}\), we call \begin{center}\(\bra{\psi}H\ket{\psi} = \sum_\alpha \bra{\psi}H_\alpha\ket{\psi}\)\end{center} the \emph{energy} of \(\ket{\psi}\)."
        slide_text_7b = r"\(\rightarrow\) We have that \(\max_{\ket{\psi}}(\bra{\psi}H\ket{\psi}) = \eig_{\max}(H)\)."
        slide_text_8 = fr"\(\rightarrow\) {{\color[HTML]{{{GREEN_E.to_hex()[1:]}}}Goal}}: Find a state, \(\ket{{\psi}} \in (\C^d)^{{\otimes n}}\), that optimizes the energy, \(\bra{{\psi}}H\ket{{\psi}}\)."
        slide_text_9 = r"\(H\) is said to be \(k\)-local if each \(H_\alpha\) acts as the identity on all but \(k\) qudits."

        slide_text_5_mo = Tex(fr"{{8cm}}\RaggedRight{{{slide_text_5}}}", 
                           font_size=28, tex_environment="minipage")
        slide_text_6_mo = Tex(fr"{{7.75cm}}\RaggedRight{{{slide_text_6}}}", 
                           font_size=28, tex_environment="minipage")
        slide_text_7_mo = Tex(fr"{{7.75cm}}\RaggedRight{{{slide_text_7}}}", 
                           font_size=28, tex_environment="minipage")
        slide_text_7b_mo = Tex(fr"{{7.75cm}}\RaggedRight{{{slide_text_7b}}}", 
                           font_size=28, tex_environment="minipage")
        slide_text_8_mo = Tex(fr"{{7.75cm}}\RaggedRight{{{slide_text_8}}}", 
                           font_size=28, tex_environment="minipage")
        slide_text_9_mo = Tex(fr"{{7.75cm}}\RaggedRight{{{slide_text_9}}}", 
                           font_size=28, tex_environment="minipage")
        slide_text_5_mo.to_corner(UL, buff=0.5).shift(DOWN).shift(RIGHT*8)
        slide_text_6_mo.next_to(slide_text_5_mo, DOWN, aligned_edge=LEFT, buff=0.25).shift(RIGHT * 0.25)
        slide_text_7_mo.next_to(slide_text_6_mo, DOWN, aligned_edge=LEFT, buff=0.25)
        slide_text_7b_mo.next_to(slide_text_7_mo, DOWN, aligned_edge=LEFT, buff=0.25)
        slide_text_8_mo.next_to(slide_text_7b_mo, DOWN, aligned_edge=LEFT, buff=0.25)
        slide_text_9_mo.next_to(slide_text_8_mo, DOWN, aligned_edge=LEFT, buff=0.25).shift((LEFT + DOWN) * 0.25)

        arrow1 = Arrow(start=slide_text_3b_mo.get_edge_center(RIGHT)+RIGHT*0.25, end=slide_text_5_mo.get_edge_center(LEFT)+LEFT*0.25,tip_length=0.2,color=GOLD,stroke_width=4)
        arrow2 = Arrow(start=slide_text_3b_mo.get_edge_center(RIGHT)+RIGHT*0.25, end=slide_text_6_mo.get_edge_center(LEFT)+LEFT*0.25,tip_length=0.2,color=GOLD,stroke_width=4)
        arrow3 = Arrow(start=slide_text_4b_mo.get_edge_center(RIGHT)+RIGHT*0.25, end=slide_text_7_mo.get_edge_center(LEFT)+LEFT*0.25,tip_length=0.2,color=GOLD,stroke_width=4)
        arrow3b = Arrow(start=slide_text_4b_mo.get_edge_center(RIGHT)+RIGHT*0.25, end=slide_text_7b_mo.get_edge_center(LEFT)+LEFT*0.25,tip_length=0.2,color=GOLD,stroke_width=4)
        arrow4 = Arrow(start=slide_text_5b_mo.get_edge_center(RIGHT)+RIGHT*0.25, end=slide_text_8_mo.get_edge_center(LEFT)+LEFT*0.25,tip_length=0.2,color=GOLD,stroke_width=4)

        self.play(LaggedStart(Create(box1,run_time=0.5), GrowArrow(arrow1), Write(slide_text_5_mo,run_time=0.5), lag_ratio=0.5))

        self.wait(0.1)
        self.next_slide(notes="We call this the Hamiltonian and the H_alpha's the local hamiltonians.")

        self.play(LaggedStart(Transform(arrow1,arrow2,run_time=0.5), Write(slide_text_6_mo, run_time=0.5),lag_ratio=0.5))
        self.remove(arrow1,arrow2)
        self.add(arrow2)

        self.wait(0.1)
        self.next_slide(notes="the quantity of most importance is teh quadratic form, which we call the energy. Instead of taking the quadratic form over only computation basis vectors we consider arbitrary states.")

        self.play(LaggedStart(AnimationGroup(Uncreate(arrow2, run_time=0.5), Uncreate(box1, run_time=0.5), Create(box2, run_time=0.5)),
                              GrowArrow(arrow3, run_time=0.5), 
                              Write(slide_text_7_mo, run_time=0.5), lag_ratio=0.5))
        
        self.wait(0.1)
        self.next_slide()

        self.play(LaggedStart(Transform(arrow3,arrow3b,run_time=0.5), Write(slide_text_7b_mo, run_time=0.5),lag_ratio=0.5))
        self.remove(arrow3,arrow3b)
        self.add(arrow3b)

        self.wait(0.1)
        self.next_slide(notes="the quantity of most importance is teh quadratic form, which we call the energy. Instead of taking the quadratic form over only computation basis vectors we consider arbitrary states.")

        # self.play(Create(box2, rate_func=lambda t: 1 - t), Create(box3), Write(slide_text_8_mo), run_time=0.5)
        self.play(LaggedStart(AnimationGroup(Uncreate(arrow3b, run_time=0.5), Uncreate(box2, run_time=0.5), Create(box3, run_time=0.5)),
                              GrowArrow(arrow4, run_time=0.5), 
                              Write(slide_text_8_mo, run_time=0.5), lag_ratio=0.5))
        self.wait(0.1)

        self.wait(0.1)
        self.next_slide()

        self.play(Uncreate(arrow4), Uncreate(box3), Write(slide_text_9_mo), run_time=0.5)
        self.wait(0.1)


class QuantumMaxCut(Slide):
    def setup(self):
        theme = "Monokai Pro Light" # select a theme from https://iterm2colorschemes.com
        apply_theme(manim_scene=self, theme_name=theme, light_theme=True) # use the theme


    def construct(self):
        title = FancyTitle("Quantum Max-Cut")
        self.play(title.anim())

        self.wait(0.1)
        self.next_slide(notes="Lets dissect this a little.")

        slide_text_1 = Tex(r"{8cm}Quantum Max-Cut is a 2-local Hamiltonian problem defined over a graph, \(G = (V,E,w)\).", 
                           font_size=28, tex_environment="minipage")
        slide_text_2 = MathTex(r"H = \sum_{(a,b) \in E} w_{(a,b)} \overbrace{\frac{1}{2}\left(\ket{01}-\ket{10}\right)\left(\bra{01}-\bra{10}\right)^{ab} \otimes I^{[n]\setminus\{a,b\} } }^{h_{(a,b)}", font_size=28)
        slide_text_1.to_corner(UL, buff=0.5).shift(DOWN)
        slide_text_2.next_to(slide_text_1, DOWN, buff=0.5)

        nxG = nx.Graph()
        nxG.add_edges_from([(1,2),(2,3),(3,4),(1,4),(3,5),(4,5)])
        sl = nx.spring_layout(nxG, seed=1, scale=2)
        sl2 = {k: [x, y, 0] for k, (x, y) in sl.items()}
        G = Graph.from_networkx(nxG, layout=sl2,vertex_config={
                "radius": 0.15,
            }).shift(RIGHT * 4).shift(UP*1.5)

        vertex_labels = VGroup(*[
            MathTex(str(v)).next_to(G[v], RIGHT*0.1).shift(UP * 0.1 if str(v) == "3" else UP * 0.0).scale(0.5)
            for v in G.vertices
        ])

        self.play(LaggedStart(Write(slide_text_1, run_time=1), Create(G, run_time=1), Write(slide_text_2, run_time=1), lag_ratio=0.5))
        self.play(*[Write(item) for item in vertex_labels], run_time=0.25)

        self.wait(0.1)
        self.next_slide(notes="Lets dissect this a little. Recall Max-cut... We use this notation to denote the outer product.")

        slide_text_3 = Tex(r"{8cm}Recall, in Max-Cut, the local terms (as matrices), were projectors onto the ``different'' subspace: \(\Span\{\ket{01},\ket{10}\}\)", 
                           font_size=28, tex_environment="minipage")
        slide_text_4 = MathTex(r"\calC_{(a,b)} = \ket{01}\bra{10} + \ket{10}\bra{10}", 
                           font_size=28)
        slide_text_3.next_to(slide_text_1, DOWN, aligned_edge=LEFT, buff=3)
        slide_text_4.next_to(slide_text_3, DOWN, buff=0.5)

        self.play(Write(slide_text_3),Write(slide_text_4), run_time=0.5)

        self.wait(0.1)
        self.next_slide(notes="In QMC we not only want the state to be in the \"different\" subspace but we also want there to be this quantum anti-correlation between the two ways of being different. This is called the antisymmetric subspace and is of extreme important in the study of quantum information.")

        slide_text_5 = Tex(r"{8cm}In Quantum Max-Cut, the local terms are projectors onto the \emph{antisymmetric subspace} subspace: \(\Span\{\ket{01}-\ket{10}\}\)", 
                           font_size=28, tex_environment="minipage")
        slide_text_6 = MathTex(r"h_{(a,b)} = \frac{1}{2}\left(\ket{01}-\ket{10}\right)\left(\bra{01}-\bra{10}\right)", 
                           font_size=28)
        slide_text_5.next_to(slide_text_1, DOWN, aligned_edge=LEFT, buff=3).shift(RIGHT*8)
        slide_text_6.next_to(slide_text_5, DOWN, buff=0.5)

        self.play(Write(slide_text_5),Write(slide_text_6), run_time=0.5)
        self.wait(0.1)


class WhyCare(Slide):
    def setup(self):
        theme = "Monokai Pro Light" # select a theme from https://iterm2colorschemes.com
        apply_theme(manim_scene=self, theme_name=theme, light_theme=True) # use the theme


    def construct(self):
        title = FancyTitle("Why Care About Approximations for LHPs")
        self.play(title.anim())

        slide_text_1 = r"1 Classically, we have developed a lot of tools and understanding for approximation algorithms."
        slide_text_1a = r".a There are optimality results for certain algorithms (assuming UGC) [KKMO07]."

        slide_text_2 = r"2 Quantumly, understanding the limits of approximation algorithms for local Hamiltonian problems (LHPs) is at the intersection of mathematics, theoretical computer science, and condensed matter physics."
        slide_text_2a = r".a Approximations for LHPs are not well understood. For example there is no quantum PCP theorem (just a conjecture) [AAV13; NN24]."
        slide_text_2b = r".b For LHP beyond qubits, there isn't a good candidate problem to study."
        slide_text_2bi = r"...i A lot of things break down in the quantum setting in ways that are unlike the classical setting."

        bullets = Bullets(slide_text_1,slide_text_1a,slide_text_2,slide_text_2a,slide_text_2b,slide_text_2bi,
                          double_space_for_new_sections=True)
        for _ in range(bullets.get_num_lines()):
            self.wait(0.1)
            self.next_slide()
            self.play(bullets.write_next_line(run_time=0.5))

        self.wait(0.1)


class ALittleMoreQuantum(Slide):
    def setup(self):
        theme = "Monokai Pro Light" # select a theme from https://iterm2colorschemes.com
        apply_theme(manim_scene=self, theme_name=theme, light_theme=True) # use the theme


    def construct(self):
        title = FancyTitle("A Little More Quantum")
        self.play(title.anim())

        self.wait(0.1)
        self.next_slide()

        slide_text_1 = Tex(r"{16cm}Often, we write the energy of \(\ket{\psi}\) as \(\Tr(\ket{\psi}\bra{\psi} H) = \bra{\psi} H \ket{\psi}\).", 
                           font_size=28, tex_environment="minipage")
        slide_text_2 = Tex(r"{15.75cm}\(\rightarrow\) Indeed, we often identify a quantum state by a projector onto a one-dimensional subspace, \(\ket{\psi}\bra{\psi}\).", 
                           font_size=28, tex_environment="minipage")
        slide_text_1.to_corner(UL, buff=0.5).shift(DOWN)
        slide_text_2.next_to(slide_text_1, DOWN, aligned_edge=LEFT, buff=0.25).shift(RIGHT * 0.25)

        self.play(Write(slide_text_1), run_time=0.5)

        self.wait(0.1)
        self.next_slide()

        self.play(Write(slide_text_2), run_time=1)

        self.wait(0.1)
        self.next_slide()

        slide_text_3a = Tex(r"{16cm}\textbf{Mixed State/Density Matrix:} A ``classical mixture'' of quantum states.", 
                           font_size=28, tex_environment="minipage")
        slide_text_3b = Tex(r"{16cm}\textbf{Mixed State/Density Matrix:} A matrix, \(\rho \in M_{d^n}(\C)\), that is non-negative, \(\rho \succcurlyeq 0\), and has unit trace, \(\Tr(\rho) = 1\).", 
                           font_size=28, tex_environment="minipage")
        slide_text_3a.next_to(slide_text_2, DOWN, aligned_edge=LEFT, buff=0.25).shift(LEFT * 0.25)
        slide_text_3b.next_to(slide_text_2, DOWN, aligned_edge=LEFT, buff=0.25).shift(LEFT * 0.25)

        self.play(Write(slide_text_3a), run_time=1)

        self.wait(0.1)
        self.next_slide()

        convex_comb_states = MathTex(r"\rho = \sum_i \lambda_i \ket{\psi_i}\bra{\psi_i}").shift(DOWN*1.5)
        pure_state = MathTex(r"\ket{\psi}\bra{\psi}").next_to(convex_comb_states, LEFT, buff=2)
        non_neg_const_a = MathTex(r"\forall i: \lambda_i \geq 0").next_to(convex_comb_states, RIGHT, buff=2).shift(UP*1)
        non_sum_1_const_a = MathTex(r"\sum_i \lambda_i = 1").next_to(non_neg_const_a, DOWN, buff=1)
        non_neg_const_b = MathTex(r"\rho \succcurlyeq 0").move_to(non_neg_const_a)
        non_sum_1_const_b = MathTex(r"\Tr(\rho) = 1").move_to(non_sum_1_const_a)

        pure_state_text = Tex(r"Pure State",font_size=28).next_to(pure_state, UP, buff=0.5)
        convex_comb_states_text = Tex(r"Convex Combination",font_size=28).next_to(convex_comb_states, UP, buff=0.5)
        posit_text = Tex(r"Positivity",font_size=28).next_to(non_neg_const_a, UP, buff=0.2)
        unit_tr_text = Tex(r"Unit Trace",font_size=28).next_to(non_sum_1_const_a, UP, buff=0.2)

        self.play(Write(pure_state), Write(pure_state_text),run_time=0.5)

        self.wait(0.1)
        self.next_slide()

        self.play(Write(convex_comb_states), Write(convex_comb_states_text),run_time=0.5)

        self.wait(0.1)
        self.next_slide()

        self.play(Write(non_neg_const_a), Write(posit_text), run_time=0.5)
        self.play(Write(non_sum_1_const_a), Write(unit_tr_text), run_time=0.5)

        self.wait(0.1)
        self.next_slide()

        self.play(TransformMatchingShapes(non_neg_const_a,non_neg_const_b), run_time = 0.5)

        self.wait(0.1)
        self.next_slide()

        self.play(TransformMatchingShapes(non_sum_1_const_a,non_sum_1_const_b), run_time = 0.5)

        self.wait(0.1)
        self.next_slide()

        convex_comb_stuff = [convex_comb_states,pure_state,non_neg_const_b,non_sum_1_const_b,pure_state_text,convex_comb_states_text,posit_text,unit_tr_text]
        animations = [
            item.animate.scale(0.1).move_to(slide_text_3b).set_opacity(0)
            for item in convex_comb_stuff
        ]
        self.play(*animations,TransformMatchingTex(slide_text_3a,slide_text_3b))
        self.remove(*convex_comb_stuff)

        self.wait(0.1)
        self.next_slide()

        slide_text_4 = Tex(r"{15.75cm}\(\rightarrow\) The energy of \(\rho\) is the ``expected'' energy over the pure states in the mixture: \\\begin{center}\(\Tr(\rho H) = \sum_i \lambda_i \Tr(\ket{\psi_i}\bra{\psi_i} H)\)\end{center}", 
                           font_size=28, tex_environment="minipage")
        slide_text_4.next_to(slide_text_3b, DOWN, aligned_edge=LEFT, buff=0.25).shift(RIGHT * 0.25)

        self.play(Write(slide_text_4), run_time=0.5)

        self.wait(0.1)
        self.next_slide()

        slide_text_5 = Tex(r"{15.75cm}\(\rightarrow\) Mixed states show up as marginals of pure states. Consider the marginal on the first qubit of the\\\phantom{\(\rightarrow\)} antisymmetric state.", 
                           font_size=28, tex_environment="minipage")
        slide_text_5.next_to(slide_text_4, DOWN, aligned_edge=LEFT, buff=0.5)

        self.play(Write(slide_text_5), run_time=0.5)

        self.wait(0.1)
        self.next_slide()

        singlet_state = MathTex(r"\rho = \frac{1}{2}({{\ket{01} }}-{{\ket{10} }})({{\bra{01} }}-{{\bra{10} }})",font_size=28).shift(DOWN*2)

        singlet_state_expanded = MathTex(r"\rho = \frac{1}{2}({{\ket{01} }}{{\bra{01} }} - {{\ket{01} }}{{\bra{10} }} - {{\ket{10} }}{{\bra{01} }} + {{\ket{10} }}{{\bra{10} }})",font_size=28).move_to(singlet_state)
        singlet_state_expanded_2 = MathTex(r"\rho = \frac{1}{2}(", r"\ket{01}\bra{01}", r"- \ket{01}\bra{10} - \ket{10}\bra{01} + \ket{10}\bra{10})",font_size=28).move_to(singlet_state)

        singlet_state_expanded_3 = MathTex(r"\rho = \frac{1}{2}(", r"\ket{0}\bra{0} \otimes \ket{1}\bra{1}", r"- \ket{01}\bra{10} - \ket{10}\bra{01} + \ket{10}\bra{10})",font_size=28).move_to(singlet_state)
        singlet_state_expanded_4 = MathTex(r"\rho = \frac{1}{2}(", r"\ket{0}\bra{0} \otimes \ket{1}\bra{1}", r"-\ket{01}\bra{10}", r"- \ket{10}\bra{01}", r" + \ket{10}\bra{10})",font_size=28).move_to(singlet_state)

        singlet_state_expanded_5 = MathTex(r"\rho = \frac{1}{2}(", r"\ket{0}\bra{0} \otimes \ket{1}\bra{1}", r"- \ket{0}\bra{1} \otimes \ket{1}\bra{0}", r"- \ket{1}\bra{0} \otimes \ket{0}\bra{1}", r"+ \ket{1}\bra{1} \otimes \ket{0}\bra{0})",font_size=28).move_to(singlet_state)

        singlet_state_rdm = MathTex(r"\rho^1 = \frac{1}{2}(", r"\ket{0}\bra{0}", r"+ \ket{1}\bra{1})",font_size=28).next_to(singlet_state_expanded_5,DOWN,aligned_edge=LEFT,buff=0.25)

        max_mix_state = MathTex(r"= \frac{1}{2} I",font_size=28).next_to(singlet_state_rdm,RIGHT,buff=0.2)

        self.play(Write(singlet_state),run_time=0.5)
        
        self.wait(0.1)
        self.next_slide()
        
        self.play(TransformMatchingTex(singlet_state,singlet_state_expanded))
        self.add(singlet_state_expanded_2)
        self.remove(singlet_state_expanded)
        
        self.wait(0.1)
        self.next_slide()
        
        self.play(Transform(singlet_state_expanded_2[0],singlet_state_expanded_3[0]),
                  TransformMatchingShapes(singlet_state_expanded_2[1],singlet_state_expanded_3[1]),
                  Transform(singlet_state_expanded_2[2],singlet_state_expanded_3[2]))
        self.add(singlet_state_expanded_4)
        self.remove(singlet_state_expanded_3,singlet_state_expanded_3[0],singlet_state_expanded_3[1],singlet_state_expanded_3[2],
                    singlet_state_expanded_2[0],singlet_state_expanded_2[1],singlet_state_expanded_2[2])
        
        self.wait(0.1)
        self.next_slide()
        
        self.play(LaggedStart(Transform(singlet_state_expanded_4[0],singlet_state_expanded_5[0]),
                              Transform(singlet_state_expanded_4[1],singlet_state_expanded_5[1]),
                              TransformMatchingShapes(singlet_state_expanded_4[2],singlet_state_expanded_5[2]),
                              TransformMatchingShapes(singlet_state_expanded_4[3],singlet_state_expanded_5[3]),
                              TransformMatchingShapes(singlet_state_expanded_4[4],singlet_state_expanded_5[4]),lag_ratio=0.15))
        
        self.remove(singlet_state_expanded_4[2],singlet_state_expanded_4[3],singlet_state_expanded_4[4]) # because annoying 
        self.wait(0.1)

        self.wait(0.1)
        self.next_slide()

        cross1a = Line(
            singlet_state_expanded_5[1].get_corner(UL) + RIGHT * 0.75, singlet_state_expanded_5[1].get_corner(DR),
            color=RED, stroke_width=6
        )
        cross1b = Line(
            singlet_state_expanded_5[1].get_corner(DL) + RIGHT * 0.75, singlet_state_expanded_5[1].get_corner(UR),
            color=RED, stroke_width=6
        )
        cross2a = Line(
            singlet_state_expanded_5[2].get_corner(UL), singlet_state_expanded_5[2].get_corner(DR),
            color=RED, stroke_width=6
        )
        cross2b = Line(
            singlet_state_expanded_5[2].get_corner(DL), singlet_state_expanded_5[2].get_corner(UR),
            color=RED, stroke_width=6
        )
        cross3a = Line(
            singlet_state_expanded_5[3].get_corner(UL), singlet_state_expanded_5[3].get_corner(DR),
            color=RED, stroke_width=6
        )
        cross3b = Line(
            singlet_state_expanded_5[3].get_corner(DL), singlet_state_expanded_5[3].get_corner(UR),
            color=RED, stroke_width=6
        )
        cross4a = Line(
            singlet_state_expanded_5[4].get_corner(UL) + RIGHT, singlet_state_expanded_5[4].get_corner(DR),
            color=RED, stroke_width=6
        )
        cross4b = Line(
            singlet_state_expanded_5[4].get_corner(DL) + RIGHT, singlet_state_expanded_5[4].get_corner(UR),
            color=RED, stroke_width=6
        )

        sse5a_copy = singlet_state_expanded_5[0].copy()
        sse5b_copy = singlet_state_expanded_5[1].copy()
        sse5c_copy = singlet_state_expanded_5[4].copy()

        self.play(LaggedStart(AnimationGroup(Create(cross1a),Create(cross1b)),
                              AnimationGroup(Create(cross2a),Create(cross2b)),
                              AnimationGroup(Create(cross3a),Create(cross3b)),
                              AnimationGroup(Create(cross4a),Create(cross4b)),lag_ratio=0.15))

        self.play(LaggedStart(TransformMatchingShapes(sse5a_copy,singlet_state_rdm[0]),
                              TransformMatchingShapes(sse5b_copy,singlet_state_rdm[1]),
                              TransformMatchingShapes(sse5c_copy,singlet_state_rdm[2]),lag_ratio=0.15))

        self.wait(0.1)
        self.next_slide()

        self.play(Write(max_mix_state),run_time=0.5)
        self.wait(0.1)
        self.next_slide()

        slide_text_6 = Tex(r"{15.75cm}\(\rightarrow\) A pure state is entangled exactly when its marginals are mixed.", 
                           font_size=28, tex_environment="minipage")
        slide_text_6.next_to(slide_text_5, DOWN, aligned_edge=LEFT, buff=2.5)

        self.play(Write(slide_text_6),run_time=0.5)

        self.wait(0.1)


class ALittleMoreQuantum2(Slide):
    def setup(self):
        theme = "Monokai Pro Light" # select a theme from https://iterm2colorschemes.com
        apply_theme(manim_scene=self, theme_name=theme, light_theme=True) # use the theme


    def construct(self):
        title = FancyTitle("Even More Quantum")
        self.play(title.anim())

        self.wait(0.1)
        self.next_slide()

        slide_text_1 = Tex(r"{16cm}\textbf{Maximally Entangled State:} A pure state, \(\ket{\psi}\bra{\psi}\), is said to be maximally entangled if its reduced marginals are the maximally mixed state, \(\frac{1}{d} I = \frac{1}{d}\sum_{i \in [d]}\ket{i}\bra{i}\).", 
                           font_size=28, tex_environment="minipage")
        slide_text_2 = Tex(r"{16cm}\textbf{The Maximal Entanglement Problem:} We consider the 2-local Hamiltonian Problem \emph{over qudits}, where each local term is a projector into a maximally entangled state, \(h_e = \ket{\psi_e}\bra{\psi_e}\) (\(\ket{\psi_e} \in (\C^d)^{\otimes 2}\)).", 
                           font_size=28, tex_environment="minipage")
        slide_text_3 = Tex(r"{16cm}\textbf{Monogamy of Entanglement:} The idea that one system cannot be maximally entangled to multiple other systems at the same time.", 
                           font_size=28, tex_environment="minipage")
        slide_text_1.to_corner(UL, buff=0.5).shift(DOWN)
        slide_text_2.next_to(slide_text_1, DOWN, aligned_edge=LEFT, buff=0.25)
        slide_text_3.next_to(slide_text_2, DOWN, aligned_edge=LEFT, buff=0.25)

        self.play(Write(slide_text_1), run_time=0.5)

        self.wait(0.1)
        self.next_slide()

        self.play(Write(slide_text_2), run_time=0.5)

        self.wait(0.1)
        self.next_slide()

        self.play(Write(slide_text_3), run_time=0.5)

        self.wait(0.1)
        self.next_slide()

        nxG_star = nx.Graph()
        nxG_star.add_edges_from([(1,2),(1,3),(1,4),(1,5),(1,6)])
        sl = nx.spring_layout(nxG_star, seed=1, scale=2)
        sl2 = {k: [x, y, 0] for k, (x, y) in sl.items()}
        G_star = Graph.from_networkx(nxG_star, layout=sl2,vertex_config={
                "radius": 0.15,
            }).shift(DOWN*1.5).shift(RIGHT*2)
        
        v_copies = []
        for v in G_star.vertices:
            G_star[v].set_color(GOLD)
            v_copies.append(G_star[v].copy())
        v_copies = VGroup(*v_copies)

        vertex_labels = VGroup(*[
            MathTex(str(v)).next_to(G_star[v], RIGHT*0.1).shift(UP * 0.15 if str(v) == "1" else UP * 0.0).scale(0.5)
            for v in G_star.vertices
        ])

        edge_labels = VGroup(*[
            MathTex(f"\\ket{{\\psi_{max(uv)}}}\\bra{{\\psi_{max(uv)}}}",
                    color=GREEN).move_to(edge.get_center()).scale(0.5).rotate(edge.get_angle()+(PI if uv == (1,2) or uv == (1,4) else 0)).shift(0.2 * rotate_vector(UP, edge.get_angle() + (PI if uv == (1,2) or uv == (1,4) else 0)))
            for uv, edge in G_star.edges.items()
        ])
        edge_label_copy = edge_labels.copy()

        energy_text = MathTex(r"\sum_{i=2}^6\Tr(",r"\rho",r"\ket{\psi_i}\bra{\psi_i}^{1i}",")").next_to(G_star,LEFT,buff=2)
        less_5_text = MathTex(r"< 5").next_to(energy_text,RIGHT,buff=0.2)
        less_3_text = MathTex(r"\leq 3").next_to(energy_text,RIGHT,buff=0.2)
        astr = MathTex(r"^\ast", font_size=28,color=TEAL_D).next_to(less_3_text,RIGHT).shift(LEFT*0.1+UP*0.2)
        whend2_text = Tex(r"\(^*\)When \(d=2\)", font_size=28,color=TEAL_D).next_to(less_3_text,DOWN,aligned_edge=RIGHT,buff=1)
        energy_text[1].set_color(GOLD)
        energy_text[2].set_color(GREEN)

        self.play(Create(G_star), run_time=1)
        self.play(LaggedStart(*[Write(item, run_time=0.25) for item in vertex_labels],lag_ratio=0.2))
        self.play(LaggedStart(*[Write(item, run_time=0.25) for item in edge_labels], lag_ratio=0.3))
        self.play(Transform(v_copies,energy_text[1]),Transform(edge_label_copy,energy_text[2]),Write(energy_text,run_time=1))

        self.wait(0.1)
        self.next_slide()

        self.play(Write(less_5_text), run_time=0.25)

        self.wait(0.1)
        self.next_slide()

        self.play(LaggedStart(Transform(less_5_text,less_3_text,run_time=0.25), Write(astr), Write(whend2_text), lag_ratio=0.75))

        self.wait(0.1)


class ALittleMoreQuantum2Video(Scene):
    def setup(self):
        theme = "Monokai Pro Light" # select a theme from https://iterm2colorschemes.com
        apply_theme(manim_scene=self, theme_name=theme, light_theme=True) # use the theme


    def construct(self):
        nxG_star = nx.Graph()
        nxG_star.add_edges_from([(1,2),(1,3),(1,4),(1,5),(1,6)])
        sl = nx.spring_layout(nxG_star, seed=1, scale=2)
        sl2 = {k: [x, y, 0] for k, (x, y) in sl.items()}
        G_star = Graph.from_networkx(nxG_star, layout=sl2,vertex_config={
                "radius": 0.15,
            }).shift(UP*1)
        
        v_copies = []
        for v in G_star.vertices:
            G_star[v].set_color(GOLD)
            v_copies.append(G_star[v].copy())
        v_copies = VGroup(*v_copies)

        vertex_labels = VGroup(*[
            MathTex(str(v)).next_to(G_star[v], RIGHT*0.1).shift(UP * 0.15 if str(v) == "1" else UP * 0.0).scale(0.5)
            for v in G_star.vertices
        ])

        edge_labels = VGroup(*[
            MathTex(f"\\ket{{\\psi_{max(uv)}}}\\bra{{\\psi_{max(uv)}}}",
                    color=GREEN).move_to(edge.get_center()).scale(0.5).rotate(edge.get_angle()+(PI if uv == (1,2) or uv == (1,4) else 0)).shift(0.2 * rotate_vector(UP, edge.get_angle() + (PI if uv == (1,2) or uv == (1,4) else 0)))
            for uv, edge in G_star.edges.items()
        ])
        edge_label_copy = edge_labels.copy()

        energy_text = MathTex(r"\sum_{i=2}^6\Tr(",r"\rho",r"\ket{\psi_i}\bra{\psi_i}^{1i}",")").next_to(G_star,DOWN,buff=0.5).shift(LEFT)
        less_5_text = MathTex(r"\leq \frac{n+d-2}{d}").next_to(energy_text,RIGHT,buff=0.2)
        energy_text[1].set_color(GOLD)
        energy_text[2].set_color(GREEN)

        self.play(Create(G_star), run_time=1)
        self.play(LaggedStart(*[Write(item, run_time=0.25) for item in vertex_labels],lag_ratio=0.2))
        self.play(LaggedStart(*[Write(item, run_time=0.25) for item in edge_labels], lag_ratio=0.3))
        self.play(Transform(v_copies,energy_text[1]),Transform(edge_label_copy,energy_text[2]),Write(energy_text,run_time=1))

        self.play(Write(less_5_text), run_time=0.5)

        self.wait(1)


class BabysFirstProofTheStarBound(Slide):
    def setup(self):
        theme = "Monokai Pro Light" # select a theme from https://iterm2colorschemes.com
        apply_theme(manim_scene=self, theme_name=theme, light_theme=True) # use the theme


    def construct(self):
        nxG_star = nx.Graph()
        nxG_star.add_edges_from([(1,2),(1,3),(1,4),(1,5),(1,6)])
        sl = nx.spring_layout(nxG_star, seed=1, scale=2)
        sl2 = {k: [x, y, 0] for k, (x, y) in sl.items()}
        G_star = Graph.from_networkx(nxG_star, layout=sl2,vertex_config={
                "radius": 0.15,
            }).shift(DOWN*1.5).shift(RIGHT*2)
        
        v_copies = []
        for v in G_star.vertices:
            G_star[v].set_color(GOLD)
            v_copies.append(G_star[v].copy())
        v_copies = VGroup(*v_copies)

        vertex_labels = VGroup(*[
            MathTex(str(v)).next_to(G_star[v], RIGHT*0.1).shift(UP * 0.15 if str(v) == "1" else UP * 0.0).scale(0.5)
            for v in G_star.vertices
        ])

        edge_labels = VGroup(*[
            MathTex(f"\\ket{{\\psi_{max(uv)}}}\\bra{{\\psi_{max(uv)}}}",
                    color=GREEN).move_to(edge.get_center()).scale(0.5).rotate(edge.get_angle()+(PI if uv == (1,2) or uv == (1,4) else 0)).shift(0.2 * rotate_vector(UP, edge.get_angle() + (PI if uv == (1,2) or uv == (1,4) else 0)))
            for uv, edge in G_star.edges.items()
        ])

        star_graph_all = VGroup(G_star,*vertex_labels,*edge_labels)

        self.add(star_graph_all)
        
        title = FancyTitle("The Star Bound")
        self.play(title.anim(),AnimationGroup(star_graph_all.animate.scale(0.75).shift(RIGHT * 2.5 + UP * 4), run_time=0.5))

        slide_text_1 = MathTex(r"H_\bigstar = \sum_{a=2}^n \ket{\psi_a}\bra{\psi_a}^{1a}", 
                           font_size=28)
        slide_text_2 = Tex(r"\textbf{Lemma:} \(\eig_{\max}(H_\bigstar) = \frac{n-1}{d}+\frac{d-1}{d}\), in particular, ", r"\(\frac{n+d-2}{d}I - H_\bigstar\)", r"\(\succcurlyeq 0\).", 
                           font_size=28)
        slide_text_1.to_corner(UL, buff=0.5).shift(DOWN)
        slide_text_2.next_to(slide_text_1, DOWN, aligned_edge=LEFT, buff=0.25)
        
        slide_text_1.to_corner(UL, buff=0.5).shift(DOWN)
        # slide_text_2.next_to(slide_text_1, DOWN, aligned_edge=LEFT, buff=0.25)
        # slide_text_3.next_to(slide_text_2, DOWN, aligned_edge=LEFT, buff=0.25)

        base_line_text = Tex(r"Product state energy.", font_size=20, color=GREEN_E).next_to(slide_text_2,UP,aligned_edge=LEFT,buff=0.25).shift(RIGHT*3.4)
        surplus_text = Tex(r"Must come from entanglement.", font_size=20, color=GREEN_E).next_to(base_line_text, RIGHT, buff=0.5).shift(LEFT*1.55)
        
        braces = Tex(r"\(\overbrace{\phantom{\frac{n-1}{d} } }\phantom{+}\overbrace{\phantom{\frac{d-1}{d} } }\)", font_size=22, color=GREEN_E).next_to(slide_text_2,UP,aligned_edge=LEFT,buff=0).shift(RIGHT*3.15)
        
        base_line_text.rotate(PI/8,about_point=base_line_text.get_corner(DL))
        surplus_text.rotate(PI/8,about_point=surplus_text.get_corner(DL))


        self.wait(0.1)
        self.next_slide()

        self.play(Write(slide_text_1), run_time=0.5)

        self.wait(0.1)
        self.next_slide()

        self.play(Write(slide_text_2), run_time=0.5)

        self.wait(0.1)
        self.next_slide()

        self.play(LaggedStart(Write(braces,run_time=0.5),
                              Write(base_line_text,run_time=0.5),
                              Write(surplus_text,run_time=0.5),lag_ratio=0.5))

        self.wait(0.1)
        self.next_slide()

        proof_text = Tex(r"\emph{Proof (Sketch):}", font_size=28).next_to(slide_text_2, DOWN, aligned_edge=LEFT, buff=0.5)

        # star_bound_proof_1 = MathTex(r"H_\bigstar = \sum_{a=2}^n \left(\ket{\psi_a}\bra{\psi_a}^{1a}\right)^2", font_size=28).next_to(slide_text_2, DOWN, aligned_edge=LEFT, buff=0.5)
        star_bound_proof_1 = MathTex(r"(H_\bigstar)^2", r"= \sum_{a=2}^n \left(\ket{\psi_a}\bra{\psi_a}^{1a}\right)^2" ,r"+ \sum_{2 \leq a < b \leq n}", r"\left(\ket{\psi_a}\bra{\psi_a}^{1a} \ket{\psi_b}\bra{\psi_b}^{1b} + \ket{\psi_b}\bra{\psi_b}^{1b} \ket{\psi_a}\bra{\psi_a}^{1a}\right)",
                                     font_size=28).next_to(proof_text, DOWN, aligned_edge=LEFT, buff=0.25)
        star_bound_proof_2 = MathTex(r"= \sum_{a=2}^n \ket{\psi_a}\bra{\psi_a}^{1a}", r"+ \sum_{2 \leq a < b \leq n}", r"\frac{1}{d} \Big(\ket{\psi_a}\bra{\psi_a}^{1a} + \ket{\psi_b}\bra{\psi_b}^{1b} - \frac{2(d-1)}{d} P_{1ab}^{1ab}\Big)",
                                     font_size=28).next_to(star_bound_proof_1[1],DOWN,aligned_edge=LEFT,buff=0.25)
        star_bound_proof_3 = MathTex(r"\left(P_{1ab}^{1ab}\right)^2 = P_{1ab}^{1ab}",font_size=28).next_to(star_bound_proof_2,RIGHT,buff=1)
        star_bound_proof_2b = MathTex(r"= \sum_{a=2}^n \ket{\psi_a}\bra{\psi_a}^{1a} +", r"\sum_{2 \leq a < b \leq n}", r"\frac{1}{d} \Big(", r"\ket{\psi_a}\bra{\psi_a}^{1a} + \ket{\psi_b}\bra{\psi_b}^{1b}", r"- \frac{2(d-1)}{d} P_{1ab}^{1ab}\Big)",
                                     font_size=28).next_to(star_bound_proof_1[1],DOWN,aligned_edge=LEFT,buff=0.25)
        star_bound_proof_4 = MathTex(r"= H_\bigstar +", r"\frac{n-2}{d}H_\bigstar", r"- \frac{2(d-1)}{d^2} \sum_{2 \leq a < b \leq n} P_{1ab}^{1ab}",
                                     font_size=28).next_to(star_bound_proof_2,DOWN,aligned_edge=LEFT,buff=0.25)
        star_bound_proof_5 = MathTex(r"(H_\bigstar)^2 = ", r"\left(\frac{n+d-2}{d}\right)H_\bigstar", r"- \frac{2(d-1)}{d^2} \sum_{2 \leq a < b \leq n} P_{1ab}^{1ab}",
                                     font_size=28).next_to(star_bound_proof_1,DOWN,aligned_edge=LEFT)
        star_bound_proof_5.shift(DOWN * (abs(star_bound_proof_5.get_bottom() - star_bound_proof_1.get_top()) + 0.25))
        star_bound_proof_5b = MathTex(r"(H_\bigstar)^2 = ", r"\left(\frac{n+d-2}{d}\right)H_\bigstar - \frac{2(d-1)}{d^2} \sum_{2 \leq a < b \leq n} P_{1ab}^{1ab}",
                                     font_size=28).next_to(star_bound_proof_1,DOWN,aligned_edge=LEFT).move_to(star_bound_proof_5)
        
        self.play(Write(proof_text),run_time=0.5)

        self.wait(0.1)
        self.next_slide()

        self.play(Write(star_bound_proof_1[0]),run_time=0.25)

        self.wait(0.1)
        self.next_slide()

        self.play(Write(star_bound_proof_1[1:]),run_time=0.5)

        self.wait(0.1)
        self.next_slide()

        star_bound_proof_11_copy = star_bound_proof_1[1].copy()
        self.play(TransformMatchingShapes(star_bound_proof_11_copy,star_bound_proof_2[0]))

        self.wait(0.1)
        self.next_slide()

        star_bound_proof_12_copy = star_bound_proof_1[2].copy()
        star_bound_proof_13_copy = star_bound_proof_1[3].copy()
        self.play(LaggedStart(TransformMatchingShapes(star_bound_proof_12_copy,star_bound_proof_2[1]),
                              TransformMatchingShapes(star_bound_proof_13_copy,star_bound_proof_2[2]),lag_ratio=0.25))
        self.add(star_bound_proof_2b)
        self.wait(0.5)
        self.play(Write(star_bound_proof_3),run_time=0.5)

        self.wait(0.1)
        self.next_slide()
        
        self.play(LaggedStart(TransformMatchingShapes(star_bound_proof_2b[0],star_bound_proof_4[0]),
                              TransformMatchingShapes(star_bound_proof_2b[3],star_bound_proof_4[1]),
                              TransformMatchingShapes(VGroup(star_bound_proof_2b[1],star_bound_proof_2b[2],star_bound_proof_2b[4]),star_bound_proof_4[2]),lag_ratio=0.5))

        self.wait(0.1)
        self.next_slide()

        star_bound_proof_4_copy = star_bound_proof_4.copy()
        self.add(star_bound_proof_4_copy)
        self.play(LaggedStart(Write(star_bound_proof_5[0]),
                              TransformMatchingShapes(VGroup(star_bound_proof_4_copy[0],star_bound_proof_4_copy[1]),star_bound_proof_5[1]),
                              Transform(star_bound_proof_4_copy[2],star_bound_proof_5[2]),
                              lag_ratio=0.25))
        
        self.wait(0.1)
        self.next_slide()
        
        self.add(star_bound_proof_5b)
        self.remove(star_bound_proof_5,star_bound_proof_5[0],star_bound_proof_5[1],star_bound_proof_5[2],star_bound_proof_4_copy,star_bound_proof_4_copy[0],star_bound_proof_4_copy[1],star_bound_proof_4_copy[2])

        Hpow2_stuff = [star_bound_proof_1,star_bound_proof_2,star_bound_proof_2b,star_bound_proof_3,star_bound_proof_4]
        self.play(*[
            item.animate.shift(RIGHT*2).set_opacity(0)
            for item in Hpow2_stuff
        ])
        self.wait(0.1)

        star_bound_proof_6 = MathTex(r"\Bigg({{\left(\frac{n+d-2}{d}\right)I - H_\bigstar}}\Bigg)^2", r"= \left(\frac{n+d-2}{d}\right)^2 - 2\left(\frac{n+d-2}{d}\right) H_\bigstar +", r"\left(H_\bigstar\right)^2",
                                     font_size=28).next_to(proof_text, DOWN, aligned_edge=LEFT, buff=0.25)
        star_bound_proof_6[1].set_color(TEAL_D)
        star_bound_proof_7 = MathTex(r"\Bigg({{\left(\frac{n+d-2}{d}\right)I - H_\bigstar}}\Bigg)^2", r"= \left(\frac{n+d-2}{d}\right)^2 - 2\left(\frac{n+d-2}{d}\right) H_\bigstar +", r"\left(\frac{n+d-2}{d}\right)H_\bigstar - \frac{2(d-1)}{d^2} \sum_{2 \leq a < b \leq n} P_{1ab}^{1ab}",
                                     font_size=28).next_to(star_bound_proof_6, DOWN, aligned_edge=LEFT, buff=0.25)
        star_bound_proof_7[1].set_color(TEAL_D)
        star_bound_proof_7b = MathTex(r"{{\Bigg(}}{{\left(\frac{n+d-2}{d}\right)I - H_\bigstar}}{{\Bigg)^2}} = {{\left(\frac{n+d-2}{d}\right)^2}} - 2{{\left(\frac{n+d-2}{d}\right) H_\bigstar}} + {{\left(\frac{n+d-2}{d}\right)H_\bigstar}} - {{\frac{2(d-1)}{d^2} \sum_{2 \leq a < b \leq n} }} {{P_{1ab}^{1ab} }}",
                                     font_size=28).move_to(star_bound_proof_7)
        star_bound_proof_7b[1].set_color(TEAL_D)
        star_bound_proof_8 =  MathTex(r"{{\Bigg(}}{{\left(\frac{n+d-2}{d}\right)I - H_\bigstar}}{{\Bigg)^2}} = {{\left(\frac{n+d-2}{d}\right)}}\Bigg({{\left(\frac{n+d-2}{d}\right)}} - {{H_\bigstar}}\Bigg) - {{\frac{2(d-1)}{d^2} \sum_{2 \leq a < b \leq n} }} {{P_{1ab}^{1ab} }}",
                                     font_size=28).move_to(star_bound_proof_7b, aligned_edge=LEFT)
        star_bound_proof_8[1].set_color(TEAL_D)
        star_bound_proof_8[6:9].set_color(TEAL_D)
        star_bound_proof_8b =  MathTex(r"{{\Bigg(}}{{\left(\frac{n+d-2}{d}\right)I- H_\bigstar}}{{\Bigg)^2}} = {{\left(\frac{n+d-2}{d}\right)\Bigg(}}{{\left(\frac{n+d-2}{d}\right) - H_\bigstar}}{{\Bigg)}} - {{\frac{2(d-1)}{d^2} \sum_{2 \leq a < b \leq n} }} {{P_{1ab}^{1ab} }}",
                                     font_size=28).move_to(star_bound_proof_7b, aligned_edge=LEFT)
        star_bound_proof_8b[1].set_color(TEAL_D)
        star_bound_proof_8b[5].set_color(TEAL_D)
        star_bound_proof_9 =  MathTex(r"{{\left(\frac{n+d-2}{d}\right)\Bigg(}}{{\left(\frac{n+d-2}{d}\right) - H_\bigstar}}{{\Bigg)}} = {{\Bigg(}}{{\left(\frac{n+d-2}{d}\right)I - H_\bigstar}}{{\Bigg)^2}} + {{\frac{2(d-1)}{d^2} \sum_{2 \leq a < b \leq n} }} {{P_{1ab}^{1ab} }}",
                                     font_size=28).move_to(star_bound_proof_8, aligned_edge=LEFT)
        star_bound_proof_9[1].set_color(TEAL_D)
        star_bound_proof_9[5].set_color(TEAL_D)
        star_bound_proof_9b =  MathTex(r"\left(P_{1ab}^{1ab}\right)^2",
                                     font_size=28).move_to(star_bound_proof_9[-1], aligned_edge=LEFT)
        star_bound_proof_10 =  MathTex(r"\succcurlyeq 0",
                                     font_size=28).next_to(star_bound_proof_9b,RIGHT,buff=0.25)
        
        self.play(Write(star_bound_proof_6[0:3]),slide_text_2[1].animate.set_color(TEAL_D), run_time = 0.25)

        self.wait(0.1)
        self.next_slide()

        self.play(Write(star_bound_proof_6[3:]), run_time = 0.5)

        self.wait(0.1)
        self.next_slide()

        star_bound_proof_6_copy = star_bound_proof_6.copy()
        self.add(star_bound_proof_6_copy)
        self.play(LaggedStart(Transform(star_bound_proof_6_copy[0:3],star_bound_proof_7[0:3]),
                              Transform(star_bound_proof_6_copy[3],star_bound_proof_7[3]),
                              AnimationGroup(Transform(star_bound_proof_5b[1],star_bound_proof_7[4]),FadeOut(star_bound_proof_5b[0],run_time=0.5)),lag_ratio=0.25))
        self.add(star_bound_proof_7b)
        self.remove(star_bound_proof_7,*star_bound_proof_7[:],
                    star_bound_proof_5b,star_bound_proof_5b[0],star_bound_proof_5b[1],
                    star_bound_proof_6_copy,*star_bound_proof_6_copy[:])

        self.wait(0.1)
        self.next_slide()

        self.play(TransformMatchingTex(star_bound_proof_7b,star_bound_proof_8))
        self.add(star_bound_proof_8b)
        self.remove(star_bound_proof_8)
        self.wait(0.1)
        self.next_slide()

        self.play(TransformMatchingTex(star_bound_proof_8b,star_bound_proof_9))

        self.wait(0.1)
        self.next_slide()

        star_bound_proof_10a = MathTex(r"\succcurlyeq 0",font_size=28).next_to(star_bound_proof_9[5],DOWN,buff=0.25)
        star_bound_proof_10b = MathTex(r"\succcurlyeq 0",font_size=28).next_to(star_bound_proof_9[-1],DOWN,buff=0.25).shift(RIGHT*0.25)

        self.play(LaggedStart(Write(star_bound_proof_10a), TransformMatchingShapes(star_bound_proof_9[-1],star_bound_proof_9b), Write(star_bound_proof_10b),lag_ratio=0.25))

        self.wait(0.1)
        self.next_slide()

        self.play(Write(star_bound_proof_10))
        # self.play(TransformMatchingShapes(VGroup(star_bound_proof_10a,star_bound_proof_10b,star_bound_proof_9),star_bound_proof_10[1]))

        self.wait(0.25)

        self.play(DrawBorderThenFill(Rectangle(width=0.15,height=0.15,fill_opacity=1).to_corner(DR,buff=1).shift(UP*2+LEFT*1.5)),run_time=1)

        self.wait(0.1)
        self.next_slide()

        slide_text_last = Tex(r"{16cm}\textbf{Corollary:} For all density matrices, \(\rho\), we have that \(\Tr(\rho H_\bigstar) \leq \frac{n+d-2}{d} = \frac{n-1}{d} + \frac{d-1}{d}\).", 
                           font_size=28, tex_environment="minipage").move_to(star_bound_proof_5b,aligned_edge=LEFT).shift(DOWN * 1)
        self.play(Write(slide_text_last),run_time=0.5)

        self.wait(0.1)


class AnAlgorithmForME(Slide):
    def setup(self):
        theme = "Monokai Pro Light" # select a theme from https://iterm2colorschemes.com
        apply_theme(manim_scene=self, theme_name=theme, light_theme=True) # use the theme


    def construct(self):
        title = FancyTitle("An Algorithm For the Maximal Entanglement Problem")
        self.play(title.anim())

        self.wait(0.1)
        self.next_slide()

        slide_text_1 = r"For each pair, \(a,b \in V\), and a state \(\rho\), we define: \\\[x_{ab} = \Tr(\rho \overbrace{\ket{\psi_{ab}}\bra{\psi_{ab}}^{ab}}^{h_{ab}}),\ \ y_{ab} = \max\left(0, x_{ab} - \frac{1}{d}\right)\]"
        slide_text_2 = r"\(\rightarrow\) Think: every edge gets a base-line, \(\frac{1}{d}\), amount of energy and any additional energy must come from entanglement."
        slide_text_3 = r"\textbf{Theorem:} For all density matrices, \(\rho\), we have that \(\Tr(\rho H) \leq \frac{W}{d} + \frac{d-1}{d} \LP_{\mathsc{Match}}(G)\)."
        slide_text_4 = r"\emph{Proof (Sketch):} The \(\frac{d}{d-1} y_{ab}\) values give a fractional matching, by the star bound."

        algo = r"""\textbf{Algorithm:} \emph{Input:} Graph, \(G=(V,E,w)\), and local Hamiltonians, \(h_e\).
            \begin{enumerate}
                \item Find the maximum matching of \(G\),  denoted by \(m : E \to \{0,1\}\). 
                \item \emph{Output:} \(\displaystyle\rho = \bigotimes_{(a,b) \in m} h_{ab}^{ab} \otimes \bigotimes_{c \notin m} \frac{1}{d}I^c\)
            \end{enumerate}
        """

        # slide_text_5 = r"\textbf{Theorem:} This algorithm has an approximation ratio of \(\alpha_d = \frac{1}{d}\)."
        slide_text_5 = fr"\textbf{{Theorem:}} This algorithm has an approximation ratio of \(\alpha_d = \frac{{1}}{{d}}\). \\\color[HTML]{{{GRAY_C.to_hex()[1:]}}}{{Note, random assignment has an approximation ratio of \(\alpha_d = \frac{{1}}{{d^2}}.\)}}"
        
        slide_text_1_mo = Tex(f"{{11cm}}{slide_text_1}", font_size=28, tex_environment="minipage").to_corner(UL, buff=0.5).shift(DOWN)
        slide_text_2_mo = Tex(f"{{10.75cm}}{slide_text_2}", font_size=28, tex_environment="minipage").next_to(slide_text_1_mo, DOWN, aligned_edge=LEFT, buff=0.25).shift(RIGHT * 0.25)
        slide_text_3_mo = Tex(f"{{11cm}}{slide_text_3}", font_size=28, tex_environment="minipage").next_to(slide_text_2_mo, DOWN, aligned_edge=LEFT, buff=0.25).shift(LEFT * 0.25)
        slide_text_4_mo = Tex(f"{{11cm}}{slide_text_4}", font_size=28, tex_environment="minipage").next_to(slide_text_3_mo, DOWN, aligned_edge=LEFT, buff=0.25)

        algo_mo = Tex(f"{{16cm}}{algo}", font_size=28, tex_environment="minipage").next_to(slide_text_4_mo, DOWN, aligned_edge=LEFT, buff=0.5)

        slide_text_5_mo = Tex(f"{{5.75cm}}{slide_text_5}", font_size=28, tex_environment="minipage").next_to(algo_mo, RIGHT, buff=1).shift(DOWN*0.4)

        algo_surrbox = SurroundingRectangle(algo_mo, buff=0.2, color=BLACK)
        
        black_box = Rectangle(width=0.15,height=0.15,fill_opacity=1).next_to(slide_text_4_mo, RIGHT).shift(DOWN*0.15+LEFT*0.4)

        nxG = nx.Graph()
        nxG.add_edges_from([(2,1),(3,1),(1,4),(1,5),(1,6),(2,3)])
        sl = nx.spring_layout(nxG, seed=1, scale=2)
        sl2 = {k: [x, y, 0] for k, (x, y) in sl.items()}
        G = Graph.from_networkx(nxG, layout=sl2,vertex_config={
                "radius": 0.15,
            }).scale(0.75).shift(RIGHT * 4.5 + UP * 1.5)

        vertex_labels = VGroup(*[
            MathTex(str(v)).next_to(G[v], LEFT*0.1).scale(0.5) if str(v) == "3" else MathTex(str(v)).next_to(G[v], RIGHT*0.1).scale(0.5)
            for v in G.vertices
        ])

        flip_edges = [(2,3), (1,3)]
        edge_labels = VGroup(*[
            MathTex(f"h_{{{u}{v}}}").move_to(edge.get_center()).scale(0.5).rotate(edge.get_angle()+(PI if (u,v) in flip_edges else 0)).shift(0.2 * rotate_vector(UP, edge.get_angle()+(PI if (u,v) in flip_edges else 0)))
            for (u,v), edge in G.edges.items()
        ])

        # surrbox1 = SurroundingRectangle(G.edges[(2,3)], color=GOLD, buff=0.25,corner_radius=0.2)
        # surrbox2 = SurroundingRectangle(G.edges[(1,5)], color=GOLD, buff=0.25,corner_radius=0.2)

        surrbox1 = RoundedRectangle(
            width=G.edges[(2,3)].get_length() + 0.5,
            height=0.6,
            corner_radius=0.2,
            stroke_color=GOLD,
            fill_color=GOLD,
            fill_opacity=0.5,
        ).move_to(G.edges[(2,3)].get_center()).rotate(G.edges[(2,3)].get_angle() + PI).shift(0.1 * rotate_vector(UP, G.edges[(2,3)].get_angle() + PI))

        surrbox2 = RoundedRectangle(
            width=G.edges[(1,5)].get_length() + 0.5,
            height=0.6,
            corner_radius=0.2,
            stroke_color=GOLD,
            fill_color=GOLD,
            fill_opacity=0.5,
        ).move_to(G.edges[(1,5)].get_center()).rotate(G.edges[(1,5)].get_angle()).shift(0.1 * rotate_vector(UP, G.edges[(1,5)].get_angle()))

        prob_ham = MathTex(r"H = \sum_{ab \in E} w_{ab} h_{ab}", font_size=28).next_to(G,DOWN,buff=0.5)

        self.play(Create(G, run_time=1))
        self.play(LaggedStart(LaggedStart(*[Write(item, run_time=0.25) for item in vertex_labels],lag_ratio=0.2),
                              LaggedStart(*[Write(item, run_time=0.25) for item in edge_labels], lag_ratio=0.3),
                              Write(prob_ham, run_time=0.5),
                              Write(slide_text_1_mo, run_time=0.5),lag_ratio=0.5))

        self.wait(0.1)
        self.next_slide()

        self.play(Write(slide_text_2_mo), run_time=0.5)

        self.wait(0.1)
        self.next_slide()

        self.play(Write(slide_text_3_mo), run_time=0.5)

        self.wait(0.1)
        self.next_slide()

        self.play(Write(slide_text_4_mo), run_time=0.5)
        self.wait(0.25)
        self.play(DrawBorderThenFill(black_box), run_time=1)

        self.wait(0.1)
        self.next_slide()

        self.play(LaggedStart(Create(algo_surrbox), Write(algo_mo), lag_ratio=0.25))

        self.wait(0.1)
        self.next_slide()

        max_mix_1 = MathTex(r"\frac{1}{d}I",font_size=24,color=GOLD).next_to(G[4], LEFT*0.1)
        max_mix_2 = MathTex(r"\frac{1}{d}I",font_size=24,color=GOLD).next_to(G[6], UP*0.1)

        rho_eq_text = MathTex(r"\rho =",font_size=34,color=GOLD).next_to(G,LEFT,buff=0.45).shift(UP*0.45)

        self.bring_to_front(G,*vertex_labels,*edge_labels)
        self.play(LaggedStart(Write(rho_eq_text), DrawBorderThenFill(surrbox1), DrawBorderThenFill(surrbox2), Write(max_mix_1), Write(max_mix_2), lag_ratio=0.25))

        rho_copy = rho_eq_text.copy()
        max_mix_1_copy = max_mix_1.copy()
        max_mix_2_copy = max_mix_2.copy()
        surrbox1_copy = surrbox1.copy()
        surrbox2_copy = surrbox2.copy()
        self.add(rho_copy,max_mix_1_copy,max_mix_2_copy,surrbox1_copy,surrbox2_copy)

        rho_text = MathTex(r"{{\rho =}}{{h_{15}^{15}}} \otimes {{h_{23}^{23}}} \otimes {{\frac{1}{d}I^4}} \otimes {{\frac{1}{d} I^6}}",
                           color=GOLD,font_size=28).move_to(prob_ham,aligned_edge=UP)

        self.play(LaggedStart(prob_ham.animate.next_to(prob_ham,DOWN,buff=0.25),
                              Transform(rho_copy,rho_text[0]),
                              Transform(surrbox2_copy,rho_text[1]),
                              AnimationGroup(Transform(surrbox1_copy,rho_text[3]),Write(rho_text[2])),
                              AnimationGroup(Transform(max_mix_1_copy,rho_text[5]),Write(rho_text[4])),
                              AnimationGroup(Transform(max_mix_2_copy,rho_text[7]),Write(rho_text[6])),
                              lag_ratio=0.5))

        self.wait(0.1)
        self.next_slide()

        self.play(Write(slide_text_5_mo), run_time=0.5)

        self.wait(0.1)


class AnAlgorithmForMEVideo(Scene):
    def setup(self):
        theme = "Monokai Pro Light" # select a theme from https://iterm2colorschemes.com
        apply_theme(manim_scene=self, theme_name=theme, light_theme=True) # use the theme


    def construct(self):
        nxG = nx.Graph()
        nxG.add_edges_from([(2,1),(3,1),(1,4),(1,5),(1,6),(2,3)])
        sl = nx.spring_layout(nxG, seed=1, scale=2)
        sl2 = {k: [x, y, 0] for k, (x, y) in sl.items()}
        G = Graph.from_networkx(nxG, layout=sl2,vertex_config={
                "radius": 0.15,
            }).scale(1.25).shift(UP * 1)

        vertex_labels = VGroup(*[
            MathTex(str(v)).next_to(G[v], LEFT*0.1).scale(0.5) if str(v) == "3" else MathTex(str(v)).next_to(G[v], RIGHT*0.1).scale(0.5)
            for v in G.vertices
        ])

        flip_edges = [(2,3), (1,3)]
        edge_labels = VGroup(*[
            MathTex(f"h_{{{u}{v}}}").move_to(edge.get_center()).scale(0.5).rotate(edge.get_angle()+(PI if (u,v) in flip_edges else 0)).shift(0.2 * rotate_vector(UP, edge.get_angle()+(PI if (u,v) in flip_edges else 0)))
            for (u,v), edge in G.edges.items()
        ])

        # surrbox1 = SurroundingRectangle(G.edges[(2,3)], color=GOLD, buff=0.25,corner_radius=0.2)
        # surrbox2 = SurroundingRectangle(G.edges[(1,5)], color=GOLD, buff=0.25,corner_radius=0.2)

        surrbox1 = RoundedRectangle(
            width=G.edges[(2,3)].get_length() + 0.5,
            height=0.6,
            corner_radius=0.2,
            stroke_color=GOLD,
            fill_color=GOLD,
            fill_opacity=0.5,
        ).move_to(G.edges[(2,3)].get_center()).rotate(G.edges[(2,3)].get_angle() + PI).shift(0.1 * rotate_vector(UP, G.edges[(2,3)].get_angle() + PI))

        surrbox2 = RoundedRectangle(
            width=G.edges[(1,5)].get_length() + 0.5,
            height=0.6,
            corner_radius=0.2,
            stroke_color=GOLD,
            fill_color=GOLD,
            fill_opacity=0.5,
        ).move_to(G.edges[(1,5)].get_center()).rotate(G.edges[(1,5)].get_angle()).shift(0.1 * rotate_vector(UP, G.edges[(1,5)].get_angle()))

        prob_ham = MathTex(r"H = \sum_{ab \in E} w_{ab} h_{ab}").next_to(G,DOWN,buff=0.5)

        self.play(Create(G, run_time=1))
        self.play(LaggedStart(LaggedStart(*[Write(item, run_time=0.25) for item in vertex_labels],lag_ratio=0.2),
                              LaggedStart(*[Write(item, run_time=0.25) for item in edge_labels], lag_ratio=0.3),
                              Write(prob_ham, run_time=0.5),lag_ratio=0.5))

        max_mix_1 = MathTex(r"\frac{1}{d}I",color=GOLD).next_to(G[4], LEFT*0.1).scale(0.5)
        max_mix_2 = MathTex(r"\frac{1}{d}I",color=GOLD).next_to(G[6], UP*0.1).scale(0.5)
        
        rho_eq_text = MathTex(r"\rho =",color=GOLD).next_to(G,LEFT,buff=0.45)

        self.bring_to_front(G,*vertex_labels,*edge_labels)
        self.play(LaggedStart(Write(rho_eq_text), DrawBorderThenFill(surrbox1,run_time=0.5), DrawBorderThenFill(surrbox2,run_time=0.5), Write(max_mix_1,run_time=0.25), Write(max_mix_2,run_time=0.25), lag_ratio=0.25))

        rho_copy = rho_eq_text.copy()
        max_mix_1_copy = max_mix_1.copy()
        max_mix_2_copy = max_mix_2.copy()
        surrbox1_copy = surrbox1.copy()
        surrbox2_copy = surrbox2.copy()
        self.add(rho_copy,max_mix_1_copy,max_mix_2_copy,surrbox1_copy,surrbox2_copy)

        rho_text = MathTex(r"{{\rho =}}{{h_{15}^{15}}} \otimes {{h_{23}^{23}}} \otimes {{\frac{1}{d}I^4}} \otimes {{\frac{1}{d} I^6}}",
                           color=GOLD,font_size=28).move_to(prob_ham,aligned_edge=UP)

        self.play(LaggedStart(prob_ham.animate.next_to(prob_ham,DOWN,buff=0.25),
                              Transform(rho_copy,rho_text[0]),
                              Transform(surrbox2_copy,rho_text[1]),
                              Transform(surrbox1_copy,rho_text[3]),
                              Transform(max_mix_1_copy,rho_text[5]),
                              Transform(max_mix_2_copy,rho_text[7]),
                              AnimationGroup(Write(rho_text[2]),
                                             Write(rho_text[4]),
                                             Write(rho_text[6]))))

        self.wait(1)


class CSPsOverDistributions(Slide):
    def setup(self):
        theme = "Monokai Pro Light" # select a theme from https://iterm2colorschemes.com
        apply_theme(manim_scene=self, theme_name=theme, light_theme=True) # use the theme


    def construct(self):
        title = FancyTitle("An Algorithm With a Bit More Sauce (SOS)")
        self.play(title.anim())

        self.wait(0.1)
        self.next_slide()

        slide_text_1 = r"The key difficulty in optimization for LHPs (and CSPs) is that the search space is exponential in size (or rather dimension)."
        slide_text_2 = r"We need to relax the problem somehow."
        slide_text_3 = r"\(\rightarrow\) We optimize over distributions of strings."
        slide_text_4 = r"\(\rightarrow\) Observe that the expectation only depends on the marginal distribution, \(\mu^{ab}\)."
        slide_text_5 = r"\(\rightarrow\) We relax the notion of a distribution to only be consistent on low-degree marginals/moments and their interaction."
        
        slide_text_1_mo = Tex(f"{{11cm}}{slide_text_1}", font_size=28, tex_environment="minipage").to_corner(UL, buff=0.5).shift(DOWN)
        slide_text_2_mo = Tex(f"{{11cm}}{slide_text_2}", font_size=28, tex_environment="minipage").next_to(slide_text_1_mo, DOWN, aligned_edge=LEFT, buff=0.25)
        slide_text_3_mo = Tex(f"{{10.75cm}}{slide_text_3}", font_size=28, tex_environment="minipage").next_to(slide_text_2_mo, DOWN, aligned_edge=LEFT, buff=0.25).shift(RIGHT * 0.25)
        slide_text_4_mo = Tex(f"{{10.75cm}}{slide_text_4}", font_size=28, tex_environment="minipage").next_to(slide_text_3_mo, DOWN, aligned_edge=LEFT, buff=0.25)
        slide_text_5_mo = Tex(f"{{10.75cm}}{slide_text_5}", font_size=28, tex_environment="minipage").next_to(slide_text_4_mo, DOWN, aligned_edge=LEFT, buff=0.25)

        self.play(Write(slide_text_1_mo), run_time=0.5)

        self.wait(0.1)
        self.next_slide()

        self.play(Write(slide_text_2_mo), run_time=0.5)

        self.wait(0.1)
        self.next_slide()

        nxG = nx.Graph()
        nxG.add_edges_from([(1,2),(2,3),(3,4),(1,4),(3,5),(4,5)])
        sl = nx.spring_layout(nxG, seed=1, scale=2)
        sl2 = {k: [x, y, 0] for k, (x, y) in sl.items()}
        G = Graph.from_networkx(nxG, layout=sl2,vertex_config={
                "radius": 0.15,
            }).shift(RIGHT * 4.5)

        vertex_labels = VGroup(*[
            MathTex(str(v)).next_to(G[v], RIGHT*0.1).shift(UP * 0.1 if str(v) == "3" else UP * 0.0).scale(0.4)
            for v in G.vertices
        ])

        max_cut_text = Tex("Max-Cut", font_size=28).next_to(G, UP, buff=0.5)

        max_cut_eq = MathTex(r"\max_{x \in \{-1,+1\}^n}", r"\Bigg(\sum_{(a,b) \in E} w_{(a,b)}", r"\frac{1}{2}(1 - x_a x_b)", r"\Bigg)"
                             , font_size=28).next_to(G,DOWN,buff=0.5)
        max_cut_eq2 = MathTex(r"\max_{\mu \in \operatorname{Dist}(\{-1,+1\}^n)}", r"\Bigg(\sum_{(a,b) \in E} w_{(a,b)}", r"\E_{x \sim \mu}\left[\frac{1}{2}(1 - x_a x_b)\right]", r"\Bigg)"
                             , font_size=28).next_to(G,DOWN,buff=0.5)
        max_cut_eq3 = MathTex(r"\E_{x \sim \mu^{ab}}\left[\frac{1}{2}(1 - x_a x_b)\right]", r"\Bigg)"
                             , font_size=28).move_to(max_cut_eq2[-2],aligned_edge=LEFT)

        self.play(LaggedStart(Write(max_cut_text), Create(G,run_time=1), lag_ratio=0.5))
        self.play(LaggedStart(*[Write(item) for item in vertex_labels], Write(max_cut_eq,run_time=0.5), lag_ratio=0.25))
        
        surrbox1 = SurroundingRectangle(max_cut_eq[0], color=GOLD, buff=0.1)

        self.play(Create(surrbox1), run_time=0.5)

        self.wait(0.1)
        self.next_slide()

        self.play(LaggedStart(Create(surrbox1, rate_func=lambda t: 1 - t, run_time=0.5),Write(slide_text_3_mo, run_time = 0.25)))

        self.play(LaggedStart(TransformMatchingShapes(max_cut_eq[0], max_cut_eq2[0]),
                              Transform(max_cut_eq[1], max_cut_eq2[1]),
                              TransformMatchingShapes(max_cut_eq[2], max_cut_eq2[2]),
                              Transform(max_cut_eq[3], max_cut_eq2[3]),
                              lag_ratio=0.25))
        
        self.wait(0.1)
        self.next_slide()
        self.remove(max_cut_eq,max_cut_eq2,*[max_cut_eq[i] for i in range(4)],*[max_cut_eq2[i] for i in range(4)])
        self.add(max_cut_eq2)

        self.play(LaggedStart(Write(slide_text_4_mo, run_time=0.5),
                              TransformMatchingShapes(max_cut_eq2[2], max_cut_eq3[0]),
                              Transform(max_cut_eq2[3],max_cut_eq3[1]),
                              lag_ratio=0.25))
        
        self.wait(0.1)
        self.next_slide()

        self.play(Write(slide_text_5_mo), run_time=0.5)
        
        self.wait(0.1)
        self.next_slide()

        # positivity_eq = MathTex(r"\E_{x \sim \mu}[\calP(x)^2]", r"= \sum_{x \in \{-1,+1\}} \mu(x) \calP(x)^2 \geq 0",
        #                                     font_size=28).shift(LEFT*3 + DOWN*1)
        # unit_eq = MathTex(r"\E_{x \sim \mu}[1] = \sum_{x \in \{-1,+1\}} \mu(1) = 1",
        #                                     font_size=28).next_to(positivity_eq,DOWN,buff=0.25)
        # what_is_dist_text = Tex("What is a Distribution?",font_size=28).next_to(positivity_eq,UP,buff=0.25)
        # wid_vg = VGroup(what_is_dist_text,unit_eq,positivity_eq)
        # surrbox2 = SurroundingRectangle(wid_vg, color=BLACK, buff=0.25)


        # low_degree_poly_1 = MathTex(r"{{ \E_{x \sim \mu}\left[\left(x_1 + x_2\right)^2\right] }} = \E_{x \sim \mu}[{{x_1^2}} + 2 {{x_1 x_2}} + {{x_2^2}}]",
        #                                     font_size=28).next_to(wid_vg,DOWN,buff=0.5)
        # low_degree_poly_2 = MathTex(r"{{ \E_{x \sim \mu}\left[\left(x_1 + x_2\right)^2\right] }} = \E_{x \sim \mu}[{{x_1^2}}] + 2 \E_{x \sim \mu}[{{x_1 x_2}}] + \E_{x \sim \mu}[{{x_2^2}}]",
        #                                     font_size=28).move_to(low_degree_poly_1,aligned_edge=LEFT)
        
        # self.play(Write(what_is_dist_text,run_time=0.25))

        # self.wait(0.1)
        # self.next_slide()

        # self.play(LaggedStart(Write(positivity_eq,run_time=0.25),
        #                       Write(unit_eq,run_time=0.25),
        #                       Create(surrbox2),
        #                       lag_ratio=0.25))

        # self.wait(0.1)
        # self.next_slide()

        # positivity_eq_0_copy = positivity_eq[0].copy()
        # self.play(TransformMatchingShapes(positivity_eq_0_copy, low_degree_poly_1[0]))
        # self.wait(0.25)
        # self.play(Write(low_degree_poly_1[1:]),run_time=0.5)

        # self.wait(0.1)
        # self.next_slide()
        # self.remove(low_degree_poly_1,positivity_eq_0_copy,low_degree_poly_1[0])
        # self.add(low_degree_poly_1)

        # self.play(TransformMatchingTex(low_degree_poly_1,low_degree_poly_2))

        # self.wait(0.1)
        # self.next_slide()


class ALittleSOS(Slide):
    def setup(self):
        theme = "Monokai Pro Light" # select a theme from https://iterm2colorschemes.com
        apply_theme(manim_scene=self, theme_name=theme, light_theme=True) # use the theme


    def construct(self):
        title = FancyTitle("Pseudo-Distributions and SDPs")

        slide_text_1 = r"We relax the notion of a distribution to only be consistent on low-degree marginals/moments and their interaction."
        
        slide_text_0_mo = Tex(f"{{10.75cm}}\\(\\rightarrow\\) {slide_text_1}", font_size=28, tex_environment="minipage").to_corner(UL, buff=0.5).shift(DOWN*3.75+RIGHT*0.25)

        slide_text_1_mo = Tex(f"{{16cm}}{slide_text_1}", font_size=28, tex_environment="minipage").to_corner(UL, buff=0.5).shift(DOWN)

        self.add(slide_text_0_mo)

        
        self.play(title.anim(), TransformMatchingShapes(slide_text_0_mo,slide_text_1_mo))

        self.wait(0.1)
        self.next_slide()

        positivity_eq = MathTex(r"{{\forall \calP : \E_{x \sim \mu}[\calP(x)^2]}} = \sum_{x \in \{-1,+1\}} \mu(x) \calP(x)^2 {{\geq 0}}",
                                            font_size=28).shift(UP*1+LEFT*4)
        unit_eq = MathTex(r"{{\E_{x \sim \mu}[1]}} = \sum_{x \in \{-1,+1\}} \mu(1) {{= 1}}",
                                            font_size=28).next_to(positivity_eq,DOWN,buff=0.25)
        positivity_eq2 = MathTex(r"{{\forall \calP : \E_{x \sim \mu}[\calP(x)^2]}} {{\geq 0}}",
                                            font_size=28).shift(UP*1+LEFT*4)
        unit_eq2 = MathTex(r"{{\E_{x \sim \mu}[1]}} {{= 1}}",
                                            font_size=28).next_to(positivity_eq2,DOWN,buff=0.25)
        
        what_is_dist_text = Tex("What is a Distribution?",font_size=28).next_to(positivity_eq,UP,buff=0.25)
        wid_vg = VGroup(what_is_dist_text,unit_eq,positivity_eq)
        surrbox2 = SurroundingRectangle(wid_vg, color=BLACK, buff=0.25)
        wid_vg2 = VGroup(what_is_dist_text,unit_eq2,positivity_eq2)
        surrbox2b = SurroundingRectangle(wid_vg2, color=BLACK, buff=0.25).stretch_to_fit_width(what_is_dist_text.get_width()+0.5)


        low_degree_poly_1 = MathTex(r"{{ \E_{x \sim \mu}\left[\left(x_1 - x_2\right)^2\right] }} = \E_{x \sim \mu}[{{x_1^2}} - 2 {{x_1 x_2}} + {{x_2^2}}]",
                                            font_size=28).next_to(wid_vg,RIGHT,buff=1).shift(UP * 0.75)
        low_degree_poly_2 = MathTex(r"{{ \E_{x \sim \mu}\left[\left(x_1 - x_2\right)^2\right] }} = \E_{x \sim \mu}[{{x_1^2}}] - 2 \E_{x \sim \mu}[{{x_1 x_2}}] + \E_{x \sim \mu}[{{x_2^2}}]",
                                            font_size=28).move_to(low_degree_poly_1,aligned_edge=LEFT)
        low_degree_poly_3 = MathTex(r"{{ \E_{x \sim \mu}\left[\left(x_1 - x_2\right)^2\right] }} = (\bra{x_1} - \bra{x_2}) M (\ket{x_1} - \ket{x_2})",
                                            font_size=28).next_to(low_degree_poly_1,DOWN,aligned_edge=LEFT,buff=0.25)
        
        # moment_mat = MathTex(r"""
        #     M = \begin{blockarray}{ccccccc}
        #         & \vcenter{\hbox{\scriptsize $1$}} & \vcenter{\hbox{\scriptsize $x_1$}} & \vcenter{\hbox{\scriptsize $x_2$}} & \vcenter{\hbox{\scriptsize $\cdots$}} & \vcenter{\hbox{\scriptsize $x_1 x_2$}} & \vcenter{\hbox{\scriptsize $\cdots$}} \\
        #         \begin{block}{c[cccccc]}
        #             \vcenter{\hbox{\scriptsize $1$}}       & \E_\mu[1] \tstrut\bstrut     & \E_\mu[x_1]       & \E_\mu[x_2]       & \cdots & \E_\mu[x_1 x_2]     & \cdots \\
        #             \vcenter{\hbox{\scriptsize $x_1$}}     & \E_\mu[x_1]                  & \E_\mu[x_1^2]     & \E_\mu[x_1 x_2]   & \cdots & \E_\mu[x_1^2 x_2]   & \cdots \\
        #             \vcenter{\hbox{\scriptsize $x_2$}}     & \E_\mu[x_2]                  & \E_\mu[x_1 x_2]   & \E_\mu[x_2^2]     & \cdots & \E_\mu[x_1 x_2^2]   & \cdots \\
        #             \vcenter{\hbox{\scriptsize $\vdots$}}  & \vdots                       & \vdots            & \vdots            & \ddots & \vdots              &        \\
        #             \vcenter{\hbox{\scriptsize $x_1 x_2$}} & \E_\mu[x_1 x_2]              & \E_\mu[x_1^2 x_2] & \E_\mu[x_1 x_2^2] & \cdots & \E_\mu[x_1^2 x_2^2] & \cdots \\
        #             \vcenter{\hbox{\scriptsize $\vdots$}}  & \vdots                       & \vdots            &  \vdots           &        & \vdots              & \ddots \\
        #         \end{block}
        #     \end{blockarray}
        # """,font_size=28).next_to(low_degree_poly_2,DOWN, buff=1)

        # moment_mat_2 = MathTex(r"""
        #     M = \begin{blockarray}{ccccccc}
        #         & \vcenter{\hbox{\scriptsize $1$}} & \vcenter{\hbox{\scriptsize $x_1$}} & \vcenter{\hbox{\scriptsize $x_2$}} & \vcenter{\hbox{\scriptsize $\cdots$}} & \vcenter{\hbox{\scriptsize $x_1 x_2$}} & \vcenter{\hbox{\scriptsize $\cdots$}} \\
        #         \begin{block}{c[cccccc]}
        #             \vcenter{\hbox{\scriptsize $1$}}       & \E_\mu[1] \tstrut\bstrut     & \E_\mu[x_1]       & \E_\mu[x_2]       & \cdots & \E_\mu[x_1 x_2] & \cdots \\
        #             \vcenter{\hbox{\scriptsize $x_1$}}     & \E_\mu[x_1]                  & 1                 & \E_\mu[x_1 x_2]   & \cdots & \E_\mu[x_2]     & \cdots \\
        #             \vcenter{\hbox{\scriptsize $x_2$}}     & \E_\mu[x_2]                  & \E_\mu[x_1 x_2]   & 1                 & \cdots & \E_\mu[x_1]     & \cdots \\
        #             \vcenter{\hbox{\scriptsize $\vdots$}}  & \vdots                       & \vdots            & \vdots            & \ddots & \vdots          &        \\
        #             \vcenter{\hbox{\scriptsize $x_1 x_2$}} & \E_\mu[x_1 x_2]              & \E_\mu[x_2]       & \E_\mu[x_1]       & \cdots & 1               & \cdots \\
        #             \vcenter{\hbox{\scriptsize $\vdots$}}  & \vdots                       & \vdots            &  \vdots           &        & \vdots          & \ddots \\
        #         \end{block}
        #     \end{blockarray}
        # """,font_size=28).next_to(low_degree_poly_2,DOWN, buff=1)

        moment_mat_b = Matrix([
            [r"\E_\mu[1]",       r"\E_\mu[x_1]",       r"\E_\mu[x_2]",         r"\cdots",      r"\E_\mu[x_1 x_2]",     r"\cdots"     ],
            [r"\E_\mu[x_1]",     r"\E_\mu[x_1^2]",     r"\E_\mu[x_1 x_2]",     r"\cdots",      r"\E_\mu[x_1^2 x_2]",   r"\cdots"     ],
            [r"\E_\mu[x_2]",     r"\E_\mu[x_1 x_2]",   r"\E_\mu[x_2^2]",       r"\cdots",      r"\E_\mu[x_1 x_2^2]",   r"\cdots"     ],
            [r"\vdots",          r"\vdots",            r"\vdots",              r"\ddots",      r"\vdots",              r"\vdots"     ],
            [r"\E_\mu[x_1 x_2]", r"\E_\mu[x_1^2 x_2]", r"\E_\mu[x_1 x_2^2]",   r"\cdots",      r"\E_\mu[x_1^2 x_2^2]", r"\cdots"     ],
            [r"\vdots",          r"\vdots",            r"\vdots",              r"\cdots",      r"\vdots",              r"\ddots"     ]
        ],element_alignment_corner=UL,h_buff=2,v_buff=1.1).scale(0.75)

        moment_mat_b_2 = Matrix([
            [r"1",               r"\E_\mu[x_1]",     r"\E_\mu[x_2]",     r"\cdots",      r"\E_\mu[x_1 x_2]", r"\cdots"     ],
            [r"\E_\mu[x_1]",     r"1",               r"\E_\mu[x_1 x_2]", r"\cdots",      r"\E_\mu[x_2]",     r"\cdots"     ],
            [r"\E_\mu[x_2]",     r"\E_\mu[x_1 x_2]", r"1",               r"\cdots",      r"\E_\mu[x_1]",     r"\cdots"     ],
            [r"\vdots",          r"\vdots",          r"\vdots",          r"\ddots",      r"\vdots",          r"\vdots"     ],
            [r"\E_\mu[x_1 x_2]", r"\E_\mu[x_2]",     r"\E_\mu[x_1]",     r"\cdots",      r"1",               r"\cdots"     ],
            [r"\vdots",          r"\vdots",          r"\vdots",          r"\cdots",      r"\vdots",          r"\ddots"     ]
        ],element_alignment_corner=UL,h_buff=2,v_buff=1.1).scale(0.75)

        moment_mat_b_label = MathTex("M = ").next_to(moment_mat_b,LEFT,buff=0.75)
        moment_mat_b_psd = MathTex(r"\succcurlyeq 0",font_size=42).next_to(moment_mat_b,RIGHT,buff=0.3)

        moment_mat_b_col_labels = VGroup(
            MathTex(r"1",font_size=28), MathTex(r"x_1",font_size=28), MathTex(r"x_2",font_size=28), MathTex(r"\cdots",font_size=28), MathTex(r"x_1 x_2",font_size=28), MathTex(r"\cdots",font_size=28)
        ).scale(0.75).arrange(RIGHT, buff=1.4).next_to(moment_mat_b, UP).shift(RIGHT*0.5)
        moment_mat_b_col_labels[-1].shift(LEFT*0.8)
        moment_mat_b_col_labels[-2].shift(LEFT*0.25) 
        moment_mat_b_col_labels[-3].shift(LEFT*0.35)

        moment_mat_b_row_labels = VGroup(
            MathTex(r"1",font_size=28), MathTex(r"x_1",font_size=28), MathTex(r"x_2",font_size=28), MathTex(r"\vdots",font_size=28), MathTex(r"x_1 x_2",font_size=28), MathTex(r"\vdots",font_size=28)
        ).scale(0.75).arrange(DOWN, buff=0.75).next_to(moment_mat_b, LEFT)
        moment_mat_b_row_labels[-1].shift(UP*0.1)

        moment_mat_group = VGroup(moment_mat_b,moment_mat_b_2,moment_mat_b_label,moment_mat_b_col_labels,moment_mat_b_row_labels,moment_mat_b_psd)
        moment_mat_group.scale(0.75).next_to(low_degree_poly_2, DOWN, buff=1)

        surrbox0 = SurroundingRectangle(moment_mat_b.get_columns()[1][2] ,color=GOLD)
        moment_mat_def = MathTex(r"M_{xy} = \E_\mu[xy]", font_size=28).next_to(low_degree_poly_2,DOWN,buff=0.25)
        
        self.play(Write(what_is_dist_text,run_time=0.25))

        self.wait(0.1)
        self.next_slide()

        self.play(LaggedStart(Write(positivity_eq,run_time=0.25),
                              Write(unit_eq,run_time=0.25),
                              Create(surrbox2),
                              lag_ratio=0.25))

        self.wait(0.1)
        self.next_slide()

        self.play(TransformMatchingTex(positivity_eq,positivity_eq2,transform_mismatches=True),TransformMatchingTex(unit_eq,unit_eq2,transform_mismatches=True), Transform(surrbox2,surrbox2b))

        self.wait(0.1)
        self.next_slide()

        positivity_eq2_0_copy = positivity_eq2[0].copy()
        self.play(TransformMatchingShapes(positivity_eq2_0_copy, low_degree_poly_1[0]))
        self.wait(0.25)
        self.play(Write(low_degree_poly_1[1:]),run_time=0.5)

        self.wait(0.1)
        self.next_slide()
        self.remove(low_degree_poly_1,positivity_eq2_0_copy,low_degree_poly_1[0])
        self.add(low_degree_poly_1)

        self.play(TransformMatchingTex(low_degree_poly_1,low_degree_poly_2))

        self.wait(0.1)
        self.next_slide()

        # self.play(Write(moment_mat))
        self.play(LaggedStart(Write(moment_mat_b_label),
                              Write(moment_mat_b,run_time=1),
                              Write(moment_mat_b_col_labels),
                              Write(moment_mat_b_row_labels)))

        self.wait(0.1)
        self.next_slide()

        self.play(Create(surrbox0),Write(moment_mat_def))

        self.wait(0.1)
        self.next_slide()

        self.play(Uncreate(surrbox0))
        self.play(*[Transform(a, b) for a, b in zip(moment_mat_b.get_entries(), moment_mat_b_2.get_entries())],Unwrite(moment_mat_def))

        self.wait(0.1)
        self.next_slide()

        self.play(Write(low_degree_poly_3[1]), run_time=0.5)

        self.wait(0.1)
        self.next_slide()

        surrbox3 = RoundedRectangle(corner_radius=0.0, height=positivity_eq2.get_height()-0.35, width=positivity_eq2.get_width()-2.25, color=GOLD).move_to(positivity_eq2)
        positivity_eq2_copy = positivity_eq2.copy()
        self.add(positivity_eq2_copy)
        self.play(Create(surrbox3))
        self.play(Transform(positivity_eq2_copy,moment_mat_b_psd))

        self.wait(0.1)
        self.next_slide()

        submatrix = VGroup(*[col[0:4] for col in moment_mat_b_2.get_columns()[0:4]])

        surrbox4 = SurroundingRectangle(submatrix, color=GOLD, buff=0.15)

        self.play(Uncreate(surrbox3))
        self.play(Create(surrbox4))

        self.wait(0.1)
        self.next_slide()

        pdist_text = Tex(r"Degree-\(2t\) Pseudo-Distribution",font_size=28).next_to(wid_vg,DOWN,buff=1)

        sos_positivity_eq = MathTex(r"{{\forall \calP \text{ of degree } \leq t : \E_{x \sim \Tilde{\mu} }[\calP(x)^2]}} {{\geq 0}}",
                                            font_size=28).next_to(pdist_text,DOWN,buff=0.25)
        sos_unit_eq = MathTex(r"{{\E_{x \sim \Tilde{\mu} }[1]}} {{= 1}}",
                                            font_size=28).next_to(sos_positivity_eq,DOWN,buff=0.25)

        pd_vg = VGroup(pdist_text,sos_unit_eq,sos_positivity_eq)
        # surrbox5 = RoundedRectangle(corner_radius=0.0, height=pd_vg.get_height()-0.75, width=sos_positivity_eq.get_width()-1.25).move_to(pd_vg)
        surrbox5 = SurroundingRectangle(pd_vg,color=BLACK,buff=-0.5)
        surrbox5.stretch_to_fit_height(surrbox5.height+0.25)

        self.play(LaggedStart(Write(pdist_text,run_time=0.25),
                              Write(sos_positivity_eq,run_time=0.25),
                              Write(sos_unit_eq,run_time=0.25),
                              Create(surrbox5),
                              lag_ratio=0.25))
        
        self.wait(0.1)


class ALittleMoreSOS(Slide):
    def setup(self):
        theme = "Monokai Pro Light" # select a theme from https://iterm2colorschemes.com
        apply_theme(manim_scene=self, theme_name=theme, light_theme=True) # use the theme


    def construct(self):
        title = FancyTitle("Pseudo-Distributions and SDPs")

        slide_text_1 = r"We relax the notion of a distribution to only be consistent on low-degree marginals/moments and their interaction."
        
        slide_text_1_mo = Tex(f"{{16cm}}{slide_text_1}", font_size=28, tex_environment="minipage").to_corner(UL, buff=0.5).shift(DOWN)


        self.add(title)
        self.add(slide_text_1_mo)

        moment_mat_b = Matrix([
            [r"1",               r"\E_\mu[x_1]",     r"\E_\mu[x_2]",     r"\cdots",      r"\E_\mu[x_1 x_2]", r"\cdots"     ],
            [r"\E_\mu[x_1]",     r"1",               r"\E_\mu[x_1 x_2]", r"\cdots",      r"\E_\mu[x_2]",     r"\cdots"     ],
            [r"\E_\mu[x_2]",     r"\E_\mu[x_1 x_2]", r"1",               r"\cdots",      r"\E_\mu[x_1]",     r"\cdots"     ],
            [r"\vdots",          r"\vdots",          r"\vdots",          r"\ddots",      r"\vdots",          r"\vdots"     ],
            [r"\E_\mu[x_1 x_2]", r"\E_\mu[x_2]",     r"\E_\mu[x_1]",     r"\cdots",      r"1",               r"\cdots"     ],
            [r"\vdots",          r"\vdots",          r"\vdots",          r"\cdots",      r"\vdots",          r"\ddots"     ]
        ],element_alignment_corner=UL,h_buff=2,v_buff=1.1).scale(0.75)

        moment_mat_b_label = MathTex("M = ").next_to(moment_mat_b,LEFT,buff=0.75)
        moment_mat_b_psd = MathTex(r"\succcurlyeq 0",font_size=42).next_to(moment_mat_b,RIGHT,buff=0.3)

        moment_mat_b_col_labels = VGroup(
            MathTex(r"1",font_size=28), MathTex(r"x_1",font_size=28), MathTex(r"x_2",font_size=28), MathTex(r"\cdots",font_size=28), MathTex(r"x_1 x_2",font_size=28), MathTex(r"\cdots",font_size=28)
        ).scale(0.75).arrange(RIGHT, buff=1.4).next_to(moment_mat_b, UP).shift(RIGHT*0.5)
        moment_mat_b_col_labels[-1].shift(LEFT*0.8)
        moment_mat_b_col_labels[-2].shift(LEFT*0.25) 
        moment_mat_b_col_labels[-3].shift(LEFT*0.35)

        moment_mat_b_row_labels = VGroup(
            MathTex(r"1",font_size=28), MathTex(r"x_1",font_size=28), MathTex(r"x_2",font_size=28), MathTex(r"\vdots",font_size=28), MathTex(r"x_1 x_2",font_size=28), MathTex(r"\vdots",font_size=28)
        ).scale(0.75).arrange(DOWN, buff=0.75).next_to(moment_mat_b, LEFT)
        moment_mat_b_row_labels[-1].shift(UP*0.1)

        moment_mat_group = VGroup(moment_mat_b,moment_mat_b_label,moment_mat_b_col_labels,moment_mat_b_row_labels,moment_mat_b_psd)
        moment_mat_group.scale(0.75).shift(RIGHT*3.3 + DOWN*1.9)

        self.add(moment_mat_group)

        pdist_text = Tex(r"Degree-\(2t\) Pseudo-Distribution",font_size=28).shift(LEFT*4 + DOWN*1.4)

        sos_positivity_eq = MathTex(r"{{\forall \calP \text{ of degree } \leq t : \E_{x \sim \Tilde{\mu} }[\calP(x)^2]}} {{\geq 0}}",
                                            font_size=28).next_to(pdist_text,DOWN,buff=0.25)
        sos_unit_eq = MathTex(r"{{\E_{x \sim \Tilde{\mu} }[1]}} {{= 1}}",
                                            font_size=28).next_to(sos_positivity_eq,DOWN,buff=0.25)
        
        moment_mat_text = Tex(r"Moment Matrix",font_size=28).shift(RIGHT*4 + UP*1.5)

        moment_mat_positivity_eq = MathTex(r"M \in M_{n^{\calO(t)} }(\R),\ M\succcurlyeq 0",
                                            font_size=28).next_to(moment_mat_text,DOWN,buff=0.25)
        moment_mat_unit_eq = MathTex(r"M_{11}= 1,\ M^\sfT = M, \cdots",
                                            font_size=28).next_to(moment_mat_positivity_eq,DOWN,buff=0.25)
        
        # lrarrow = MathTex(r"\Leftrightarrow").shift(UP*1.25)
        lrarrow = LeftRightArrows(start=LEFT,end=RIGHT,buff=0.2,tip_length=0.2).shift(UP*1.25+RIGHT*0.5)

        pd_vg = VGroup(pdist_text,sos_unit_eq,sos_positivity_eq)
        # surrbox5 = RoundedRectangle(corner_radius=0.0, height=pd_vg.get_height()-0.75, width=sos_positivity_eq.get_width()-1.25).move_to(pd_vg)
        surrbox5 = SurroundingRectangle(pd_vg,color=BLACK,buff=-0.5)
        surrbox5.stretch_to_fit_height(surrbox5.height+0.25)


        mm_vg = VGroup(moment_mat_text,moment_mat_positivity_eq,moment_mat_unit_eq)
        # surrbox6 = RoundedRectangle(corner_radius=0.0, height=mm_vg.get_height()+0.5, width=moment_mat_positivity_eq.get_width()+0.5).move_to(mm_vg)
        surrbox6 = SurroundingRectangle(mm_vg,color=BLACK,buff=0.25)

        self.add(pd_vg,surrbox5)

        self.play(LaggedStart(AnimationGroup(pd_vg.animate.shift(UP*(1.4+1.5)),
                                             surrbox5.animate.shift(UP*(1.4+1.5)),
                                             Transform(moment_mat_group,mm_vg)),
                              Create(surrbox6),
                              Create(lrarrow,run_time=0.5),lag_ratio=0.75))
        
        self.wait(0.1)
        self.next_slide()

        sdp_text = Tex("Efficiently Solvable SDP",font_size=28,color=GOLD).next_to(surrbox6,DOWN,buff=0.25)
        self.play(Write(sdp_text), run_time=0.5)
        
        self.wait(0.1)
        self.next_slide()

        pdensmat_text = Tex(r"Degree-\(2t\) Pseudo-Density Matrix",font_size=28).next_to(surrbox5,DOWN,buff=1.5)

        sos_positivity2_eq = MathTex(r"{{\forall B \in M_{d^n}(\C) \text{ with degree } \leq t : \Tr(\Tilde{\rho}B^\dagger B)}} {{\geq 0}}",
                                            font_size=28).next_to(pdensmat_text,DOWN,buff=0.25)
        sos_unit2_eq = MathTex(r"{{\Tr(\Tilde{\rho} } I)}} {{= 1}}",
                                            font_size=28).next_to(sos_positivity2_eq,DOWN,buff=0.25)
        
        ast_text = MathTex(r"\ast",font_size=24,color=TEAL_D).next_to(sos_positivity2_eq,
                                                                      UP,aligned_edge=RIGHT,buff=0).shift(LEFT*0.5+DOWN*0.05)
        footnote_text = Tex(r"\(^\ast\)Here, \(B^\dagger \coloneq \overline{B}^\sfT\) is the conjugate transpose.",
                            font_size=24,color=TEAL_D).to_corner(DR, buff=0.5)
        
        moment_mat2_text = Tex(r"Moment Matrix",font_size=28).next_to(surrbox5,DOWN,buff=1.5).shift(RIGHT*8)

        moment_mat2_positivity_eq = MathTex(r"M \in M_{n^{\calO(t)}}(\C),\ M\succcurlyeq 0",
                                            font_size=28).next_to(moment_mat2_text,DOWN,buff=0.25)
        moment_mat2_unit_eq = MathTex(r"M_{II} = 1,\ M^\dagger = M,\ \cdots",
                                            font_size=28).next_to(moment_mat2_positivity_eq,DOWN,buff=0.25)

        # lrarrow = MathTex(r"\Leftrightarrow").shift(UP*1.25)
        lrarrow2 = LeftRightArrows(start=LEFT,end=RIGHT,buff=0.2,tip_length=0.2).shift(DOWN*2.5+RIGHT*0.5)

        pdmat_vg = VGroup(pdensmat_text,sos_positivity2_eq,sos_unit2_eq)
        # surrbox7 = RoundedRectangle(corner_radius=0.0, height=pdmat_vg.get_height()-0.75, width=sos_unit2_eq.get_width()-1.25).move_to(pdmat_vg)
        surrbox7 = SurroundingRectangle(pdmat_vg, color=BLACK, buff=-0.5)
        surrbox7.stretch_to_fit_width(surrbox7.width+0.5)
        # surrbox7.stretch_to_fit_height(surrbox7.height+0.25)

        mm2_vg = VGroup(moment_mat2_text,moment_mat2_positivity_eq,moment_mat2_unit_eq)
        # surrbox8 = RoundedRectangle(corner_radius=0.0, height=mm2_vg.get_height()+0.5, width=moment_mat2_positivity_eq.get_width()+0.5).move_to(mm2_vg)
        surrbox8 = SurroundingRectangle(mm2_vg, color=BLACK, buff=0.25)

        self.play(LaggedStart(
            LaggedStart(AnimationGroup(Write(pdmat_vg,run_time=0.5)), Create(surrbox7), lag_ratio=0.75),
            LaggedStart(AnimationGroup(Write(mm2_vg,run_time=0.5)), Create(surrbox8), lag_ratio=0.75),
            Create(lrarrow2, run_time=0.5),
            lag_ratio=0.5
        ))
        self.play(Write(ast_text),Write(footnote_text,run_time=1))

        self.wait(0.1)


class ALittleSOSVideo(Scene):
    def setup(self):
        theme = "Monokai Pro Light" # select a theme from https://iterm2colorschemes.com
        apply_theme(manim_scene=self, theme_name=theme, light_theme=True) # use the theme


    def construct(self):
        positivity_eq = MathTex(r"{{\forall \calP : \E_{x \sim \mu}[\calP(x)^2]}} = \sum_{x \in \{-1,+1\}} \mu(x) \calP(x)^2 {{\geq 0}}",
                                            font_size=28).shift(UP*1+LEFT*4)
        unit_eq = MathTex(r"{{\E_{x \sim \mu}[1]}} = \sum_{x \in \{-1,+1\}} \mu(1) {{= 1}}",
                                            font_size=28).next_to(positivity_eq,DOWN,buff=0.25)
        positivity_eq2 = MathTex(r"{{\forall \calP : \E_{x \sim \mu}[\calP(x)^2]}} {{\geq 0}}",
                                            font_size=28).shift(UP*1+LEFT*4)
        unit_eq2 = MathTex(r"{{\E_{x \sim \mu}[1]}} {{= 1}}",
                                            font_size=28).next_to(positivity_eq2,DOWN,buff=0.25)
        
        what_is_dist_text = Tex("What is a Distribution?",font_size=28).next_to(positivity_eq,UP,buff=0.25)
        wid_vg = VGroup(what_is_dist_text,unit_eq,positivity_eq)
        surrbox2 = SurroundingRectangle(wid_vg, color=BLACK, buff=0.25)
        wid_vg2 = VGroup(what_is_dist_text,unit_eq2,positivity_eq2)
        surrbox2b = SurroundingRectangle(wid_vg2, color=BLACK, buff=0.25).stretch_to_fit_width(what_is_dist_text.get_width()+0.5)

        moment_mat_b = Matrix([
            [r"1",               r"\E_\mu[x_1]",     r"\E_\mu[x_2]",     r"\cdots",      r"\E_\mu[x_1 x_2]", r"\cdots"     ],
            [r"\E_\mu[x_1]",     r"1",               r"\E_\mu[x_1 x_2]", r"\cdots",      r"\E_\mu[x_2]",     r"\cdots"     ],
            [r"\E_\mu[x_2]",     r"\E_\mu[x_1 x_2]", r"1",               r"\cdots",      r"\E_\mu[x_1]",     r"\cdots"     ],
            [r"\vdots",          r"\vdots",          r"\vdots",          r"\ddots",      r"\vdots",          r"\vdots"     ],
            [r"\E_\mu[x_1 x_2]", r"\E_\mu[x_2]",     r"\E_\mu[x_1]",     r"\cdots",      r"1",               r"\cdots"     ],
            [r"\vdots",          r"\vdots",          r"\vdots",          r"\cdots",      r"\vdots",          r"\ddots"     ]
        ],element_alignment_corner=UL,h_buff=2,v_buff=1.1).scale(0.75)

        moment_mat_b_label = MathTex("M = ").next_to(moment_mat_b,LEFT,buff=0.75)
        moment_mat_b_psd = MathTex(r"\succcurlyeq 0",font_size=42).next_to(moment_mat_b,RIGHT,buff=0.3)

        moment_mat_b_col_labels = VGroup(
            MathTex(r"1",font_size=28), MathTex(r"x_1",font_size=28), MathTex(r"x_2",font_size=28), MathTex(r"\cdots",font_size=28), MathTex(r"x_1 x_2",font_size=28), MathTex(r"\cdots",font_size=28)
        ).scale(0.75).arrange(RIGHT, buff=1.4).next_to(moment_mat_b, UP).shift(RIGHT*0.5)
        moment_mat_b_col_labels[-1].shift(LEFT*0.8)
        moment_mat_b_col_labels[-2].shift(LEFT*0.25) 
        moment_mat_b_col_labels[-3].shift(LEFT*0.35)

        moment_mat_b_row_labels = VGroup(
            MathTex(r"1",font_size=28), MathTex(r"x_1",font_size=28), MathTex(r"x_2",font_size=28), MathTex(r"\vdots",font_size=28), MathTex(r"x_1 x_2",font_size=28), MathTex(r"\vdots",font_size=28)
        ).scale(0.75).arrange(DOWN, buff=0.75).next_to(moment_mat_b, LEFT)
        moment_mat_b_row_labels[-1].shift(UP*0.1)

        moment_mat_group = VGroup(moment_mat_b,moment_mat_b_label,moment_mat_b_col_labels,moment_mat_b_row_labels,moment_mat_b_psd)
        moment_mat_group.scale(0.75).next_to(surrbox2b, RIGHT, buff=1).shift(DOWN*1.5)
        
        self.play(Write(what_is_dist_text,run_time=0.25))

        self.play(LaggedStart(Write(positivity_eq,run_time=0.25),
                              Write(unit_eq,run_time=0.25),
                              Create(surrbox2),
                              lag_ratio=0.25))

        self.play(TransformMatchingTex(positivity_eq,positivity_eq2,transform_mismatches=True),TransformMatchingTex(unit_eq,unit_eq2,transform_mismatches=True), Transform(surrbox2,surrbox2b))

        # self.play(Write(moment_mat))
        self.play(LaggedStart(Write(moment_mat_b_label),
                              Write(moment_mat_b,run_time=0.5),
                              Write(moment_mat_b_col_labels,run_time=0.25),
                              Write(moment_mat_b_row_labels,run_time=0.25),lag_ratio=0.25))

        pdist_text = Tex(r"Degree-\(2t\) Pseudo-Distribution",font_size=28).next_to(wid_vg,DOWN,buff=1)

        sos_positivity_eq = MathTex(r"{{\forall \calP \text{ of degree } \leq t : \E_{x \sim \Tilde{\mu} }[\calP(x)^2]}} {{\geq 0}}",
                                            font_size=28).next_to(pdist_text,DOWN,buff=0.25)
        sos_unit_eq = MathTex(r"{{\E_{x \sim \Tilde{\mu} }[1]}} {{= 1}}",
                                            font_size=28).next_to(sos_positivity_eq,DOWN,buff=0.25)

        pd_vg = VGroup(pdist_text,sos_unit_eq,sos_positivity_eq)
        # surrbox5 = RoundedRectangle(corner_radius=0.0, height=pd_vg.get_height()-0.75, width=sos_positivity_eq.get_width()-1.25).move_to(pd_vg)
        surrbox5 = SurroundingRectangle(pd_vg,color=BLACK,buff=-0.5)
        surrbox5.stretch_to_fit_height(surrbox5.height+0.25)

        self.play(LaggedStart(Write(pdist_text,run_time=0.25),
                              Write(sos_positivity_eq,run_time=0.25),
                              Write(sos_unit_eq,run_time=0.25),
                              Create(surrbox5),
                              lag_ratio=0.25))
        
        self.wait(0.1)

        moment_mat_text = Tex(r"Moment Matrix",font_size=28).shift(RIGHT*4+UP)

        moment_mat_positivity_eq = MathTex(r"M \in M_{n^{\calO(t)} }(\R),\ M\succcurlyeq 0",
                                            font_size=28).next_to(moment_mat_text,DOWN,buff=0.25)
        moment_mat_unit_eq = MathTex(r"M_{11}= 1,\ M^\sfT = M, \cdots",
                                            font_size=28).next_to(moment_mat_positivity_eq,DOWN,buff=0.25)
        
        # lrarrow = MathTex(r"\Leftrightarrow").shift(UP*1.25)
        lrarrow = LeftRightArrows(start=LEFT,end=RIGHT,buff=0.2,tip_length=0.2).shift(UP*0.5+RIGHT*0.5)


        mm_vg = VGroup(moment_mat_text,moment_mat_positivity_eq,moment_mat_unit_eq)
        # surrbox6 = RoundedRectangle(corner_radius=0.0, height=mm_vg.get_height()+0.5, width=moment_mat_positivity_eq.get_width()+0.5).move_to(mm_vg)
        surrbox6 = SurroundingRectangle(mm_vg,color=BLACK,buff=0.25)

        self.play(LaggedStart(AnimationGroup(wid_vg2.animate.shift(UP*5),
                                             surrbox2.animate.shift(UP*6),
                                             surrbox2b.animate.shift(UP*6),
                                             pd_vg.animate.shift(UP*(2.4)),
                                             surrbox5.animate.shift(UP*(2.4)),
                                             Transform(moment_mat_group,mm_vg)),
                              Create(surrbox6),
                              Create(lrarrow,run_time=0.5),lag_ratio=0.5))
        
        self.wait(1)


class TheFinalSOSSlide(Slide):
    def setup(self):
        theme = "Monokai Pro Light" # select a theme from https://iterm2colorschemes.com
        apply_theme(manim_scene=self, theme_name=theme, light_theme=True) # use the theme


    def construct(self):
        title = FancyTitle("Pseudo-Distributions and SDPs")
        slide_text_1 = r"We relax the notion of a distribution to only be consistent on low-degree marginals/moments and their interaction."
        slide_text_1_mo = Tex(f"{{16cm}}{slide_text_1}", font_size=28, tex_environment="minipage").to_corner(UL, buff=0.5).shift(DOWN)

        pdensmat_text = Tex(r"Degree-\(2t\) Pseudo-Density Matrix",font_size=28).shift(DOWN*1.95+LEFT*4)

        sos_positivity2_eq = MathTex(r"{{\forall B \in M_{d^n}(\C) \text{ with degree } \leq t : \Tr(\Tilde{\rho}B^\dagger B)}} {{\geq 0}}",
                                            font_size=28).next_to(pdensmat_text,DOWN,buff=0.25)
        sos_unit2_eq = MathTex(r"{{\Tr(\Tilde{\rho} } I)}} {{= 1}}",
                                            font_size=28).next_to(sos_positivity2_eq,DOWN,buff=0.25)
        
        moment_mat2_text = Tex(r"Moment Matrix",font_size=28).shift(DOWN*1.95+RIGHT*4)

        moment_mat2_positivity_eq = MathTex(r"M \in M_{n^{\calO(t)}}(\C),\ M\succcurlyeq 0",
                                            font_size=28).next_to(moment_mat2_text,DOWN,buff=0.25)
        moment_mat2_unit_eq = MathTex(r"M_{II} = 1,\ M^\dagger = M,\ \cdots",
                                            font_size=28).next_to(moment_mat2_positivity_eq,DOWN,buff=0.25)

        # lrarrow = MathTex(r"\Leftrightarrow").shift(UP*1.25)
        lrarrow2 = LeftRightArrows(start=LEFT,end=RIGHT,buff=0.2,tip_length=0.2).shift(DOWN*2.5+RIGHT*0.5)

        pdmat_vg = VGroup(pdensmat_text,sos_positivity2_eq,sos_unit2_eq)
        # surrbox7 = RoundedRectangle(corner_radius=0.0, height=pdmat_vg.get_height()-0.75, width=sos_unit2_eq.get_width()-1.25).move_to(pdmat_vg)
        surrbox7 = SurroundingRectangle(pdmat_vg, color=BLACK, buff=-0.5)
        surrbox7.stretch_to_fit_width(surrbox7.width+0.3)
        # surrbox7.stretch_to_fit_height(surrbox7.height+0.25)

        mm2_vg = VGroup(moment_mat2_text,moment_mat2_positivity_eq,moment_mat2_unit_eq)
        # surrbox8 = RoundedRectangle(corner_radius=0.0, height=mm2_vg.get_height()+0.5, width=moment_mat2_positivity_eq.get_width()+0.5).move_to(mm2_vg)
        surrbox8 = SurroundingRectangle(mm2_vg, color=BLACK, buff=0.25)

        self.add(title,slide_text_1_mo,pdmat_vg,surrbox7,mm2_vg,surrbox8,lrarrow2)

        self.play(pdmat_vg.animate.shift(UP*3.5),
                  surrbox7.animate.shift(UP*3.5),
                  mm2_vg.animate.shift(UP*3.5),
                  surrbox8.animate.shift(UP*3.5),
                  lrarrow2.animate.shift(UP*3.5), run_time=0.5)
        
        self.wait(0.1)
        self.next_slide()

        slide_text_2 = r"Recall the star bound:"
        slide_text_2_mo = Tex(f"{{16cm}}{slide_text_2}",
                              font_size=28, tex_environment="minipage").next_to(slide_text_1_mo, DOWN, aligned_edge=LEFT, buff=3)
        
        slide_text_3_mo = Tex(r"{{\textbf{Lemma:} For all}} {{density matrices,}} {{\(\rho\),}} {{we have that \(\Tr(\rho H_\bigstar) \leq \frac{n+d-2}{d} = \frac{n-1}{d} + \frac{d-1}{d}\).}}", 
                           font_size=28)
        slide_text_3_mo.next_to(slide_text_2_mo, DOWN, aligned_edge=LEFT, buff=0.25)

        slide_text_3b_mo = Tex(r"{{\textbf{Lemma:} For all}} {{degree-6 pseudo-density matrices,}} {{\(\Tilde{\rho}\),}} {{we have that \(\Tr(\Tilde{\rho} H_\bigstar) \leq \frac{n+d-2}{d} = \frac{n-1}{d} + \frac{d-1}{d}\).}}", 
                           font_size=28)
        slide_text_3b_mo.next_to(slide_text_2_mo, DOWN, aligned_edge=LEFT, buff=0.25)

        proof_text = Tex(r"\emph{Proof:}",font_size=28)
        star_bound_proof =  MathTex(r"{{\left(\frac{n+d-2}{d}\right)\Bigg(\left(\frac{n+d-2}{d}\right) - H_\bigstar\Bigg)}} = {{\left(\frac{n+d-2}{d}I - H_\bigstar\right)^2}} + {{\frac{2(d-1)}{d^2} \sum_{2 \leq a < b \leq n} }} {{\left(P_{1ab}^{1ab}\right)^2 }}",
                                     font_size=28)
        black_box = Rectangle(width=0.15,height=0.15,fill_opacity=1)
        proof_vg = VGroup(proof_text,star_bound_proof,black_box).arrange(RIGHT, buff=0.25)
        proof_vg.next_to(slide_text_3_mo, DOWN, aligned_edge=LEFT, buff=0.25)

        self.play(LaggedStart(
            Write(slide_text_2_mo, run_time=0.25),
            Write(slide_text_3_mo, run_time=0.5),
            Write(proof_text, run_time=0.25),
            Write(star_bound_proof, run_time=0.5),
            DrawBorderThenFill(black_box, run_time=1), lag_ratio=0.5))

        self.wait(0.1)
        self.next_slide()

        thing = MathTex(r"\underbrace{\phantom{\frac{n+d-2}{d}I\!\!\!\! - \!\!\!\! H_\bigstar}}_{\text{Degree 2} }",
                        font_size=28).next_to(star_bound_proof[2],DOWN,buff=0.15).shift(LEFT*0.1)
        thing2 = MathTex(r"\underbrace{\phantom{ \!\!\!\! P_{1ab}^{1ab} \!\!\!\!}}_{\text{Degree \(\leq 3\)} }",
                         font_size=28).next_to(star_bound_proof[-1],DOWN,buff=0.15).shift(LEFT*0.05)
        
        self.play(Write(thing),Write(thing2))

        self.wait(0.1)
        self.next_slide()
        
        self.play(TransformMatchingTex(slide_text_3_mo,slide_text_3b_mo,transform_mismatches=True))

        self.wait(0.1)
        self.next_slide()

        slide_text_4 = fr"{{16cm}}\textbf{{Theorem:}} There is a algorithm for \algprobm{{Maximal Entanglement}} over qubits with an approximation ratio\\\phantom{{\textbf{{Theorem:}} }} of \(0.595\) (our algorithm adapts the algorithms of [PT21; LP24]).\\\phantom{{\textbf{{Theorem:}} }}\color[HTML]{{{GRAY_C.to_hex()[1:]}}}{{Previous best had an approximation ratio of \(0.5\) [PT22].}}"
        slide_text_4_mo = Tex(slide_text_4, font_size=28, tex_environment="minipage").next_to(slide_text_3_mo,DOWN,aligned_edge=LEFT,buff=1.75) 

        self.play(Write(slide_text_4_mo), run_time=0.5)

        self.wait(0.1)


class QMdCIntro(Slide):
    def setup(self):
        theme = "Monokai Pro Light" # select a theme from https://iterm2colorschemes.com
        apply_theme(manim_scene=self, theme_name=theme, light_theme=True) # use the theme


    def construct(self):
        title = FancyTitle(r"Quantum Max-\(d\)-Cut")
        self.play(title.anim())

        self.wait(0.1)
        self.next_slide()

        slide_text_1 = Tex(r"{8cm}Quantum Max-\(d\)-Cut is a 2-local Hamiltonian problem defined over a graph, \(G = (V,E,w)\).", 
                           font_size=28, tex_environment="minipage")
        slide_text_2 = MathTex(r"H = \sum_{(u,v) \in E} w_{(u,v)} \overbrace{\sum_{1\leq a<b\leq d}\frac{1}{2}\left(\ket{ab}-\ket{ba}\right)\left(\bra{ab}-\bra{ba}\right)^{uv} }^{h_{(u,v)}", font_size=28)
        slide_text_2b = Tex(r"\begin{center}No longer rank one!\\Not an instance of Maximal Entanglement.\end{center}", color=GOLD, font_size=28)
        slide_text_1.to_corner(UL, buff=0.5).shift(DOWN)
        slide_text_2.next_to(slide_text_1, DOWN, buff=0.5)
        slide_text_2b.next_to(slide_text_2,DOWN,buff=0.25).shift(RIGHT)

        nxG = nx.Graph()
        nxG.add_edges_from([(1,2),(2,3),(3,4),(1,4),(3,5),(4,5)])
        sl = nx.spring_layout(nxG, seed=1, scale=2)
        sl2 = {k: [x, y, 0] for k, (x, y) in sl.items()}
        G = Graph.from_networkx(nxG, layout=sl2,vertex_config={
                "radius": 0.15,
            }).shift(RIGHT * 4).shift(UP*1.5)

        vertex_labels = VGroup(*[
            MathTex(str(v)).next_to(G[v], RIGHT*0.1).scale(0.5)
            for v in G.vertices
        ])

        self.play(Write(slide_text_1), Write(slide_text_2), Create(G), run_time=1)
        self.play(*[Write(item) for item in vertex_labels], run_time=0.25)

        self.wait(0.1)
        self.next_slide()

        slide_text_3 = Tex(r"{8cm}Recall, in Max-Cut, the local terms, were projectors onto the ``different'' subspace: \(\Span\{\ket{01},\ket{10}\}\)", 
                           font_size=28, tex_environment="minipage")
        slide_text_4 = MathTex(r"\calC_{(a,b)} = \ket{01}\bra{10} + \ket{10}\bra{10}", 
                           font_size=28)
        slide_text_3.next_to(slide_text_1, DOWN, aligned_edge=LEFT, buff=3)
        slide_text_4.next_to(slide_text_3, DOWN, buff=0.5)

        self.play(Write(slide_text_3),Write(slide_text_4), run_time=0.5)

        self.wait(0.1)
        self.next_slide()

        slide_text_3b = Tex(r"{8cm}In Max-\(d\)-Cut, the local terms, were projectors onto the ``different'' subspace: \(\Span\{\ket{ab},\ket{ba}\}_{a<b}\)", 
                           font_size=28, tex_environment="minipage")
        slide_text_4b = MathTex(r"\begin{split}\calC_{(a,b)} &= \ket{12}\bra{12} + \ket{21}\bra{21}\\&+ \cdots\\&+ \ket{ab}\bra{ab} + \ket{ba}\bra{ba}\\&+ \cdots\end{split}", 
                           font_size=28)
        slide_text_3b.next_to(slide_text_1, DOWN, aligned_edge=LEFT, buff=3)
        slide_text_4b.next_to(slide_text_3b, DOWN, buff=0.5)

        # TODO: fix this animation
        self.play(TransformMatchingShapes(slide_text_3,slide_text_3b),TransformMatchingShapes(slide_text_4,slide_text_4b), run_time=0.5)

        self.wait(0.1)
        self.next_slide()

        slide_text_5 = Tex(r"{8cm}In Quantum Max-\(d\)-Cut, the local terms are projectors onto the \emph{antisymmetric subspace} subspace: \(\Span\{\ket{ab}-\ket{ba}\}_{a<b}\)", 
                           font_size=28, tex_environment="minipage")
        slide_text_6 = MathTex(r"\begin{split}h_{(u,v)} &= \frac{1}{2}\left(\ket{12}-\ket{21}\right)\left(\bra{12}-\bra{21}\right)\\&+ \cdots \\&+ \frac{1}{2}\left(\ket{ab}-\ket{ba}\right)\left(\bra{ab}-\bra{ba}\right)\\&+ \cdots\end{split}", 
                           font_size=28)
        slide_text_5.next_to(slide_text_1, DOWN, aligned_edge=LEFT, buff=3).shift(RIGHT*8)
        slide_text_6.next_to(slide_text_5, DOWN, buff=0.25)

        self.play(Write(slide_text_5),Write(slide_text_6), run_time=0.5)

        self.wait(0.1)
        self.next_slide()

        self.play(Write(slide_text_2b))

        self.wait(0.1)


class QMdCStarBound(Slide):
    def setup(self):
        theme = "Monokai Pro Light" # select a theme from https://iterm2colorschemes.com
        apply_theme(manim_scene=self, theme_name=theme, light_theme=True) # use the theme


    def construct(self):
        title = FancyTitle(r"Quantum Max-\(d\)-Cut: Star Bound and Resulting Algorithm")
        self.play(title.anim())

        self.wait(0.1)
        self.next_slide()

        slide_text_1 = r"\algprobm{Quantum Max-\(d\)-Cut} is \emph{not} an instance of the \algprobm{Maximal Entanglement} problem."
        slide_text_2 = r"\(\rightarrow\) We shouldn't expect the star bound to be the same."
        slide_text_3 = [r"\textbf{Lemma ([Jor24; KŠV25]):} We have that \(\eig_{\max}\left(H_{\bigstar}^{\mathsc{qm\(d\)c}}\right) = \frac{n + d - 1}{2} = \frac{n-1}{2} +\)", r"\(\frac{d-1}{2}\)", "."]
        slide_text_4 = fr"\emph{{Proof (Sketch):}} Eigenvalue calculation using the representation theory of the symmetric group (not SOS)."
        slide_text_5 = r"\textbf{Theorem:} For all density matrices, \(\rho\), we have that \(\Tr(\rho H) \leq \frac{W}{2} + \frac{1}{2} \LP_{\mathsc{\((d-1)\)-Match}}(G)\)."
        slide_text_6 = [r"\emph{Proof (Sketch):} The ", rf"{{\color[HTML]{{ {TEAL_D.to_hex()[1:]} }}{{``surplus''}} }}", r"values give a fractional \(b\)-matching, by the above star bound."]
        slide_text_7 = [r"\textbf{Theorem:} There is an algorithm for \algprobm{Quantum Max-\(3\)-Cut} with approximation ratio 0.555.\\", fr"\phantom{{\textbf{{Theorem:}} }}\color[HTML]{{{GRAY_C.to_hex()[1:]}}}{{Previous best had an approximation ratio of \(0.4\) [FJ97; CJKKW23].}}"]
        slide_text_7b = [r"\textbf{Conjecture:} There is an algorithm for \algprobm{Quantum Max-\(3\)-Cut} with approximation ratio 0.611.\\", fr"\phantom{{\textbf{{Conjecture:}} }}\color[HTML]{{{GRAY_C.to_hex()[1:]}}}{{Previous best had an approximation ratio of \(0.4\) [FJ97; CJKKW23].}}"]

        slide_text_1_mo = Tex(fr"{{16cm}}{slide_text_1}", 
                           font_size=28, tex_environment="minipage").to_corner(UL, buff=0.5).shift(DOWN)
        slide_text_2_mo = Tex(fr"{{15.75cm}}{slide_text_2}", 
                           font_size=28, tex_environment="minipage").next_to(slide_text_1_mo, DOWN, aligned_edge=LEFT, buff=0.25).shift(RIGHT*0.25)
        
        slide_text_3_mo = Tex(*slide_text_3, 
                           font_size=28).next_to(slide_text_2_mo, DOWN, aligned_edge=LEFT, buff=0.5).shift(LEFT*0.25)
        slide_text_4_mo = Tex(fr"{{16cm}}{slide_text_4}", 
                           font_size=28, tex_environment="minipage").next_to(slide_text_3_mo, DOWN, aligned_edge=LEFT, buff=0.25)
        black_box1 = Rectangle(width=0.15,height=0.15,fill_opacity=1).next_to(slide_text_4_mo, RIGHT)

        slide_text_5_mo = Tex(f"{{16cm}}{slide_text_5}", 
                              font_size=28, tex_environment="minipage").next_to(slide_text_4_mo, DOWN, aligned_edge=LEFT, buff=0.5)
        slide_text_6_mo = Tex(*slide_text_6, 
                              font_size=28).next_to(slide_text_5_mo, DOWN, aligned_edge=LEFT, buff=0.25)
        black_box2 = Rectangle(width=0.15,height=0.15,fill_opacity=1).next_to(slide_text_6_mo, RIGHT)

        slide_text_7_mo = Tex(*slide_text_7, 
                              font_size=28, tex_environment="flushleft").next_to(slide_text_6_mo, DOWN, aligned_edge=LEFT, buff=0.5)
        slide_text_7b_mo = Tex(*slide_text_7b, 
                              font_size=28, tex_environment="flushleft").next_to(slide_text_6_mo, DOWN, aligned_edge=LEFT, buff=0.5)

        self.play(Write(slide_text_1_mo), run_time=0.5)

        self.wait(0.1)
        self.next_slide()

        self.play(Write(slide_text_2_mo), run_time=0.5)

        self.wait(0.1)
        self.next_slide()

        self.play(Write(slide_text_3_mo), run_time=0.5)

        self.wait(0.1)
        self.next_slide()

        self.play(Write(slide_text_4_mo), run_time=0.5)
        self.play(Create(black_box1), run_time=0.25)

        self.wait(0.1)
        self.next_slide()

        self.play(Write(slide_text_5_mo), run_time=0.5)

        self.wait(0.1)
        self.next_slide()

        self.play(Write(slide_text_6_mo), slide_text_3_mo[1].animate.set_color(TEAL_D), run_time=0.5)
        self.play(Create(black_box2), run_time=0.25)
        self.play(Indicate(slide_text_3_mo[1], scale_factor=2), Indicate(slide_text_6_mo[1]))
        
        self.wait(0.1)
        self.next_slide()

        self.play(Write(slide_text_7_mo), run_time = 0.5)
        
        self.wait(0.1)
        self.next_slide()

        nxG = nx.Graph()
        nxG.add_edges_from([(1,2),(2,3),(3,4),(4,5),(1,5),(6,7),(7,8),(8,9),(9,10),(6,10),(1,6),(2,7),(3,8),(4,9),(5,10)])
        sl = nx.spring_layout(nxG, seed=2, scale=2.5)
        sl2 = {k: [x*3, y*0.75, 0] for k, (x, y) in sl.items()}
        G = Graph.from_networkx(nxG, layout=sl2,vertex_config={
                "radius": 0.15,
            }).scale(0.5).shift(DOWN*3.25+LEFT*3)

        cycles = [(1,2),(2,3),(3,4),(4,5),(1,5),(6,7),(7,8),(8,9),(9,10),(6,10)]
        cycles_top = [(1,2),(2,3),(3,4),(4,5),(1,5)]
        cycles_bot = [(6,7),(7,8),(8,9),(9,10),(6,10)]
        cycle_edges_vg = VGroup(*[emob for e, emob in G.edges.items() if e in cycles])

        edge_to_ment = [(1,2),(3,4),(7,8),(9,10)]
        all_other_cycle_edges=[(2,3),(4,5),(1,5),(6,7),(8,9),(6,10)]

        edgeboxes = [RoundedRectangle(
            width=G.edges[e].get_length() + 0.5,
            height=0.5,
            corner_radius=0.2,
            stroke_color=GOLD,
            fill_color=GOLD,
            fill_opacity=0.5,
        ).move_to(G.edges[e].get_center()).rotate(G.edges[e].get_angle())
        for e in G.edges.keys() if e in edge_to_ment]

        edgeboxes2 = [RoundedRectangle(
            width=G.edges[e].get_length() + 0.5,
            height=0.5,
            corner_radius=0.2,
            stroke_color=GOLD,
            fill_color=GOLD,
            fill_opacity=0.5,
        ).move_to(G.edges[e].get_center()).rotate(G.edges[e].get_angle())
        for e in G.edges.keys() if e in all_other_cycle_edges]
        
        self.play(Create(G,run_time=0.5))

        self.wait(0.1)
        self.next_slide()

        bmatch_text = Tex(r"Find \(2\)-Matching", font_size=28, color=GREEN_D).next_to(G,RIGHT,buff=1).shift(UP*0.25)
        output_text = Tex("Output:", font_size=28).next_to(G,RIGHT,buff=1).shift(DOWN*0.25)
        state1 = MathTex(r"{{\rho = }}{{\rho_{e_1} }} \otimes {{\rho_{e_2} }} \otimes {{\rho_{e_3} }} \otimes {{\rho_{e_4} }} \otimes \frac{1}{9}I", font_size=28, color=GOLD).next_to(output_text,RIGHT,buff=0.25)
        state2 = MathTex(r"{{\rho = }}{{\rho_{C_1}}} \otimes {{\rho_{C_2} }}", font_size=28, color=GOLD).next_to(output_text,RIGHT,buff=0.25)

        self.play(Write(bmatch_text),LaggedStart(*[e.animate.set_color(GREEN_D) for e in cycle_edges_vg], lag_ratio=0.5, run_time=0.75))

        self.wait(0.1)
        self.next_slide()

        self.bring_to_front(*(G.edges.values()), *(G.vertices.values()))
        self.play(Write(output_text), LaggedStart(*[DrawBorderThenFill(eb,run_time=0.5) for eb in edgeboxes], lag_ratio=0.25))

        edgeboxes_copy = [eb.copy() for eb in edgeboxes]
        self.add(*edgeboxes_copy)
        self.play(LaggedStart(*[AnimationGroup(Write(state1[i*2]),Transform(edgeboxes_copy[i], state1[i*2+1])) for i in range(4)],
                              Write(state1[8]),
                              lag_ratio=0.5))

        # TODO make state line in the first slide

        self.wait(0.1)
        self.next_slide()

        self.remove(state1,*state1[:],*edgeboxes_copy)
        self.add(state1)

        edgeboxes_top = [RoundedRectangle(
            width=G.edges[e].get_length() + 0.5,
            height=0.5,
            corner_radius=0.2,
            stroke_color=GOLD,
            fill_color=GOLD,
            fill_opacity=0.5,
        ).move_to(G.edges[e].get_center()).rotate(G.edges[e].get_angle())
        for e in G.edges.keys() if e in cycles_top]
        edgeboxes_bot = [RoundedRectangle(
            width=G.edges[e].get_length() + 0.5,
            height=0.5,
            corner_radius=0.2,
            stroke_color=GOLD,
            fill_color=GOLD,
            fill_opacity=0.5,
        ).move_to(G.edges[e].get_center()).rotate(G.edges[e].get_angle())
        for e in G.edges.keys() if e in cycles_bot]

        self.play(FadeOut(state1[1:]))
        self.bring_to_front(*(G.edges.values()), *(G.vertices.values()))
        self.play(LaggedStart(*[DrawBorderThenFill(eb,run_time=0.5) for eb in edgeboxes2], lag_ratio=0.25))

        self.play(LaggedStart(Transform(VGroup(*edgeboxes_top), state2[1],path_arc=1),
                              AnimationGroup(Write(state2[2]),Transform(VGroup(*edgeboxes_bot), state2[3],path_arc=-1)),
                              lag_ratio=0.5))

        self.play(TransformMatchingShapes(slide_text_7_mo[0],slide_text_7b_mo[0]),Transform(slide_text_7_mo[1],slide_text_7b_mo[1]))
        

        # TODO make state line in the first slide

        self.wait(0.1)


class QMdCPartialResults(Slide):
    def setup(self):
        theme = "Monokai Pro Light" # select a theme from https://iterm2colorschemes.com
        apply_theme(manim_scene=self, theme_name=theme, light_theme=True) # use the theme


    def construct(self):
        title = FancyTitle(r"\algprobm{Quantum Max-\(3\)-Cut}: Partial SOS Results")
        self.play(title.anim())

        slide_text_1 = r" To get better algorithms we need a sum-of-squares (SOS) proof of the star bound so we can use an SDP."
        slide_text_2 = r".-> An SOS proof has remained surprisingly elusive."
        slide_text_3 = r"\textbf{Theorem:} There is a low-degree SOS proof that certifies the star bound for at most 4 neighbors."

        slide_text_4 = r"\textbf{Theorem:} With certain global constraints (SOS axioms) there is an SOS proof the certifies the star bound on the star graph for all sizes."
        slide_text_5 = r".-> The global constraints restrict the search space to irreps/isotypical subspaces."
        slide_text_6 = r".-> Can't be use for algorithms on general graphs."

        slide_text_7 = r"\textbf{Question:} Is there a low-degree SOS proof of the star bound for any number of neighbors?"

        bullets = Bullets(slide_text_1,slide_text_2,slide_text_3,slide_text_4,slide_text_5,slide_text_6,slide_text_7,double_space_for_new_sections=True,bullet_aligned_edge=None)
        for _ in range(bullets.get_num_lines()):
            self.wait(0.1)
            self.next_slide()
            self.play(bullets.write_next_line(run_time=0.5))

        self.wait(0.1)


class FutureWork(Slide):
    def setup(self):
        theme = "Monokai Pro Light" # select a theme from https://iterm2colorschemes.com
        apply_theme(manim_scene=self, theme_name=theme, light_theme=True) # use the theme


    def construct(self):
        title = FancyTitle("Future Work")
        self.play(title.anim())

        slide_text_1 = r" We summarize some future directions inspired by the present work."
        slide_text_2 = r".1 Are there low-degree SOS proofs of the \algprobm{Quantum Max-\(d\)-Cut} star bound for any number of neighbors? Or are there low-degree refutations?"
        slide_text_3 = r".2 Can we find an improved approximation algorithm for the \algprobm{Maximal Entanglement} problem."
        slide_text_4 = r".3 We can generalize \algprobm{Quantum Max-\(d\)-Cut} to a class of Hamiltonians known as swap operators algebra Hamiltonians. Can the tools developed for QMC and QM\(d\)C in this regime."

        bullets = Bullets(slide_text_1,slide_text_2,slide_text_3,slide_text_4)
        for _ in range(bullets.get_num_lines()):
            self.wait(0.1)
            self.next_slide()
            self.play(bullets.write_next_line(run_time=0.5))

        self.wait(0.1)


class Thanks(Slide):
    def setup(self):
        theme = "Monokai Pro Light" # select a theme from https://iterm2colorschemes.com
        apply_theme(manim_scene=self, theme_name=theme, light_theme=True) # use the theme


    def construct(self):
        t_text = Text("Thank You!", font_size=48)
        line = Line(LEFT*3,RIGHT*3)
        q_text = Text("Questions?", font_size=28, slant=ITALIC)

        title_and_author = VGroup(t_text, line, q_text).arrange(DOWN, buff=0.15)

        self.play(LaggedStart(Write(t_text),Create(line),Write(q_text),lag_ratio=0.5))

        self.wait(0.1)
        # IDK add some fun looping animation
