from deq import Deq
from r2point import R2Point
from math import sqrt, inf


class Figure:
    """ Абстрактная фигура """

    def perimeter(self):
        return 0.0

    def area(self):
        return 0.0

    def count(self):
        return 0


class Void(Figure):
    """ "Hульугольник" """

    def add(self, p):
        return Point(p)


class Point(Figure):
    """ "Одноугольник" """

    def __init__(self, p):
        self.p = p

    def add(self, q):
        return self if self.p == q else Segment(self.p, q)

    def count(self):
        c = 0
        if R2Point.dist_centre(self.p) <= 1:
            c += 1
        return c


class Segment(Figure):
    """ "Двуугольник" """

    def __init__(self, p, q):
        self.p, self.q = p, q

    def perimeter(self):
        return 2.0 * self.p.dist(self.q)

    def add(self, r):
        if R2Point.is_triangle(self.p, self.q, r):
            return Polygon(self.p, self.q, r)
        elif self.q.is_inside(self.p, r):
            return Segment(self.p, r)
        elif self.p.is_inside(r, self.q):
            return Segment(r, self.q)
        else:
            return self

    def count(self):
        c = 0
        if R2Point.distance_centre_to_segment(self.p, self.q) == 1:
            c += 1
        elif R2Point.distance_centre_to_segment(self.p, self.q) <= 1:
            c = inf
        return c


class Polygon(Figure):
    """ Многоугольник """

    def __init__(self, a, b, c):
        self.points = Deq()
        self.points.push_first(b)
        if b.is_light(a, c):
            self.points.push_first(a)
            self.points.push_last(c)
        else:
            self.points.push_last(a)
            self.points.push_first(c)
        self._perimeter = a.dist(b) + b.dist(c) + c.dist(a)
        self._area = abs(R2Point.area(a, b, c))
        self._count = Polygon.count3(self)

    def perimeter(self):
        return self._perimeter

    def area(self):
        return self._area

    def count(self):
        return self._count

    def count3(self):
        c = 0
        for i in range(0, 3):
            if i == 2:
                h = 0
                k = 1
            elif i == 1:
                h = i + 1
                k = 0
            else:
                h = i + 1
                k = i + 2
            if R2Point.distance_centre_to_segment(self.points.array[i],
                                                  self.points.array[h]) < 1:
                c = inf
            elif R2Point.distance_centre_to_segment(self.points.array[i],
                                                    self.points.array[h]) == 1:
                c += 1
                if (R2Point.projection(self.points.array[i],
                                       self.points.array[h]) >= 1 and
                    R2Point.projection(
                                        self.points.array[h],
                                        self.points.array[k]) <= 0):
                    c -= 1
        return c

    # добавление новой точки
    def add(self, t):

        # поиск освещённого ребра
        for n in range(self.points.size()):
            if t.is_light(self.points.last(), self.points.first()):
                break
            self.points.push_last(self.points.pop_first())

        # хотя бы одно освещённое ребро есть
        if t.is_light(self.points.last(), self.points.first()):

            # учёт удаления ребра, соединяющего конец и начало дека
            self._perimeter -= self.points.first().dist(self.points.last())
            self._area += abs(R2Point.area(t,
                                           self.points.last(),
                                           self.points.first()))

            # удаление освещённых рёбер из начала дека
            p = self.points.pop_first()
            while t.is_light(p, self.points.first()):
                self._perimeter -= p.dist(self.points.first())
                self._area += abs(R2Point.area(t, p, self.points.first()))
                p = self.points.pop_first()
            self.points.push_first(p)

            # удаление освещённых рёбер из конца дека
            p = self.points.pop_last()
            while t.is_light(self.points.last(), p):
                self._perimeter -= p.dist(self.points.last())
                self._area += abs(R2Point.area(t, p, self.points.last()))
                p = self.points.pop_last()
            self.points.push_last(p)

            # добавление двух новых рёбер
            self._perimeter += t.dist(self.points.first()) + \
                t.dist(self.points.last())
            self.points.push_first(t)

            c = 0
            for i in range(self.points.size()):
                if i + 1 > self.points.size() - 1:
                    k = 1
                    h = 0
                elif i + 1 > self.points.size():
                    k = 0
                    h = i + 1
                else:
                    k = i + 2
                    h = i + 1
                if R2Point.distance_centre_to_segment(self.points.array[i],
                                                      self.points.array[h])\
                        < 1:
                    c = inf
                elif R2Point.distance_centre_to_segment(self.points.array[i],
                                                        self.points.array[h]) \
                        == 1:
                    if (R2Point.projection(self.points.array[i],
                                           self.points.array[h]) >= 1 and
                            R2Point.projection(self.points.array[h],
                                               self.points.array[k]) <= 0):
                        c -= 1
                    c += 1
                self._count = c
        return self


if __name__ == "__main__":
    f = Void()
    print(type(f), f.__dict__)
    f = f.add(R2Point(0.0, 0.0))
    print(type(f), f.__dict__)
    f = f.add(R2Point(1.0, 0.0))
    print(type(f), f.__dict__)
    f = f.add(R2Point(0.0, 1.0))
    print(type(f), f.__dict__)
