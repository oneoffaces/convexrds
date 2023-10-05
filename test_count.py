from pytest import approx
from math import inf
from r2point import R2Point
from convex import Point


class TestCount:

    # Инициализация (выполняется для каждого из тестов класса)
    def setup_method(self):
        self.f = Point(
            R2Point(0.0, 3.0))

    # Точка 0
    def test_amount1(self):
        assert self.f.count() == approx(0)

    # Отрезок 0
    def test_amount2(self):
        assert self.f.add(R2Point(0.0, 2.0)).count() == approx(0)

    # Отрезок 1
    def test_amount3(self):
        assert self.f.add(R2Point(0.0, 1.0)).\
                   count() == approx(1)

    # Треугольник ноль
    def test_amount4(self):
        assert self.f.add(R2Point(-3.0, 3.0)).add(R2Point(-3.0, -3.0))\
                   .count() == approx(0)

    # Треугольник касание
    def test_amount5(self):
        assert self.f.add(R2Point(0.0, 1.0)).add(R2Point(1.0, 1.0))\
                   .count() == approx(1)

    # Треугольник касание 2
    def test_amount6(self):
        assert self.f.add(R2Point(-5.0, -1.0)).add(R2Point(5.0, -1.0))\
                   .count() == approx(1)

    # Треугольник inf
    def test_amount7(self):
        assert self.f.add(R2Point(0.0, 0.0)).add(R2Point(1.0, 1.0))\
                   .count() == approx(inf)

    # Многоугольник 0
    def test_amount8(self):
        assert self.f.add(R2Point(3.0, 3.0)).add(R2Point(3.0, -3.0)).\
                   add(R2Point(-3.0, 3.0)).add(R2Point(-3.0, -3.0))\
                   .count() == approx(0)

    # Многоугольник не ноль и не inf
    def test_amount9(self):
        assert self.f.add(R2Point(1.0, 1.0)).add(R2Point(- 1.0, 1.0)).\
                   add(R2Point(1.0, - 1.0)).\
                   add(R2Point(- 1.0, - 1.0)).count() == approx(3)

    # Многоугольник inf
    def test_amount10(self):
        assert self.f.add(R2Point(0.0, 0.0)).add(R2Point(- 1.0, 0.0)).\
                   add(R2Point(1.0, - 1.0)).\
                   add(R2Point(- 1.0, - 1.0)).count() == approx(inf)

    # Касание в многоугольнике
    def test_amount11(self):
        assert self.f.add(R2Point(0.0, 1.0)).add(R2Point(- 1.0, 1.0)).\
                   add(R2Point(- 1.0, 3.0)).count() == approx(1)
