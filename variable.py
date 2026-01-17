# creating variables
a = "5 "
b = "jhon"
print(a + b)

# output:5 jhon


# Variables do not need to be declared with any particular type, and can even change type after they have been set.
a = 4
a = "sally"
print(a)
# op: sally

# type casting
a = str(5)
b = int(5)
c = float(5)
print(a, b, c)


# Get the Type
x = 5
y = "jhon"

print(type(x))
print(type(y))

# op:<class 'int'>
# <class 'str'>

# Single or Double Quotes?

a = "jhon"
a = 'Jhon'
print(a)

# Case-Sensitive
# Variable names are case-sensitive.
a = 3
A = 5
# op:3
    # 5

# Variable names are case-sensitive.
# A variable can have a short name (like x and y) or a more descriptive name (age, carname, total_volume).

# Rules for Python variables:

# A variable name must start with a letter or the underscore character
# A variable name cannot start with a number
# A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
# Variable names are case-sensitive (age, Age and AGE are three different variables)
# A variable name cannot be any of the Python keywords.


# wright

myvar = "jhon"
my_var = "jhon"
_my_var = "jhon"
myVer = "jhon"
MYVER = "jhon"
myver2 = "jhon"


# woring
# 2myvar = "jhon"
# my-ver = "jhon"
# my ver = "jhon"


# Multi Words Variable Names
# Camel Case
myVariavleName = 'jhon'


# pascal Case
Myvariablename = 'jhon'


# snake case
my_variavle_name = 'jhon'


# Python Variables - Assign Multiple Values

# Many Values to Multiple Variables

a, b, c = "orange", "banana", "cherry"
print(a)
print(b)
print(c)

# orange
# banana
# cherry


# One Value to Multiple Variables
a = b = c = "Orange"
print(a)
print(b)
print(c)
# op:
# Orange
# Orange
# Orange


# Unpack a Collection
fruits = ["apple", "banana", "cherry"]
a, b, c = fruits
print(a)
print(b)
print(c)
# op:
# apple
# banana
# cherry



# Python - Output Variables
# Output Variables
a = "pyrhon is awesome"
print(a)


a = "pthon"
b = "is"
c = "awesome"

print(a, b, c)

# You can also use the + operator to output multiple variables:
a = 'python '
b = 'is '
c = 'awesome'
print(a + b + c)
# op:python is awesome

# For numbers, the + character works as a mathematical operator:
a = 5
b = 7
print(a + b)
# op:12
print(33 + 55)

# In the print() function, when you try to combine a string and a number with the + operator, Python will give you an error:
# a = 5
# b = "awesome"
# print(a + b)
# op:TypeError: unsupported operand type(s) for +: 'int' and 'str'

# right
a = 3
b = "nice"
print(a, b)
# op: 3 nice


# Python - Global Variables
a = "awesome"

def myfunc():
    print("python is " + a)
    
myfunc()


# Create a variable inside a function, with the same name as the global variable
a = "awesome"
def my_func():
    a = "fantastic"
    print("python is " + a)
my_func()

print("python is " + a)
