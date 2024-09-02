import os
import platform


def clear():
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")


def is_correct(input_display):
    for letter in input_display:
        if letter == "_":
            return False
    return True
