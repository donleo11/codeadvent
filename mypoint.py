class MyPoint:
    def __init__(self, x, y, direction, value):
        self.x: int = x
        self.y: int = y
        self.direction: str = direction
        self.value: int = value

    def __repr__(self):
        return "hello"

    def next_point(self):
        nextx = 0
        nexty = 0
        if self.direction == "R":
            nextx = self.x + self.value
            nexty = self.y
        elif self.direction == "L":
            nextx = self.x - self.value
            nexty = self.y
        elif self.direction == "U":
            nexty = self.y + self.value
            nextx = self.x
        elif self.direction == "D":
            nexty = self.y - self.value
            nextx = self.x
        return [nextx, nexty]

    def in_range(self, point):
        if self.next_point()[0] == point[0]:
            return self.next_point()[1] < point[1] < self.y or self.y < point[1] < self.next_point()[1]
        elif self.next_point()[1] == point[1]:
            return self.next_point()[0] < point[0] < self.y or self.y < point[0] < self.next_point()[0]
        return False