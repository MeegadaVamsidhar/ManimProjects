from manim import *
from commonFun import *

class Scene05_PlaceServers(Scene):
    def construct(self):
        title = create_title("Placing Servers on the Hash Ring")
        self.play(Write(title))
        ring = HashRing(radius=1.9)
        self.play(Create(ring.circle), run_time=2)
        self.play(FadeIn(ring.labels))
        self.play(FadeIn(ring.center_label))
        legend = create_legend()
        self.play(FadeIn(legend))
        server_data = [("A", 120, GREEN), ("B", 420, RED), ("C", 810, YELLOW)]
        manager = HashRingManager(ring)
        for name, hash_value, color in server_data:
            info = InfoBox(f"Server {name}", f"Hash = {hash_value}")
            info.to_edge(LEFT)
            self.play(FadeIn(info))
            server = ServerNode(name, hash_value, color)
            server.place_on_ring(ring)
            self.play(GrowFromCenter(server.dot), FadeIn(server.label), run_time=1)
            self.play(server.highlight(), run_time=0.5)
            self.play(server.reset(), run_time=0.5)
            manager.add_server(server)
            self.play(FadeOut(info))
        explanation = VGroup(
            Text("Servers are hashed into the same hash space", font_size=28),
            Text(
                "Each server occupies one position on the ring",
                font_size=22,
                color=BLUE,
            ),
        )
        explanation.arrange(DOWN)
        explanation.to_edge(DOWN)
        self.play(FadeIn(explanation))
        self.wait(2)
        ownership = manager.build_ownership()
        self.play(
            LaggedStart(*[Create(arc) for arc in ownership], lag_ratio=0.2),
            run_time=2,
        )
        ownership_text = Text(
            "Each colored arc represents the ownership range of a server",
            font_size=24,
            color=YELLOW,
        )
        ownership_text.to_edge(DOWN, buff=0.4)
        self.play(ReplacementTransform(explanation, ownership_text))
        self.wait(3)
        self.play(FadeOut(ownership_text), FadeOut(ownership))
        summary = VGroup(
            Text("Next:", font_size=30, color=GREEN),
            Text("Keys will also be placed on the same ring", font_size=26),
        )
        summary.arrange(DOWN)
        summary.to_edge(DOWN)
        self.play(FadeIn(summary))
        self.wait(3)
