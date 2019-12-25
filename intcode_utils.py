from constants import Constants
from intcode import Intcode
import random


# def intcode_calculations(intlist, noun, verb):
#     set_noun(intlist, noun)
#     set_verb(intlist, verb)
#     i = 0
#     while i < len(intlist):
#         opscode = intlist[i]
#         if opscode == 1:
#             intlist[intlist[i + 3]] = intlist[intlist[i + 1]] + intlist[intlist[i + 2]]
#         elif opscode == 2:
#             intlist[intlist[i + 3]] = intlist[intlist[i + 1]] * intlist[intlist[i + 2]]
#         elif opscode == 99:
#             break
#         i = i + 4
#     return intlist


def calculate_intcode(intlist: list):
    i = 0
    while i < len(intlist):
        intcode: Intcode = Intcode(intlist[i:i + 4])
        if intcode.get_instruction() == Constants.add:
            intlist[intcode.get_location()] = intlist[intcode.get_first_location()] + intlist[
                intcode.get_second_location()]
        elif intcode.get_instruction() == Constants.multiply:
            intlist[intcode.get_location()] = intlist[intcode.get_first_location()] * intlist[
                intcode.get_second_location()]
        elif intcode.get_instruction() == Constants.exit:
            break
        i = i + 4
    return intlist


def find_output(intlist: list, target: int):
    address = calculate_intcode(intlist.copy())[0]
    noun: int = 0
    verb: int = 0
    while address != target:
        noun = random.randint(0, len(intlist) - 1)
        verb = random.randint(0, len(intlist) - 1)
        newintlist = intlist.copy()
        set_noun(newintlist, noun)
        set_verb(newintlist, verb)
        address = calculate_intcode(newintlist)[0]
    print(address)
    return noun, verb


def set_noun(intlist: list, noun: int):
    intlist[1] = noun


def set_verb(intlist: list, verb: int):
    intlist[2] = verb
