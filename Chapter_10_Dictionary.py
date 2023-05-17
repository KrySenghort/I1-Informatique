#=====================================================================================================================================
#==================================================== Chapter 10: Dictionary ========================================================
#=====================================================================================================================================
# Dictionary is sequence of keys,which each key is separated from its value by a colon(:), the items are separated by commas. and the
# whole thing is enclosed in curly braces. An empty dictionary without any item is written with just two curly braces, like this: {}
# keys are unique within a dictionary while values may not be. The values of a dictionary can be of any type, but the keys must be of
# immutable data type such as strings, numbers, or tuples.

#****************** Exercise 1: Introduction to dictionary
# dict = {'Name':'Zara','Age':7,'Sex':'M','Class':'12A'}
# print("dict['Name'] : ",dict['Name'])  #  dict['Name'] :  Zara
# print("dict['Age']  : ",dict['Age'])   #  dict['Age']  :  7
# print("dict['Sex']  : ",dict['Sex'])   #  dict['Sex']  :  M

#****************** Exercise 2: Update element in dictionary
# dict = {'Name':'Senghort','Age':20,'Job':'Data Scientist','Address':'Phnom Penh','Salary':1200}
# dict['ID']   = 'e20200706'   # insert key and its value in dictionary.
# dict['Name'] = 'Kry Senghort'
# dict['Age']  = 18               # update existing data entry.
# dict['Job']  = 'Cyber Security'
# print(dict) 
# #     {'Name': 'Kry Senghort', 'Age': 18, 'Job': 'Cyber Security', 'Address': 'Phnom Penh', 'Salary': 1200, 'ID': 'e20200706'}

#****************** Exercise 3: Delete element in dictionary
# dict = {'Name':'Seyha','Age':17,'DOB':'12-Jan-2006','Salary':700,'Position':'Marketing'}
# del dict['Name']      # remove data entry with key 'Name'
# del dict['Position']
# print(dict)    # {'Age': 17, 'DOB': '12-Jan-2006', 'Salary': 700}

# dict.clear()   # remove all data entry in dictionary
# print(dict)    # {}

# del dict       # delete entire dictionary
# print(dict)    # <class 'dict'>  : mean that dictionary was deleted so no result to display or dictionary does not exist anymore.

#****************** Exercise 4: Key value discussion
# # Key is unique and more than one of data entry is not allowed. If key is duplicated so the last assignment win or will be displayed.
# # this is overwrite method.
# dict = {'Name':'Senghort','ID':123456,'Name':'Kry'}
# print(dict)  #  {'Name': 'Kry', 'ID': 123456}
# dict = {'ID':433,'age':34,'Name':'Daro','ID':123,'age':34}
# print(dict)  #  {'ID':123, 'age': 34, 'Name': 'Daro'}

# # Key must be immutable. this mean that you can use string, numbers or tuple as dictionary keys but sometime like ['key'] is not 
# # allowed.
# dict1 = {'ID':1200,['Name']:1200}
# print(dict1[['Name']])      #   dict = {'ID':1200,['Name']:1200}   TypeError: unhashable type: 'list'

# list  = ['Senghort','engineer',123]
# tuple = (1200,'Manager')
# dict  = {'Sex':'Male','Phone':'0974554582'}
# dict2 = {'ID':1200,'Name':list[0],'Career':list[1],'Position':tuple[1],'Salary':tuple[0],'Code':list[2],'Sex and Phone':dict}
# print(dict2['Sex and Phone'])  # {'Sex' :'Male', 'Phone' :0974554582}}
# print(dict2) 
# # {'ID': 1200, 'Name': 'Senghort','Career' :'engineer' ,'Position' :'Manager' ,'Salary' :1200 ,'Code' :123 ,'Sex and Phone':
# # {'Sex' :'Male', 'Phone' :0974554582}}

#****************** Exercise 5: len(dict) method is used to display the total length of the dictionary. It would be equal to number
# # of items in the dictionary.
# dict = {'ID':123, 'age': 34, 'Name': 'Daro'}
# print(len(dict))  # 3
# dict = {'Sex':'male','Department':'data science'}
# print(len(dict))  # 2

# list = ['abc',123,234,'Jaik','defe']
# tuple = (1,2,3,6,7,8)
# dict = {'x':list,'y':tuple}
# print(dict)          #  {'x': ['abc', 123, 234, 'Jaik', 'defe'], 'y': (1, 2, 3, 6, 7, 8)}
# print(len(dict))     # 2
# print(len(list)+len(tuple))  # 11

#****************** Exercise 6: str(dict) method is used to produces a printable string representation of a dictionary.
# dict = {'Name':'Senghort','Age':20,'Department':'Data Science'}
# print('Equivalent string is : %s' % str(dict)) # Equivalent string is : {'Name': 'Senghort', 'Age': 20, 'Department': 'Data Science'}

# dict = {'ID':123, 'age': 34, 'Name': 'Daro'}
# print('the equivalent string is : %s' %str(dict)) # the equivalent string is : {'ID': 123, 'age': 34, 'Name': 'Daro'}

#****************** Exercise 7: type(dict) method is used to return the type of passed variable. if passed variable is dictionary.
# # then it would return a dictionary type.
# x={'Unit1':'Complex Number','Unit2':'Algebraic&Transcendental Function','Unit3':'Limit&Continuity','Unit4':'Derivative Application'}
# print('Variable Type of x : %s' %type(x))  #  Variable Type of x : <class 'dict'>
# y = [1,2,3,4,4,5,6,6]
# print('Variable Type of y : %s' %type(y))  # Variable Type of y : <class 'list'> 
# z = (3,4,5,6,7,8)
# print('Variable Type of z : %s' %type(z))  # Variable Type of z : <class 'tuple'>
# a = 2
# b = 'dara'
# c = 2.3333
# d = 'c'
# from cmath import e, pi
# f = e
# g = pi
# print('a',type(a))  # a <class 'int'>
# print('b',type(b))  # b <class 'str'>
# print('c',type(c))  # c <class 'float'>
# print('d',type(d))  # d <class 'str'>
# print('f',type(f))  # f <class 'float'>
# print('g',type(g))  # g <class 'float'>

#****************** Exercise 8: dict.clear() method is used to removes all element of dictionary.
# x = {'a':2,'b':4,'c':5,'d':9,'e':'def','f':'xyz'}
# print(len(x)) # 6
# x.clear()
# print(len(x)) # 0

#****************** Exercise 9: dict.copy() method is used to return a shallow copy of dictionary.
# dict1 = {1,2,3,4,5,6,6,7,7,8,9,0}
# dict2 = dict1.copy()
# print(dict2)  #  {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}  for number element it will put them in order from smallest to largest.

# dict3 = {'s','w','z','x','t'}
# dict4 = dict3.copy()
# print(dict4)  #  {'s', 'x', 't', 'w', 'z'}  for sequence of character or string it will put randomly.

#****************** Exercise 10: dict.fromkeys() method is used create a new dictionary with keys from seq and values set to value.
# seq1 = ('name','age','sex')
# dict1 = dict.fromkeys(seq1)
# print('new dictionary is such that : %s' %str(dict1))  # new dictionary is such that : {'name': None, 'age': None, 'sex': None}

# dict1 = dict1.fromkeys(seq1,10)
# print('new dictionary is such that : %s' %str(dict1))  # new dictionary is such that : {'name': 10, 'age': 10, 'sex': 10}

# seq2 = ('position','salary','career','phone','email','address')
# dict2 = dict.fromkeys(seq2)
# print('The new dictionary is such that : %s ' % dict2)
# # The new dictionary is such that : {'position': None, 'salary': None, 'career': None, 'phone': None, 'email': None, 'address': None}
# print('The new dictionary is such that :',dict2)
# # The new dictionary is such that : {'position': None, 'salary': None, 'career': None, 'phone': None, 'email': None, 'address': None}        
# seq3 = ['Senghort','Engineering','Computer Science','Data Science']
# dict3 = dict.fromkeys(seq3,2)
# print(dict3)   #  {'Senghort': 2, 'Engineering': 2, 'Computer Science': 2, 'Data Science': 2}

#****************** Exercise 11: dict.get(key,default=None) method is used to return value or default if key not in dictionary.
# dict = {'name':'senghort','sex':'male','age':20}
# print('value of age is : ',dict.get('age'))
# print('value of name is : ',dict.get('name'))
# print('value of sex is : ',dict.get('sex'))

# list  = ['Senghort','engineer',123]
# tuple = (1200,'Manager')
# dict  = {'Sex':'Male','Phone':'0974554582'}
# dict2 = {'ID':1200,'Name':list[0],'Career':list[1],'Position':tuple[1],'Salary':tuple[0],'Code':list[2],'Sex and Phone':dict}
# print('Name is : ',dict2.get('Name'))         # Name is :  Senghort
# print('Position is : ',dict2.get('Position')) # Position is :  Manager
# print('Salary is : ',dict2.get('Salary'))     # Salary is :  1200
# print('ID is : ',dict2.get('ID'))             # ID is :  1200
# print('Sex and Phone is : ',dict2.get('Sex and Phone'))  # Sex and Phone is :  {'Sex': 'Male', 'Phone': '0974554582'}

#****************** Exercise 12: dict.__hash__(key) is used to remove element that used the (in) operation instead.
# dict = {'Name':'Senghort','Sex':'male'}
# print(dict.__hash__('Name'))
# print(dict.__hash__('Sex'))

#****************** Exercise 13: dict.items() is used return a list of dict's(key,value) tuple pairs.
# dict = {'num1':1,'num2':34}
# print('Dictionary items is such that : %s' % dict.items())
# # Dictionary items is such that : dict_items([('num1', 1), ('num2', 34)])
# list  = ['Senghort','engineer',123]
# tuple = (1200,'Manager')
# dict  = {'Sex':'Male','Phone':'0974554582'}
# dict2 = {'ID':1200,'Name':list[0],'Career':list[1],'Position':tuple[1],'Salary':tuple[0],'Code':list[2],'Sex and Phone':dict}
# print('Dictionary items is such that : %s' % dict2.items())
# # Dictionary items is such that :
# # dict_items([('ID', 1200), ('Name', 'Senghort'), ('Career', 'engineer'), ('Position', 'Manager'), ('Salary', 1200), ('Code', 123),
# # ('Sex and Phone', {'Sex': 'Male', 'Phone': '0974554582'})])

#****************** Exercise 14: dict.keys() is used to return the list of all available keys in the dictionary. 
# list  = ['Senghort','engineer',123]
# tuple = (1200,'Manager')
# dict  = {'Sex':'Male','Phone':'0974554582'}
# dict2 = {'ID':1200,'Name':list[0],'Career':list[1],'Position':tuple[1],'Salary':tuple[0],'Code':list[2],'Sex and Phone':dict}
# print('The availale key in this dictionary is such that : ',dict2.keys())
# # The availale key in this dictionary is such that :  
# # dict_keys(['ID', 'Name', 'Career', 'Position', 'Salary', 'Code', 'Sex and Phone']) 

#****************** Exercise 15: dict.setdefault(key,default=None) : is similar to get(), but it will set dict[key] = default if key
# # is not already in dict.
# list  = ['Senghort','engineer',123]
# tuple = (1200,'Manager')
# dict  = {'Sex':'Male','Phone':'0974554582'}
# dict2 = {'ID':1200,'Name':list[0],'Career':list[1],'Position':tuple[1],'Salary':tuple[0],'Code':list[2],'Sex and Phone':dict}
# dict = {'Name':'Senghort','ID':123456,'Sex':'male'}
# print('Name :%s'%dict.setdefault('Name',None))  # Name :Senghort
# print('ID   :',dict.setdefault('ID',None))      # ID   : 123456

#****************** Exercise 16: dict.update(dict2) is used to adds dictionary dict2's key-values pairs to dict. 
# dict1 = {'Name':'Zara','ID':123456,'Sex':'male'}
# dict2 = {'Salary':1200,'Position':'Engineer'}
# dict1.update(dict2)
# dict2.update(dict1)
# print('Updated dictionary is such that : ',dict1)
# print('Updated dictionary is such that : ',dict2)
# # Updated dictionary is such that :  {'Name': 'Zara', 'ID': 123456, 'Sex': 'male', 'Salary': 1200, 'Position': 'Engineer'}
# # Updated dictionary is such that :  {'Salary': 1200, 'Position': 'Engineer', 'Name': 'Zara', 'ID': 123456, 'Sex': 'male'}

#****************** Exercise 17: dict.values() is used to return the list of all the available values in a given dictionary. 
# dict = {'Sex':'female','Age':21,'Name':'Nareth'}
# print('Values list : ',list(dict.values()))
# # Values list :  ['female', 21, 'Nareth']
# list1  = ['Senghort','engineer',123]
# tuple = (1200,'Manager')
# dict  = {'Sex':'Male','Phone':'0974554582'}
# dict2 = {'ID':1200,'Name':list1[0],'Career':list1[1],'Position':tuple[1],'Salary':tuple[0],'Code':list1[2],'Sex and Phone':dict}
# dict = {'Name':'Senghort','ID':123456,'Sex':'male'}
# print('Values List : ',list(dict2.values()))
# # Values List :  [1200, 'Senghort', 'engineer', 'Manager', 1200, 123, {'Sex': 'Male', 'Phone': '0974554582'}]

#****************** Exercise 18: 









#****************** Exercise 19:








#****************** Exercise 20:






#****************** Exercise 21:






#****************** Exercise 21:






#****************** Exercise 22:






#****************** Exercise 23:






#****************** Exercise 24:




