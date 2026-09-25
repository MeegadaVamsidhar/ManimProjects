from manim import *
from commonFun import *

class Scene10_VirtualNodes(Scene):
    def construct(self):
        title = create_title("Virtual Nodes")
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
        manager.show_servers(self)
        regions = manager.redraw_regions()
        self.play(Create(regions))
        text1 = VGroup(
            Text("Problem", font_size=30, color=RED),
            Text("Servers own different sized regions", font_size=24),
        )
        text1.arrange(DOWN)
        text1.to_edge(DOWN, buff=0.4)
        self.play(FadeIn(text1))
        self.wait(2)
        self.play(FadeOut(text1), FadeOut(regions))
        info = InfoBox("Solution", "Virtual Nodes")
        info.to_edge(LEFT)
        self.play(FadeIn(info))
        virtual_nodes = []
        virtual_nodes.extend(manager.add_virtual_nodes("A", [40, 180, 920], GREEN))
        virtual_nodes.extend(manager.add_virtual_nodes("B", [300, 500, 680], RED))
        virtual_nodes.extend(manager.add_virtual_nodes("C", [760, 860, 980], YELLOW))
        for vnode in virtual_nodes:
            self.play(GrowFromCenter(vnode.dot), FadeIn(vnode.label), run_time=0.25)
        self.play(FadeOut(info))
        new_regions = manager.redraw_regions()
        self.play(Create(new_regions))
        explanation = VGroup(
            Text("Each Physical Server", font_size=28, color=GREEN),
            Text("Owns Multiple Virtual Nodes", font_size=24),
            Text("Load Becomes Balanced", font_size=24, color=BLUE),
        )
        explanation.arrange(DOWN)
        explanation.to_edge(DOWN, buff=0.4)
        self.play(FadeIn(explanation))
        self.wait(3)
        self.play(FadeOut(explanation))
        keys = [
            KeyNode("Apple", 210),
            KeyNode("Banana", 560),
            KeyNode("Mango", 730),
            KeyNode("Orange", 360),
            KeyNode("Cherry", 260),
            KeyNode("Lemon", 470),
        ]
        for key in keys:
            manager.add_key(key)
        manager.show_keys(self)
        manager.assign_keys()
        manager.animate_lookup(self)
        summary = VGroup(
            Text("Benefits", font_size=30, color=GREEN),
            Text("Better Load Balancing", font_size=24),
            Text("Better Fault Tolerance", font_size=24),
            Text("Minimal Data Movement", font_size=24, color=YELLOW),
        )
        summary.arrange(DOWN)
        summary.to_edge(DOWN, buff=0.4)
        self.play(FadeIn(summary))
        self.wait(4)
