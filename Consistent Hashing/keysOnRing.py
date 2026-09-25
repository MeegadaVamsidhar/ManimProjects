from manim import *
from commonFun import *

class Scene06_PlaceKeys(Scene):
    def construct(self):
        title = create_title("Placing Keys on the Hash Ring")
        self.play(Write(title))
        ring = HashRing()
        self.play(Create(ring.circle), run_time=2)
        self.play(FadeIn(ring.labels))
        self.play(FadeIn(ring.center_label))
        legend = create_legend()
        self.play(FadeIn(legend))
        servers = [
            ServerNode("A",120,GREEN),
            ServerNode("B",420,RED),
            ServerNode("C",810,YELLOW)
        ]
        for server in servers:
            server.place_on_ring(ring)
            self.add(server)
        server_info = Text(
            "Servers are already placed",
            font_size=26,
            color=GREEN
        )
        server_info.to_edge(DOWN)
        self.play(FadeIn(server_info))
        self.wait(1)
        self.play(FadeOut(server_info))
        key_data = [
            ("Apple",210),
            ("Banana",560),
            ("Mango",730),
            ("Orange",920)
        ]
        keys = []
        for name, value in key_data:
            info = InfoBox(
                name,
                f"Hash = {value}"
            )
            info.to_edge(LEFT)
            self.play(FadeIn(info))
            key = KeyNode(name,value)
            key.place_on_ring(ring)
            self.play(
                GrowFromCenter(key.dot),
                FadeIn(key.label),
                run_time=1
            )
            keys.append(key)
            self.play(FadeOut(info))
        explanation = VGroup(
            Text(
                "Keys and Servers share the same hash space",
                font_size=28
            ),
            Text(
                "Keys are NOT assigned yet",
                font_size=22,
                color=YELLOW
            ),
            Text(
                "Assignment happens using Clockwise Lookup",
                font_size=22,
                color=BLUE
            )
        )
        explanation.arrange(DOWN)
        explanation.to_edge(DOWN)
        self.play(FadeIn(explanation))
        self.wait(3)
        self.play(FadeOut(explanation))
        arrows = VGroup()
        for key in keys:
            arrow = CurvedArrow(
                key.get_center(),
                ring.circle.get_center(),
                angle=-PI/5,
                color=ORANGE
            )
            arrows.add(arrow)
        self.play(
            LaggedStart(
                *[Create(a) for a in arrows],
                lag_ratio=0.2
            ),
            run_time=2
        )
        summary = Text(
            "Next: Find the First Server Clockwise",
            font_size=30,
            color=GREEN
        )
        summary.to_edge(DOWN)
        self.play(
            FadeOut(arrows),
            FadeIn(summary)
        )
        self.wait(3)
