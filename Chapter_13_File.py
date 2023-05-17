#=====================================================================================================================================
#==================================================== Chapter 14: File ===============================================================
#=====================================================================================================================================
# # file = open('header file.txt','x')   # is used to create new files.
# file = open('header file.txt','w')   # is used to write data into file with new thing.
# file.write('string'+'senghort')      # is used to input data into file.
# file.close()                         # is used to close file.

# file = open('header file.txt','a')   # is used to append data into file.
# file.write('aaa'+'ddfdf')            # is used to input data into file.
# file.close()

# file = open('header file.txt','r')   # is used to read data from file.
# print(file.read())                   # is used to display data from file.
# file.close()

# import os                            # is the library that used neccessary to delete file
# os.remove('header file.txt')         # is used to delete file with specific file's name.

#*********************** Exercise 1: How to open, write file and add data in file on number file.
# # Number = open("number.txt","x")   # we put "x" to create a new file.
# Number = open("number.txt",'w')
# for i in range(1,11):
#    Number.write(str(i)+',')
# Number.write('\n')
# for i in range(11,21):
#    Number.write(str(i)+',')
# Number.write('\n')
# for i in range(21,31):
#    Number.write(str(i)+',')
# Number.write('\n')
# for i in range(31,41):
#    Number.write(str(i)+',')
# Number.write('\n')
# for i in range(41,51):
#    Number.write(str(i)+',')
# Number.write('\n')
# for i in range(51,61):
#    Number.write(str(i)+',')
# Number.write('\n')
# Number.close()
# # How to add data in file.  add mode()
# Number = open('number.txt','a')
# for j in range(61,71):
#    Number.write(str(j)+',')
# Number.write('\n')
# for i in range(71,81):
#    Number.write(str(i)+',')
# Number.write('\n')
# for i in range(81,91):
#    Number.write(str(i)+',')
# Number.write('\n')
# for i in range(91,101):
#    Number.write(str(i)+',')
# Number.close()

# x = open('a.txt','w')
# name = input('Enter from user :')
# x.write('name'+name)
# x.close()

# x = open('a.txt','a')
# x.write('Dara Seyhak')
# x.close()

# import os
# os.remove('a.txt')

#*********************** Exercise 2: How to add data and read data in file
# x = open('personal data1.txt','w')
# x.write('Name\t\t\t: Senghort\n')
# x.write('Age\t\t\t: 20\nSex\t\t\t: Male')
# x.write('\nCareer\t\t: Data Science')
# x.write('\nSalary\t\t: 2000$')
# x.write('\nEmail\t\t\t: SenghortKry@gmail.com')
# x.write('\nPhone\t\t\t: 097 45 54 678')
# x.write('\nAddress\t\t: Takeo province')
# x.close()

# x = open('personal data1.txt','a')
# print('What do you want to add in personal data1.txt file ?')
# title = input('Enter title of data :')
# print('Enter',title,':',end='')
# a = input()
# x.write('\n'+title+'\t\t:'+a)
# x.close()

# x = open('personal data1.txt','r')
# print(x.read(29))
# x.close()
# # Name                    : Senghort
# # Age                     : 20        there ae just 29 characters for displaying.

# x = open('personal data1.txt','r')
# print(x.read())
# x.close()

# # Deletion method need import os as neccessary because  
# import os
# os.remove('personal data1.txt')
# os.remove('personal data2.txt')
# os.remove('number.txt')

# #========================================
# y = open('personal data2.txt','w')
# name = input('Enter your name : ')
# sex = input('Enter your sex :')
# age = int(input('Enter your age :'))
# career = input('Enter your career :')
# salary = float(input('Enter your salary :'))
# position = input('Enter your positon :')
# phone = input('Enter your phone number :')
# address = (input('Enter your address :'))
# y.write('Name\t\t\t\t: '+name)
# y.write('\nSex\t\t\t\t: '+sex)
# y.write('\nAge\t\t\t\t: '+str(age))
# y.write('\nCareer\t\t\t: '+career)
# y.write('\nSalary\t\t\t: '+str(salary))
# y.write('\nposition\t\t\t: '+position)
# y.write('\nPhone Number\t: '+str(int(phone)))
# y.write('\nAddress\t\t\t: '+address)
# y.close()

#*********************** Exercise 3:

# dict1 = {'Name':'Zara','ID':123456,'Sex':'male'}
# dict2 = {'Salary':1200,'Position':'Engineer'}
# dict1.update(dict2)
# dict2.update(dict1)
# print('Updated dictionary is such that : ',dict1)
# print('Updated dictionary is such that : ',dict2)
# # Updated dictionary is such that :  {'Name': 'Zara', 'ID': 123456, 'Sex': 'male', 'Salary': 1200, 'Position': 'Engineer'}
# # Updated dictionary is such that :  {'Salary': 1200, 'Position': 'Engineer', 'Name': 'Zara', 'ID': 123456, 'Sex': 'male'}







#*********************** Exercise 4:










#*********************** Exercise 5:









