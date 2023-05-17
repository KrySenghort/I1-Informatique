#=====================================================================================================================================
#==================================================== Chapter 05: Loop ==============================================================
#=====================================================================================================================================

#**************** Exercise 01: Exercise 01 For loop 01:
# for i in range(1,10):
#         print("\t",i,end="")
# print("\n")

# for j in range(1,10):
#         print("Hello Wold#",j,end="")
# print("\n")

# for i in range(1,100):
#         print("\t",i,end="")
# print("\n")

# for j in range(2,100):
#         print("\t",j,end="")
# print("\n")

# for k in range(7,100):
#         print("Hello World#",k,end="")


x = -281
y = 1452
print(x%y)

#***************** Exercise 02: Nested for loop 02:
# for i in range(3):
#         for j in range(4):
#                 print('A'+'B',end="")
#         print(end=" ")
# end="" is used to ផ្ដាច់ដាក់ជាជួរដេក
# Output: 
                # ABABABAB ABABABAB ABABABAB 

#***************** Exercise 03: Nested Loop 03:
# for i in range(0,10):
#         for j in range(0,10-i):
#                 print(" ",end="")
#         for k in range(0,i):
#                 print("*",end="")
#         print("")
# Output: 
                #          *
                #         **
                #        ***
                #       ****
                #      *****
                #     ******
                #    *******
                #   ********
                #  *********

#***************** Exercise 04: Nested Loop 04:
# for i in range(0,10):
#         for j in range(10):
#                 print(" ",end="")
#         for k in range(i):
#                 print("*",end="")
#         print("") 
# we can input space in the middle of this double quotes. but we cannot comment on this line because it help to cut and remove the 
# string in the order.
# Output:
                        #   *        
                        #   **       
                        #   ***      
                        #   ****     
                        #   *****    
                        #   ******   
                        #   *******  
                        #   ******** 
                        #   *********

#***************** Exercise 05: Nested for loop 05:
# for i in range(0,10):
#         for j in range(0,10-i):
#                 print(" ",end="")
#         for k in range(0,2*i+1):
#                 print("*",end="")
#         print("")
# print(end="")
#print(end="")
# Output:
                #           *
                #          ***        
                #         *****       
                #        *******      
                #       *********     
                #      ***********    
                #     *************   
                #    ***************  
                #   ***************** 
                #  *******************

#***************** Exercise 06: Nested Loop 06:
# for l in range(-10,1):
#         for m in range(l+10):
#                 print(" ",end="")
#         for n in range(1-2*l):
#                 print("*",end="")
#         print("")
# print(end="")
# for z in range(5):
#         for i in range(-10,1):
#                 for j in range(i+10):
#                         print(" ",end="")
#                 for k in range(1-2*i):
#                         print("*",end="")
#                 print("")
#         print(end="")

# for l in range(-10,1):
#         for m in range(l+10):
#                 print(" ",end="")
#         for n in range(1-2*l):
#                 print("*",end="")
#         print("")
# print(end="")
# Output: 
                        # *********************
                        #  *******************
                        #   *****************
                        #    ***************
                        #     *************
                        #      ***********
                        #       *********
                        #        *******
                        #         *****
                        #          ***
                        #           *

#***************** Exercise 07: Nested Loop 07:
# for l in range(-10,1):
#         for m in range(l+10):
#                 print(" ",end="")
#         for n in range(1-l):
#                 print("*",end="")
#         print("")
# Output:
                        # ***********
                        #  **********
                        #   *********
                        #    ********
                        #     *******
                        #      ******
                        #       *****
                        #        ****
                        #         ***
                        #          **
                        #           *

#***************** Exercise 08: Nested Loop 08:
# for l in range(-10,1):
#         for m in range(l):
#                 print(" ",end="")
#         for n in range(1-l):
#                 print("*",end="")
#         print("")
# Output:
                                        # ***********
                                        # **********
                                        # *********
                                        # ********
                                        # *******
                                        # ******
                                        # *****
                                        # ****
                                        # ***
                                        # **
                                        # *

#****************** Exercise 09: Keyword "pass":
# pass is just a placeholder for functionality to be added later.
# for i in range(0,10):
#         print("Hello world")
# sequence = {'p', 'a', 's', 's'}
# for val in sequence:
#         pass
# The keyword pass is used as a placeholder for future code. it is used to hide the error of the code that is wrong 
# syntax without no result. but for right code it will display the output.

#****************** Exercise 10: Keyword "continue":
# print("The odd number which are between 1 until 100 are such that: ")
# for i in range(1,100):
#         if(i%2==0):
#                 print(i,end=" ")
#         else:
#                 continue
# print("\nThe even number which are between 1 until 100 are such that: ")
# for j in range(1,100):
#         if(j%2!=0):
#                 print(j,end=",")
#         else:
#                 continue
# #Keyword "continue" is used to over or hide the data that does not follow the condition.

# #****************** Exercise 11: Keyword "break":
# name = input("Enter your name: ")
# for a in range(1,100):
#         if(name =="S e n g h o r t"):
# #               print(name,end="",a)
#                 print(name.replace(" ",""),a)      # is used to cut the space of the string.
#         else:
#                 print("Invalid")
#                 break
# #keyword "break" is used to stop the running of the code. Output has only once time when we put break.
# #if we don't put break so it will display the Invalid for 100 times.

# #****************** Exercise 12: While loop 01
# x=0
# while x<9:
#         print("The number are such following: ",x)
#         x+=1
# print("Good bye")

#****************** Exercise 13: While loop 02
# Increasement of order word
# i=0
# while i<100:
#         print("Hello World",i)
#         i+=1
# # Decreasement of order word
# j=100
# while j>0:
#         print("Cat",j,end=",")
#         j-=1
# # Comparision with string.
# name = input("\nEnter your name: ")
# while name=="Senghort":
#         for k in range(1,100):
#                 print("Dara")
# Infinite loop because the string has no comparison condition.
# flag=1
# while(flag):
#         print("Given flag is really true!")
# print("Goodbye!")
# It will display infinite loop.

#****************** Exercise 14: write a program that prints your name for 100 times.
# for k in range(100):
#         print("Senghort",k)

#****************** Exercise 15: Write a program to fill the screen horizontally and vertically with your name.
# [Hint: add the option end="" into the print function to fill the screen horizontal.]
# for k in range(10):
#         print("Senghort",k,end=",")
# print("\n")
# for k in range(10,20):
#         print("Senghort",k,end=",")
# print("\n")
# for k in range(20,30):
#         print("Senghort",k,end=",")
# print("\n")
# for k in range(30,40):
#         print("Senghort",k,end=",")
# print("\n")
# for k in range(40,50):
#         print("Senghort",k,end=",")
# print("\n")
# for k in range(50,60):
#         print("Senghort",k,end=",")
# print("\n")
# for k in range(60,70):
#         print("Senghort",k,end=",")
# print("\n")
# for k in range(70,80):
#         print("Senghort",k,end=",")
# print("\n")
# for k in range(80,90):
#         print("Senghort",k,end=",")    
# print("\n")
# for k in range(90,100):
#         print("Senghort",k,end=",")
# print("\n")

#****************** Exercise 16: Write a program that outputs 100 lines, numbered 1 to 100, each with your name on it.
# i = 1
# while i<=100:
#         print(i,"\tSenghort")
#         i+=1

#****************** Exercise 17: Write a program to print out of a list of the integers from 1 to 20 and their squares.
# for i in range(1,21):
#         print(i,"---",i**2)

#****************** Exercise 18: Write a program to print the number 8,11,14,17,20,...,83,86,89.
# for i in range(1,29):
#         print(3*i+5,end=",")

#****************** Exercise 19: Write a program that use a for loop to print the numbers 100,98,96,...,4,2
# for i in range(-50,0):
#         print(-i*2)

#****************** Exercise 20: Write a program that use exactly four for loops to print the sequence of the letters
# below.
# AAAAAAAAAABBBBBBBCDCDCDCDEFFFFFFG
# for i in range(10):    
#         print("A",end="")
# print(end="")
# for j in range(7):
#         print("B",end="")
# print(end="")
# for k in range(4):
#         print("CD",end="")
# print(end="")
# for l in range(1):
#         print("E",end="")
# print(end="")
# for m in range(6):
#         print("F",end="")
# print(end="")
# for n in range(1):
#         print("G",end="")
# print(end="")
# Output:
        # AAAAAAAAAABBBBBBBCDCDCDCDEFFFFFFG

#******************** Exercise 21: Write a program to display the fibonacci sequence that is finish with specific 
# number which specified by user.
# num = int(input("Enter number: "))
# n1,n2 = 0,1
# sum = 0
# if num<0:
#         print("Please enter number greater than 0.")
# else:
#         for i in range(num):
#                 n1=n2
#                 n2=sum
#                 sum=n1+n2
#                 print(sum,end=",")
#         print(end="")                                
#===============================================
# while(2>0):
#         x = int(input("Enter number: "))
#         n1,n2 = 0,1
#         sum = 0
#         if x<0:
#                 print("Enter the positive number")
#         else:
#                 for i in range(x):
#                         n1=n2
#                         n2 = sum
#                         sum = n1+n2
#                         print(sum,end=", ")
#         print("\nDo you want to continue or not ?")
#         option=input("Enter your option: ")
#         if option =="N" or "n" or "no" or "No" or "NO" or "nO":
#                 break

#********************* Exercise 22: Display four lines of star
# for i in range(4):
#         for j in range(10):
#                 print("*",end="")
#         print("")

#********************* Exercise 23: Display the box of star
# for i in range(30):
#         print("*",end="")
# print("")
# for j in range(2):
#         print("*","\t\t\t","    *",end="")
#         print("")
# for k in range(30):
#         print("*",end="")

#********************* Exercise 24: Display the triangle of stars.
# for i in range(10):
#         for j in range(i):
#                 print("",end="")
#         for k in range(i+1):
#                 print("*",end="")
#         print("")

# for i in range(10):
#         for j in range(i):
#                 print("",end="")
#         for k in range(10-i):
#                 print("*",end="")
#         print("")
# Output:
                        # *
                        # **        
                        # ***       
                        # ****      
                        # *****     
                        # ******    
                        # *******   
                        # ********  
                        # ********* 
                        # **********
                        # **********
                        # ********* 
                        # ********  
                        # *******   
                        # ******    
                        # *****     
                        # ****      
                        # ***       
                        # **        
                        # *

#********************* Exercise 25: Display the pyramids of stars.
# for i in range(11):
#         for j in range(11-i):
#                 print(" ",end="")
#         for k in range(2*i-1):
#                 print("*",end="")
#         print("")
# for i in range(-10,1):
#         for j in range(i+10):
#                 print(" ",end="")
#         for k in range(1-2*i):
#                         print("*",end="")
#         print("")
# print(end="")
#Output:
                        #           *
                        #          ***
                        #         *****
                        #        *******
                        #       *********
                        #      ***********
                        #     *************
                        #    ***************
                        #   *****************
                        #  *******************
                        # *********************
                        #  *******************
                        #   *****************
                        #    ***************
                        #     *************
                        #      ***********
                        #       *********
                        #        *******
                        #         *****
                        #          ***
                        #           *
#********************* Exercise 26: Display the heart stars using nested loop
# # define size n = even only
# n = 8
# # so this heart can be made n//2 part left,
# # n//2 part right, and one middle line
# # i.e; columns m = n + 1
# m = n+1
# # loops for upper part
# for i in range(n//2-1):
#     for j in range(m):
#         # condition for printing stars to GFG upper line
#         if i == n//2-2 and (j == 0 or j == m-1):
#             print("*", end=" ")
#         # condition for printing stars to left upper
#         elif j <= m//2 and ((i+j == n//2-3 and j <= m//4) \
#                             or (j-i == m//2-n//2+3 and j > m//4)):
#             print("*", end=" ")
#         # condition for printing stars to right upper
#         elif j > m//2 and ((i+j == n//2-3+m//2 and j < 3*m//4) \
#                            or (j-i == m//2-n//2+3+m//2 and j >= 3*m//4)):
#             print("*", end=" ")  
#         # condition for printing spaces
#         else:
#             print(" ", end=" ")
#     print()
# # loops for lower part
# for i in range(n//2-1, n):
#     for j in range(m):
#         # condition for printing stars
#         if (i-j == n//2-1) or (i+j == n-1+m//2):
#             print('*', end=" ")
#         # condition for printing GFG
#         elif i == n//2-1:
#             if j == m//2-1 or j == m//2+1:
#                 print('G', end=" ")
#             elif j == m//2:
#                 print('F', end=" ")
#             else:
#                 print(' ', end=" ")
#         # condition for printing spaces
#         else:
#             print(' ', end=" ")         
#     print()
# Output:
                        #   *   *   *   *
                        # *       *       *
                        # *               *
                        # *     G F G     *
                        #   *           *
                        #     *       *
                        #       *   *
                        #         *

#********************* Exercise 27: The code below prints the numbers from 1 to 50. Rewrite the code using a while loop to accomplish 
# the same thing.
# for i in range(1,51):
#         print(i,end=",")
# print("")
# j = 1
# while j<=50:
#         print(j,end=",")
#         j+=1

#********************** Exercise 28: 
# A). Write a program that uses a while loop(not a for loop) to read through a string and print the characters of the string one-by
# -one on separate lines.
# B). Modify the program above to print out every second character of the string.

#********************** Exercise 29: A program will make sure that the data its users enter is valid. Write a program 
# that asks the user for a weight and converts it from kilograms to pounds. Whenever the user enters a weight below 0,
# , the program should tell them that their entry is invalid and then ask them again to enter a weight.
# [Hint: use a while loop, not an if statement]
# while 2>0:
#         weight = 1
#         weight = float(input("Enter your weight: "))
#         kind = input("what kind of weigt do you refer to Kilogram or Pound ?: ")
#         if kind =="kilogram" or kind=="Kilogram" or kind=='k' or kind=='K':
#                 if weight>=0:
#                         pound = 2.2046*weight
#                         print("The covertion from kilogram to pound is: ",pound)
#                 else:
#                         print("your data entry is invalid!!")
#         elif kind=="pound" or kind=="Pound" or kind=='p' or kind=='P':
#                 if weight>=0:
#                         kilogram = weight/2.2046
#                         print("The convertion from pound to kilogram is: ",kilogram)
#                 else:
#                         print("your data entry is invalid!!")
#         choice=input("Do you want to play again or not (yes/no): ")
#         if(choice!="yes"):
#                 break

#*********************** Exercise 30: Write a program that asks the user to enter a password. if the user enters the 
# right password, the program should tell them they are logged in to the system. Otherwise, the program should ask 
# them to reenter the password. The user should only get five tries to enter the password, after which point the 
# program should tell them that they are kicked off of the system.
# i=0
# while i<5:
#         code = 1234
#         password = int(input("Enter password: "))
#         if(code==password):
#                 print("They are logged in to the system.")
#                 break
#         else:
#                 print("Please try again !!!")
#                 i+=1

#************************ Exercise 31: Write a program that allows the users to enter any number of test scores. The
# user indicates they are done by entering in a negative number. Print how many of the scores are 'A's(90 or above).
# Also print out the average.
# math      = int(input("Enter math's score: "))
# physic    = int(input("Enter physic's score: "))
# chemistry = int(input("Enter chemistry's score: "))
# biology   = int(input("Enter biology's score: "))
# earth     = int(input("Enter earth's score: "))
# khmer     = int(input("Enter khmer's score: "))
# history   = int(input("Enter history's score: "))
# morality  = int(input("Enter morality's score: "))
# total     = math+physic+chemistry+biology+earth+khmer+history+morality
# average   = total/8
# print("your total score is: ",total)
# print("your averge is : ",average)
# if(average>=90):
#         print("you passed grad A")
# elif average>=80:
#         print("you passed grad B")
# elif average>=70:
#         print("you passed grad C")
# elif average>=60:
#         print("you passed grad D")
# elif average>=50:
#         print("you passed grad E")
# else:
#         print("you passed grad F")

#*********************** Exercise 32: Recall that, given a string s, s.index('x') returns the index of the first x in
# s and an error if there is no x.
#a.) Write a program that asks the user for a string and a letter. Using a while loop, the program should print the
# index of the first occurrence of that letter and a message if the string does not contain the letter.
#b.) Write the above program using a for/break loop instead of a while loop.

#************************* Exercise 33: The GCD(greatest common divisor) of two numbers is the largest number that 
# both are divisible by. for instance, gcd(18,42) is 6 because the largest number that both 18 and 42 are divisible by 
# is 6. Write a program that ask the user for two numbers and computes their GCD. Shown below is a way to compute the 
# GCD, called Euclid's Algorithm
#       a.) First compute the remainder of dividing the largest number by the smaller number.
#       b.) Next, replace the larger number with the smaller number and the smaller number with the remainder.
#       c.) Repeat this process until the smaller number is 0. The GCD is the last value of the larger number.
x = int(input("Enter num1: "))
y = int(input("Enter num2: "))
while x%y != 0:
        r = x%y
        x = y
        y = r
gcd = y
print("GCD is: ",gcd)
a = x
b = y
lcm = (a*b)//gcd
print("PPCM is : ",lcm)
#======================== How to find LCM and GCD of three numbers:
# from math import gcd
# #3 digit lcm calculation
# h=input("(1) 2 Digit LCM or (2) 3 Digit LCM :")
# if h == "1":
#     while True:
#         x = int(input("Number 1: "))
#         y = int(input("Number 2: "))
#         def lcm(x, y):
#             a = gcd(x, y)
#             num = x
#             num2 = y
#             LCM = num * num2 // a
#             return LCM
#         print("The LCM Of " + str(x) + " And " + str(y) + " Is " + str(lcm(x, y)))
# if h == "2":
#         while True:
#                 x = int(input("number 1: "))
#                 y = int(input("number 2: "))
#                 z = int(input("number 3: "))
#                 def lcm(x, y, z):
#                         a = gcd(x, y, z)
#                         num = x
#                         num2 = y * z // a
#                         LCM = num * num2 // a
#                         return LCM
#                 print("The LCM of "+str(x)+" and "+str(y),"and",str(z)+" is "+str(lcm(x, y, z)))

#************************** Exercise 35: A 4000-years old method to compute the square root of 5 is as follows: 
# Start with an initial guess, say 1. Then compute
#                                                       (1+(5/1))/2 = 3
# Next, take that 3 and replace the 1's in the previous formula with 3's. This gives 
#                                                       ((3+5/3))/2 ~ 2.33
# Next replace the 3 in the previous formula with 7/3. This gives
#                                                       ((7/3)+(5/(7/3)))/2 ~ 2.24
# If you keep doing this process of computing this formulas, getting a result, and plugging it back in, the values 
# will eventually get closer and closer to sqrt(5). This method works for numbers other than 5. Write a program that
# asks the user for a number and uses this method to estimate the square root of the number correct to within 10^(-10)
# The estimate will be correct to within 10^(-10) when the absolute value of the difference between consecutive values
# is less than 10^(-10)
# x = int(input("Enter number: "))
# y = (1+x/1)/2
# z = (y+x/y)/10
# w = (z+x/z)/10
# print("The root of",x,"is",w)
