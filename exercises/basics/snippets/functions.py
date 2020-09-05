"""
Functions
---------

A Function is a particular block* of code that is basically written in majority of the programming languages to increase the reusability of the
code.

 - They make code more modular.
 - They make debugging easy.

BT: Finc is a grup of related statements that perform a specific task.
SK: Block of code which runs when called.

Rules:
------

 - Exercise referential transparency.
 - Follow rules of identifier's nomenclature.
 - Practise function definitions in max. 15 lines.
"""

# _ = "XA"

yield # generator
return # function

import sys

def xa_print(msg=None):
    return sys.stdout.write(msg + "\n")

def _():
    x = 25
    y = 35
    z = x + y
    return f"The total is {z}."
    # return z
    # print("This works just fine!")

# def xa():
    # pass


print()
xa_print(_())
# print(xa())


# x = 25
# y = 35
# z = x + y
# print(z)
