class PasswordValidator:
    nodoubles: bool = True
    decrease: bool = False
    length: int = 0

    def __init__(self, nodoubles: bool, decrease: bool, length: int):
        self.nodoubles: bool = nodoubles
        self.decrease: bool = decrease
        self.length: int = length

    def validateLength(self, digit: str):
        return self.length == len(digit)

    def isDouble(self, digit: str):
        previous_digit: int = -1
        for c in digit:
            if previous_digit == int(c):
                return True
            previous_digit = int(c)
        return False

    def isDecrease(self, digit: str):
        previous_digit: int = -1
        for c in digit:
            if previous_digit > int(c):
                return False
            previous_digit = int(c)
        return True

    # double digit not part of a larger group of digits
    def isOnlyDouble(self, digit: str):
        previous_digit: int = -1
        for c in digit:
            if previous_digit == int(c) and not self.ingroup(digit, int(c)):
                return True
            previous_digit = int(c)
        return False

    def ingroup(self, digit: str, number: int):
        for i in range(1, len(digit) - 1):
            if int(digit[i]) == number and int(digit[i - 1]) == number and int(digit[i + 1]) == number:
                return True
        return False