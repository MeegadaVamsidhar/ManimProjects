from manim import *

from common import create_matrix, create_title


class Scene05_DegreeMatrix(Scene):
    def construct(self):
        title = create_title("Step 2: Measure Connectivity")
        self.play(Write(title))
        degree_values = [
            [2, 0, 0, 0, 0],
            [0, 3, 0, 0, 0],
            [0, 0, 2, 0, 0],
            [0, 0, 0, 2, 0],
            [0, 0, 0, 0, 3],
        ]
        degree_matrix = create_matrix(degree_values, cell_size=0.68, font_size=20)
        degree_matrix.shift(LEFT * 2.3)
        label = Text("D  (degree matrix)", font_size=27, color=BLUE)
        label.next_to(degree_matrix, DOWN, buff=0.5)
        self.play(FadeIn(degree_matrix), Write(label))
        definition = VGroup(
            Text("Dᵢᵢ = sum of weights leaving node i", font_size=27),
            Text("D is diagonal because degrees belong to one node.", font_size=24, color=GRAY_B),
        )
        definition.arrange(DOWN, aligned_edge=LEFT, buff=0.35)
        definition.next_to(degree_matrix, RIGHT, buff=0.7)
        self.play(FadeIn(definition, shift=RIGHT))
        self.wait(3)
