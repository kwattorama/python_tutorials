"""Classes in Python"""


# class Employee(object):
#     _id = "IN6969"
#     name = "XA"
#     employer = "Google"
#     location = "Mumbai"

#     def eat(self):
#         print("We're eating...")

#     def talk(self):
#         print("We're talking...")

#     def leave(self):
#         print("We're leaving...")

# # Multilevel, Multiple, Hierarchical and Hybrid Inheritance


# class God:  # Base Class
#     print("I'm God.")


# class Father(God):  # Derived Class or Child Class
#     print("I'm Pappa.")


# class Mother(God):  # Derived Class or Child Class
#     print("I'm Mum.")


# class Child(Mother, Father):
#     print("I'm Child.")


# class YoMama(object):
#     name = "XA"

#     def paint():
#         print("Painting...")


# class DK(YoMama):
#     name = "Shailesh"
#     paint = "Acrylic"

#     print(YoMama.paint())


# DK()

# class Grandparent(object):
#     skill = "Painting"


# class Parent(Grandparent):
#     print(Grandparent.skill)

class PhoneBox(object):
    obj_1 = "Phone"
    obj_2 = "Charger"
    obj_3 = "Charging Cord"
    obj_4 = "Paperwork"

    class Phone():
        obj_1 = "Gallery"
        obj_2 = "Phone"
        obj_3 = "Settings"

        class PhoneApp():

            def call_xa():
                print("Calling God...")


# PhoneBox().Phone.PhoneApp.call_xa()

# To perform communication.
class Communicate(object):
    def timepass(self, how_much, with_whom):
        print("Action of communicating..."
              f"with {with_whom} for {how_much} secs.")


class Human(Communicate):
    def timepass(self):
        Communicate.timepass(self, 86400, "CP")
    # Communicate().timepass()

    def timepass(self):
        print(1 + 1)
        print("Hello babe")
        print("XA roxxx...")


Human().timepass()


# class Dog(Communicate):
#     print("Dog will start barking... woof woof")


# class Cat(Communicate):
#     print("Cat will start meowing... meow meow")


# x = ["XA"]
# a = ["XA"]

# xa = x + a

# Operator Overloading...
# Functional Overloading...
