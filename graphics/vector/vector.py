import math

class Vector(object):

    __x = 0.0
    __y = 0.0
    __z = 0.0

    def __init__(self, x, y, z):
        self.__x = x
        self.__y = y
        self.__z = z

    def x(self):
        return self.__x

    def y(self):
        return self.__y

    def z(self):
        return self.__z

    def r(self):
        return self.__x

    def g(self):
        return self.__y

    def b(self):
        return self.__z

    def length(self):
        return math.sqrt(self.__x * self.__x \
            + self.__y * self.__y \
            + self.__z * self.__z)

    def squaredLength(self):
        return self.__x * self.__x \
            + self.__y * self.__y \
            + self.__z * self.__z

    def dot(self, vec1, vec2):
        return vec1.x() * vec2.x() \
            + vec1.y() * vec2.y() \
            + vec1.z() * vec2.z()

    def cross(self, vec1, vec2):
        x = vec1.y() * vec2.z() - vec1.z() * vec2.y()
        y = vec1.x() * vec2.z() - vec1.z() * vec2.x()
        z = vec1.x() * vec2.y() - vec1.y() * vec2.x()

        return Vector(x, y, z)

    def unitVector(self):
        return self.div(self.length())

    def plus(self, vec1, vec2):
        x = vec1.x() + vec2.x()
        y = vec1.y() + vec2.y()
        z = vec1.z() + vec2.z()

        return Vector(x, y, z)

    def multif(self, nFloat):
        x = self.__x * nFloat
        y = self.__y * nFloat
        z = self.__z * nFloat

        return Vector(x, y, z)

    def div(self, n):
        x = self.__x / n
        y = self.__y / n
        z = self.__z / n

        return Vector(x, y, z)
