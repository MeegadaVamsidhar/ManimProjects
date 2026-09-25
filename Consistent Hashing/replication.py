from manim import *
from commonFun import *

class Scene11_Replication(Scene):
    def construct(self):
        title = create_title("Replication")
        self.play(Write(title))
        ring = HashRing()
        manager = HashRingManager(ring)
        manager.initialize_scene(self)
        servers = [
            ServerNode("A",120,GREEN),
            ServerNode("B",420,RED),
            ServerNode("C",620,PURPLE),
            ServerNode("D",810,YELLOW)
        ]
        for server in servers:
            manager.add_server(server)
        keys = [
            KeyNode("Apple",210),
            KeyNode("Banana",560),
            KeyNode("Orange",930)
        ]
        for key in keys:
            manager.add_key(key)
        manager.show_servers(self)
        manager.show_keys(self)
        manager.assign_keys()
        intro = VGroup(
            Text(
                "One Primary Copy",
                font_size=30,
                color=GREEN
            ),
            Text(
                "Two Replica Copies",
                font_size=24
            )
        )
        intro.arrange(DOWN)
        intro.to_edge(DOWN)
        self.play(FadeIn(intro))
        self.wait(2)
        self.play(FadeOut(intro))
        for key in manager.keys:
            manager.animate_replication(
                self,
                key,
                replicas=2
            )
        summary = VGroup(
            Text(
                "Replication Benefits",
                font_size=30,
                color=GREEN
            ),
            Text(
                "High Availability",
                font_size=24
            ),
            Text(
                "Fault Tolerance",
                font_size=24
            ),
            Text(
                "Data Durability",
                font_size=24,
                color=YELLOW
            )
        )
        summary.arrange(DOWN)
        summary.to_edge(DOWN)
        self.play(FadeIn(summary))
        self.wait(4)
