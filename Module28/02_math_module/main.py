import math

class MyMath:
    @classmethod
    def circle_len(cls, radius):
        return 2 * radius * math.pi

    @classmethod
    def circle_sq(cls, radius):
        return radius ** 2 * math.pi

    @classmethod
    def cube_vol(cls, edge):
        return (2 * edge) ** 3

    @classmethod
    def sphere_sq(cls, radius):
        return radius ** 2 * math.pi * 4

res_1 = MyMath.circle_len(radius=5)
res_2 = MyMath.circle_sq(radius=6)
print(res_1)
print(res_2)