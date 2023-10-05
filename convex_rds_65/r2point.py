from math import sqrt


class R2Point:
    """ Точка (Point) на плоскости (R2) """

    # Конструктор
    def __init__(self, x=None, y=None):
        if x is None:
            x = float(input("x -> "))
        if y is None:
            y = float(input("y -> "))
        self.x, self.y = x, y

    # Площадь треугольника
    @staticmethod
    def area(a, b, c):
        return 0.5 * ((a.x - c.x) * (b.y - c.y) - (a.y - c.y) * (b.x - c.x))

    # Лежат ли точки на одной прямой?
    @staticmethod
    def is_triangle(a, b, c):
        return R2Point.area(a, b, c) != 0.0

    # Расстояние до другой точки
    def dist(self, other):
        return sqrt((other.x - self.x)**2 + (other.y - self.y)**2)

    def dist_centre(self):
        return sqrt(self.x ** 2 + self.y ** 2)

    # Лежит ли точка внутри "стандартного" прямоугольника?
    def is_inside(self, a, b):
        return (((a.x <= self.x and self.x <= b.x) or
                 (a.x >= self.x and self.x >= b.x)) and
                ((a.y <= self.y and self.y <= b.y) or
                 (a.y >= self.y and self.y >= b.y)))

    # Освещено ли из данной точки ребро (a,b)?
    def is_light(self, a, b):
        s = R2Point.area(a, b, self)
        return s < 0.0 or (s == 0.0 and not self.is_inside(a, b))

    # Совпадает ли точка с другой?
    def __eq__(self, other):
        if isinstance(other, type(self)):
            return self.x == other.x and self.y == other.y
        return False

    @staticmethod
    def distance_centre_to_segment(a, b):
        if R2Point.projection(a, b) <= 0:
            # Точка ближе к началу отрезка
            return R2Point.dist_centre(a)
        elif R2Point.projection(a, b) >= 1:
            # Точка ближе к концу отрезка
            return R2Point.dist_centre(b)
        else:
            # Точка ближе к промежуточной точке на отрезке
            projection_point = (a.x + R2Point.projection(a, b) * (b.x - a.x),
                                a.y + R2Point.projection(a, b) * (b.y - a.y))
            return sqrt((projection_point[0]) ** 2 +
                        (projection_point[1]) ** 2)

    @staticmethod
    def projection(a, b):
        return (-a.x * (b.x - a.x) - a.y * (b.y - a.y)) / \
            ((b.x - a.x) ** 2 + (b.y - a.y) ** 2)


if __name__ == "__main__":
    x = R2Point(1.0, 1.0)
    print(type(x), x.__dict__)
    print(x.dist(R2Point(1.0, 0.0)))
    a, b, c = R2Point(0.0, 0.0), R2Point(1.0, 0.0), R2Point(1.0, 1.0)
    print(R2Point.area(a, c, b))
