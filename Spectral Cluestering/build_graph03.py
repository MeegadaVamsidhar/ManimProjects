from manim import *

from common import create_cluster_legend, create_data_graph, create_title


class Scene03_BuildGraph(Scene):
    def construct(self):
        title = create_title("Step 1: Build a Similarity Graph")
        self.play(Write(title))
        edges, nodes, labels = create_data_graph(show_edges=False)
        self.play(FadeIn(nodes), FadeIn(labels))
        explanation = Text("Nearby or similar points become connected.", font_size=28, color=YELLOW)
        explanation.to_edge(DOWN)
        self.play(Write(explanation))
        connected_edges, _, _ = create_data_graph(show_edges=True)
        self.play(Create(connected_edges), run_time=2)
        self.play(FadeOut(explanation))
        weights = Text("Edge weight = strength of similarity", font_size=26, color=GREEN)
        weights.to_edge(DOWN)
        self.play(Write(weights))
        legend = create_cluster_legend()
        legend.to_edge(RIGHT).shift(DOWN * 1.5)
        self.play(FadeIn(legend))
        self.wait(3)
