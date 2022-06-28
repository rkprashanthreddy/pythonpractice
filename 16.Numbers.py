# 3 Types Of Numbers
x = 10  # int
y = 10.20  # float
z = 1j  # complex
print(x, type(x))
print(y, type(y))
print(z, type(z))

# int can be unlimited length positive or negative, no decimal values
x = 1028308309090
y = -20930
print(x, type(x))
print(y, type(y))

# float can be unlimited lenght positive or negative+use of e (scientific number denotion)
# to indicate the power of 10  with decimal values 1 or more, e or E both same
x = 20.0
y = -200039.2e10
# z = 32e10.2e2      # We cant use decimals if we mention e power in main numbers.
z = 20e2
a = 3E3
print(x, type(x))
print(y, type(y))
print(z, type(z))
print(a, type(a))

# complex numbers written as j as imaginary part
x = 2+1j
y = 2j
z = -30j
print(x, type(x))
print(y, type(y))
print(z, type(z))
