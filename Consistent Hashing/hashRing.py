from manim import *
from commonFun import *

class Scene04_HashRing(Scene):
    def construct(self):
        title = create_title("Consistent Hash Ring")
        self.play(Write(title))
        line = NumberLine(x_range=[0, 1024, 128], length=10, include_numbers=False)
        line.shift(UP)
        line_label = Text("Linear Hash Space", font_size=28)
        line_label.next_to(line, UP)
        number_labels = VGroup(
            *[Text(str(value), font_size=18) for value in range(0, 1025, 128)]
        )
        for label, value in zip(number_labels, range(0, 1025, 128)):
            label.next_to(line.n2p(value), DOWN, buff=0.1)
        self.play(Create(line))
        self.play(FadeIn(line_label))
        self.play(FadeIn(number_labels))
        self.wait(2)
        wrap = CurvedArrow(line.n2p(1024), line.n2p(0), angle=-PI / 2, color=YELLOW)
        wrap_text = Text("Wrap Around", font_size=24, color=YELLOW)
        wrap_text.next_to(wrap, DOWN)
        self.play(Create(wrap), FadeIn(wrap_text))
        self.wait(2)
        self.play(FadeOut(line), FadeOut(line_label), FadeOut(wrap), FadeOut(wrap_text))
        ring = HashRing()
        self.play(Create(ring.circle), run_time=2)
        self.play(FadeIn(ring.labels))
        self.play(FadeIn(ring.center_label))
        clockwise_arrow = CurvedArrow(
            ring.circle.point_at_angle(PI / 3),
            ring.circle.point_at_angle(-PI / 3),
            angle=-PI / 2,
            color=ORANGE,
        )
        clockwise_text = Text("Clockwise Lookup", font_size=26, color=ORANGE)
        clockwise_text.next_to(clockwise_arrow, RIGHT, buff=0.5)
        clockwise_text.shift(UP * 1.4)
        self.play(Create(clockwise_arrow), FadeIn(clockwise_text))
        explanation = VGroup(
            Text("Hash Space is Circular", font_size=28),
            Text("After 1023 comes 0", font_size=22, color=BLUE),
        )
        explanation.arrange(DOWN)
        explanation.to_edge(DOWN)
        self.play(FadeIn(explanation))
        self.wait(3)
        self.play(
            FadeOut(clockwise_arrow), FadeOut(clockwise_text), FadeOut(explanation)
        )
        final_text = Text(
            "Servers and Keys will be placed on this ring", font_size=30, color=GREEN
        )
        final_text.to_edge(DOWN)
        self.play(Write(final_text))
        self.wait(3)
