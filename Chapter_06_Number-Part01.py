#=====================================================================================================================================
#==================================================== Chapter 06: Number ============================================================
#=====================================================================================================================================
#=============================================== Part 01: Mathematical Function =====================================================
# (1): abs() method is used to returns the absolute value of x. Ex: positive between x and zero. It convert the all of
#      numbers becoming positive number.
# (2): math.ceil() method is used to return the ceiling value of x. Ex: the smallest integer does not less than x. 
#      If the positive number it will round up and if negative number it will round down.
# (3): exp() method is used to find the exponential of x, where x is the real number. 
# (4): fabs(float abs) method is used to return the absolute value of x that is similar to abs() function. there are 
#      different points between these two functions such that:
#           I.)  abs () is a built in function whereas fabs() is defined in math module. ==> absolute value.
#           II.) fabs() is a function works only on float and integer whereas abs() works with complex number also.
# (5): log() method is used to return the natural logarithm of x,"ln(x)". for x>0
# (6): log10() method is used to return the base-10 logarithm of x for x>0:
# (7): max() and min() methods are used to find the maximum value and minimum value.
# (8): modf() method is used to return the fractional and integer parts of x in a two-item tupple. Both parts have the
#      same as x. The integer part is returned as a float.
# (9): sqrt() and pow() is used to return the square root of x and power of x by a.
# (10):round() method is used to round up and round down the fractional number.

#***************** Exercise 1: Number abs() method is used to returns the absolute value of x. Ex: positive between x
# and zero. It convert the all of numbers becoming positive number.
# from cmath import sqrt
# print("The absolute value of -45 is : ",abs(-45))
# print("The absolute value of 100.2 is :",abs(100.12))
# x = 20
# y = 30
# z = x**y
# a = x/y
# b = x**2 + y**2
# c = sqrt(b)
# d = abs(a**2 - b**2)
# e = y%x-b
# f = complex(2)
# print(abs(f))
# print("The value of z is :",z)
# print("The value division between x and y is :",a)
# print("The sqare summation of x and y is :",b)
# print("The square root of b is :",c)
# print("The absolute value of square substraction between a and b is :",d)
# print("The absolute value of remainder obatained from division between y and x then minus b is :",abs(e))

# Output:
            # The absolute value of -45 is :  45
            # The absolute value of 100.2 is : 100.12
            # 2.0
            # The value of z is : 1073741824000000000000000000000000000000
            # The value division between x and y is : 0.6666666666666666
            # The sqare summation of x and y is : 1300
            # The square root of b is : (36.05551275463989+0j)
            # The absolute value of square substraction between a and b is : 1689999.5555555555
            # The absolute value of remainder obatained from division between y and x then minus b is : 1290

#***************** Exercise 2: Number math.ceil() method is used to return the ceiling value of x. 
# Ex: the smallest integer does not less than x. 
# If the positive number it will round up and if negative number it will round down.
# from cmath import pi
# import math
# a = -45.17
# b = 100.12
# c = 100.72
# d = pi
# print("The math.ceil(a) is :",math.ceil(a))
# print("The math.ceil(b) is :",math.ceil(b))
# print("The math.ceil(c) is :",math.ceil(c))
# print("The math.ceil(d) is :",math.ceil(d))
# print(math.ceil(-100.99))
# Output:
            # The math.ceil(a) is : -45
            # The math.ceil(b) is : 101
            # The math.ceil(c) is : 101
            # The math.ceil(d) is : 4

#***************** Exercise 3: Number exp() method is used to find the exponential of x, where x is the real number.
# from cmath import exp, pi
# print("exponential of -45.17 is :",exp(-45.17))
# print("exponential of 100.12 is :",exp(100.12))
# print("exponential of 100.72 is :",exp(-45.17))
# print("exponential of pi is :",exp(pi))

# import math   # is used to transform the complex number to real number.
# print("exponential of -45.17 is :",math.exp(-45.17))
# print("exponential of 100.12 is :",math.exp(100.12))
# print("exponential of 100.72 is :",math.exp(-45.17))
# print("exponential of pi is :",math.exp(pi))
# Output:
                    # exponential of -45.17 is : (2.4150062132629406e-20+0j)
                    # exponential of 100.12 is : (3.0308436140742566e+43+0j)
                    # exponential of 100.72 is : (2.4150062132629406e-20+0j)
                    # exponential of pi is : (23.140692632779267+0j)

                    # exponential of -45.17 is : 2.4150062132629406e-20
                    # exponential of 100.12 is : 3.0308436140742566e+43
                    # exponential of 100.72 is : 2.4150062132629406e-20
                    # exponential of pi is : 23.140692632779267

#***************** Exercise 4: Number fabs() method is used to return the absolute value of x that is similar to 
# abs() function, there are different points between these two functions such that:
# (1): abs () is a built in function whereas fabs() is defined in math module. ==> absolute value
# (2): fabs() is a function works only on float and integer whereas abs() works with complex number also.==>float abs.
# from math import fabs
# x = -12.234
# y = -19
# print("The flaot absolute value of x is :",fabs(x))
# print("The flaot absolute value of y is :",fabs(y))
# from cmath import pi
# import math
# print(math.fabs(pi))

# Output:      
            # The flaot absolute value of x is : 12.234
            # The flaot absolute value of y is : 19.0
            # 3.141592653589793

#***************** Exercise 5: Number log() method is used to return the natural logarithm of x,"ln(x)". for x>0
# from cmath import e, log, sqrt
# import math
# a = log(2)
# b = log(2*3)
# c = log(sqrt(4))
# d = log(e**2)
# print("The natural logarithm of 2 is :",a)
# print("The natural logarithm of 2x3 is :",b)
# print("The natural logarithm of sqrt(4) is :",c)
# print("The natural logarithm of e^2 is :",d)

# print("The natural logarithm of 2 is :",math.log(2))
# print("The natural logarithm of 2x3 is :",math.log(2*3))
# print("The natural logarithm of sqrt(4) is :",math.log(2/3))
# print("The natural logarithm of e^2 is :",math.log(e**2))

# Output:
            # The natural logarithm of 2 is : (0.6931471805599453+0j)
            # The natural logarithm of 2x3 is : (1.791759469228055+0j)
            # The natural logarithm of sqrt(4) is : (0.6931471805599453+0j)
            # The natural logarithm of e^2 is : (2+0j)
            # The natural logarithm of 2 is : 0.6931471805599453
            # The natural logarithm of 2x3 is : 1.791759469228055
            # The natural logarithm of sqrt(4) is : -0.40546510810816444
            # The natural logarithm of e^2 is : 2.0

#***************** Exercise 6: Number log10() method is used to return the base-10 logarithm of x for x>0:
# from cmath import log10
# x = log10(100)
# y = log10(200)
# z = log10(1/2)
# u = log10(17%3)
# v = log10(x+y+z)
# w = log10(x*y - (z/(2*u)) + v**100)
#
# print("The base-10 logarithm of 100 is :",x)
# print("The base-10 logarithm of 200 is :",y)
# print("The base-10 logarithm of 1/2 is :",z)
# print("The base-10 logarithm of 5%2 is :",u)
# print("The base-10 logarithm of x+y+z is :",v)
# print("The base-10 logarithm of x*y-z/u+v is :",w)

# Output:
            # The base-10 logarithm of 100 is : (2+0j)
            # The base-10 logarithm of 200 is : (2.301029995663981+0j)
            # The base-10 logarithm of 1/2 is : (-0.30102999566398114+0j)
            # The base-10 logarithm of 5%2 is : (0.30102999566398114+0j)
            # The base-10 logarithm of x+y+z is : (0.6020599913279623+0j)
            # The base-10 logarithm of x*y-z/u+v is : (0.7077455608495299+0j)

#*************** Exercise 7: Number max() and min() methods are used to find the maximum value and minimum value.
# a = max(1,3.13,56,87,99.879,54,82)
# b = min(1,3.13,56,87,99.879,54,82)
# c = max(80,100,1000)
# d = min(80,100,1000)
# e = max(-80,-20,-10)
# f = min(e,3,4,5,6,9)
# g = max(a,b,c,d,e,f)
# h = min(g+e,f+d,e-c,a+b,b**2,c%d,2)

# print("The maximum number in this list = (1,3.13,56,87,99.879,54,82) is :",a)
# print("The minimum number in this list = (1,3.13,56,87,99.879,54,82) is :",b)
# print("The maximum number in this list = (80,100,1000) is :",c)
# print("The minimum number in this list = (80,100,1000) is :",d)
# print("The maximum number in this list = (-80,-20,-10) is :",e)
# print("The minimum number in this list = (e,3,4,5,6,9) is :",f)
# print("The maximum number in this list = (a,b,c,d,e,f) is :",g)
# print("The minimum number in this list = (g+e,f+d,e-c,a+b,b**2,c modulus d,2) is :",h)

# Output:
            # The maximum number in this list = (1,3.13,56,87,99.879,54,82) is : 99.879
            # The minimum number in this list = (1,3.13,56,87,99.879,54,82) is : 1
            # The maximum number in this list = (80,100,1000) is : 1000
            # The minimum number in this list = (80,100,1000) is : 80
            # The maximum number in this list = (-80,-20,-10) is : -10
            # The minimum number in this list = (e,3,4,5,6,9) is : -10
            # The maximum number in this list = (a,b,c,d,e,f) is : 1000
            # The minimum number in this list = (g+e,f+d,e-c,a+b,b**2,c modulus d,2) is : -1010

#**************** Exercise 8: Number modf() method is used to return the fractional and integer parts of x in a two-
# item tupple. Both parts have the same as x. The integer part is returned as a float.
# import math
# print("math.modf(100.12) : ",math.modf(100.12))
# print("math.modf(199.345 : ",math.modf(199.345))
# print("math.modf(199)    : ",math.modf(199))
# print("math.modf(pi)     : ",math.modf(math.pi))

# math.modf(x) is used to check and mention the fraction and integer that break as two items such that output below.
# Output:
        # math.modf(100.12) :  (0.12000000000000455, 100.0)
        # math.modf(199.345 :  (0.34499999999999886, 199.0)
        # math.modf(199)    :  (0.0, 199.0)
        # math.modf(pi)     :  (0.14159265358979312, 3.0)

#****************** Exercise 9: Number sqrt() and pow() is used to return the square root of x and power of x by a.
# from cmath import sqrt
# import math
# a = sqrt(24/4 + 8%5)
# b = pow(3,2)
# c = sqrt(a*5)
# d = sqrt(b-2+c*a)
# e = pow(c,d)
# f = pow(c**2,d+2*a-20)
# g = pow(8,1/3)
# h = pow(90,5/3)

# print("The square root of (24/4 +8%5) is :",a)
# print("The power of 3^2 is :",b)
# print("The sqare root of a*5 is :",c)
# print("The square root of (b-2+c*a) is :",d)
# print("The power of c by d is: ",e)
# print("The power of c**2 by d+2*a-20 is :",f)
# print("The cube root of 8 is :",g)
# print("The cube root of 90^5 is :",h)

# Output:
            # The square root of (24/4 +8%5) is : (3+0j)
            # The power of 3^2 is : 9
            # The sqare root of a*5 is : (3.872983346207417+0j)
            # The square root of (b-2+c*a) is : (4.314968138772551+0j)
            # The power of c by d is:  (344.66577107771+0j)
            # The power of c**2 by d+2*a-20 is : (4.069290404438062e-12-0j)
            # The cube root of 8 is : 2.0
            # The cube root of 90^5 is : 1807.4689652218583

#***************** Exercise 10: round() method is used to round up and round down the fractional number. There are two
# cases of round method such that: 
# (1): round(a,b) : mean that a will round up or down that depend on b digits and display as form a.(.....) where 
#      #b = (.....) is the number of digits that stay after fraction.
# (2): round(a): mean that a will round up or round down depend on mathematical theorem for the fractional afterward.  
# a = round(70.23456)
# b = round(56.659,1)
# c = round(80.264,2)
# d = round(100.000056,3)
# e = round(-100.000056,3)

# print("The round of a is :",a)
# print("The round of b is :",b)
# print("The round of c is :",c)
# print("The round of d is :",d)
# print("The round of e is :",e)

# Output:
        # The round of a is : 70
        # The round of b is : 56.7
        # The round of c is : 80.26
        # The round of d is : 100.0
        # The round of e is : -100.0

#====================================================================================================================================
#================================================ Part 02: Random Number Function ===================================================
# (1): choice(seq)    : is used to return a random item from a list, tupple or string
# (2): randrange([start,] stop [,step]) : A randomly selected element from range(start,stop,step).
# (3): random()       : a random float r, such that 0 is less than or equal to r and r is less than 1. (0 <= r < 1)
# (4): seed([x])      : Sets the integer starting value used in generating random numbers. Call this function before 
#                       calling any other random module function. Returns None.
# (5): shuffle(lst)   : randomize the items of a list in place. Returns None.
# (6): uniform(x,y)   : a random float r, such that x is less than or equal to r and r is less than y. (x<=r<=y)

#***************** Exercise 11: choice(seq)    : is used to return a random item from a list, tupple or string. it is
# different from one to one depend on running beacause of random selected without particular destination. 
# import random
# print("Return a random number from range(100) : ",random.choice(range(100)))
# print("Return a random element from list [1,2,3,5,9] : ",random.choice([1,2,3,5,9]))
# print("Return a random character from a string 'Hello World' : ",random.choice("Hello World"))

# Output:
#               1(st)
# Return a random number from range(100) :  90
# Return a random element from list [1,2,3,5,9] :  5
# Return a random character from a string 'Hello World' :  d
#               2(nd)
# Return a random number from range(100) :  10
# Return a random element from list [1,2,3,5,9] :  2
# Return a random character from a string 'Hello World' :  o
#               3(rd)
# Return a random number from range(100) :  18
# Return a random element from list [1,2,3,5,9] :  1
# Return a random character from a string 'Hello World' :  r

#***************** Exercise 12: randrange([start,] stop [,step]) : is used to return a randomly selected element from 
# range(start,stop,step).
# start : start point of the range.
# step  : value with number that is increment.
# stop  : stop point of the range. 
# import random
# # A randomly selected an odd number between 1-100:
# print("Randrange(1,100,2) : ",random.randrange(1,100,2))
# # A randomly selected a number between 0-99
# print("Randomrange(100) : ",random.randrange(100))
# print("Randomrange(-2,23,7) : ",random.randrange(-2,23,7))

# Output:
#       1(st)
# Randrange(1,100,2) :  23
# Randomrange(100) :  93
# Randomrange(-2,23,7) :  -2
#       2(nd)
# Randrange(1,100,2) :  5
# Randomrange(100) :  22
# Randomrange(-2,23,7) :  5
#       3(rd)
# Randrange(1,100,2) :  85
# Randomrange(100) :  76
# Randomrange(-2,23,7) :  -2

#***************** Exercise 13: random() is used to return the a random floating point number in the range[0.0,1.0]
# import random
# # First random number: 
# print("random() 1(st): ",random.random())
# # Second random number:
# print("random() 2(nd) : ",random.random())
# # Third random number: 
# print("random() 3(rd) : ",random.random())

# Output:
        # random() 1(st):  0.6890253721578521
        # random() 2(nd) :  0.5653791864869704
        # random() 3(rd) :  0.3097740339403252
# It randomly selected on interval 0 <= r <= 1

#***************** Exercise 14: seed([x],[y]) : Sets the integer starting value used in generating random numbers. 
# We call this function before calling any other random module function. Returns None. " seed([x],[y]) "
# x     : is the seed for the next random number. If we omitted, then it takes system time to generte the next random
#         number. if x is an integer, it is used directly.
# y     : is the version number (default is 2). str, byte or byte array object gets converted in int. Version 1 used 
# hash() of x.
# import random

# random.seed()
# print("random number with default seed",random.random())

# random.seed(10)
# print("random number with int seed",random.random())

# random.seed("hello",2)
# print("random number with string seed",random.random())

# Output: 
#                       1(st) If "hello"
        # random number with default seed 0.9852112830009181
        # random number with int seed 0.5714025946899135
        # random number with string seed 0.3537754404730722
#                       2(nd) If "Hello"
        # random number with default seed 0.025644021302407394
        # random number with int seed 0.5714025946899135
        # random number with string seed 0.009708374518246354

#***************** Exercise 15: shuffle() is used to randomize the items of a list in place.
# shuffle(lst,[random])
# lst    : it could be a list or tuple.
# random : this is an optional 0 argument function returning float between 0.0 to 1.0. Default is None.
# import random
# list = [20,16,10,5];

# random.shuffle(list)
# print("Reshuffle list : ",list)

# random.shuffle(list)
# print("Reshuffle list : ",list)

# Output:
#                      1(st)
        # Reshuffle list :  [16, 10, 20, 5]
        # Reshuffle list :  [5, 10, 20, 16]
#                      2(nd)
        # Reshuffle list :  [16, 20, 10, 5]
        # Reshuffle list :  [5, 16, 20, 10]
#                       3(rd)
        # Reshuffle list :  [5, 20, 10, 16]
        # Reshuffle list :  [16, 20, 5, 10]

#***************** Exercise 16: uniform() is used to return a random float r, such that x is less than or equal to r
# and r is less than y. (x <= r <= y)
# uniform(x,y) : where x is the sets lower limit of the random float and y is the sets upper limit of the random float.
# import random
# print("Random float uniform(5,2) : ",random.uniform(5,2))
# print("Random float uniform(7,14) : ",random.uniform(7,14))

# Output:
#                       1(st)
        # Random float uniform(5,2) :  3.0004418617462365
        # Random float uniform(7,14) :  10.71673123001669
#                        2(nd)
        # Random float uniform(5,2) :  4.769669404215465
        # Random float uniform(7,14) :  10.507665782157327

#====================================================================================================================================
#============================================ Part 03: Trigonometric Function =======================================================
# (1)   acos(x)   : return the arccosine of x, in radians
# (2)   asin(x)   : return the arcsine of x, in radians.
# (3)   atan(x)   : return the arctangent of x, in radians.
# (4)   atan2(x,y): return the arctangent of y/x, in radians.
# (5)   cos(x)    : return the cosine of x, in radians.
# (6)   hypot(x,y): return the Euclidean norm, sqrt(x^2 + y^2)
# (7)   sin(x)    : return the sine of x, in radians.
# (8)   tan(x)    : return the tangent of x, in radians.
# (9)   degrees(x): converts angle x from radians to degrees.
# (10)  radians(x): converts angle x from degrees to radians.
# (11)  atanh(x), asinh(x), acosh(x) are the hyperbolic function.

#***************** Exercise 17: The inverse function of trigonometric function acos(x), asin(x) and atan(x) where x 
# as in radians
# from cmath import acos, asin, sqrt, atan
# import math
# print("arccos(0.64) is :",acos(0.64))
# a = math.acos(0.34)
# b = math.acos(1)
# c = math.asin(0.45)
# d = math.asin(1)
# e = acos((sqrt(2))/2)
# f = acos((sqrt(3))/2)
# g = asin((sqrt(2))/2)
# h = atan((sqrt(3)/3))
# i = math.atan(1)
# j = math.atan2(0.34,0.3)
# print("The arctan2(0.34,0.3) or arctan(0.34/0.3) is : ",j)
# print("The arcos(0.34) is : ",a)
# print("The arcos(1) is : ",b)
# print("The arcsin(0.45) is : ",c)
# print("The arcsin(1) is : ",d)
# print("The arcos(sqrt(2)/2) is : ",e)
# print("The arcos(sqrt(3)/2) is : ",f)
# print("The arcsin(sqrt(2)/2) is : ",g)
# print("The arctan(sqrt(3)/3) is : ",h)
# print("The atan(1) is : ",i)

# Output:
        # The arctan2(0.34,0.3) or arctan(0.34/0.3) is :  0.8478169733934057
        # arccos(0.64) is : (0.8762980611683405-0j)
        # The arcos(0.34) is :  1.2238794292677349
        # The arcos(1) is :  0.0
        # The arcsin(0.45) is :  0.4667653390472964
        # The arcsin(1) is :  1.5707963267948966
        # The arcos(sqrt(2)/2) is :  (0.7853981633974482-0j)
        # The arcos(sqrt(3)/2) is :  (0.5235987755982989-0j)
        # The arcsin(sqrt(2)/2) is :  (0.7853981633974484+0j)
        # The arctan(sqrt(3)/3) is :  (0.5235987755982988+0j)
        # The atan(1) is :  0.7853981633974483

#***************** Exercise 18: The inverse function of hyperbolic acosh(x), asinh(x) and atanh(x).
# from cmath import acosh, asinh, atanh
# a = atanh(2)
# b = atanh(3)
# c = asinh(6)
# d = acosh(7)
# e = asinh(1) + acosh(1)
# f = atanh(3*c-4*a)
# g = 1/atanh(3*c-4*a)
# print("arctanh(2) is : ",a)
# print("arctanh(3) is : ",b)
# print("arcsinh(6) is : ",c)
# print("arcosh(7) : ",d)
# print("arcsinh(1) + arccosh(1) : ",e)
# print("arctanh(3*c-4*c) =",f)
# print("arccoth(3*c-4*c) =",g)

# Output:
        # arctanh(2) is :  (0.5493061443340549+1.5707963267948966j)
        # arctanh(3) is :  (0.34657359027997264+1.5707963267948966j)
        # arcsinh(6) is :  (2.491779852644912+0j)
        # arcosh(7) :  (2.6339157938496336+0j)
        # arcsinh(1) + arccosh(1) :  (0.8813735870195429+0j)
        # arctanh(3*c-4*c) = (0.07785994721743644-1.477189224463233j)
        # arccoth(3*c-4*c) = (0.03558254276259765+0.6750858512801606j)

#***************** Exercise 19: The trigonometric function and hyperbolic function such that: 
# sin(x), cos(x), tan(x), cot(x), sec(x), cosec(x) where (0 <= x<= 2*pi)
# sinh(x), cosh(x), tanh(x) and coth(x), where x is the real number.
# from cmath import cos, cosh, pi, sin, sinh, sqrt, tan, tanh
# import math
# a = math.sin(pi/2)
# b = math.cos(-pi/2)
# c = math.tan(pi/4)
# d = math.sin(pi/5)
# e = sin(3.14)
# f = cos(pi/6)
# g = tan(2*pi)
# h = cosh(pi/a)
# i = math.sinh(a+b+c)
# j = tanh(a**2+b**2)
# k = math.cosh(pow(a,b))
# l = 1/a
# m = 1/b
# n = 1/g
# o = 1/j
# print("a = sin(pi/2) = ",a)
# print("b = cos(-pi/2) = ",b)
# print("c = tan(pi/4) = ",c)
# print("d = sin(pi/5) = ",d)
# print("e = sin(3.14) = ",e)
# print("f = cos(pi/6) = ",f)
# print("g = tan(2*pi) = ",g) 
# print("h = cosh(pi/a) = ",h)
# print("i = sinh(a+b+c) = ",i)
# print("j = tanh(a**2+b**2) = ",j)
# print("k = cosh(pow(a,b)+sqrt(j)) = ",k)
# print("l = cosec(pi/2) = ",l)
# print("m = sec(-pi/2) = ",m)
# print("n = cot(pi/4) = ",n)
# print("o = coth(a**2+b**2) = ",o)

# Output:
        # a = sin(pi/2) =  1.0
        # b = cos(-pi/2) =  6.123233995736766e-17
        # c = tan(pi/4) =  0.9999999999999999
        # d = sin(pi/5) =  0.5877852522924731
        # e = sin(3.14) =  (0.0015926529164868282-0j)     
        # f = cos(pi/6) =  (0.8660254037844387-0j)        
        # g = tan(2*pi) =  (-2.4492935982947064e-16+0j)   
        # h = cosh(pi/a) =  (11.591953275521519+0j)       
        # i = sinh(a+b+c) =  3.6268604078470186
        # j = tanh(a**2+b**2) =  (0.7615941559557649+0j)  
        # k = cosh(pow(a,b)+sqrt(j)) =  1.5430806348152437
        # l = cosec(pi/2) =  1.0
        # m = sec(-pi/2) =  1.633123935319537e+16
        # n = cot(pi/4) =  (-4082809838298842.5-0j)       
        # o = coth(a**2+b**2) =  (1.3130352854993315+0j) 

#***************** Exercise 20: hypot(x,y) Vs degrees(x) Vs radians(x)
# (1)   hypot(x,y): return the Euclidean norm, sqrt(x^2 + y^2)
# (2)   degrees(x): converts angle x from radians to degrees.
# (3)   radians(x): converts angle x from degrees to radians.
# from cmath import pi
# from math import degrees, hypot, radians
# a = hypot(2,3)
# b = degrees(pi)
# c = radians(180)
# d = hypot(a,b)
# e = degrees(pi/6)
# f = degrees(pi/12)
# g = radians(15)
# h = radians(270)
# print("a = hypot(2,3) = ",a)
# print("b = degrees(pi) = ",b)
# print("c = radians(180) = ",c)
# print("d = hypot(a,b) = ",d)
# print("e = degrees(pi/6) = ",e)
# print("f = degrees(pi/12) = ",f)
# print("g = radians(15) = ",g)
# print("h = radians(270) = ",h)
# Output:
        # a = hypot(2,3) =  3.6055512754639896
        # b = degrees(pi) =  180.0
        # c = radians(180) =  3.141592653589793
        # d = hypot(a,b) =  180.0361074895811
        # e = degrees(pi/6) =  29.999999999999996
        # f = degrees(pi/12) =  14.999999999999998
        # g = radians(15) =  0.2617993877991494
        # h = radians(270) =  4.71238898038469

#====================================================================================================================================
# print(234)
# print(2.334)
# print(-334)
# print(1+2)
# print(2*4)
# print(2/3)
# print(4-2)
# print(1*2 + 2*3 + 3/4 + 4-2 + 5*8)
# # Output : 
#                 # 234
#                 # 2.334
#                 # -334
#                 # 3
#                 # 8
#                 # 0.6666666666666666
#                 # 2
#                 # 50.75
# print((1+3) + 3*5*(9-3)/4-23)
# print((2*3/(5/3)-20/3))
# print(10%3)
# print(22%3*32-21)
# # Output : 
#                 # 3.5
#                 # -3.0666666666666673
#                 # 1
#                 # 11
# num = 5
# print(num)      # 5
# print(str(num)) # 5
# print(str(num)+" is my favorite number") # 5 is my favorite number
# #print(num+" my favorite number")   # error . Because number cannot use arithmetic with string.
# x = -9
# print(abs(x))                  # 9. Because absolute value return the positive number.
# print(pow(x,2))                # 81 The power of x
# print(max(2,x))                # 2  The maximum number was displayed.
# print(min(x,19))               # -9 The minimum number was displayed. 
# print(max(x,1,5,3,8,9,56,43))  # 56 
# print(min(1,x,5,8,6,9,0,23))   # -9
# from math import sqrt
# print(sqrt(100))               # 10
# print(sqrt(x+30*100/3))        # 31.480152477394387
# print(round(3.7))              # 4  roundup based on arithmetic math rule.
# print(round(3.2))              # 3  rounddown based on arithmetic math rule.
# # The above arithmetic operatoin, we cannot set as we want that roundup or rounddown are depend on math rule.
# # if we want to roundup or rounddown, please input the library math  
# from math import *
# print(floor(3.7))  # 3  round down the number.
# print(ceil(3.7))   # 4  round up the number.

#==================================================== More additional exercises =====================================================
#***************** Exercise 21: Write a program that generates and prints 50 random integers, each between 3 and 6
# result = []
# for i in range(1,50):
#     if i%3==0 and i%6==0 :
#         result.append(i)
# print(result)


# #***************** Exercise 22: Write a program that generate a random number, x, between 1 and 50, a random number y
# # between 2 and 5, and then compute x^y
# i = []
# for x in range(1,50):
#     i.append(x)
# print(i)




#****************** Exercise 23: Write a program that generates a random decimal number between 1 and 10 and print your
# name that many times.






#****************** Exercise 24: Write a program that generate a random decimal number between 1 and 10 with two decimal
# places of accuracy. Examples are 1.23, 3.45, 9.80 and 5.00






#******************* Exercise 25: Write a program that generate 50 random numbers such that the first number is between
# 1 and 2, the second is between 1 and 3, the third is between 1 and 4,....,and the last is between 1 and 51.






#******************** Exercise 26: Write a program that ask the user to enter two numbers x and y and computes 
# |x-y|/(x+y)




#******************** Exercise 27: Write a program that ask the user to enter an angle between -180 degrees and 180 
# degrees. Using an expression with the modulo operator, convert the angle to its equivalent between 0 degree and 
# 360 degrees.






