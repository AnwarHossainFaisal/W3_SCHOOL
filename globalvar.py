# Create a variable outside of a function, and use it inside the function

# x = "Awesome"
# def myFunc():
#     print("python is " + x)

# myFunc()


# Create a variable inside a function, with the same name as the global variable

# x = "awesome"
# def my_func():
#     x = "Fantastic"
#     print("python is " + x)

# my_func()
# print("python is" + x)


# If you use the global keyword, the variable belongs to the global scope:
# def myFunction():
#     global x
#     x = "Fantastics"

# myFunction()
# print("python iss " + x)


x = "awesome"
def MYfunc():
    global x
    x = "fantastic"

MYfunc()
print("pyton is " + x)
