from constants import Constants
from day3.mypoint import MyPoint


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


