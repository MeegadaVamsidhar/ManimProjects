from manim import *

class Scene02_ScalingProblem(Scene):
    def construct(self):
        title = Text("Scaling the System", font_size=46, weight=BOLD)
        title.to_edge(UP)
        self.play(Write(title))
        self.wait()
        server = RoundedRectangle(
            width=2.5, height=1, corner_radius=0.1, color=GREEN, fill_opacity=0.25
        )
        server_label = Text("Server", font_size=28)
        server_label.move_to(server)
        self.play(FadeIn(server), Write(server_label))
        self.wait()
        users = VGroup()
        for i in range(12):
            circle = Circle(radius=0.18, color=BLUE, fill_opacity=1)
            label = Text(f"U{i + 1}", font_size=14)
            label.move_to(circle)
            user = VGroup(circle, label)
            row = i // 4
            col = i % 4
            user.move_to(LEFT * 5 + RIGHT * col * 1.2 + UP * (2 - row))
            users.add(user)
        self.play(LaggedStart(*[GrowFromCenter(u) for u in users], lag_ratio=0.08))
        arrows = VGroup()
        for user in users:
            arrow = Arrow(
                start=user.get_right(), end=server.get_left(), buff=0.2, stroke_width=2
            )
            arrows.add(arrow)
        self.play(
            LaggedStart(*[GrowArrow(a) for a in arrows], lag_ratio=0.05), run_time=2
        )
        self.wait()
        overload = Text("Overloaded!", color=RED, font_size=34)
        overload.next_to(server, DOWN)
        self.play(server.animate.set_fill(RED, opacity=0.4), Write(overload))
        self.wait(2)
        server1 = RoundedRectangle(width=2, height=0.9, corner_radius=0.1, color=GREEN)
        server2 = server1.copy()
        server3 = server1.copy()
        server_group = VGroup(server1, server2, server3)
        server_group.arrange(RIGHT, buff=1)
        server_group.move_to(DOWN * 1)
        labels = VGroup()
        for i, s in enumerate(server_group):
            txt = Text(f"Server {i}", font_size=22)
            txt.move_to(s)
            labels.add(txt)
        self.play(
            FadeOut(arrows), FadeOut(server), FadeOut(server_label), FadeOut(overload)
        )
        self.play(
            LaggedStart(*[FadeIn(s) for s in server_group], lag_ratio=0.2),
            LaggedStart(*[Write(l) for l in labels], lag_ratio=0.2),
        )
        self.wait()
        self.play(
            users.animate.arrange(RIGHT, buff=0.5)
            .scale(0.8)
            .next_to(title, DOWN, buff=0.4)
        )
        self.wait()
        question = Text("Which Server Stores Alice?", font_size=34, color=YELLOW)
        question.next_to(server_group, DOWN)
        self.play(Write(question))
        self.wait(2)
        examples = VGroup()
        names = ["Alice", "Bob", "Charlie", "David"]
        for i, name in enumerate(names):
            txt = Text(name, font_size=28)
            txt.move_to(LEFT * 5 + DOWN * (i * 0.8))
            examples.add(txt)
        self.play(LaggedStart(*[FadeIn(x) for x in examples], lag_ratio=0.2))
        self.wait()
        final = Text("We Need A Rule!", font_size=42, color=BLUE)
        final.to_edge(DOWN)
        self.play(Transform(question, final))
        self.wait(3)
