import math

def dist(p1, p2):
    return math.sqrt( (p1[0] - p2[0])**2 + (p1[1] - p2[1])**2 )

# Задача-1: Написать класс для фигуры-треугольника, заданного координатами трех точек.
# Определить методы, позволяющие вычислить: площадь, высоту и периметр фигуры.

print('=== 1 ===')

class Triangle:
    def set(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def area(self):
        return 0.5 * dist(self.b, self.c) * self.height()

    def perimeter(self):
        return dist(self.a, self.b) + dist(self.a, self.c) + dist(self.b, self.c)

    def height(self):
        p = self.perimeter() / 2
        dist_ab = dist(self.a, self.b)
        dist_ac = dist(self.a, self.c)
        dist_bc = dist(self.b, self.c)
        return 2 / dist_bc * math.sqrt(p * (p - dist_bc) * (p - dist_ac) * (p - dist_ab))


triangle = Triangle()
triangle.set((10, 20), (15, 50), (20, 30))

print('Area      = {}'.format(triangle.area()))
print('Perimeter = {}'.format(triangle.perimeter()))
print('Height    = {}'.format(triangle.height()))

# Задача-2: Написать Класс "Равнобочная трапеция", заданной координатами 4-х точек.
# Предусмотреть в классе методы:
# проверка, является ли фигура равнобочной трапецией;
# вычисления: длины сторон, периметр, площадь.

print('\n=== 2 ===')

def check_parallel(a1, a2, b1, b2):
    if a1[1] == a2[1]: return b1[1] == b2[1]
    if b1[1] == b2[1]: return False
    return (a1[0] - a2[0]) / (a1[1] - a2[1]) == \
           (b1[0] - b2[0]) / (b1[1] - b2[1])


def ccw(a, b, c):
    return (c[1]-a[1]) * (b[0]-a[0]) > (b[1]-a[1]) * (c[0]-a[0])

def check_intersect(a,b,c,d):
    return ccw(a,c,d) != ccw(b,c,d) and ccw(a,b,c) != ccw(a,b,d)


class Trapezoid:
    def set(self, a, b, c, d):
        self.points = (a, b, c, d)

    def check(self):
        nb0, nb1, nb2, nb3 = self.__find_not_bases()
        if nb0 is None:
            return False
        return dist(nb0, nb1) == dist(nb2, nb3)

    def lens(self):
        base0, base1, base2, base3 = self.__find_bases()
        if base0 is None:
            raise Exception()
        nb0, nb1, nb2, nb3 = self.__find_not_bases()
        return dist(base0, base1), dist(base2, base3), dist(nb0, nb1), dist(nb2, nb3)

    def perimeter(self):
        d0, d1, d2, d3 = self.lens()
        return d0 + d1 + d2 + d3

    def area(self):
        base0, base1, base2, base3 = self.__find_bases()
        if base0 is None:
            raise Exception()
        triangle1 = Triangle()
        triangle2 = Triangle()
        triangle1.set(base0, base1, base2)
        triangle2.set(base2, base3, base1)
        return triangle1.area() + triangle2.area()

    def __find_bases(self):
        for i1 in range(3):
            for i2 in range(i1 + 1, 4):
                for j1 in range(3):
                    for j2 in range(j1 + 1, 4):
                        if i1 == j1 or i1 == j2 or i2 == j1 or i2 == j2:
                            continue
                        if check_parallel(self.points[i1], self.points[i2], self.points[j1], self.points[j2]):
                            return self.points[i1], self.points[i2], self.points[j1], self.points[j2]
        return None, None, None, None

    def __find_not_bases(self):
        base0, base1, base2, base3 = self.__find_bases()
        if base0 is None:
            return None, None, None, None
        if check_intersect(base0, base2, base1, base3):
            return base0, base2, base1, base3
        return base0, base3, base1, base2


trapezoid = Trapezoid()
#trapezoid.set((0, 0), (10, 0), (8, 10), (2, 10))
trapezoid.set((0, 0), (10, 10), (5, 10), (0, 5))

try:
    print('Equilateral trapezoid: {}'.format(trapezoid.check()))
    print('Lengths: ', trapezoid.lens())
    print('Perimeter: {}'.format(trapezoid.perimeter()))
    print('Area: {}'.format(trapezoid.area()))
except:
    print("Error: not trapezoid")
