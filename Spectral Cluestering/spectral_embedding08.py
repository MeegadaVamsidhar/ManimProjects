from manim import *

from common import create_data_graph, create_title


class Scene08_SpectralEmbedding(Scene):
    def construct(self):
        title = create_title("Turn Structure into Coordinates")
        self.play(Write(title))
        _, nodes, labels = create_data_graph(show_edges=False)
        original = VGroup(nodes, labels)
        self.play(FadeIn(original))
        arrow = Arrow(LEFT * 0.5, RIGHT * 0.5, color=YELLOW)
        arrow.shift(DOWN * 0.2)
        arrow_label = Text("eigenvector coordinates", font_size=22, color=YELLOW)
        arrow_label.next_to(arrow, DOWN, buff=0.2)
        self.play(GrowArrow(arrow), FadeIn(arrow_label))
        embedded_points = VGroup()
        embedded_labels = VGroup()
        positions = [
            (-3, 0.8), (-2.4, 0.5), (-2.8, -0.2), (-2.1, -0.7),
            (2.0, 0.7), (2.8, 0.4), (2.3, -0.3), (3.1, -0.7),
        ]
        for index, (x, y) in enumerate(positions):
            point = Dot((x, y, 0), radius=0.16, color=BLUE if index < 4 else ORANGE)
            embedded_points.add(point)
            label = Text(str(index + 1), font_size=18)
            label.next_to(point, DOWN, buff=0.08)
            embedded_labels.add(label)
        embedded = VGroup(embedded_points, embedded_labels)
        self.play(TransformFromCopy(original, embedded), run_time=2)
        caption = Text("Points close in graph structure become close here.", font_size=27, color=GREEN)
        caption.to_edge(DOWN)
        self.play(Write(caption))
        self.wait(3)
