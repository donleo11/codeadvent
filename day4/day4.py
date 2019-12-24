import read_utils

# It is a six-digit number.
# The value is within the range given in your puzzle input.
# Two adjacent digits are the same (like 22 in 122345).
# Going from left to right, the digits never decrease; they only ever increase or stay the same (like 111123 or 135679).

# get puzzle input
from day4.password_validator import PasswordValidator

puzzle_input = read_utils.getinput('day4.txt')[0]
ranges = str(puzzle_input).strip().split("-")
low_range: int = int(ranges[0])
high_range: int = int(ranges[1])

# create validator
password_validator = PasswordValidator(True, False, 6)

# count the amount of numbers within the range that meets the criteria
count = 0
for i in range(low_range+1, high_range-1):
    digit_str: str = str(i)
    valid = password_validator.validateLength(digit_str) & password_validator.isDouble(digit_str) \
            & password_validator.isDecrease(digit_str)
    if valid:
        count = count + 1
        print("Valid password: ", i)

print("Total number of possible passwords: ", count)

