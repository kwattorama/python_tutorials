# """Classes in Python"""


# # class Employee(object):
# #     _id = "IN6969"
# #     name = "XA"
# #     employer = "Google"
# #     location = "Mumbai"

# #     def eat(self):
# #         print("We're eating...")

# #     def talk(self):
# #         print("We're talking...")

# #     def leave(self):
# #         print("We're leaving...")

# # # Multilevel, Multiple, Hierarchical and Hybrid Inheritance


# # class God:  # Base Class
# #     print("I'm God.")


# # class Father(God):  # Derived Class or Child Class
# #     print("I'm Pappa.")


# # class Mother(God):  # Derived Class or Child Class
# #     print("I'm Mum.")


# # class Child(Mother, Father):
# #     print("I'm Child.")


# # class YoMama(object):
# #     name = "XA"

# #     def paint():
# #         print("Painting...")


# # class DK(YoMama):
# #     name = "Shailesh"
# #     paint = "Acrylic"

# #     print(YoMama.paint())


# # DK()

# # class Grandparent(object):
# #     skill = "Painting"


# # class Parent(Grandparent):
# #     print(Grandparent.skill)

# class PhoneBox(object):
#     obj_1 = "Phone"
#     obj_2 = "Charger"
#     obj_3 = "Charging Cord"
#     obj_4 = "Paperwork"

#     class Phone():
#         obj_1 = "Gallery"
#         obj_2 = "Phone"
#         obj_3 = "Settings"

#         class PhoneApp():

#             def call_xa():
#                 print("Calling God...")


# PhoneBox().Phone.PhoneApp.call_xa()


# # To perform communication.
# class Communicate(object):
#     def talking(self, how_much, with_whom):
#         print("Action of communicating..."
#               f"with {with_whom} for {how_much} secs.")



#     # Communicate().talking()

#     # def talking(self):
#     #     print(1 + 1)
#     #     print("Hello babe")
#     #     print("XA roxxx...")


# class Dog(Communicate):
#     def talking(self):
#         print("I'm barking...")
#     # print("Dog will start barking... woof woof")


# class Cat(Communicate):
#     print("Cat will start meowing... meow meow")


# # from abc import ABC, abstractmethod


# # # Abstract Base Class
# # class XA(ABC):

# #     # @abstractmethod
# #     def some_work(self):
# #         pass


# # x = XA().some_work()


# # x = 1
# # a = "2"

# # xa = x * a
# # print(xa)

# # # Operator Overloading...
# # # Functional Overloading..

# class Human(Communicate):
#     # Communicate().talking(86400, "SP")

#     def talking(self):
#         print("I'm dancing...")


# Human().talking()

# class ActionTeachHowToCode(Actions):

#     def __name__(self):
#         return repr(class.__init__.name() at id)

#     def __name__(self):
#         return "teaching_how_to_code"

#     def something(self):
#         pass

def decodeco(fnc):
    def normal():
        fnc()
        return 25
    return normal   



# def normal():
#     xa = 10
#     return xa
#     print("XA")


# def nimesh():
#     xa = 10
#     yield xa
#     xa += 1 # xa = xa + 1
#     yield xa


# for x in nimesh():
#     print(x)


# @decodeco
# def rdn():
#     print("XA")


def decodeco(fnc):
    def normal():
        print("Normal is running now...")
        fnc()
    return normal


# @decodeco
# def tryout():
#     print("I'm tryout function")


# x = decodeco(tryout)
# x()
# @decodeco


x = xa = {"xa", "XA", "daulat", 420, 89.0, 2.03}
for i in x:
    print(i)
# {'XA', 2.03, 420, 'xa', 'daulat', 89.0}
