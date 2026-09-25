from manim import *
from commonFun import *

class Scene09_RemoveServer(Scene):
    def construct(self):
        title = create_title("Removing a Server")
        self.play(Write(title))
        ring = HashRing()
        manager = HashRingManager(ring)
        manager.initialize_scene(self)
        servers = [
            ServerNode("A", 120, GREEN),
            ServerNode("B", 420, RED),
            ServerNode("C", 810, YELLOW),
            ServerNode("D", 620, PURPLE),
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
        info = InfoBox("Remove Server", "Server B")
        info.to_edge(LEFT)
        self.play(FadeIn(info))
        previous = manager.snapshot()
        server_b = None
        for server in manager.servers:
            if server.name == "B":
                server_b = server
                break
        self.play(server_b.dot.animate.scale(1.5), server_b.label.animate.scale(1.3))
        self.wait(1)
        self.play(FadeOut(server_b))
        manager.remove_server("B")
        self.play(FadeOut(info), FadeOut(regions))
        manager.update()
        new_regions = manager.redraw_regions()
        self.play(Create(new_regions))
        changes = manager.changed_keys(previous)
        for key, old_owner, new_owner in changes:
            self.play(key.dot.animate.set_color(ORANGE), run_time=0.3)
            manager.update_arrow(self, key)
            text = Text(
                f"{key.name}: {old_owner.name} → {new_owner.name}",
                font_size=24,
                color=GREEN,
            )
            text.to_edge(DOWN)
            self.play(FadeIn(text))
            self.wait(0.7)
            self.play(FadeOut(text), key.dot.animate.set_color(WHITE))
        summary = VGroup(
            Text("Observation", font_size=30, color=GREEN),
            Text("Only keys owned by Server B", font_size=24),
            Text("are reassigned", font_size=24, color=YELLOW),
        )
        summary.arrange(DOWN)
        summary.to_edge(DOWN, buff=0.4)
        self.play(FadeIn(summary))
        self.wait(3)
        self.play(FadeOut(summary), FadeOut(new_regions))
        final = Text(
            "Server failures affect only a small portion of the ring",
            font_size=28,
            color=GREEN,
        )
        final.to_edge(DOWN)
        self.play(Write(final))
        self.wait(3)
