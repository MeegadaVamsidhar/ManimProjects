from manim import *
import math

HASH_SPACE = 1024
RING_RADIUS = 3

SERVER_RADIUS = 0.10
KEY_RADIUS = 0.07
VNODE_RADIUS = 0.06

SERVER_FONT = 22
KEY_FONT = 18

SERVER_COLORS = [GREEN, RED, YELLOW, PURPLE, ORANGE, TEAL]

def hash_to_angle(value):
    return PI / 2 - (value / HASH_SPACE) * TAU

def hash_to_point(value, circle):
    return circle.point_at_angle(hash_to_angle(value))

class HashRing(VGroup):
    def __init__(self, radius=RING_RADIUS):
        super().__init__()
        self.radius = radius
        self.circle = Circle(radius=radius, color=BLUE, stroke_width=6)
        self.labels = VGroup()
        for value in range(0, HASH_SPACE, 128):
            txt = Text(str(value), font_size=20)
            txt.move_to(hash_to_point(value, self.circle) * 1.26)
            self.labels.add(txt)
        self.title = Text("Hash Ring", font_size=30, color=GREEN)
        self.center_label = self.title
        self.title.move_to(self.circle.get_center())
        self.add(self.circle, self.labels, self.title)
    def point(self, value):
        return hash_to_point(value, self.circle)

class ServerNode(VGroup):
    def __init__(self, name, hash_value, color=GREEN):
        super().__init__()
        if not name:
            raise ValueError("A server name is required")
        if not isinstance(hash_value, int) or not 0 <= hash_value < HASH_SPACE:
            raise ValueError(f"Server hash must be an integer in [0, {HASH_SPACE})")
        self.name = name
        self.physical_name = name
        self.hash = hash_value
        self.color = color
        self.dot = Dot(radius=SERVER_RADIUS, color=color)
        self.label = Text(name, font_size=SERVER_FONT)
        self.label.next_to(self.dot, UP, buff=0.08)
        self.add(self.dot, self.label)
    def place(self, ring):
        self.move_to(ring.point(self.hash))
    def place_on_ring(self, ring):
        self.place(ring)
    def highlight(self):
        return AnimationGroup(
            self.dot.animate.scale(1.4), self.label.animate.scale(1.2), lag_ratio=0
        )
    def reset(self):
        return AnimationGroup(
            self.dot.animate.scale(1 / 1.4),
            self.label.animate.scale(1 / 1.2),
            lag_ratio=0,
        )

class VirtualServerNode(ServerNode):
    def __init__(self, parent, index, hash_value, color=GREEN):
        super().__init__(f"{parent}{index}", hash_value, color)
        self.physical_name = parent
        self.dot.scale(0.75)
        self.label.scale(0.6)

class KeyNode(VGroup):
    def __init__(self, name, hash_value):
        super().__init__()
        if not name:
            raise ValueError("A key name is required")
        if not isinstance(hash_value, int) or not 0 <= hash_value < HASH_SPACE:
            raise ValueError(f"Key hash must be an integer in [0, {HASH_SPACE})")
        self.name = name
        self.hash = hash_value
        self.dot = Dot(radius=KEY_RADIUS, color=WHITE)
        self.label = Text(name[0], font_size=KEY_FONT)
        self.label.next_to(self.dot, DOWN, buff=0.05)
        self.add(self.dot, self.label)
    def place(self, ring):
        self.move_to(ring.point(self.hash))
    def place_on_ring(self, ring):
        self.place(ring)
    def activate(self):
        return self.dot.animate.set_color(ORANGE)
    def assigned(self):
        return self.dot.animate.set_color(WHITE)

class OwnershipArrow(CurvedArrow):
    def __init__(self, key, server, color=ORANGE):
        super().__init__(
            key.get_center(),
            server.get_center(),
            angle=-PI / 3,
            color=color,
            stroke_width=3,
        )

class ReplicationArrow(CurvedArrow):
    def __init__(self, server1, server2):
        super().__init__(
            server1.get_center(),
            server2.get_center(),
            angle=-PI / 5,
            color=BLUE,
            stroke_width=2,
        )

class InfoBox(VGroup):
    def __init__(self, title, subtitle):
        super().__init__()
        box = RoundedRectangle(width=3, height=1.2, corner_radius=0.15, color=YELLOW)
        t1 = Text(title, font_size=24)
        t2 = Text(subtitle, font_size=20, color=BLUE)
        texts = VGroup(t1, t2)
        texts.arrange(DOWN, buff=0.1)
        texts.move_to(box)
        self.add(box, texts)

def create_title(text):
    t = Text(text, font_size=42, weight=BOLD)
    t.to_edge(UP)
    return t

def create_legend():
    legend = VGroup(
        Dot(color=GREEN),
        Text("Server", font_size=18),
        Dot(color=WHITE),
        Text("Key", font_size=18),
    )
    legend.arrange(RIGHT, buff=0.2)
    legend.scale(0.8)
    legend.to_corner(DOWN + LEFT)
    return legend

# ==========================
# Hash Ring Manager
# ==========================

class HashRingManager:
    def __init__(self, ring):
        self.ring = ring
        self.servers = []
        self.keys = []
        self.assignments = {}
        self.arrows = {}
    def sort_servers(self):
        self.servers.sort(key=lambda s: s.hash)
    def add_server(self, server):
        if any(existing.name == server.name for existing in self.servers):
            raise ValueError(f"Server name already exists: {server.name}")
        if any(existing.hash == server.hash for existing in self.servers):
            raise ValueError(f"Hash position already occupied: {server.hash}")
        server.place(self.ring)
        self.servers.append(server)
        self.sort_servers()
    def remove_server(self, name):
        self.servers = [s for s in self.servers if s.physical_name != name]
        self.sort_servers()
    def add_key(self, key):
        if any(existing.name == key.name for existing in self.keys):
            raise ValueError(f"Key name already exists: {key.name}")
        key.place(self.ring)
        self.keys.append(key)
    def clear_assignments(self):
        self.assignments.clear()
    def find_owner(self, key):
        if len(self.servers) == 0:
            return None
        key_hash = key.hash if hasattr(key, "hash") else key
        if not isinstance(key_hash, int) or not 0 <= key_hash < HASH_SPACE:
            raise ValueError(f"Key hash must be an integer in [0, {HASH_SPACE})")
        for server in self.servers:
            if key_hash <= server.hash:
                return server
        return self.servers[0]
    def assign_keys(self):
        self.assignments.clear()
        for key in self.keys:
            owner = self.find_owner(key)
            self.assignments[key] = owner
    def owner(self, key):
        try:
            return self.assignments[key]
        except KeyError as exc:
            raise KeyError(f"Key has not been assigned: {getattr(key, 'name', key)!r}") from exc
    def assignment_changed(self, key, old):
        if key not in old:
            return False
        return old[key] != self.owner(key)
    def create_arrow(self, key, owner=None):
        if owner is None:
            owner = self.owner(key)
        return OwnershipArrow(key, owner)
    def build_arrows(self):
        self.arrows.clear()
        for key in self.keys:
            self.arrows[key] = self.create_arrow(key)
    def server_after(self, server):
        index = self.servers.index(server)
        if index == len(self.servers) - 1:
            return self.servers[0]
        return self.servers[index + 1]
    def server_before(self, server):
        index = self.servers.index(server)
        if index == 0:
            return self.servers[-1]
        return self.servers[index - 1]
    def ownership_arc(self, server):
        if len(self.servers) == 1:
            return Arc(
                radius=self.ring.radius + 0.15,
                start_angle=0,
                angle=TAU,
                stroke_width=8,
                color=server.color,
            )
        previous = self.server_before(server)
        start = hash_to_angle(previous.hash)
        end = hash_to_angle(server.hash)
        if end > start:
            end -= TAU
        return Arc(
            radius=self.ring.radius + 0.15,
            start_angle=start,
            angle=end - start,
            stroke_width=8,
            color=server.color,
        )
    def build_ownership(self):
        arcs = VGroup()
        for server in self.servers:
            arcs.add(self.ownership_arc(server))
        return arcs
    def show_servers(self, scene):
        for server in self.servers:
            scene.play(GrowFromCenter(server.dot), FadeIn(server.label), run_time=0.6)
    def show_keys(self, scene):
        for key in self.keys:
            scene.play(GrowFromCenter(key.dot), FadeIn(key.label), run_time=0.5)
    def animate_replication(self, scene, key, replicas=2):
        owner = self.owner(key)
        scene.play(key.dot.animate.set_color(ORANGE), run_time=0.3)
        scene.play(
            owner.dot.animate.scale(1.4), owner.label.animate.scale(1.2), run_time=0.3
        )
        primary = OwnershipArrow(key, owner)
        scene.play(Create(primary))
        info = Text(f"Primary : {owner.name}", font_size=24, color=GREEN)
        info.to_edge(DOWN)
        scene.play(FadeIn(info))
        replica_servers = self.replication_targets(owner, replicas)
        arrows = VGroup()
        for replica in replica_servers:
            arrow = ReplicationArrow(owner, replica)
            arrows.add(arrow)
            scene.play(Create(arrow), run_time=0.6)
            scene.play(
                replica.dot.animate.scale(1.3),
                replica.label.animate.scale(1.15),
                run_time=0.3,
            )
        scene.wait(1)
        scene.play(FadeOut(info), FadeOut(primary), FadeOut(arrows))
        scene.play(owner.dot.animate.scale(1 / 1.4), owner.label.animate.scale(1 / 1.2))
        for replica in replica_servers:
            scene.play(
                replica.dot.animate.scale(1 / 1.3),
                replica.label.animate.scale(1 / 1.15),
                run_time=0.2,
            )
        scene.play(key.dot.animate.set_color(WHITE))
    def show_arrows(self, scene):
        if len(self.arrows) == 0:
            self.build_arrows()
        scene.play(
            LaggedStart(*[Create(a) for a in self.arrows.values()], lag_ratio=0.1)
        )
    def update_arrow(self, scene, key):
        old_arrow = self.arrows[key]
        new_arrow = OwnershipArrow(key, self.owner(key))
        self.play_arrow_change(scene, old_arrow, new_arrow)
        self.arrows[key] = new_arrow
    def play_arrow_change(self, scene, old_arrow, new_arrow):
        scene.play(ReplacementTransform(old_arrow, new_arrow), run_time=1)
    def remove_arrows(self, scene):
        scene.play(*[FadeOut(a) for a in self.arrows.values()])
        self.arrows.clear()
    def highlight_server(self, scene, server):
        scene.play(
            server.dot.animate.scale(1.4), server.label.animate.scale(1.2), run_time=0.3
        )
    def reset_server(self, scene, server):
        scene.play(
            server.dot.animate.scale(1 / 1.4),
            server.label.animate.scale(1 / 1.2),
            run_time=0.3,
        )
    def highlight_key(self, scene, key):
        scene.play(key.dot.animate.set_color(ORANGE), run_time=0.3)
    def reset_key(self, scene, key):
        scene.play(key.dot.animate.set_color(WHITE), run_time=0.3)
    def animate_lookup(self, scene):
        self.assign_keys()
        for key in self.keys:
            owner = self.owner(key)
            arrow = OwnershipArrow(key, owner)
            self.highlight_key(scene, key)
            self.highlight_server(scene, owner)
            scene.play(Create(arrow), run_time=0.8)
            text = Text(
                f"{key.name} → Server {owner.physical_name}",
                font_size=24,
                color=GREEN,
            )
            text.to_edge(DOWN, buff=0.4)
            scene.play(FadeIn(text))
            scene.wait(0.4)
            scene.play(FadeOut(text), FadeOut(arrow))
            self.reset_server(scene, owner)
            self.reset_key(scene, key)
    # ==========================
    # Dynamic Updates
    # ==========================
    def snapshot(self):
        return dict(self.assignments)
    def update(self):
        self.assign_keys()
    def changed_keys(self, old_assignments):
        changed = []
        for key in self.keys:
            if key not in old_assignments:
                continue
            old_owner = old_assignments[key]
            new_owner = self.owner(key)
            if old_owner != new_owner:
                changed.append((key, old_owner, new_owner))
        return changed
    def animate_changes(self, scene, changes):
        for key, old_owner, new_owner in changes:
            scene.play(key.dot.animate.set_color(ORANGE), run_time=0.3)
            scene.play(
                old_owner.dot.animate.scale(1.3),
                new_owner.dot.animate.scale(1.3),
                run_time=0.3,
            )
            old_arrow = OwnershipArrow(key, old_owner, color=RED)
            new_arrow = OwnershipArrow(key, new_owner, color=GREEN)
            scene.play(Create(old_arrow))
            scene.play(ReplacementTransform(old_arrow, new_arrow), run_time=1)
            text = Text(
                f"{key.name} : {old_owner.name} → {new_owner.name}",
                font_size=24,
                color=GREEN,
            )
            text.to_edge(DOWN, buff=0.4)
            scene.play(FadeIn(text))
            scene.wait(0.6)
            scene.play(FadeOut(text), FadeOut(new_arrow))
            scene.play(
                old_owner.dot.animate.scale(1 / 1.3),
                new_owner.dot.animate.scale(1 / 1.3),
                key.dot.animate.set_color(WHITE),
                run_time=0.3,
            )
    # ==========================
    # Virtual Nodes
    # ==========================
    def add_virtual_nodes(self, parent, hashes, color=GREEN):
        nodes = []
        if not hashes:
            return nodes
        if any(not isinstance(value, int) or not 0 <= value < HASH_SPACE for value in hashes):
            raise ValueError(f"Virtual-node hashes must be integers in [0, {HASH_SPACE})")
        existing_hashes = {server.hash for server in self.servers}
        duplicate_hashes = existing_hashes.intersection(hashes)
        if duplicate_hashes:
            raise ValueError(f"Hash position already occupied: {min(duplicate_hashes)}")
        if len(set(hashes)) != len(hashes):
            raise ValueError("Virtual-node hash positions must be unique")
        for index, value in enumerate(hashes):
            vnode = VirtualServerNode(parent, index + 1, value, color)
            vnode.place(self.ring)
            self.servers.append(vnode)
            nodes.append(vnode)
        self.sort_servers()
        return nodes
    # ==========================
    # Replication
    # ==========================
    def replication_targets(self, owner, replicas=2):
        if replicas < 0:
            raise ValueError("replicas must be non-negative")
        if replicas == 0 or len(self.servers) <= 1:
            return []
        targets = []
        seen_physical = {owner.physical_name}
        current = owner
        for _ in range(len(self.servers) - 1):
            current = self.server_after(current)
            if current.physical_name in seen_physical:
                continue
            targets.append(current)
            seen_physical.add(current.physical_name)
            if len(targets) == replicas:
                break
        return targets
    def replication_arrows(self, owner, replicas=2):
        arrows = VGroup()
        for target in self.replication_targets(owner, replicas):
            arrows.add(ReplicationArrow(owner, target))
        return arrows
    # ==========================
    # Ownership Region
    # ==========================
    def redraw_regions(self):
        return self.build_ownership()
    # ==========================
    # Scene Helpers
    # ==========================
    def initialize_scene(self, scene):
        scene.play(Create(self.ring.circle), run_time=2)
        scene.play(FadeIn(self.ring.labels), FadeIn(self.ring.title))
    def display(self, scene):
        self.show_servers(scene)
        self.show_keys(scene)
        self.assign_keys()
        self.show_arrows(scene)
    # ==========================
    # Utility
    # ==========================
    def server_names(self):
        return [server.name for server in self.servers]
    def key_names(self):
        return [key.name for key in self.keys]
    def print_assignments(self):
        for key in self.keys:
            owner = self.owner(key)
            print(key.name, "->", owner.physical_name)
