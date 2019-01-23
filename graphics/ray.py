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
        return self.__a.plus(self.__b.multif(t))

    def color_environment(self):
        unitDirection = self.direction().unitVector()
        t = 0.5 * (unitDirection.y() + 1.0)
        vec1 = Vector(1, 1, 1).multif(1-t)
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

if __name__ == '__main__':
    vec1 = Vector(3.0, 0, 0)
    vec2 = Vector(0, 6.0, 0)
    r = Ray(vec1, vec2)
    data = r.draw()
    r.write('environment.ppm', data)
