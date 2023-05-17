#=====================================================================================================================================
#==================================================== Chapter 04: Decision Making ====================================================
#=====================================================================================================================================
#************************* IF Elif and Else Condition format:
#************ Exercise 01:
# amount = int(input("Enter amount: $ "))  # we must have the integer form because of arithmetic above. 
# if(amount>=3000):
#         discount = amount*0.2
#         print("you get discount for : $ ",discount)
#         payment = amount - discount
#         print("you need to pay for : $ ",payment)
# elif(amount>=2500):
#         discount = amount*0.15
#         print("you get discount for : $ ",discount)
#         payment = amount - discount
#         print("you need to pay for : $ ",payment)
# elif(amount>=2000):
#         discount = amount*0.1
#         print("you get discount for : $ ",discount)
#         payment = amount - discount
#         print("you need to pay for : $ ",payment)
# elif(amount>=1500):
#         discount = amount*0.05
#         print("you get discount for : $ ",discount)
#         payment = amount - discount
#         print("you need to pay for : $ ",payment)
# elif(amount>=1000):
#         discount = amount*0.02
#         print("you get discount for : $ ",discount)
#         payment = amount - discount
#         print("you need to pay for : $ ",payment)
# elif(amount>=500):
#         print("you get speaker for discount")
#         print("you need to pay for : $ ",amount)
# else:
#         print("you do not get discount for this amount")
#         print("you need to pay for : $ ",amount)
# Output:
        # Enter amount: $ 4000
        # you get discount for : $  800.0
        # you need to pay for : $  3200.0

        # Enter amount: $ 2800
        # you get discount for : $  420.0
        # you need to pay for : $ 2380.0

        # Enter amount: $ 2150
        # you get discount for : $  215.0
        # you need to pay for : $  1935.0

        # Enter amount: $ 1660
        # you get discount for : $  83.0
        # you need to pay for : $  1577.0

        # Enter amount: $ 650
        # you get speaker for discount
        # you need to pay for : $  650

        # Enter amount: $ 432
        # you do not get discount for this amount
        # you need to pay for : $  432

#******** Exercise 02:
# name = input("Enter your name : ")
# if(name=="Kry Senghort"):
#         print("your email is Senghortkry@gmail.com")
# else:
#         print("please try again!")
# Output:
        # Enter your name : Kry Senghort
        # your email is Senghortkry@gmail.com

#******* Exercise 03:
# number = int(input("Enter number : "))
# if(number==10):
#         num = number*2
#         print("num = ",num)
# elif(number==9):
#         num = number/3
#         print("num = ",num)
# else:
#         print("no operation")
# Output:
#         Enter number : 10
#         num =  20
#         Enter number : 9
#         num =  3.0

#******* Exercise 04:
# num = float(input("Enter number : "))
# if(num%2==0):
#         if(num%3==0):
#                 print("Divisible by 3 and 2")
#         else:
#                 print("Divisible by 2 not divisible by 3")
# else:
#         if(num%3==0):
#                 print("Divisible by 3 not divisible by 2")
#         else:
#                 print("not divisible by 2 not divisibe by 3")
# Output:
        # Enter number : 12
        # Divisible by 3 and 2

#******** Exercise 05: write a program to find the largest number that get input from user.
# a = int(input("Enter a: "))
# b = int(input("Enter b: "))
# c = int(input("Enter c: "))
# d = int(input("Enter d: "))
# e = int(input("Enter e: "))
# f = int(input("Enter f: "))
# if(a>b and a>c and a>d and a>e):
#         print("The largest number is ",a)
# elif(b>a and b>c and b>d and b>e):
#         print("The largest number is: ",b)
# elif(c>a and c>b and c>d and c>e):
#         print("The largest number is: ",c)
# elif(d>a and d>c and d>e and d>b):
#         print("The largest number is: ",d)
# elif(e>a and e>b and e>c and e>d):
#         print("The largest number is: ",e)
# else:
#         print("Invalid")

#******** Exercise 06: Write a program to find the largest number that get input from user.
# a = int(input("Enter a: "))
# b = int(input("Enter b: "))
# c = int(input("Enter c: "))
# d = int(input("Enter d: "))
# e = int(input("Enter e: "))
# f = int(input("Enter f: "))
# m = a
# if(m<b):
#         m = b
# if(m<c):
#         m = c
# if(m<d):
#         m = d
# if(m<e):
#         m = e
# print("The maximum number is ",m)
# Output:
        # Enter a: 1
        # Enter b: 34
        # Enter c: 43
        # Enter d: 56
        # Enter e: 65
        # Enter f: 32
        # The maximum number is  65

#******** Exercise 07: Write an algorithm to check and set the rank.
# score = float(input("Enter your score: "))
# if(score>=90):
#         print("your grade is A")
# elif(score>=80):
#         print("your grade is B")
# elif(score>=70):
#         print("your grade is C")
# elif(score>=60):
#         print("your grade is D")
# elif(score>=50):
#         print("your grade is E")
# else:
#         print("your grade is F")

#******** Exercise 08: Write a program to check and show the smallest number.
# a = float(input("Enter a: "))
# b = float(input("Enter b: "))
# c = float(input("Enter c: "))
# d = float(input("Enter d: "))
# e = float(input("Enter e: "))
# f = float(input("Enter f: "))
# Min = a
# if(Min>b):
#         Min = b
# if(Min>c):
#         Min = c
# if(Min>d):
#         Min = d
# if(Min>e):
#         Min = e
# if(Min>f):
#         Min = f
# print("The smallest number is ",Min)

#*********** Exercise 09: Write an algorithm to check the date input from user wether valid or invalid.
# d = int(input("Enter date : "))
# m = int(input("Enter month: "))
# y = int(input("Enter year: "))
# if(y>0):
#         if(m>0 and m<=12):
#                 if(m==1 or m==3 or m==5 or m==7 or m==8 or m==10 or m==12):
#                         if(d>0 and d<=31):
#                                 print("Available Date")
#                         else:
#                                 print("Invalid Date")
#                 elif(m==2):
#                         if(d>0 and (d<=28 or d<=29)):
#                                 print("Available Date")
#                         else:
#                                 print("Invalid Date")
#                 elif(m==4 or m==6 or m==9 or m==11):
#                         if(d>0 and d<=30):
#                                 print("Available Date")
#                         else:
#                                 print("Invalid Date")
#                 else:
#                         print("Invalid Date")
#         else:
#                 print("Invalid Date")
# else:
#         print("Invalid Date")

#************** Exercise 10: Write an algorithm to check whether a number is odd or even number.
# x = float(input("Enter number: "))
# if(x%2==0):
#         print("x is an even number.")
# else:
#         print("x is an odd number.")

#*************** Exercise 11: Write an algorithm to solve quadratic equation.
# from cmath import sqrt
# a = float(input("Input a : "))
# b = float(input("Input b : "))
# c = float(input("Input c : "))
# delta = b**2 - 4*a*c
# x1 = (-b+sqrt(delta))/(2*a)
# x2 = (-b-sqrt(delta))/(2*a)
# if(delta>0):
#         print("The root of equation such that : ")
#         print("\t\t\tx1 = ",x1)
#         print("\t\t\tx2 = ",x2)
# elif(delta==0):
#         print("The root of equation such that : ")
#         print("x1 = x2 = ",x1)
# else:
#         print("The equation has imaginary root.")

#*************** Exercise 12: Write an algorithm to compute the taxation value.
# name = input("Enter your name: ")
# sex = input("Enter your sex: ")
# salary = float(input("Enter your salary; "))
# if(sex=='M' or sex =='m'):
#         tax = 0.03*salary
#         print("you need to pay tax = ",tax)
#         salary = salary - tax
#         print("Salary remainder is : ", salary)
# elif(sex=='F' or sex=='f'):
#         tax = 0.02*salary
#         print("you need to pay the tax = ",tax)
#         salary -= tax
#         print("Salary remainder is : ", salary)
# else:
#         print("not available")

#*************** Exercise 13: Write an algorithm which allows a user to input 2 numbers and an operation(+,-,/,*) then
# using the SWITCH...DO to perform the given operation between those two numbers.
# i = float(input("Enter number#1: "))
# j = float(input("Enter number#2: "))
# print(" [1]. Summation\n [2]. Substraction\n [3]. Multiplication\n [4]. Division\n [5]. Modulus\n")
# choice = int(input("Enter your choice: "))
# if(choice==1):
#         summation = i+j
#         print("the summation between these two numbers is : ",summation)
# elif(choice==2):
#         substraction = i-j
#         print("The substraction between these two numbers is : ",substraction)  
# elif(choice==3):
#         multiplication = i*j
#         print("The multiplication between these two numbers is : ",multiplication)
# elif(choice==4):
#         division = i/j
#         print("The division between these two numbers is : ",division)
# elif(choice==5):
#         modulus = i%j
#         print("The remainder between these two numbers is : ",modulus)
# else:
#         print("Please enter correct choice !")

#**************** Exercise 14: Write a program to ask the users to enter a length in cm. if the user enters a negative
# length, the program should tell the user that the entry is invalid. Otherwise, the program should convert the length
# to inches and print out the result. There are 2.54cm in an inch.
# cm = float(input("Enter a length in cm: "))
# if(cm<0):
#         print("Data entry is invalid.")
# else:
#         inch = 2.24*cm
#         print("The length of",cm,"is equal = ",inch,"inch")

#***************** Exercise 15: Ask the user for a temperature. then ask them what units, celsius, fahrenheit or kelven,
# the temperature is in. your program should convert the temperature to unit. The conversion are F = (9/5)*c + 32 and 
# c = (5/9)*(f-32), k = c + 273
# tem = float(input("Enter the temperature that you want to convert: "))
# print("What unit you input farenheit/kelvin or celsius")
# print("[1]. Celsius")
# print("[2]. Kelvin")
# print("[3]. Farenheit")
# print("Choose one option c/k/f or 1/2/3")
# unit = input(("Enter your option: "))
# if unit=='c':
#         k = tem+273
#         f = (9/5)*tem + 32
#         print("The conversion from celsius to another units are such following: ")
#         print("Kelvin =",k,end=" k\n")
#         print("Farenheit =",f,end=" f")
# elif unit=='k':
#         c = tem-273
#         f = (9/5)*(tem-273)+32
#         print("The conversion from kelvin to another units are such following: ")
#         print("Celsius =",c,end=" c\n")
#         print("Farenheit =",f,end=" f")
# elif unit=='f':
#         c = (tem-32)*(5/9)
#         k = (tem-32)*(5/9) + 273
#         k = c + 273
#         print("The conversion from farenheit to another units are such following: ")
#         print("Celsius =",c,end=" c\n")
#         print("Kelvin =",k,end=" k",)
# elif int(unit)==1:
#         k = tem+273
#         f = (9/5)*tem + 32
#         print("The conversion from celcuis to another units are such following: ")
#         print("Kelvin =",k,end=" k\n")
#         print("Farenheit =",f,end=" f")
# elif int(unit)==2:
#         c = tem-273
#         f = (9/5)*(tem-273)+32
#         print("The conversion from kelvin to another units are such following: ")
#         print("Celsius =",c,end=" c\n")
#         print("Farenheit =",f,end=" f")
# elif int(unit)==3:
#         c = (tem-32)*(5/9)
#         k = (tem-32)*(5/9) + 273
#         k = c + 273
#         print("The conversion from farenheit to another units are such following: ")
#         print("Celsius =",c,end=" c\n")
#         print("Kelvin =",k,end=" k",)
# else:
#         print("Please enter correct option")

#***************** Exercise 15: Ask the user to enter a temperature in celsius. The program should print a message 
# based on the temperature.
#[1]. if the temperature is less than -273.15, print that the temperature is invalid because it is below absolutely 
# zero.
#[2]. if it is exactly -273.15, print that the temperature is absolute 0.
#[3]. if it is 0, print that the temperature is at the freezing point.
#[4]. if it is between 0 and 100, print that the temperature is in normal line.
#[5]. if it is 100, print that the temperature is at the boiling point.
#[6]. if it is above 100, print that the temperature is above the boiling point.
# tem = float(input("Enter the temperature(celsius): "))
# if tem < -273.15:
#         print("the temperature is invalid because it is below absolutely zero.")
# elif tem == -273.15:
#         print("the temperature is absolute 0.")
# elif tem >-273.15 and tem<0:
#         print("the temperature is absolute 0.")
# elif tem == 0:
#         print("the temperature is at the freezing point.")
# elif tem >0 and tem<100:
#         print("temperature is in normal line.")
# elif tem==100:
#         print("The temperature is at boiling point.")
# else:
#         print("The temperature is above the boiling point.")

#***************** Exercise 16: Write a program that ask the user how many credits they have taken. if they have taken
# 23 or less, print that the student is a freshman. if they have taken between 24 and 53, print that they are a 
# sophormore. The range for junoirs is 54 to 83, and for seniors it is 84 and over.
# credit = int(input("Enter your credit: "))
# if credit<=23: 
#         print("The student is a freshman.")
# elif credit>=24 and credit<=53:
#         print("They have taken a sophormore.")
# elif credit>=54 and credit<=83:
#         print("The student is a junoirs.")
# else:
#         print("The student is a senior.")

#****************** Exercise 17: Generate a random number between 1 and 10. Ask the user to guess the number and print
# a message based on whether they get it right or not.
# i = int(input("Input the number: "))
# if i>0 and i<=10:
#         print("you guess right.")
# else:
#         print("it is not right.")

#******************* Exercise 18: A store charges $12 per item if you buy less than 10 items. if you buy between 10
# and 99 items, the cost is $10 per item. if you buy 100 or more items, the cost is $7 per item. write a program that 
# ask the user how many items they are buying and prints the total cost.
# item = int(input("Enter the number of items that you want to buy: "))
# if item<10:
#         cost = 12*item
#         print("The total price is $",cost)
# elif item>=10 and item<=99:
#         cost = 10*item
#         print("The total price is $",cost)
# elif item>=100:
#         cost = 7*item
#         print("The total price is $",cost)

#******************** Exercise 19: Write a program that ask the user for a year and prints out whether it is a leap 
# year or not. A leap year is a year that are divisible by 4, except that years divisible by 100 are not leap years 
# unless they are also divisible by 400.
# leap year = ឆ្នាំបង្រ្គប់មាន  366 ថ្ងៃ
year = int(input("Enter the year: "))
if year%4 == 0 and year%100 !=0 :
        print("It is a leap year.")
if year%400==0:
        print("It is a leap year.")
else:
        print("It is not a leap year.")

#******************** Exercise 20: Write a program that asks the user to enter a number and prints out all the divisors
# of that number.[Hint: the % operator is used to tell if a number is divisible by something. See section 3.2.]
# i = int(input("Enter number: "))
# j = 0
# print("The divisors of",i,"are such that:")
# for k in range(1,i+1):
#         if i%k==0:
#                 j+=1
#                 print(k,end=",")
# print("\nThe number of divisor of",i,"is",j)

#********************* Exercise 21: Write a multiplication game for kids. The program should give the player ten 
# randomly generated multiplication questions to do. After each, the program should tell them whether they got it 
# right or wrong and what the correct answer is.
# for k in range(1,11):
#         print("Question",k,":")
#         i = int(input("Enter number1: "))
#         j = int(input("Enter number2: "))
#         l = int(input("Input result: "))
#         print(i,"x",j,"=",l)
#         mul = i*j
#         if mul==l:
#                 print("Right!")
#         else:
#                 print("Wrong!")

#********************** Exercise 22: Write a program that asks the user for an hour between 1 and 12, asks them to 
# enter am or pm, and asks them how many hours into the future they want to go. Print out what the hour will be that
# many hours into the future, printting am or pm as appropriate. An example is shown below.
# hour = int(input("Enter hour: "))
# kind = int(input("am(1) or pm(2): "))
# ahead= int(input("How many hours ahead ?"))
# if(hour>0 and hour<=12):
#         if(kind==1):
#                 new_hour = hour+ahead
#                 if(new_hour>0 and new_hour<=12):
#                         print("you will arrive at",new_hour,"am")
#                 else:
#                         new_hour = new_hour-12
#                         print("you will arrive at",new_hour,"pm")
#         else:
#                 new_hour = hour+ahead
#                 if(new_hour>0 and new_hour<=12):
#                         print("you will arrive at",new_hour,"pm")
#                 else:
#                         new_hour = new_hour-12
#                         print("you will arrive at",new_hour,"am")
# else:
#         print("No result !")

#*********************** Exercise 23: A jar of Halloween candy contains an unknown amount of candy and if you can 
# guess exactly how much candy is in the bowl, then you win all the candy. You ask the person in charge the following:
# if the candy is divided evenly among 5 people, how many pieces would be left over(នៅសល់) ?
# The answer is 2 pieces. 
# You then ask about dividing the candy evenly among 6 people, and the amount left over is 3 pieces. 
# Finally, you ask about dividing the candy evenly among 7 people, and the amount left over is 2 pieces. By looking at
# the bowl you can tell that there are less than 200 pieces. Write a program to determine how many pieces are in the 
# bowl 
# Method 1:
# for candies in range(200):
#         if (candies%5!=2):
#                 continue
#         if (candies%6!=3):
#                 continue
#         if (candies%7!=2):
#                 continue
#         print("The number of pieces is : " + str(candies))
#         break
# # Method 2:
# for candies in range(200):
#         if (candies%5!=2 or candies%6!=3 or candies%7!=2):
#                 continue
#         print("The number of pieces is :",str(candies))
#         break
# # Method 3:
# x = 200
# for i in range(x):
#         if(i%5==2):
#                 if(i%6==3):
#                         if(i%7==2):
#                                 print("The number of pieces is :",i)
#                                 break                        

#************************ Exercise 24: Write a program that lets the user play Rock-Paper-Scissors against the 
# computer. There should be five rounds, and after those five rounds, your program should print out who won and lost
# or that there is a tie. (លេងប៉ាវ ស៊ីងស៊ុម ក្ដាប់(rock)​ លា(paper) ចាក់​កន្រ្តៃ(scissors))
# import random
# while True:
#         choices = ["rock","paper","scissors"]

#         computer = random.choice(choices)
#         player = None

#         while player not in choices:
#                 player = input("rock, paper, or scissors ?: ").lower()
#         if player==computer:
#                 print("computer: ",computer)
#                 print("player: ",player)
#                 print("Tie!")
#         elif player=="rock":
#                 if computer=="paper":
#                         print("computer: ",computer)
#                         print("player: ",player)
#                         print("you lose !")
#                 if computer=="scissors":
#                         print("computer: ",computer)
#                         print("player: ",player)
#                         print("you win!")
#         elif player=="scissors":
#                 if computer=="rock":
#                         print("computer: ",computer)
#                         print("player: ",player)
#                         print("you lose!")
#                 if computer=="paper":
#                         print("computer: ",computer)
#                         print("player: ",player)
#                         print("you win!")
#         elif player=="paper":
#                 if computer=="scissors":
#                         print("computer: ",computer)
#                         print("player: ",player)
#                         print("you lose!")
#                 if computer=="rock":
#                         print("computer: ",computer)
#                         print("player: ",player)
#                         print("you win!")
#         play_again = input("Play again? (yes/no): ").lower()
#         if play_again!="yes":
#                 break
# print("bye!")
# The rule and object of scissors, paper and rock game are such that: 
# The object of this two-player game is to beat the symbol your opponent throws in a best of three. There are three 
# symbols: Rock (a closed fist), Paper (a flat hand palm down), and Scissors (a fist with two fingers out). Symbols 
# are always thrown on an open palm.
# To throw a symbol, the 2 players face each other and hold one hand open, palm up and rest their other hand in a fist
# on top of it. One player asks if the other is ready, once they are that player says, “Rock, paper, scissors, shoot.” 
# Both players hit their fist into their palm when each word is said. When the final word is said, “shoot”, on that 
# hit, both players simultaneously make one of the symbols with their moving hand and hold it open on the palm.
# Rock beats scissors, scissors beats paper, and paper beats rock. If there is a tie you re throw. If a player changes 
# their symbol after both players have thrown, then they lose that throw. The first player to beat their opponent 
# 2 times wins.




