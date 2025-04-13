

from FirstDemo import a

value = [1, 4, "Ashok", 0.007]

print(value)

print(value[0])

print(value[2])

print(value[1:3])

value.insert(3, "Babu")

print(value)

value.append("python")
print(value)

value[2] = "ashok"

print(value)

del value[0]

print(value)

# Tuple Same as list but not update the value

values = (1, 4, "Ashok", 0.007)

print(values)

#Dictionary

named = {"bs" : "babu", "b":87, "c":"Ashok", 2:"a"}

print(named[2])

# add value to Dictionary

ashok = {}

ashok ["first name"] = "AshokBabu"
ashok ["last name"] = "TB"
ashok ["age"] = 29

print(ashok["age"])
