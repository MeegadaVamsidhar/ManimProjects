from manim import *

class Hello(Scene):
    def construct(self):
        text = Text("Consistent Hashing!!")
        self.play(Write(text))
        self.wait(2)