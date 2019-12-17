from constants import Constants
from mypoint import MyPoint


class Segment:
    def __init__(self, direction: str, length: int, firstpoint: MyPoint):
        self.direction: str = direction
        self.length: int = length
        self.firstpoint: MyPoint = firstpoint

    def getfirstpoint(self):
        return self.firstpoint

    def getsecondpoint(self):
        if self.direction == Constants.left or self.direction == Constants.right:
            return MyPoint(self.firstpoint.x + self.getoperator(), self.firstpoint.y)
        else:
            return MyPoint(self.firstpoint.x, self.firstpoint.y + self.getoperator())

    def getoperator(self):
        if self.direction == Constants.left or self.direction == Constants.down:
            return 0 - self.length
        else:
            return self.length

    def ishorizontal(self):
        return self.direction == Constants.right or self.direction == Constants.left

    def isvertical(self):
        return self.direction == Constants.up or self.direction == Constants.down

    def inxrange(self, segment):
        if self.direction == Constants.right:
            return self.firstpoint.x < segment.firstpoint.x < self.getsecondpoint().x
        elif self.direction == Constants.left:
            return self.getsecondpoint().x < segment.firstpoint.x < self.firstpoint.x
        return False

    def inyrange(self, segment):
        if self.direction == Constants.up:
            return self.firstpoint.y < segment.firstpoint.y < self.getsecondpoint().y
        elif self.direction == Constants.down:
            return self.getsecondpoint().y < segment.firstpoint.y < self.firstpoint.y
        return False


