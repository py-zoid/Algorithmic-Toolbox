# Uses python3
import sys
from collections import namedtuple

Segment = namedtuple('Segment', 'start end')

def optimal_points(segments):
    points = []
    while (len(segments) > 0):
        max_start = 0
        for s in segments:
            if s.start > max_start:
                max_start = s.start
        points.append(max_start)
        for s in segments[:]:
            if s.start <= max_start and s.end >= max_start:
                segments.remove(s)
    return points

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *data = map(int, input.split())
    segments = list(map(lambda x: Segment(x[0], x[1]), zip(data[::2], data[1::2])))
    points = optimal_points(segments)
    print(len(points))
    for p in points:
        print(p, end = ' ')