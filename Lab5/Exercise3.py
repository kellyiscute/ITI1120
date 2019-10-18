import math


def deg_rad(deg):
    return math.pi/180*deg


def calc_distance(v):
    result = []
    for i in range(0, 90, 10):
        theta = deg_rad(i)
        result.append((2 * v ** 2 * math.cos(theta) * math.sin(theta)) / 9.8)
    return result


v = float(input('velocity = '))
distances = calc_distance(v)
for d in range(distances.__len__()):
    print(f'For the angle {(d+1)*10} degrees, the ball travels parcount {distances[d]} meters')
