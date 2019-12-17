class Step:

    def __init__(self, direction: str, length: int):
        self.direction: str = direction
        self.length: int = length

    def __repr__(self):
        return self.direction + str(self.length)