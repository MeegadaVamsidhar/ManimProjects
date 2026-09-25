from manim import *
from commonFun import *

class Scene07_ClockwiseLookup(Scene):
    def construct(self):
        title = create_title("Clockwise Lookup")
        self.play(Write(title))
        ring = HashRing()
        self.play(Create(ring.circle))
        self.play(FadeIn(ring.labels))
        self.play(FadeIn(ring.center_label))
        legend = create_legend()
        self.play(FadeIn(legend))
        manager = HashRingManager(ring)
        server_data = [
            ("A",120,GREEN),
            ("B",420,RED),
            ("C",810,YELLOW)
        ]
        for name,value,color in server_data:
            server = ServerNode(name,value,color)
            manager.add_server(server)
            self.add(server)
        key_data = [
            ("Apple",210),
            ("Banana",560),
            ("Orange",920),
            ("Mango",730)
        ]
        for name,value in key_data:
            info = InfoBox(
                name,
                f"Hash = {value}"
            )
            info.to_edge(LEFT)
            self.play(FadeIn(info))
            key = KeyNode(name,value)
            manager.add_key(key)
            self.play(
                GrowFromCenter(key.dot),
                FadeIn(key.label)
            )
            owner = manager.find_owner(key)
            self.play(key.activate())
            self.play(owner.animate.scale(1.25), run_time=0.5)
            arrow = manager.create_arrow(key, owner)
            self.play(Create(arrow),run_time=1.5)
            owner_text = Text(
                f"Owner : Server {owner.name}",
                font_size=28,
                color=GREEN
            )
            owner_text.to_edge(DOWN)
            self.play(Write(owner_text))
            self.play(key.assigned())
            self.wait(1)
            self.play(
                FadeOut(info),
                FadeOut(owner_text),
                FadeOut(arrow)
            )
        summary = VGroup(
            Text(
                "Rule",
                font_size=30,
                color=GREEN
            ),
            Text(
                "Move Clockwise Until You Find",
                font_size=24
            ),
            Text(
                "The First Server",
                font_size=24,
                color=YELLOW
            )
        )
        summary.arrange(DOWN)
        summary.to_edge(DOWN)
        self.play(FadeIn(summary))
        self.wait(3)
