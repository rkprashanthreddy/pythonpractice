# change one data type value to other datatype
x = "10"  # it is string
y = int(x)
print(y)
print(type(y))  # int
print(type(x))  # string

# example 2
a = str(10)
b = int(10.20)  # This casting will loose .20 values.
c = float(30)
print(a)
print(b)
print(c)
print(type(a), type(b), type(c))
