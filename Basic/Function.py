def GreetMe():
    print("Good morning")


GreetMe()

def GreetMe(name):
    print("Good morning" + name)

GreetMe("Ashok")

def AddInteger(a, b):
    print(a+b)


AddInteger(2,8)


def AddInteger(a, b):
    return a+b

print(AddInteger(2,8))