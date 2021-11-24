#Exercises XP

#Exercise 1 : Built-In Functions
#
# class Newclass:
#     """This is doc string"""
#     def __init__(self):
#         pass
#
#     def abso(self):
#         """ This is how we use an abs function"""
#         print(abs.__doc__)
#         print("this is an absolute value of - 24: ", integer.__abs__())
#
#     def intr(self):
#         """ This is how we use an int function"""
#
#         print("this is int and the integer is ", (10).__int__())
#
#
# print(Newclass.__doc__)
#
# integer = -24
# print("the value is:", integer.__abs__())
# print(abs.__doc__)
#
# print("The integer value is: ", (10).__int__())
# print(int.__doc__)
# value = input("Enter a number: ")
# print("You have entered:", value)

#Exercise 2: Currencies
class Currency:
    def __init__(self, currency, amount):
        self.currency = currency
        self.amount = amount

    def __str__(self):
        return f"{self.amount} {self.currency}"

    def __int__(self):
        return self.amount

    def __repr__(self):
        return f"{self.amount} {self.currency}"

    def __add__(self, other):
        if isinstance(other, int):
            return self.amount + other
        elif isinstance(other, Currency):
            if self.currency == other.currency:
                return self.amount + other.amount
            else:
                raise Exception("Cannot add between Currency type <dollar> and <shekel>")
        else:
            raise Exception("Cannot add except objects and ints")

c1 = Currency('dollar', 5)
c2 = Currency('dollar', 10)
c3 = Currency('shekel', 1)
c4 = Currency('shekel', 10)

print(str(c1))
print(c1 + 5)
c1 +=c2
print(c1)
print(c1+c3)