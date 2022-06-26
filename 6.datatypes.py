print("Data Types: Setting The Data Types:")
print("-----------------------------------")
# Text Type : str
x = "Hello"
y = 'hello'
print(x, y)
print(type(x), type(y))

print("\n")

# Numeric Type: int,float,complex
# x=10  #gives error due to indent spaced because its in main block.
x = 10
y = 20.2
z = 20j
print(x, y, z)
print(type(x), type(y), type(z))

print("\n")

# Boolean Type: bool
x = True   # first letter should be caps
y = False
print(x, y)
print(type(x), type(y))

print("\n")

# Sequence Types: list, tuple, range
fruits = ["Apple", "Mango", "Orange"]
cars = ("BMW", "Porsche", "Lamborguini")
x = range(6)
print(fruits, cars, x)
print(type(fruits), type(cars), type(x))

print("\n")

# Mapping Types: dict /dictionary
student = {"age": 20, "name": "Prashanth"}
print(student)
print(type(student))

print("\n")

# set types: set, frozenset
numbers = {1, 2, 3, 4, 5}
# ages = frozenset(1, 2, 3, 4, 5) #gives error, fronzen set expects at most 1 argument given 5
ages = frozenset({1, 2, 3, 4, 5})
print(numbers, ages)
print(type(numbers), type(ages))

print("\n")

# None Type: noneType
x = None  # first letter should be capital
print(x)
print(type(x))

print("\n")

# Binary Types: bytes,bytearray,memoryview
# need to practice or understand below more, just a glance practiced below datatypes.
x = b"Hello"
y = bytearray(5)
z = memoryview(bytes(5))
print("bytes:", x)
print(type(x))
print("bytearray:", y)
print(type(y))
print("memoryview:", z)
print(type(z))

print("\n")

print("Setting The Specific Data Types:")
print("-----------------------------------")
# to specify the data type, use the below constructor functions, except for none type available
x = str("Prashanth")
print("string:", x)
print(type(x))

print("\n")

x = int(10)
print("int:", x)
print(type(x))

print("\n")

x = float(20.2)
print("float:", x)
print(type(x))

print("\n")

x = complex(20j)
print("complex:", x)
print(type(x))

print("\n")

x = list(("apple", "banana", "orange"))
print("list:", x)
print(type(x))

print("\n")

x = tuple(("BMW", "Lamborguinni", "Rolls Royce"))
print("tuple:", x)
print(type(x))

print("\n")

x = range(10)
print("range:", x)
print(type(x))

print("\n")

x = set((1, 2, 3, 4, 5))
print("set:", x)
print(type(x))

print("\n")

x = frozenset((1, 2, 3, 4, 5))
print("frozenset:", x)
print(type(x))

print("\n")

x = dict(name="prashanth", age=20)
print("dictionary:", x)
print(type(x))

print("\n")

x = bool(5)   # gives true, if only use bool() then gives false as no value
print("boolean:", x)
print(type(x))

print("\n")

x = bytes(5)
print("bytes:", x)
print(type(x))

print("\n")

x = bytearray(5)
print("bytearray:", x)
print(type(x))

print("\n")

x = memoryview(bytes(5))
print("memoryview:", x)
print(type(x))

print("\n")
