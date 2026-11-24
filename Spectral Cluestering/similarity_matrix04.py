from manim import *

from common import create_matrix, create_title


class Scene04_SimilarityMatrix(Scene):
    def construct(self):
        title = create_title("Similarity Matrix  W")
        self.play(Write(title))
        matrix_values = [
            [0, 1, 1, 0, 0, 0],
            [1, 0, 1, 1, 0, 0],
            [1, 1, 0, 1, 0, 0],
            [0, 1, 1, 0, 1, 0],
            [0, 0, 0, 1, 0, 1],
            [0, 0, 0, 0, 1, 0],
        ]
        matrix = create_matrix(matrix_values, cell_size=0.58, font_size=17)
        matrix.move_to(LEFT * 2.2)
        self.play(FadeIn(matrix), run_time=1.5)
        explanation = VGroup(
            Text("Wᵢⱼ is large when i and j are similar.", font_size=25),
            Text("W is symmetric: Wᵢⱼ = Wⱼᵢ", font_size=25, color=BLUE),
            Text("Zeros mean no direct connection.", font_size=25, color=ORANGE),
        )
        explanation.arrange(DOWN, aligned_edge=LEFT, buff=0.3)
        explanation.next_to(matrix, RIGHT, buff=0.8)
        for line in explanation:
            self.play(FadeIn(line), run_time=0.6)
        self.wait(3)
