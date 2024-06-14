from collections import namedtuple

import math


Point = namedtuple('Point', 'x y')


def euclidean_distance_squared(p1, p2):
    return (p1.x - p2.x) ** 2 + (p1.y - p2.y) ** 2


def closest_pair_of_points(points):
    def closest_pair_recursive(px, py):
        n = len(px)
        if n <= 3:
            return min(euclidean_distance_squared(px[i], px[j]) for i in range(n) for j in range(i + 1, n))

        mid = n // 2
        mid_x = px[mid].x
        pyl = [p for p in py if p.x <= mid_x]
        pyr = [p for p in py if p.x > mid_x]

        dl = closest_pair_recursive(px[:mid], pyl)
        dr = closest_pair_recursive(px[mid:], pyr)
        d = min(dl, dr)

        strip = [p for p in py if abs(p.x - mid_x) < d]

        strip_len = len(strip)
        for i in range(strip_len):
            for j in range(i + 1, min(i + 7, strip_len)):
                d = min(d, euclidean_distance_squared(strip[i], strip[j]))

        return d

    px = sorted(points, key=lambda p: p.x)
    py = sorted(points, key=lambda p: p.y)

    return math.sqrt(closest_pair_recursive(px, py))


if __name__ == '__main__':
    input_n = int(input())
    input_points = []
    for _ in range(input_n):
        x, y = map(int, input().split())
        input_point = Point(x, y)
        input_points.append(input_point)

    print("{0:.9f}".format(closest_pair_of_points(input_points)))