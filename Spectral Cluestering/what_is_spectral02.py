from manim import *

from common import create_title


class Scene02_WhatIsSpectral(Scene):
    def construct(self):
        title = create_title("The Key Idea")
        self.play(Write(title))
        statements = VGroup(
            Text("1. Represent data as a graph", font_size=30),
            Text("2. Encode connections in a matrix", font_size=30),
            Text("3. Use eigenvectors to reveal a new space", font_size=30),
            Text("4. Cluster the points in that space", font_size=30),
        )
        statements.arrange(DOWN, aligned_edge=LEFT, buff=0.38)
        statements.next_to(title, DOWN, buff=0.8)
        for statement in statements:
            self.play(FadeIn(statement, shift=RIGHT), run_time=0.6)
        callout = Text("Geometry becomes algebra, then geometry again.", font_size=30, color=GREEN)
        callout.to_edge(DOWN)
        self.play(Write(callout))
        self.wait(3)
