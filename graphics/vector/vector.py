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
        return vec1.x() * float(vec2.x()) \
            + vec1.y() * float(vec2.y()) \
            + vec1.z() * float(vec2.z())

    def cross(self, vec1, vec2):
        x = vec1.y() * vec2.z() - vec1.z() * vec2.y()
        y = vec1.x() * vec2.z() - vec1.z() * vec2.x()
        z = vec1.x() * vec2.y() - vec1.y() * vec2.x()

        return Vector(x, y, z)

    def unitVector(self):
        return self.divf(self.length())

    def plus(self, vec1, vec2):
        x = vec1.x() + float(vec2.x())
        y = vec1.y() + float(vec2.y())
        z = vec1.z() + float(vec2.z())

        return Vector(x, y, z)

    def minus(self, vec1, vec2):
        x = vec1.x() - float(vec2.x())
        y = vec1.y() - float(vec2.y())
        z = vec1.z() - float(vec2.z())

        return Vector(x, y, z)

    def multif(self, nFloat):
        x = self.__x * float(nFloat)
        y = self.__y * float(nFloat)
        z = self.__z * float(nFloat)

        return Vector(x, y, z)

    def divf(self, nFloat):
        n = nFloat if float(nFloat) > 0 else 1
        x = self.__x / n
        y = self.__y / n
        z = self.__z / n

        return Vector(x, y, z)

    def div(self, vec):
        vecx = vec.x() if vec.x() > 0 else 1
        vecy = vec.y() if vec.y() > 0 else 1
        vecz = vec.z() if vec.z() > 0 else 1
        x = self.__x / float(vecx)
        y = self.__y / float(vecy)
        z = self.__z / float(vecz)

        return Vector(x, y, z)
