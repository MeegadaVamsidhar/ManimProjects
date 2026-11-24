from manim import *

from common import create_title


class Scene11_Summary(Scene):
    def construct(self):
        title = create_title("Spectral Clustering")
        self.play(Write(title))
        steps = VGroup(
            Text("1. Build a similarity graph", font_size=30),
            Text("2. Create W, D, and L = D - W", font_size=30),
            Text("3. Compute informative eigenvectors", font_size=30),
            Text("4. Embed points in spectral coordinates", font_size=30),
            Text("5. Apply k-means or another clustering method", font_size=30),
        )
        steps.arrange(DOWN, aligned_edge=LEFT, buff=0.32)
        steps.next_to(title, DOWN, buff=0.65)
        for step in steps:
            self.play(FadeIn(step, shift=RIGHT), run_time=0.55)
        box = SurroundingRectangle(steps[-1], color=GREEN, buff=0.15)
        self.play(Create(box))
        self.wait(1)
        takeaway = VGroup(
            Text("Connectivity reveals the hidden structure.", font_size=34, color=GREEN),
            Text("Spectral clustering turns that structure into groups.", font_size=29),
        )
        takeaway.arrange(DOWN, buff=0.25)
        self.play(FadeOut(steps), FadeOut(box), FadeIn(takeaway), run_time=1.5)
        thanks = Text("Thank You", font_size=44, color=BLUE)
        thanks.to_edge(DOWN)
        self.play(Write(thanks))
        self.wait(3)
