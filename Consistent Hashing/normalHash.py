from manim import *

class Scene03_TraditionalHashing(Scene):
    def construct(self):
        title = Text(
            "Traditional Hashing",
            font_size=44,
            weight=BOLD
        )
        title.to_edge(UP)
        self.play(Write(title))
        formula = Text(
            "Server = hash(key) mod 3",
            font_size=30
        )
        formula.scale(0.9)
        formula.next_to(title,DOWN)
        self.play(Write(formula))
        self.wait()
        servers = VGroup()
        colors = [GREEN,BLUE,RED]
        for i in range(3):
            box = RoundedRectangle(
                width=2,
                height=0.9,
                corner_radius=0.1,
                color=colors[i],
                fill_opacity=0.25
            )
            label = Text(
                f"Server {i}",
                font_size=22
            )
            label.move_to(box)
            group = VGroup(box,label)
            servers.add(group)
        servers.arrange(RIGHT,buff=1)
        servers.to_edge(DOWN)
        self.play(
            LaggedStart(
                *[
                    FadeIn(s)
                    for s in servers
                ],
                lag_ratio=0.2
            )
        )
        names = [
            ("Alice",154),
            ("Bob",219),
            ("Charlie",401),
            ("David",96)
        ]
        y = 2
        user_objects = []
        for name,value in names:
            user = Text(
                name,
                font_size=28
            )
            user.move_to(
                LEFT*5 + UP*y
            )
            self.play(FadeIn(user))
            arrow = Arrow(
                user.get_right(),
                user.get_right()+RIGHT*1.2
            )
            self.play(GrowArrow(arrow))
            hash_box = RoundedRectangle(
                width=2.3,
                height=0.8,
                corner_radius=0.1,
                color=YELLOW
            )
            hash_box.next_to(
                arrow,
                RIGHT
            )
            hash_text = Text(
                f"hash={value}",
                font_size=22
            )
            hash_text.move_to(hash_box)
            self.play(
                FadeIn(hash_box),
                Write(hash_text)
            )
            mod = value % 3
            mod_text = Text(
                f"{value}%3={mod}",
                font_size=22,
                color=BLUE
            )
            mod_text.next_to(
                hash_box,
                RIGHT
            )
            self.play(
                Write(mod_text)
            )
            target = servers[mod].get_top()+UP*0.6
            self.play(
                user.animate.move_to(target),
                FadeOut(arrow),
                FadeOut(hash_box),
                FadeOut(hash_text),
                FadeOut(mod_text),
                run_time=1.5
            )
            user_objects.append(user)
            y -= 1
        self.wait(2)
        problem = Text(
            "Need More Capacity",
            color=YELLOW,
            font_size=30
        )
        problem.next_to(
            formula,
            DOWN
        )
        self.play(
            Write(problem)
        )
        self.wait()
        new_server = RoundedRectangle(
            width=2,
            height=0.9,
            corner_radius=0.1,
            color=PURPLE,
            fill_opacity=0.25
        )
        new_server.next_to(
            servers,
            RIGHT,
            buff=1
        )
        new_label = Text(
            "Server 3",
            font_size=22
        )
        new_label.move_to(new_server)
        self.play(
            FadeIn(new_server),
            Write(new_label)
        )
        new_formula = Text(
            "Server = hash(key) mod 4",
            font_size=30
        )
        new_formula.scale(0.9)
        new_formula.next_to(
            title,
            DOWN
        )
        self.play(
            Transform(
                formula,
                new_formula
            )
        )
        self.wait()
        all_servers = [*servers, VGroup(new_server, new_label)]
        new_assignments = [value % 4 for _, value in names]
        target_counts = {index: 0 for index in range(4)}
        movements = []
        for user, target_index in zip(user_objects, new_assignments):
            level = target_counts[target_index]
            target_counts[target_index] += 1
            target = all_servers[target_index].get_top() + UP * (0.6 + level * 0.7)
            movements.append(user.animate.move_to(target))
        self.play(*movements, run_time=3)
        warning = Text(
            "3 of 4 Keys Moved!",
            color=RED,
            font_size=36
        )
        warning.next_to(problem, DOWN, buff=0.55)
        self.play(
            Write(warning)
        )
        self.wait(3)
