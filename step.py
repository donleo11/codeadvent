from constants import Constants


class Step:

    def __init__(self, direction: str, length: int):
        self.direction: str = direction
        self.length: int = length

    def __repr__(self):
        return self.direction + str(self.length)

    def getoperator(self):
        if self.direction == Constants.right or self.direction == Constants.down:
            return 0 - self.length
        else:
            return self.length

