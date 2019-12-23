class PasswordValidator:
    nodoubles: bool = True
    decrease: bool = False
    length: int = 0

    def __init__(self, nodoubles: bool, decrease: bool, length: int):
        self.nodoubles: bool = nodoubles
        self.decrease: bool = decrease
        self.length: int = length

    # def validate_nodoubles(self, digit: str):
    #     for c in digit:

    def validateLength(self, digit: str):
        return self.length == len(digit)

    def isDouble(self, digit: str):
        previous_digit: int = -1
        for c in digit:
            if previous_digit == int(c):
                return True
            previous_digit = int(c)
        return False

    def isDecrease(self, digit:str):
        previous_digit: int = -1
        for c in digit:
            if previous_digit > int(c):
                return False
            previous_digit = int(c)
        return True
