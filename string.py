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


