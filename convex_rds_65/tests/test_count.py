from pytest import approx
from math import inf
from r2point import R2Point
from convex import Polygon


class TestPolygon:

    # Инициализация (выполняется для каждого из тестов класса)
    def setup_method(self):
        self.f = Polygon(
            R2Point(
                0.0, 0.0), R2Point(
                1.0, 0.0), R2Point(
                0.0, 1.0))

    def test_amount1(self):
        assert self.f.count() == approx(inf)

    def test_amount2(self):
        assert self.f.add(R2Point(1.0, 1.0)).count() == approx(inf)

    def test_amount3(self):
        assert self.f.add(R2Point(1.0, 1.0)).add(R2Point(0.5, 2)).\
                   count() == approx(inf)

    def test_amount4(self):
        assert self.f.add(R2Point(3.0, 3.0)).add(R2Point(3.0, -3.0)).\
                   add(R2Point(-3.0, 3.0)).add(R2Point(-3.0, -3.0))\
                   .count() == approx(0)

    def test_amount5(self):
        assert self.f.add(R2Point(1.0, 1.0)).add(R2Point(- 1.0, 1.0)).\
                   add(R2Point(1.0, - 1.0)).\
                   add(R2Point(- 1.0, - 1.0)).count() == approx(4)
