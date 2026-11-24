from manim import *

from common import create_cluster_legend, create_data_graph, create_title


class Scene09_KMeans(Scene):
    def construct(self):
        title = create_title("Step 4: Cluster the Embedding")
        self.play(Write(title))
        _, nodes, labels = create_data_graph(show_edges=False)
        self.play(FadeIn(nodes), FadeIn(labels))
        centers = VGroup(
            Star(outer_radius=0.28, color=GREEN, fill_opacity=1).move_to((-2.8, 0.2, 0)),
            Star(outer_radius=0.28, color=RED, fill_opacity=1).move_to((3.0, 0.2, 0)),
        )
        self.play(FadeIn(centers))
        caption = Text("Run a simple algorithm such as k-means.", font_size=28, color=YELLOW)
        caption.to_edge(DOWN)
        self.play(Write(caption))
        self.play(
            nodes[:4].animate.set_color(BLUE),
            nodes[4:].animate.set_color(ORANGE),
            run_time=1.5,
        )
        self.play(FadeOut(centers), FadeOut(caption))
        legend = create_cluster_legend()
        legend.to_edge(RIGHT).shift(DOWN * 1.5)
        self.play(FadeIn(legend))
        result = Text("The final clusters follow the graph, not just raw distance.", font_size=27, color=GREEN)
        result.to_edge(DOWN)
        self.play(Write(result))
        self.wait(3)
