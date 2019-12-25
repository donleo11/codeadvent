import read_utils
from day3 import segment_utils
import random

from intcode import Intcode


def set_noun(intlist, noun):
    intlist[1] = noun


def set_verb(initlist, verb):
    initlist[2] = verb


def intcode_calculations(intlist, noun, verb):
    set_noun(intlist, noun)
    set_verb(intlist, verb)
    i = 0
    while i < len(intlist):
        opscode = intlist[i]
        if opscode == 1:
            intlist[intlist[i + 3]] = intlist[intlist[i + 1]] + intlist[intlist[i + 2]]
        elif opscode == 2:
            intlist[intlist[i + 3]] = intlist[intlist[i + 1]] * intlist[intlist[i + 2]]
        elif opscode == 99:
            break
        i = i + 4
    return intlist


def find_output(intlist, target):
    noun = 0
    verb = 0
    output = intcode_calculations(intlist.copy(), noun, verb)[0]
    while output != target:
        noun = random.randint(0, len(intlist)-1)
        verb = random.randint(0, len(intlist)-1)
        output = intcode_calculations(intlist.copy(), noun, verb)[0]
    print(output)
    return noun, verb


# get content
content = read_utils.getinput("day2.txt")[0]

stringcontent = str(content)
stringlist = stringcontent.split(",")
intlist = read_utils.converttoint(stringlist)
intcode_list = list()
for i in range(len(intlist)):
    intcode_list.append(Intcode(intlist[i:i+3]))




# intcode_calculations(intlist, noun, verb)
noun, verb = find_output(intlist, 19690720)
print(noun, verb)
solution = 100*noun + verb
print(solution)
