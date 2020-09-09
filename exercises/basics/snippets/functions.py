"""
Functions
---------

A Function is a particular block* of code that is basically written in majority of the programming languages to increase the reusability of the
code.

 - They make code more modular.
 - They make debugging easy.

BT: Func is a group of related statements that perform a specific task.
SK: Block of code which runs when called.

Rules:
------

 - Exercise referential transparency.
 - Follow rules of identifier's nomenclature.
 - Practise function definitions in max. 15 lines.
"""

# _ = "XA"

# yield # generator
# return # function

# import sys

# def xa_print(msg=None):
#     return sys.stdout.write(msg + "\n")

# def _():
#     x = 25
#     y = 35
#     z = x + y
#     return f"The total is {z}."
#     # return z
#     # print("This works just fine!")

# # def xa():
#     # pass


# # def str():
# #     print("XA rocks!")
# #     type = check_type()

# def send_message_to_user():
#     pass


# def snd_msg2usr():
#     pass

# # list = [1, 2, 3]
# # print(list)

# # print(list(range(5)))

# # str()
# # xa = 420
# # xa = str(420)
# # print(xa, type(xa))


# x = 10
# y = 6
# z = x + y
# print(z)

# xa = 23
# mes3 = 23
# xames3 = xa + mes3
# print(xames3)


def calculator(num_1, num_2, opr):
    if opr == "add":
        return num_1 + num_2
    elif opr == "sub":
        return num_1 - num_2
    elif opr == "mul":
        return num_1 * num_2
    else:
        return num_1 / num_2


print(calculator(0.2568741, 0.12457845, "add"))
for idx in range(2):
    num_1 = float(input("Enter first number: "))
    num_2 = float(input("Enter second number: "))
    opr = input("Enter operation (add/mul/sub/div) for {}: ".format(idx))
    print(calculator(num_1, num_2, opr))



# opening a file to get list of names
import os
import time

# srushti.txt
# Opening the above file -> ["xa", "shree", "mini", "syed"]

# Whatever changes/fluctuates -> args
def open_from_files(file):
    return open(file).read()


def some_fnc(names):
    for name in names:
        print(len(name))

# for idx in os.listdir("some path in directory"):
#     some_fnc(open_from_files(idx))
#     time.sleep(86400)


xa = open("/mnt/storage/development/programming/python_tutorials/exercises/basics/snippets/classes.py", "r").readline(1)
print(xa)