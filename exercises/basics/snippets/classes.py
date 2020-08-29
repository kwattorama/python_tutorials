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

# Multilevel, Multiple, Hierarchical and Hybrid Inheritance


class God:  # Base Class
    print("I'm God.")


class Father(God):  # Derived Class or Child Class
    print("I'm Pappa.")


class Mother(God):  # Derived Class or Child Class
    print("I'm Mum.")


class Child(Father, Mother):
    print("I'm Child.")
