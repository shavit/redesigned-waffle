
class Gradient(object):

    def write(self, name, data):
        with open('out/{}'.format(name), 'w') as f:
            f.write(data)

    def draw(self):
        u = 600
        v = 400
        data = 'P3\n{} {}\n{}\n'.format(u, v, 255)

        for j in range(v, 0, -1):
            for i in range(0, u):
                red = float(i) / u
                green = float(j) / v
                blue = 1.618034
                r = int(red * 255.99)
                g = int(green * 255.99)
                b = int(blue * 255.99)
                data += '{} {} {}\n'.format(r, g, b)

        return data


if __name__ == '__main__':
    g = Gradient()
    data = g.draw()
    g.write('gradient.ppm', data)
