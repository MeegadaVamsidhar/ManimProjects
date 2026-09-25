from manim import *
from commonFun import *

class Scene12_Summary(Scene):
    def construct(self):
        title = create_title("Consistent Hashing")
        self.play(Write(title))
        points = [
            "Traditional Hashing",
            "Adding a Server Moves Almost Every Key",
            "Hash Ring",
            "Servers are Placed on the Ring",
            "Keys are Placed on the Ring",
            "Clockwise Lookup",
            "Adding a Server",
            "Removing a Server",
            "Virtual Nodes",
            "Replication",
            "Minimal Data Movement"
        ]
        items = VGroup()
        for point in points:
            bullet = Text(
                "• " + point,
                font_size=30
            )
            items.add(bullet)
        items.arrange(
            DOWN,
            aligned_edge=LEFT,
            buff=0.35
        )
        items.scale(0.85)
        items.next_to(title, DOWN, buff=0.6)
        for item in items:
            self.play(
                FadeIn(item, shift=RIGHT),
                run_time=0.5
            )
        self.wait(2)
        box = SurroundingRectangle(
            items[-1],
            color=GREEN,
            buff=0.15
        )
        self.play(Create(box))
        self.wait(1)
        final = VGroup(
            Text(
                "Why Consistent Hashing?",
                font_size=34,
                color=GREEN
            ),
            Text(
                "✓ Scalable",
                font_size=28
            ),
            Text(
                "✓ Fault Tolerant",
                font_size=28
            ),
            Text(
                "✓ Load Balanced",
                font_size=28
            ),
            Text(
                "✓ Minimal Key Movement",
                font_size=28,
                color=YELLOW
            )
        )
        final.arrange(
            DOWN,
            buff=0.25
        )
        final.move_to(items)
        self.play(
            FadeOut(items),
            FadeOut(box)
        )
        self.play(
            FadeIn(final),
            run_time=2
        )
        self.wait(3)
        thanks = Text(
            "Thank You",
            font_size=44,
            color=BLUE
        )
        thanks.to_edge(DOWN)
        self.play(Write(thanks))
        self.wait(3)
