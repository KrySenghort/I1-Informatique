#=====================================================================================================================================
#==================================================== Chapter 03: Basic Operators ===================================================
#=====================================================================================================================================
#******************* Arithmetic operators: 
# a = 21
# b = 10
# # Summation 
# c = a+b
# print("The summation between a and b is a+b = ",c)
# # Substraction
# c = a-b
# print("The substraction between a and b is a-b = ",c)
# # Multiplication
# c = a*b
# print("The multiplication between a and b is axb = ",c)
# # Division
# c = a/b
# print("The division between a and b is a៖b = ",c)
# # Division (result as integer)
# c = a//b
# print("The division between a and b as integer result is a//b = ",c)
# # Power of number
# c = a**b
# print("The power between a and b is power(a,b) = ",c)
# # Remainder of number
# c = a%b
# print("The remainder after division between a and b is a mod b = ",c)
# # Square of number
# from cmath import sqrt
# A = sqrt(a)
# B = sqrt(b)
# C = sqrt(a**2 + b**2)
# print("the square of a is : ",A)
# print("the square of b is : ",B)
# print("the square of a^2 + b^2 = ",C)
# Output:
        # The summation between a and b is a+b = 31
        # The substraction between a and b is a-b = 11
        # The multiplication between a and b is axb = 210
        # The division between a and b is a៖b = 2.1
        # The division between a and b as integer result is a//b = 2 
        # The power between a and b is power(a,b) = 16679880978201   
        # The remainder after division between a and b is a mod b = 1
        # the square of a is :  (4.58257569495584+0j)
        # the square of b is :  (3.1622776601683795+0j)
        # the square of a^2 + b^2 = (23.259406699226016+0j)
#******************** Comparision Operators:
# x = 34
# y = 56

# # == mean that equal 
# if(x==y):
#     print("x is equal y")
# else:
#     print("x is not equal y")

# # =! mean that not equal
# if(x!=y):
#     print("x is not equal y")
# else:
#     print("x is equal y")

# # > mean that greater than
# if(x>y):
#     print("x is greater than y")
# else:
#     print("x is smaller than y")

# # < mean that smaller than
# if(x<y):
#     print("x is smaller than y")
# else:
#     print("x is greater than y")

# # <= mean that either less than or equal
# if(x<=y):
#     print("x is either less than or equal y")
# else:
#     print("x is neither less than nor equal y")

# # >= mean that neither than nor equal 
# if(x>=y):
#     print("x is either greater than or equal y")
# else:
#     print("x is neither greater than nor equal y")
# Output:
            # x is not equal y
            # x is not equal y
            # x is smaller than y
            # x is smaller than y
            # x is either less than or equal y
            # x is neither greater than nor equal y
#********************* Assignment Operators:
# = mean equal
# a = 5
# b = 9
# c = a+b
# print("The value c is : ",c)
# # += mean summation and (c+=a <=> c=c+a) 
# c+=a
# print("The increasement of c when add a is : ",c)
# # -= mean substraction and (c-=a <=> c=c-a)
# c-=a
# print("The decreasement of c when minus a is : ",c)
# # *= mean that multiplication and (c*=b <=> c=c*b)
# c*=b
# print("The multiplication between c and b is : ",c)
# # /= mean that division and (c/=b <=> c=c/b)
# c/=b
# print("The division between c and b is : ",c)
# # %= mean that modulus and (c%=b <=> c=c%b)
# c%=b
# print("The remainder after c divide b is : ",c)
# # **= mean that power and (c**=a <=> c=power(c,a))
# c**=a
# print("The power of c with a is : ",c)
# # //= mean that division(integer result) and (c//=a <=> c=c//a)
# c//a
# print("The division(integer result) between c and a is : ",c)
# Output:
            # The value c is :  14
            # The increasement of c when add a is :  19
            # The decreasement of c when minus a is :  14
            # The multiplication between c and b is :  126
            # The division between c and b is :  14.0
            # The remainder after c divide b is :  5.0
            # The power of c with a is :  3125.0
            # The division(integer result) between c and a is :  3125.0
#********************** Bitwise Operators:
# a = 60          # 60 = 0011 1100
# b = 13          # 13 = 0000 1101
# print('a = ',a,':',bin(a),'\nb = ',b,':',bin(b))
# c = 0

# c = a&b         # 12 = 0000 1100
# print("Result of AND is ",c,':',bin(c))

# c = a|b         # 61 = 0011 1101
# print("Result of OR is ",c,":",bin(c))

# c = a^b         # 49 = 0011 0001
# print("Result of EXOR is ",c,":",bin(c))

# c = ~a          # -61 = 1100 0011
# print("Result of complement is ",c,':',bin(c))

# c = a<<2        # 240 = 1111 0000
# print("Result of left shift is ",c,":",bin(c))

# c = a>>2        # 15 = 0000 1111
# print("Result of right shift is ",c,":",bin(c))
# Output:
        # a =  60 : 0b111100 
        # b =  13 : 0b1101
        # Result of AND is  12 : 0b1100
        # Result of OR is  61 : 0b111101
        # Result of EXOR is  49 : 0b110001
        # Result of complement is  -61 : -0b111101 
        # Result of left shift is  240 : 0b11110000
        # Result of right shift is  15 : 0b1111  
#************************ Logical Operators:
# AND logical operator
# x = 5
# print(x>3 and x<10)

# # OR logical operator
# y = 12 
# print(y<20 or y<11)

# # NOT logical operator
# z = 30
# print(not(z<3))
# print(not(z>=30 and z<50))
# Output:
        # True
        # True
        # True
        # False
#************************* Membership Operators:
# a = 10
# b = 20
# c = 3
# d = 7
# list = [1,2,3,4,5]
# if(a in list):
#         print("a is available in the given list")
# else:
#         print("a is invalid in the given list")

# if(b not in list):
#         print("b is not available in the given list")
# else:
#         print("b is available in the given list")

# if(c in list):
#         print("c is available in the given list")
# else:
#         print("c is invalid in the given list")

# if(d not in list):
#         print("d is available in the given list")
# else:
#         print("d in available in the given list")

# e = b/a+8
# if(e in list):
#         print("e is available in the given list")
# else:
#         print("e is unavailable in the given list")
# Output:
                # a is invalid in the given list
                # b is not available in the given list
                # c is available in the given list
                # d is available in the given list
                # e is unavailable in the given list
#************************* Identity Operators: focus on memory location
# a = 20
# b = 20
# print('a = ',a,":",id(a),'\nb = ',b,":",id(b))

# if(a is b):
#         print("a and b have the same identity.")
# else:
#         print("a and b has no the same identity.")

# if(id(a)==id(b)):
#         print("a and b have the same identity.")
# else:
#         print("a and b do not have the same identity.")
# b = 30
# print("a = ",a,":",id(a),"\nb = ",b,":",id(b))

# if(a is not b):
#         print("a and b does not have the same identity")
# else:
#         print("a and b have the same identity.")
# Output:
        # a =  20 : 2995206515600 
        # b =  20 : 2995206515600
        # a and b have the same identity.        
        # a and b have the same identity.        
        # a =  20 : 2995206515600
        # b =  30 : 2995206515920
        # a and b does not have the same identity




