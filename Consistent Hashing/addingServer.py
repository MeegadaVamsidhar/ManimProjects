from manim import *
from commonFun import *

class Scene08_AddServer(Scene):
    def construct(self):
        title = create_title("Adding a New Server")
        self.play(Write(title))
        ring = HashRing()
        manager = HashRingManager(ring)
        manager.initialize_scene(self)
        servers = [
            ServerNode("A", 120, GREEN),
            ServerNode("B", 420, RED),
            ServerNode("C", 810, YELLOW),
        ]
        for server in servers:
            manager.add_server(server)
        keys = [
            KeyNode("Apple", 210),
            KeyNode("Banana", 560),
            KeyNode("Mango", 730),
            KeyNode("Orange", 920),
        ]
        for key in keys:
            manager.add_key(key)
        manager.show_servers(self)
        manager.show_keys(self)
        manager.assign_keys()
        manager.show_arrows(self)
        regions = manager.redraw_regions()
        self.play(Create(regions))
        self.wait(2)
        info = InfoBox("Add Server D", "Hash = 620")
        info.to_edge(LEFT)
        self.play(FadeIn(info))
        previous = manager.snapshot()
        server_d = ServerNode("D", 620, PURPLE)
        manager.add_server(server_d)
        self.play(GrowFromCenter(server_d.dot), FadeIn(server_d.label))
        self.wait(1)
        self.play(FadeOut(info), FadeOut(regions))
        manager.remove_arrows(self)
        manager.update()
        new_regions = manager.redraw_regions()
        self.play(Create(new_regions))
        changes = manager.changed_keys(previous)
        manager.animate_changes(self, changes)
        manager.show_arrows(self)
        summary = VGroup(
            Text("Observation", font_size=30, color=GREEN),
            Text("Only keys in the new server's interval", font_size=24),
            Text("change ownership", font_size=24, color=YELLOW),
        )
        summary.arrange(DOWN, buff=0.2)
        summary.to_edge(DOWN, buff=0.4)
        self.play(FadeIn(summary))
        self.wait(3)
        self.play(FadeOut(summary), FadeOut(new_regions))
        final = Text(
            "Consistent Hashing minimizes data movement", font_size=30, color=GREEN
        )
        final.to_edge(DOWN)
        self.play(Write(final))
        self.wait(3)
