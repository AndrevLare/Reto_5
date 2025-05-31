from math import acos, pi


class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def compute_distance(self, point: "Point") -> float:
        return ((self.x - point.x) ** 2 + (self.y - point.y) ** 2) ** 0.5

    def __str__(self):
        return f"({self.x}, {self.y})"


class Line:
    def __init__(self, start: "Point", end: "Point"):
        self.start = start
        self.end = end
        self.__length = ((end.x - start.x) ** 2 + (end.y - start.y) ** 2) ** 0.5
        self.__slope = (
            (end.y - start.y) / (end.x - start.x)
            if (end.x - start.x) != 0
            else "indefinida"
        )

    def compute_length(self):
        return self.__length

    def __str__(self):
        return (
            f"Line from {self.start} to {self.end}, "
            f"length: {self.__length}, slope: {self.__slope}"
        )


class Shape:
    def __init__(self, is_regular: bool, vertices: list["Point"], edges: list["Line"]):
        self._is_regular = is_regular
        self._edges = edges
        self._vertices = vertices
        self._inner_angles = self.compute_inner_angles()
        self._perimeter = self.compute_perimeter()
        self._area = self.compute_area()

    def get_edges(self):
        return self._edges

    def get_vertices(self):
        return self._vertices

    def get_is_regular(self):
        return self._is_regular

    def get_inner_angles(self):
        return self._inner_angles

    def get_perimeter(self):
        return self._perimeter

    def get_area(self):
        return self._area

    def set_edges(self, edges: list["Line"]):
        self._edges = edges

    def set_vertices(self, vertices: list["Point"]):
        self._vertices = vertices

    def set_is_regular(self, is_regular: bool):
        self._is_regular = is_regular

    def set_inner_angles(self, inner_angles: list[float]):
        self._inner_angles = inner_angles

    def compute_perimeter(self):
        return sum(edge.compute_length() for edge in self._edges)

    def compute_area(self):
        pass

    def compute_inner_angles(self):
        pass

    def __str__(self):
        return (
            f"Vertices: {self._vertices},\n"
            f"Edges: {self._edges},\n"
            f"Is regular: {self._is_regular},\n"
            f"Inner angles: {self._inner_angles},\n"
            f"Perimeter: {self._perimeter},\n"
            f"Area: {self._area}"
        )


class Rectangle(Shape):
    def __init__(
        self, vertices: list["Point"], edges: list["Line"], is_regular=False
    ):
        super().__init__(is_regular, vertices, edges)

    def compute_inner_angles(self):
        return [90, 90, 90, 90]

    def compute_area(self):
        return self._edges[0].compute_length() * self._edges[1].compute_length()


class Square(Rectangle):
    def __init__(self, vertices, edges):
        super().__init__(vertices, edges, True)


class Triangle(Shape):
    def __init__(self, is_regular, vertices, edges: list["Line"]):
        super().__init__(is_regular, vertices, edges)

    def compute_inner_angles(self):
        a = self._edges[0].compute_length()
        b = self._edges[1].compute_length()
        c = self._edges[2].compute_length()
        alpha = (
            acos((b ** 2 + c ** 2 - a ** 2) / (2 * b * c)) * (180 / pi)
        )
        beta = (
            acos((c ** 2 + a ** 2 - b ** 2) / (2 * c * a)) * (180 / pi)
        )
        gamma = (
            acos((a ** 2 + b ** 2 - c ** 2) / (2 * a * b)) * (180 / pi)
        )
        return [alpha, beta, gamma]

    def compute_area(self) -> float:
        a = self._edges[0].compute_length()
        b = self._edges[1].compute_length()
        c = self._edges[2].compute_length()
        s = (a + b + c) / 2
        area = (s * (s - a) * (s - b) * (s - c)) ** 0.5
        return area


class Equilateral(Triangle):
    def __init__(self, vertices, edge):
        super().__init__(True, vertices, [edge] * 3)


class Isosceles(Triangle):
    def __init__(self, vertices, edge):
        super().__init__(
            False, vertices, [edge] * 2 + [Line(vertices[0], vertices[2])]
        )


class Scalene(Triangle):
    def __init__(self, vertices, edges):
        super().__init__(False, vertices, edges)


class TriRectangle(Triangle):
    def __init__(self, vertices, edges):
        super().__init__(False, vertices, edges)


if __name__ == "__main__":
    print("Shapes module loaded successfully. try importing it in your code.")