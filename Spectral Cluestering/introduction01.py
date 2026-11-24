from manim import *

from common import create_cluster_legend, create_data_graph


class Scene01_Introduction(Scene):
    def construct(self):
        title = Text("Spectral Clustering", font_size=54, weight=BOLD)
        subtitle = Text("Finding groups through the structure of a graph", font_size=26, color=GRAY_B)
        subtitle.next_to(title, DOWN)
        self.play(Write(title), FadeIn(subtitle))
        self.wait(2)
        self.play(FadeOut(subtitle), title.animate.to_edge(UP))

        edges, nodes, labels = create_data_graph(show_edges=False)
        nodes.set_opacity(0)
        labels.set_opacity(0)
        self.play(FadeIn(nodes), FadeIn(labels))
        self.play(
            nodes[0].animate.set_color(BLUE),
            nodes[1].animate.set_color(BLUE),
            nodes[2].animate.set_color(BLUE),
            nodes[3].animate.set_color(BLUE),
            nodes[4].animate.set_color(ORANGE),
            nodes[5].animate.set_color(ORANGE),
            nodes[6].animate.set_color(ORANGE),
            nodes[7].animate.set_color(ORANGE),
            run_time=1.5,
        )
        self.play(Create(edges), run_time=2)
        legend = create_cluster_legend()
        legend.to_edge(RIGHT).shift(DOWN * 1.5)
        self.play(FadeIn(legend))
        question = Text("Can connectivity reveal the clusters?", font_size=30, color=YELLOW)
        question.to_edge(DOWN)
        self.play(Write(question))
        self.wait(3)
