from manim import *

from common import create_title


class Scene07_Eigenvectors(Scene):
    def construct(self):
        title = create_title("Step 3: Find Eigenvectors")
        self.play(Write(title))
        equation = Text("L v = λ v", font_size=46, color=YELLOW)
        equation.shift(UP * 1.5)
        self.play(Write(equation))
        explanation = VGroup(
            Text("Eigenvectors are special directions in the graph.", font_size=27),
            Text("The second-smallest eigenvector is the Fiedler vector.", font_size=27, color=GREEN),
            Text("Its signs often separate two communities.", font_size=27),
        )
        explanation.arrange(DOWN, aligned_edge=LEFT, buff=0.3)
        explanation.next_to(equation, DOWN, buff=0.65)
        for line in explanation:
            self.play(FadeIn(line), run_time=0.65)
        self.wait(3)
