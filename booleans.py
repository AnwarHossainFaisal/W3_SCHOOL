print(10 > 9)
print (10 == 9)
print(10 < 9)

# op:
True
False
False




a = 300
b = 55
if b > a:
    print("b is greater than a")
else:
    print(" a is greater than b")
# op:
# a is greater than b       




# Evaluate Values and Variables
print(bool("Hello"))
print(bool(15))
# op:
# True
# True


a = "Hello"
b = 55


print(bool(a))
print(bool(b))


# Most Values are True
print(bool("abe"))
print(bool(123))
print(bool(["apple", "cherry", "banana"]))
# op:
# True
# True
# True



# Some Values are False
print(bool(False))
print(bool(None))
print(bool(0))
print(bool(""))
print(bool(()))
print(bool([]))
print(bool({}))
# op:
False
False
False
False
False
False
False




class myClass():
    def _len_(self):
        return 0
    
myobj = myClass()
print(bool(myobj))



def myFunc():
    return True

print(myFunc)



def myFunction() :
    True

if myFunction():
    return True


if myFunction():
    print("YES")
else:
    print("NO")







