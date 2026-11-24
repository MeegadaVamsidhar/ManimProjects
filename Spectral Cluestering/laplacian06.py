from manim import *

from common import create_title


class Scene06_Laplacian(Scene):
    def construct(self):
        title = create_title("The Graph Laplacian")
        self.play(Write(title))
        formula = Text("L = D - W", font_size=48, color=YELLOW)
        formula.move_to(UP * 1.4)
        self.play(Write(formula))
        parts = VGroup(
            Text("D: how strongly each point is connected", font_size=27, color=BLUE),
            Text("W: which points are connected to each other", font_size=27, color=ORANGE),
            Text("L: a balance of local connection and global structure", font_size=27, color=GREEN),
        )
        parts.arrange(DOWN, aligned_edge=LEFT, buff=0.35)
        parts.next_to(formula, DOWN, buff=0.7)
        for part in parts:
            self.play(FadeIn(part), run_time=0.7)
        insight = Text("The smallest eigenvectors of L expose the easiest split.", font_size=28)
        insight.to_edge(DOWN)
        self.play(Write(insight))
        self.wait(3)
