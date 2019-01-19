class Ray(object):

    __a
    __b

    def ray(self, vector_a, vector_b):
        self.__a = vector_a
        self.__b = vector_b

    def origin(self):
        return self.__a

    def direction(self):
        return self.__b

    def point_at_parameter(self, t):
        return self.__a + t + b
