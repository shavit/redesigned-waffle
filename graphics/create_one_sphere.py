from vector.vector import Vector
from ray import Ray

if __name__ == '__main__':
    vec1 = Vector(4.0, 0, 0)
    vec2 = Vector(0, 2.0, 0)
    r = Ray(vec1, vec2)
    data = r.draw_one_sphere()
    r.write('one_sphere.ppm', data)
