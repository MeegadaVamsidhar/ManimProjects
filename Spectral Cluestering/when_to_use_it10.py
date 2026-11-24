from manim import *

from common import create_title


class Scene10_WhenToUseIt(Scene):
    def construct(self):
        title = create_title("Why Spectral Clustering?")
        self.play(Write(title))
        rows = VGroup(
            Text("✓ Finds non-convex and intertwined groups", font_size=28),
            Text("✓ Uses pairwise similarity and connectivity", font_size=28),
            Text("✓ Reveals communities in networks", font_size=28),
            Text("⚠ Eigenvector computation can be expensive", font_size=28, color=ORANGE),
        )
        rows.arrange(DOWN, aligned_edge=LEFT, buff=0.35)
        rows.next_to(title, DOWN, buff=0.8)
        for row in rows:
            self.play(FadeIn(row, shift=RIGHT), run_time=0.6)
        self.wait(3)
