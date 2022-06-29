# used to perform operations on values and variables only
# arithmetic operators
print("Arithmetic Operators")
print("---------------------------")
a, b, c = 10, 20, 30
print("Addition: ", a+b)
print("Substraction: ", b-a)
print("Multiplication: ", a*b)
print("Division: ", a/b)
print("Modulus / remainder: ", a % b)
# rounds the quotient to nearest integer value.
print("Floor Division: ", a//b)
print("Expresion Evaluation As BODMAS:  10+(20*30)/(10+30) ", a+(b*c)/(a+c))
print("Exponentation of b ie 20 by 2:", b**2)

print("\n")

# comparision operators returns boolean values
print("Comparision Operators")
print("-----------------------------")
a, b, c = 100, 200, 100
print("a: ", a, " b: ", b, " c: ", c)
print("a equal to b?: ", a == b)
print("a not equal to b?: ", a != b)
print("b greater than a?: ", b > a)
print("c less than b?: ", c < b)
print("a greater than or equal to b?: ", a >= b)
print("c less than or equal to b?: ", c <= b)
d = 10
while(d != 0):
    print(d)
    d = d-1

print("\n")

# logical operators returns boolean values
print("Logical Operators")
print("----------------------")
a, b, c = 10, 20, 10
print("a: ", a, " b: ", b, " c: ", c)
print("a equals to b? and b  not equals to c?: ", a == b and b != c)
if (a == b and b == c):
    print(" yes")
else:
    print("No")
print("a equals to c? or a equals to b?: ", a == c or a == b)
print("not( b greater than a?): ", not(b > a))

print("\n")

# membership operator: in, not in : returns boolean values
print("Membership Operators")
print("----------------------------")
txt = "Hello Prashanth"
lst = ['honey', 'sugar', 'canejuice']
print(txt)
print(lst)
print("Is Honey in lst?: ", "Honey" in lst)
print("Is Hi not in txt?: ", "Hi" not in txt)
for i in lst:
    print(i)
for x in txt:
    print(x)

print("\n")

# Identity operators: is, is not : returns boolean values
# not like equal to, its same object and same memory location
print("Identity Operator")
print("----------------------")
x = ['hello', 'how']
y = ['hello', 'how']
z = x
print("x=", x)
print("y=", y)
print("z=", z)
print("x is y?: ", x is y)
print("z is x?: ", z is x)
print("x equal to y: ", x == y)
print("y not same as x?: ", y is not x)
print("y not equal to x?: ", y != x)

print("\n")

# bitwise operators
'''
general in programming
------------------------------
short int : 2 bytes                  1 byte=8 bits
int : 4 bytes                           if 4 bytes = 4*8=32 bits
float : 4 bytes                      
etc..

Bitwise operations performed on bits of the value, first the number is converted into binary
and calculation performed and result binary number converted back to decimal.
eg: x=10    in decimal
      10=       8  4  2 1
                   1  0  1  0    ( 8+2 =10)
      hence 10=1010 in binary
'''
print("Bitwise Operators")
print("----------------------")
x = 10
y = 4
# if 1 and 1 then it is 1, if 1 and 0 then 0 and if 0 and 0 is 0
print("x & ( and ) y: ", x & y)
'''
10 in binary =1010 ( 4 bits )
4 in binary =0100 ( 4 bits )

1010
0100
----
0000
hence x&y=result 0
'''
# if 1 and 1 then it is 1, if 1 and 0 then 1 and if 0 and 0 is 0
print("x | ( or ) y: ", x | y)
'''
1010
0100
----
1110

8 4 2 1
1 1 1 0
-------
8+4+2+0 =>14

hence x|y=result 14
'''
# if 1 and 1 then it is 0, if 1 and 0 then 1 and if 0 and 0 is 0
print("x ^ ( xor ) y: ", x ^ y)
'''
1010
0100
----
1110

8 4 2 1
1 1 1 0
-------
8+4+2+0 =>14

hence x^y=result 14

unline or if any one condition is true then its true or both is true then its true, but xor it should be only one 
condition to be true not both true then its false.
'''
print("~ ( not ) x:", ~x)      # ones compliment of x
'''
-1010+1
-------
-1011 

8 4 2 1
1 0 1 1
-------
8+0+2+1 =>11 => -11

hence x|y=result -11
'''
print("x>> ( right shift by ) y (bits) : ", x >> y)
'''
10>>4
1010>>0100   move 4 bits towards right
00001010     8 bits int
move by 4 bits towards right
_ _ _ _ 0 0 0 0   ( removed 1010 )
empties are filled 0s
result= 0 0 0 0 0 0 0 0 => 0 in decimal
so 10>>4 = result 0
'''
print("x<< ( legt shift  by ) y (bits): ", x << y)
'''
10<<4
1010>>0100   move 4 bits towards left
00001010     8 bits int
move by 4 bits towards right
1 0 1 0 _ _ _ _   ( removed 1010 )
empties are filled 0s
        128 64 32 16 8 4 2 1
result= 1   0  1  0  0 0 0 0 
       ----------------------
	    128+0+32+0+0+0+0+0 =>160 in decimal
so 10<<4 = result 160
'''

print(" \n")

# assignment operators
print("Assignment Operators")
print("----------------------------")
x = 200
print("x=", x)
x, y = 10, 20
print("x=", x, " y=", y)
x += y
# if we right like this gives error, we have to assign it first to some variable
print("x+=y", x)
# no direct mention of assignment operation inside the print.
x, y = 10, 20
y -= x
print("y-=x", y)
x, y = 10, 20
x *= x
print("x*=x", x)
x, y = 10, 20
y /= x
print("y/=x", y)        # decimal values can be output
x, y = 10, 20
y %= x
print("y%=x", y)
x, y = 10, 20
y //= x
# no decimals output, if result leads to decimal then rounded off to nearest int
print("y//=x", y)
x, y = 10, 20
y **= x
print("y**=x", y)
x, y = 10, 20
y &= x
print("y&=x", y)
x, y = 10, 20
y |= x
print("y|=x", y)
x, y = 10, 20
y ^= x
print("y^=x", y)
x, y = 10, 20
y >>= x
print("y>>=x", y)
x, y = 10, 20
y <<= x
print("y<<=x", y)
print(x, " ", y)
