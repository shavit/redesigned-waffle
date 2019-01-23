import math
from vector.vector import Vector

class Ray(object):

    def __init__(self, vector_a, vector_b):
        self.__a = vector_a
        self.__b = vector_b

    def origin(self):
        return self.__a

    def direction(self):
        return self.__b

    def point_at_parameter(self, t):
        return self.__a.plus(self.__a, self.__b.multif(t))

    def color_environment(self):
        unitDirection = self.direction().unitVector()
        t = 0.5 * (unitDirection.y() + 1.0)
        vec1 = Vector(1, 1, 1).multif(1-t)
        vec2 = Vector(0.5, 0.7, 1).multif(t)

        return vec1.plus(vec1, vec2)

    def hit_sphere(self, vec_center, radius):
        oc = self.__a.minus(self.__a, vec_center)
        a = self.__a.dot(self.__b, self.__b)
        b = 2.0 * self.__a.dot(oc, self.__b)
        c = self.__a.dot(oc, oc) - radius * radius
        discriminet = b * b - 4.0 * a * c

        if (discriminet < 0):
            return -1.0
        else:
            return (-b - math.sqrt(discriminet)) / (2.0 * a)

    #
    #   Color a Sphere
    #
    # Ro - RO Ray Origin
    # Rd - Ray Direction
    # t - Time
    # P - Point on the ray
    #
    # t1 - Intersection point 1
    # t2 - Intersection point 2
    # oc - Center of the sphere
    # ot - The closest point to the center of the sphere
    #
    # Each point on the ray can be represented by the ray origin, plus the
    #   ray direction over time.
    # P = Ro + (Rd * t)
    #
    def color_one_sphere(self):
        t = self.hit_sphere(Vector(0, 0, -1.0), 0.5)
        if (t > 0):
            point = self.point_at_parameter(t)
            p = point.minus(point, Vector(0, 0, -1.0))
            # n = self.direction().div(p)
            n = p
            x = (n.x() + 1.5)
            y = (n.y() + 1.5)
            z = (n.z() + 1.5)
            return Vector(x, y, z)

        unitDirection = self.direction().unitVector()
        t = 0.5 * (unitDirection.y() + 1.0)
        vec1 = Vector(1.0, 1.0, 1.0).multif(1.0-t)
        vec2 = Vector(0.5, 0.7, 1).multif(t)

        return vec1.plus(vec1, vec2)

    def write(self, name, data):
        with open('out/{}'.format(name), 'w') as f:
            f.write(data)

    def draw(self):
        u = 600
        v = 400
        origin = Vector(0, 0, 0)
        lowerLeft = Vector(-2, -1, -1)
        data = 'P3\n{} {}\n{}\n'.format(u, v, 255)

        for j in range(v, 0, -1):
            for i in range(0, u):
                x = float(i) / u
                y = float(j) / v
                horizontal = self.__a.multif(x)
                vertical = self.__b.multif(y)
                vecDest = lowerLeft.plus(lowerLeft, horizontal)
                vecDest = vecDest.plus(vecDest, vertical)

                r = Ray(origin, vecDest)
                col = r.color_environment()
                r = int(col.r() * 255.99)
                g = int(col.g() * 255.99)
                b = int(col.b() * 255.99)
                data += '{} {} {}\n'.format(r, g, b)

        return data

    def draw_one_sphere(self):
        u = 600
        v = 400
        origin = Vector(0, 0, 0)
        lowerLeft = Vector(-2.0, -1.0, -1.0)
        data = 'P3\n{} {}\n{}\n'.format(u, v, 255)

        for j in range(v, 0, -1):
            for i in range(0, u):
                x = float(i) / u
                y = float(j) / v
                horizontal = self.__a.multif(x)
                vertical = self.__b.multif(y)
                vecDest = lowerLeft.plus(lowerLeft, horizontal)
                vecDest = vecDest.plus(vecDest, vertical)

                r = Ray(origin, vecDest)
                col = r.color_one_sphere()
                r = int(col.r() * 255.99)
                g = int(col.g() * 255.99)
                b = int(col.b() * 255.99)
                data += '{} {} {}\n'.format(r, g, b)

        return data

if __name__ == '__main__':
    vec1 = Vector(3.0, 0, 0)
    vec2 = Vector(0, 6.0, 0)
    r = Ray(vec1, vec2)
    data = r.draw()
    r.write('environment.ppm', data)
