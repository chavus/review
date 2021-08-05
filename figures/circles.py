PI = 3.1416


class Dimension:

    def __init__(self, radious):
        self.radious = radious

    def area(self):
        return PI*self.radious**2

    def diameter(self):
        return self.radious*2