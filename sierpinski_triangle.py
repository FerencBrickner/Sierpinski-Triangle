import matplotlib.pyplot as plt
from random import choice

type Point = tuple[int|float, int|float]

def compute_and_draw_sierpinski_triangle(
    *,
    number_of_points: int = int(4e5),
    color: str = "green",
    marker_size: float = 0.03,
    edges_of_triangle: list[Point] = [A:=(0, 0), B:=(5, 10), C:=(10, 0)],
    seed: Point = (0, 0)
) -> None:
    x_coordinates = list()
    y_coordinates = list()

    random_point: Point = seed

    for _ in range(number_of_points):
        random_edge_of_triangle = choice(edges_of_triangle)

        def compute_halving_point(point_1: Point, point_2: Point) -> Point:
            return ((point_1[0] + point_2[0]) / 2, (point_1[1] + point_2[1]) / 2)

        random_point = compute_halving_point(random_point, random_edge_of_triangle)

        x_coordinates.append(random_point[0])
        y_coordinates.append(random_point[1])
    plt.scatter(x_coordinates, y_coordinates, c=color, s=marker_size)
    plt.show()


def main(*args, **kwargs) -> None:
    """
    Compute and draw Sierpinski triangle.
    https://en.wikipedia.org/wiki/Sierpi%C5%84ski_triangle
    """
    compute_and_draw_sierpinski_triangle()


if __name__ == "__main__":
    main()
