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
d = 20j  # complex number
e = complex(a)
# f = int(d)  # cannot convert complex number to any other number
# g = int("H") # cant convert single letter to equivalent char number
# h = int("Hello") # cant convert string given not as number.
print(e)
print(a)
print(b)
print(c)
print(type(e), type(a), type(b), type(c))
