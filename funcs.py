import math

DISTANCE_THRESHOLD = 50


def reduceContours(rects):
    return rects
    res = []
    targets = []

    for r in rects:
        targets.append(Target(r[0], r[1], r[2], r[3]))

    # first remove all the boxes inside other boxes
    for i in range(len(targets)):
        for j in range(i + 1, len(targets) - 1):

            if i >= len(targets) or j >= len(targets):
                break

            if (check_collision(targets[i], targets[j])):
                targets[i].Combine(targets[j])
                targets.remove(targets[j])

    return targets


def check_collision(t1, t2):
    # If any of the sides from A are outside of B
    if (t1.y + t1.h <= t2.y):
        return False
    if (t1.y >= t2.y + t2.h):
        return False
    if (t1.x + t1.w <= t2.x):
        return False
    if (t1.x >= t2.x + t2.w):
        return False
    # If none of the sides from A are outside B
    return True


class Target:
    __slots__ = ["x", "y", "w", "h"]

    def __init__(self, _x, _y, _w, _h):
        self.x = _x
        self.y = _y
        self.w = _w
        self.h = _h

    def Combine(self, other):
        self.ExtendTarget(other.x, other.y)
        self.ExtendTarget(other.x + other.w, other.y + other.h)

    def ExtendTarget(self, x, y):
        if (self.x > x):
            self.x = x
        if (self.x + self.w < x):
            self.w = x - self.x
        if (self.y > y):
            self.y = y
        if (self.y + self.h < y):
            self.h = y - self.y

    def GetMiddle(self):
        X = self.x + self.w / 2
        Y = self.y + self.h / 2
        return (X, Y)

    def Distance(self, other):
        p1 = self.GetMiddle()
        p2 = other.GetMiddle()
        return dist(p1, p2)


def dist(x1, y1, x2, y2):
    return math.sqrt(((x1 - x2) ** 2) + ((y1 - y2) ** 2))


def dist(p1, p2):
    return math.sqrt(((p1[0] - p2[0]) ** 2) + ((p1[1] - p2[1]) ** 2))


if __name__ == "__main__":
    test = [
        (10, 10, 10, 10),
        (10, 10, 10, 10),
        (10, 30, 10, 10),
        (10, 10, 30, 10),
        (10, 20, 10, 10),
        (50, 10, 10, 10),
        (10, 10, 10, 60),
    ]
    print(len(test))
    a = reduceContours(test)

    for x in a:
        print(x)

    print(len(test))