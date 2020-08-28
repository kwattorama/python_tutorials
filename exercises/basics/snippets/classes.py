"""Classes in Python"""


class Employee(object):
    _id = "IN6969"
    name = "XA"
    employer = "Google"
    location = "Mumbai"

    def eat(self):
        print("We're eating...")

    def talk(self):
        print("We're talking...")

    def leave(self):
        print("We're leaving...")


class Grandparent:
    skill = "Painting"
    pass


class Parent(Grandparent):

    def __init__(self):
        print(Grandparent().skill)


Parent()
print(Parent().skill)
