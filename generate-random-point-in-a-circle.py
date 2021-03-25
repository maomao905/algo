"""
- first approach
it seems two below elements determines the point
angle random(0 - 2π)
distance random(0 - radius)

the problem of this approach is further the distance away, more points are placed
thus, it does not uniformly generate points

- second approach
assuming radius is d
Area A of circle within radius d is
A = π (d^2)

area between circle with radius 2d and d is
π (2d^2) - π (d^2) = 3π (d^2) = 3A

area between circle with radius 2d and 3d is
π (3d^2) - π (2d^2) = 5π (d^2) = 5A

area between circle with radius 3d and 4d is
π (4d^2) - π (3d^2) = 7π (d^2) = 7A

area between circle with radius 8d and 9d is
π (9d^2) - π (8d^2) = 17π (d^2) = 17A

area is linealy increasing as distance increases

https://meyavuz.wordpress.com/2018/11/15/generate-uniform-random-points-within-a-circle/
------------------------------
x^2 + y^2 <= r^2
x^2 + y^2 = random(0, 1) * r^2

r^2 = random(0, 1) * r^2
r = sqrt(random(0,1)) * r

x = r * cos(theta)
x = sqrt(random) * r * cos(theta)

y = r * sin(theta)
y = sqrt(random) * r * sin(theta)
"""
import random, math

class Solution:

    def __init__(self, radius: float, x_center: float, y_center: float):
        self.r = radius
        self.x = x_center
        self.y = y_center

    def randPoint(self) -> List[float]:
        r = math.sqrt(random.uniform(0, 1)) * self.r
        radian = random.uniform(0, 2 * math.pi)
        x = self.x + r * math.cos(radian)
        y = self.y + r * math.sin(radian)
        return [x, y]


# Your Solution object will be instantiated and called as such:
# obj = Solution(radius, x_center, y_center)
# param_1 = obj.randPoint()
