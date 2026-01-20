# Built-in Data Types
# In programming, data type is an important concept.

# Variables can store data of different types, and different types can do different things.

# Python has the following data types built-in by default, in these categories:



# 1. text Type: string
# 2. Numeric Types: int, float, complex
# 3. Sequence Types: list, tuple, range 
# 4. mapping types: dict 
# 5. set types: set, frozenset 
# 6. Boolean Types: bool> True, False
# 7. Binary Types: byte, bytearray, memoryvies
# 8. None Type: None type



x = "Hello"
print(type(x))
# op: "str"

# text type 
a = "Hello World" #str

# numeric type 
a = 200 #int
a = 30.5 #float
a = 4j #complex

# sequence type 
a = ["apple", "banana", "cherry"] #list
a = ("apple", "banana", "cherry") #tuple
a = (7) #range

# mapping 
a = {"nam": "jhon", "age": 22} #dict

# set type
a = {"apple", "banana", "cherry"} #set
a = frozenset({"apple", "banana", "cherry"}) #frozenset


a = True #bool
a = False #bool


# Binary Type 
a = b"Hello" #byte
a = bytearray(5) #bytearray
a = memoryview(bytes(5)) #memoryview

# None type 
a = None #NoneType






