from manim import *

class Scene01_Introduction(Scene):
    def construct(self):
        title = Text(
            "Consistent Hashing",
            font_size=54,
            weight=BOLD
        )
        subtitle = Text(
            "A Distributed Systems Technique",
            font_size=28,
            color=GRAY_B
        )
        subtitle.next_to(title, DOWN)
        self.play(Write(title))
        self.play(FadeIn(subtitle))
        self.wait(2)
        self.play(
            FadeOut(subtitle),
            title.animate.to_edge(UP)
        )
        users = VGroup()
        for row in range(2):
            for col in range(5):
                circle = Circle(
                    radius=0.25,
                    color=BLUE,
                    fill_opacity=1
                )
                label = Text(
                    f"U{row*5+col+1}",
                    font_size=18
                )
                label.move_to(circle)
                user = VGroup(circle, label)
                user.move_to(
                    LEFT*5 +
                    RIGHT*col*1.2 +
                    UP*(1-row)
                )
                users.add(user)
        self.play(
            LaggedStart(
                *[GrowFromCenter(user) for user in users],
                lag_ratio=0.15
            )
        )
        self.wait()
        server = RoundedRectangle(
            width=2.5,
            height=1.2,
            corner_radius=0.15,
            color=GREEN,
            fill_opacity=0.2
        )
        server.shift(DOWN*2)
        server_text = Text(
            "Server",
            font_size=28
        )
        server_text.move_to(server)
        self.play(
            FadeIn(server),
            Write(server_text)
        )
        self.wait()
        arrows = VGroup()
        for user in users:
            arrow = Arrow(
                start=user.get_bottom(),
                end=server.get_top(),
                buff=0.25,
                stroke_width=3
            )
            arrows.add(arrow)
        self.play(
            LaggedStart(
                *[
                    GrowArrow(a)
                    for a in arrows
                ],
                lag_ratio=0.08
            ),
            run_time=2
        )
        self.wait()
        overload = Text(
            "Server Overloaded!",
            color=RED,
            font_size=36
        )
        overload.next_to(server, DOWN)
        self.play(
            server.animate.set_fill(
                RED,
                opacity=0.5
            ),
            Write(overload)
        )
        self.wait(2)
        question = Text(
            "How do we distribute data efficiently?",
            font_size=34,
            color=YELLOW
        )
        question.to_edge(DOWN)
        self.play(
            FadeOut(overload),
            Write(question)
        )
        self.wait(3)
