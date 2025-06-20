def solution(x0, y0, points):
    points.sort(
        key = lambda x:[(x0 - x[0]) ** 2 + (y0 - x[1]) ** 2, x[0], x[1]]
    )
    return points