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

    def isDecrease(self, digit:str):
        previous_digit: int = -1
        for c in digit:
            if previous_digit > int(c):
                return False
            previous_digit = int(c)
        return True

    # double digit not part of a larger group of digits
    def isOnlyDouble(self, digit: str):
        previous_digit1: int = -1
        previous_digit2: int = -2
        for c in digit:
            if previous_digit1 == int(c) and previous_digit2 != int(c):
                return True
            previous_digit2 = previous_digit1
            previous_digit1 = int(c)
        return True


password_validator = PasswordValidator(True, False, 6)
print(password_validator.isOnlyDouble("123444"))




