#=====================================================================================================================================
#==================================================== Chapter 15 : OOP ===============================================================
#=====================================================================================================================================
#********************* Introduction to OOP (Object Oriented Programming) :
# 1.) Class : a user-defined prototype for an object that defines a set of attributes that characterize any object of the class. The 
#             attributes are data members (class variables and instance variables) and methods, accessed via dot notation.
# 2.) Class variable : is a variable that is shared by all instances of a class. Class variables are defined within a class but 
#                      outside any of class's methods. Class variables are not used as frequently as instance variables are.
# 3.) Data member : is a class variable or instance variable that holds data associated with a class and its objects.
# 4.) Function overloading : is the assignment of more than one behavior to a particular function. The operation performed variables 
#                            by the types of objects or arguments involved.
# 5.) Instance Variable : is a variable that is defined inside a method and belongs only to the current instance of a class.
# 6.) Inheritance : is transfering of the characteristics of a class to other classes that are derived from it.
# 7.) Instance : is an individual object of a certain class. An object that belongs to a class circle, for example, is an instance of
#                the class circle.
# 8.) Instantiation : the creation of an instance of a class.
# 9.) Method : is a special kind of function that is defined in a class definition.
# 10.)Object : is a unique instance of a data structure that is defined by its class. An object comprises both data members (class 
#     variables and instance variables) and methods.
# 11.)Operator Overloading : the assignment of more than one function to a particular operator.
 
#********************* Exercise 1: Creating Classes  
# class classname:
#    'optional class documentation string'
#    class_suite

# class employee:
#    empCount = 0
#    def __init__(self,name,salary):              
#       self.name = name
#       self.salary = salary 
#       employee.empCount += 1
#    def displayCount(self):
#       print('Total employee %d'%employee.empCount)
#    def displayEmployee(self):
#       print('Name :',self.name)
#    def displaySalary(self):
#       print('Salary :',self.salary)      

# + The variable empCount is a class variable whose value is shared among all the instances of a in this case. This can be accessed as
#   Employee.empCount from inside the class or outside the class.
# + The first method __int__() is a special method, which is called class constructor or initialization method that python calls when
#   you create a new instance of this class.
# + you declare other class methods like normal functions with the exception that the first argument to each method is self. Python 
#   adds the self argument to the list for you; you do not need to include it when you call the methods.

#********************* Exercise 2: Creating Instance Objects 
# To create instance of a class, you call the class using class name and pass in whatever arguments its __int__ method accepts.

# emp1 = employee('Senghort',2000)
# emp2 = employee('Dara',5000)

#********************* Exercise 3: Accessing Attributes
# we can acess the object's attributes using the dot operator with object. Class variable would be accessed using class name as follow:

# emp1.displayEmployee()
# emp2.displayEmployee()
# print('Total employee %d'%employee.empCount)

#********************* Exercise 4: Full coding representation
# class employee:
#    empCount = 0
#    def __init__(self,name,salary):              
#       self.name = name
#       self.salary = salary 
#       employee.empCount += 1
#    def displayCount(self):
#       print('Total employee %d'%employee.empCount)
#    def displayEmployee(self):
#       print('Name :',self.name)
#    def displaySalary(self):
#       print('Salary :',self.salary)      

# emp1 = employee('Senghort',2000)
# emp2 = employee('Dara',5000)
# emp1.displayEmployee()
# emp2.displayEmployee()
# emp1.displaySalary()
# emp2.displaySalary()
# emp1.displayCount()

# x1 = input('Enter name1 : ')
# x2 = input('Enter name2 : ')
# y1 = float(input('Enter salary1 : '))
# y2 = float(input('Enter salary2 : '))

# a = employee(x1,y1)
# b = employee(x2,y2)
# a.displayCount()
# b.displayEmployee()
# a.displayEmployee()
# a.displaySalary()
# b.displaySalary()

# Output:
                                             # Name : Senghort
                                             # Name : Dara     
                                             # Total employee

#*********************** Exercise 5: Store data in file
# file = open('data.txt','w')
# class employee:
#    empCount = 0
#    def __init__(self,Id,name,age,salary,address,career,position,phone,email) -> None:    # keyword self must at the first location among another parameters in functions.
#       self.Id = Id
#       self.name = name
#       self.age = age
#       self.salary = salary 
#       self.address = address
#       self.career = career
#       self.position = position
#       self.phone = phone
#       self.email = email      
#       employee.empCount += 1
#    def displayInfo(self):
#       print('ID\t\t:',self.Id,'\nName\t\t:',self.name,'\nAge\t\t:',self.age,'\nSalary\t\t:',self.salary,'\nAddress\t\t:',self.address)
#       print('Career\t\t:',self.career,'\nPosition\t:',self.position,'\nPhone\t\t:',self.phone,'\nEmail\t\t:',self.email)
      
# number = int(input('Enter the number of employee : '))
# for j in range(1,number+1):
#    print('Person['+str(j)+'] data')
#    a = input('Enter your ID['+str(j)+']\t\t: ')   
#    b = input('Enter name['+str(j)+']\t\t\t: ')
#    c = int(input('Enter your age['+str(j)+']\t\t: '))
#    d = float(input('Enter your salary['+str(j)+']\t\t: '))
#    e = input('Enter your address['+str(j)+']\t\t: ')
#    f = input('Enter your career['+str(j)+']\t\t: ')
#    g = input('Enter your position['+str(j)+']\t\t: ')
#    h = int(input('Enter your phone number['+str(j)+']\t: '))
#    i = input('Enter your email['+str(j)+']\t\t: ')
#    x = employee(a,b,c,d,e,f,g,h,i)
#    file.write('Person['+str(j)+'] data'+'\nID\t\t\t: '+a+'\nName\t\t: '+b+'\nAge\t\t: '+str(c)+'\nSalary\t: '+str(d)+'\nAddress\t: '+e+'\nCareer\t: '+f+'\nPosition\t: '+g+'\nPhone\t\t: '+str(h)+'\nEmail\t\t: '+i+'\n\n')
#    print('\n')
# print('The personal data are such that : ')
# for k in range(1,number+1):
#    x.displayInfo()
# print('The number of employee is : ',employee.empCount)
# file.close()

# Output: 
# Enter the number of employee : 5
# Person[1] data
# Enter your ID[1]                : e202001
# Enter name[1]                   : kry senghort
# Enter your age[1]               : 21
# Enter your salary[1]            : 210000
# Enter your address[1]           : takeo
# Enter your career[1]            : data scientist
# Enter your position[1]          : manager
# Enter your phone number[1]      : 855974554582
# Enter your email[1]             : senghortkry@itc.edu.kh

# Person[2] data
# Enter your ID[2]                : e202002
# Enter name[2]                   : chhon chanly
# Enter your age[2]               : 20
# Enter your salary[2]            : 1200
# Enter your address[2]           : kandal
# Enter your career[2]            : software engineer
# Enter your position[2]          : directore
# Enter your phone number[2]      : 85596787968
# Enter your email[2]             : chhonchanly@gmail.com

# Person[3] data
# Enter your ID[3]                : e202003 
# Enter name[3]                   : sorn tola
# Enter your age[3]               : 19
# Enter your salary[3]            : 120090
# Enter your address[3]           : tbong khmoum
# Enter your career[3]            : civil engineer
# Enter your position[3]          : site manager
# Enter your phone number[3]      : 855677693
# Enter your email[3]             : sorntola@yahoo.com

# Person[4] data
# Enter your ID[4]                : e202003
# Enter name[4]                   : san chanchariya
# Enter your age[4]               : 19
# Enter your salary[4]            : 129000
# Enter your address[4]           : prey veng
# Enter your career[4]            : chemical engineer   
# Enter your position[4]          : sub-director 
# Enter your phone number[4]      : 8556790786
# Enter your email[4]             : sanchanchariya@eng.com.kh

# Person[5] data
# Enter your ID[5]                : e202005
# Enter name[5]                   : ek vongpanharith
# Enter your age[5]               : 18
# Enter your salary[5]            : 234000
# Enter your address[5]           : siem reap
# Enter your career[5]            : web developer 
# Enter your position[5]          : data analysis
# Enter your phone number[5]      : 855973443456
# Enter your email[5]             : panharith@rupp.edu.kh

# The personal data are such that :
# ID              : e202005
# Name            : ek vongpanharith
# Age             : 18
# Salary          : 234000.0
# Address         : siem reap
# Career          : web developer
# Position        : data analysis
# Phone           : 855973443456
# Email           : panharith@rupp.edu.kh
# ID              : e202005
# Name            : ek vongpanharith
# Age             : 18
# Salary          : 234000.0
# Address         : siem reap
# Career          : web developer
# Position        : data analysis 
# Phone           : 855973443456
# Email           : panharith@rupp.edu.kh
# ID              : e202005
# Name            : ek vongpanharith
# Age             : 18
# Salary          : 234000.0
# Address         : siem reap
# Career          : web developer
# Position        : data analysis
# Phone           : 855973443456
# Email           : panharith@rupp.edu.kh
# ID              : e202005
# Name            : ek vongpanharith
# Age             : 18
# Salary          : 234000.0
# Address         : siem reap
# Career          : web developer
# Position        : data analysis
# Phone           : 855973443456
# Email           : panharith@rupp.edu.kh
# ID              : e202005
# Name            : ek vongpanharith
# Age             : 18
# Salary          : 234000.0
# Address         : siem reap
# Career          : web developer
# Position        : data analysis
# Phone           : 855973443456
# Email           : panharith@rupp.edu.kh
# The number of employee is :  5

#*********************** Exercise 6: Store data in file

# str = "insert into customer values(23,'c5','xx8');"
# mycursor.execute(str)
# mycursor.execute("select *from customer;")
# data = mycursor.fetchall()
# print(data)


