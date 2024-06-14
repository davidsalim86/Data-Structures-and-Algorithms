from sys import stdin
from collections import namedtuple

Segment = namedtuple('Segment', 'start end')

def optimal_points(segments):
    points = []
    segments.sort(key=lambda x: x.end)  # Sort segments by end point
    current_point = segments[0].end  # Start with the end point of the first segment
    
    for s in segments[1:]:
        if current_point < s.start:
            points.append(current_point)  # Add current point
            current_point = s.end  # Update current point
    
    points.append(current_point)  # Add the last point
    
    return points

if __name__ == '__main__':
    input_data = stdin.read()
    n, *data = map(int, input_data.split())
    segments = [Segment(data[i], data[i + 1]) for i in range(0, len(data), 2)]
    points = optimal_points(segments)
    print(len(points))
    print(*points)