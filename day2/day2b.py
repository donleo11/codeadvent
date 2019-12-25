import intcode_utils
import read_utils

from constants import Constants

from intcode import Intcode

# get content
content = read_utils.getinput("day2.txt")[0]

stringcontent = str(content)
stringlist = stringcontent.split(",")
intlist = read_utils.converttoint(stringlist)
intlist1 = intlist.copy()

noun = 12
verb = 2
intcode_utils.set_noun(intlist1, noun)
intcode_utils.set_verb(intlist1, verb)

intcode_utils.calculate_intcode(intlist1)
print("Question 2A: the computed address is: ", intlist1[0])

# second part of the question
target: int = 19690720
intlist2 = intlist.copy()
output = intcode_utils.find_output(intlist2, target)
print("Question 2B: the computed noun is: ", output[0])
print("Question 2B: the computed verb is: ", output[1])
