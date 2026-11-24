from manim import (
    BLUE,
    DOWN,
    GRAY,
    GREEN,
    LEFT,
    ORANGE,
    RIGHT,
    RED,
    Square,
    Text,
    UP,
    YELLOW,
    Dot,
    Line,
    VGroup,
)


POINTS = [
    (-3.5, 1.4), (-2.8, 0.4), (-3.7, -0.5), (-2.5, -1.2),
    (2.6, 1.5), (3.5, 0.7), (2.8, -0.2), (3.7, -1.0),
]
GROUP_A = list(range(4))
GROUP_B = list(range(4, 8))
EDGES = [
    (0, 1), (0, 2), (1, 2), (1, 3), (2, 3),
    (4, 5), (4, 6), (5, 6), (5, 7), (6, 7),
    (1, 4),
]
COLORS = [BLUE, BLUE, BLUE, BLUE, ORANGE, ORANGE, ORANGE, ORANGE]


def create_title(text):
    title = Text(text, font_size=44, weight="BOLD")
    title.to_edge(UP)
    return title


def create_data_graph(show_edges=True):
    nodes = VGroup()
    labels = VGroup()
    for index, (x, y) in enumerate(POINTS):
        node = Dot((x, y, 0), radius=0.16, color=COLORS[index])
        nodes.add(node)
        label = Text(str(index + 1), font_size=18)
        label.next_to(node, DOWN, buff=0.08)
        labels.add(label)

    edges = VGroup()
    if show_edges:
        for start, end in EDGES:
            edges.add(
                Line(
                    nodes[start].get_center(),
                    nodes[end].get_center(),
                    color=GRAY,
                    stroke_width=2,
                )
            )
    return edges, nodes, labels


def create_cluster_legend():
    legend = VGroup(
        VGroup(Dot(radius=0.1, color=BLUE), Text("Cluster 1", font_size=20)).arrange(RIGHT, buff=0.12),
        VGroup(Dot(radius=0.1, color=ORANGE), Text("Cluster 2", font_size=20)).arrange(RIGHT, buff=0.12),
    )
    legend.arrange(DOWN, aligned_edge=LEFT, buff=0.15)
    return legend


def create_matrix(values, cell_size=0.42, font_size=16):
    matrix = VGroup()
    for row_index, row in enumerate(values):
        for column_index, value in enumerate(row):
            cell = Square(side_length=cell_size, stroke_width=1, color=GRAY)
            cell.move_to(
                (column_index - (len(row) - 1) / 2) * cell_size * RIGHT
                + (row_index - (len(values) - 1) / 2) * cell_size * DOWN
            )
            text = Text(str(value), font_size=font_size)
            text.move_to(cell)
            matrix.add(VGroup(cell, text))
    return matrix
