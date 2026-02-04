# Strings

print("Hello")
print('Hello python')

# op:
# Hello
# Hello python


# Quotes Inside Quotes
print("it is alright")
print("he is called 'johnny'")
print('he is called "johnny"')

# op:
# it is alright
# he is called 'johnny'
# he is called "johnny"


# Multiline Strings
a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)

# op:
# Lorem ipsum dolor sit amet,
# consectetur adipiscing elit,
# sed do eiusmod tempor incididunt
# ut labore et dolore magna aliqua.



# Strings are Arrays
a = "Hello, World"
print(a[1])
# op:
# e 



# Looping Through a String
for a in "banana":
    print(a)
    
# op:
# b
# a
# n
# a
# n
# a


# String Length
a = "Hello World"
print(len(a))
# op:
# 11




# Check String
txt = "the best things in life are free"
print("free" in txt)

# op:
True



txt = "the best things in life are free!"
if "free" in txt:
    print("Yes, 'free' is present ")
# op:
# Yes, 'free' is present




# Check if NOT
txt = "the best thing il life are free"
print("expensive" not in txt)

# op:
True


txt = "the best things in life are free"
if "expensive" not in txt:
    print("No,'expensive' is NOT Present. ")

# op:
# No,'expensive' is NOT Present. 














# Python - Slicing Strings
# Python - Slicing Strings
# Python - Slicing Strings

# slicing
b = "Hello, World"
print(b[2:5])

# op:
# llo




# Slice From the Start
a = "Hello, World"
print(a[:5])
# op:
# Hello



b = "Hello World"
print(b[2:])

# op:
# llo World




# Negative Indexing
b = "Hello World"
print(b[-5:-2])
# op:
# wor





# Python - Modify Strings

# Upper Case
a = "Hello world"
print(a.upper())

# op:
# HELLO WORLD

a = "Hello World"
print(a.lower())

# op:
# hello world




# Remove Whitespace
a = " Hello     world "
print(a.strip())




# Replace String
a = "Hello World"
print(a.replace("H", "J"))

# op:
# Jello World



# Split String
# split 

a = "Hello, World"
print(a.split(","))

# op:
# ['Hello', ' World']












# Python - String Concatenation
a = "Hello "
b = "World"
c = a + b
print(c)

a = "hello"
b = "world"
c = a + " " + b
print(c)















# Python - Format - Strings

# String Format

# As we learned in the Python Variables chapter, we cannot combine strings and numbers like this:

# age = 35
# txt = "my name is Jhon, I am " + age
# print(txt)
# op:
# TypeError: can only concatenate str (not "int") to str




# F-Strings
age = 55
txt = f"my neme is jhon, and i am {age} years old"
print(txt)
# op:
# my neme is jhon, and i am 55 years old


# Placeholders and Modifiers
price = 45
txt = f"the price is {price} dollars"
print(txt)

# op:
# the price is 45 dollars






price = 53
txt = f"the price is {price:.2f} dollars"
print(txt)
# output: the price is 53.00 dollars





txt = f"the priceis {20 * 59} dollars"
print(txt)
# op:
# the priceis 1180 dollars
















