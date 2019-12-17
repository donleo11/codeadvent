class MyPoint:
    def __init__(self, x: int, y: int):
        self.x: int = x
        self.y: int = y

    def __repr__(self):
        return "x: " + str(self.x) + "| y: " + str(self.y)

    def in_range(self, point):
        if self.next_point()[0] == point[0]:
            return self.next_point()[1] < point[1] < self.y or self.y < point[1] < self.next_point()[1]
        elif self.next_point()[1] == point[1]:
            return self.next_point()[0] < point[0] < self.y or self.y < point[0] < self.next_point()[0]
        return False