#=====================================================================================================================================
#==================================================== Chapter 8: List ===============================================================
#=====================================================================================================================================
#******************** Exercise 1: Introduction to list:
# list1 = ['physic','chemistry','mathematic',1999,2020]
# print('list1[0] :',list1[0])         # list1[0] : physic
# print('list1[1:5] : ',list1[1:5])    # list1[1:5] :  ['chemistry', 'mathematic', 1999, 2020]

# list2 = [1,2,3,4,5,6,7]
# print('list2[0] :',list2[0])         # list2[0] : 1
# print('list2[1:5] : ',list2[1:5])    # list2[1:5] :  [2, 3, 4, 5]

#******************** Exercise 2: Update data in list
list = ['physics','chemistry','math',1999,2000]
print('value available at index 2 : ',list[2])
list[2] = 2001
print('New value available at index 2 : ',list[2])
print(list)
# Output:
      # value available at index 2 :  math
      # New value available at index 2 :  2001
      # ['physics', 'chemistry', 2001, 1999, 2000]

# list1 = ['I','am a','student','at Institute','of Technology','of Cambodia']
# list1[0] = 'She'
# list1[1] = 'is a'
# list1[2] = 'doctor at'
# list1[3] = 'National Polytechnic'
# list1[4] = 'Institutue'
# print('list1 = ',list1)
# list1[3] = 'University of'
# list1[4] = 'Medicine'
# list1[5] = 'in Cambodia'
# print('list1 = ',list1)

# Output:
         # list1 =  ['She', 'is a', 'doctor at', 'National Polytechnic', 'Institutue', 'of Cambodia']
         # list1 =  ['She', 'is a', 'doctor at', 'University of', 'Medicine', 'in Cambodia']

#******************** Exercise 3: Delete data in list:
# list1 = ['physic','chemistry','mathematic',1997,2000]
# del list1[0]
# del list1[1]
# del list1[2]
# print('The list after deletion is such that :',list1)    # The list after deletion is such that : ['chemistry', 1997]

# list = ['Dara',456,'Daro',5454,'Nary']
# for i in range(5):
#    print('Enter new string['+str(i)+'] : ',end='')
#    list[i] = input()
# print('List after update data :',list)
# Output:
         # Enter new string[0] : Kry Senghort
         # Enter new string[1] : is a
         # Enter new string[2] : handsome
         # Enter new string[3] : man in
         # Enter new string[4] : Institute of Technology of Cambodia
         # List after update data : ['Kry Senghort', 'is a', 'handsome', 'man in', 'Institute of Technology of Cambodia']

#******************** Exercise 4: Basic List Operations : length, concatenate, repeatition, membership and iteration.
# Length method:
# list1 = [1,2,3,4,5,6]
# x = len(list1)
# print(x)     # 6
# print(len(['dara','dina','khemarak',12,45,66,'your','name']))   # 8

# Concatenate method:
# list2 = ['Senghort','clever','student',2002]
# list3 = list2 + list1
# print(list3)    # ['Senghort', 'clever', 'student', 2002, 1, 2, 3, 4, 5, 6]
# list4 = list1 + list2
# print(list4)    # [1, 2, 3, 4, 5, 6, 'Senghort', 'clever', 'student', 2002]

# Repeatition method:
# x = ['Senghort','Srey Ya',434]
# y = x*3
# print('list x after repetition for three time are such that :',y)
# list x after repetition for three time are such that : 
#                                   ['Senghort', 'Srey Ya', 434, 'Senghort', 'Srey Ya', 434, 'Senghort', 'Srey Ya', 434]

# Membership method:
# m = [1,2,'Seyma','Sarath',45,90]
# n = 4
# o = 'Seyma'
# y = 'seyma'
# z = 'sarath'
# print(n in m)  # False
# print(y in m or o in m)  # True
# print(z in m and o in m) # False

# Iteration method:  is used to break the element from the list.
# for x in [1,2,3,4,5,6]:
#    print(x,end=',')   # 1,2,3,4,5,6,
# print('\n')
# for y in ['Sara','Lina',43,'Senghy',4343]:
#    print(y,end=' ')   # Sara Lina 43 Senghy 4343

#******************** Exercise 5: Indexing, Slicing and Matrixes:
# list = ['c++','java','python']
# x = list[2]
# y = list[-2]
# z = list[1:]
# print(x)     # python
# print(y)     # java
# print(z)     # ['java', 'python']
# print(list[:1])  # ['c++']

#******************** Exercise 6: min() and max() methods are used to show the minimum and maximum value of element in the list.
# list1 = ['dara','daro','you','are','my girlfriend']
# list2 = [4,6,9,8,9,7,5]
# print(max(list1))
# print(max(list2))

# list3 = [12,3,5,6,8,7,5,3,2]
# list4 = [45,454,67,89,674,34,89]
# list5 = [45,76,89,90,5,45,56]
# print(max(list3,list4,list5))
# print(min(list3,list4,list5))

# list6 = ['dara','senghort','python','anaconda','jupyter','visual studio','javascript']
# list7 = ['daddy','mother','father','mom','brother','daughter']
# list8 = ['water','carbon','oxygen','hydrogen']
# print(max(list6,list7,list8))
# print(min(list6,list7,list8))
# Output:
         # you
         # 9
         # [45, 454, 67, 89, 674, 34, 89]
         # [12, 3, 5, 6, 8, 7, 5, 3, 2]
         # ['water', 'carbon', 'oxygen', 'hydrogen']
         # ['daddy', 'mother', 'father', 'mom', 'brother', 'daughter']

#******************** Exercise 7: list() method is used to take sequence types and converts them to lists. this is used to convert a
# given tuple into list. Note : tuple are similar to list with only different such that element values of tuple cannot be changed and
# tuple element are put between parentheses instead of square bracket. This function also converts characters in a string into a list.
# tuple = (123,'C++','java','python')
# list1 = list(tuple)
# print('list elements are such that :',list1)    # list elements are such that : [123, 'C++', 'java', 'python']

# string = 'Hello World!!'
# list2 = list(string)
# print('list elements are such that :',list2)
# # list elements are such that :['H', 'e', 'l', 'l', 'o', ' ', 'W', 'o', 'r', 'l', 'd', '!', '!']

#******************** Exercise 8: list.append(obj): is used to append object to the list.
# list1 = ['C++','Java','Python','Html','Css']
# list1.append('C#')
# list1.append('C')
# print('Update data in list :',list1)  # Update data in list : ['C++', 'Java', 'Python', 'Html', 'Css', 'C#', 'C']

#******************** Exercise 9: list.count(obj) : is used to return count of how many times obj occurs in list.
# list1 = ['dara','senghort',122,34,56,65,45,'leakhena','sreyleak',122]
# print('Count for 122 =',list1.count(122))
# print('Count for abc =',list1.count('abc'))

# list2 = [123,'abc',34,6,67,123,'xyz','xyz','zara','abc',980]
# print('count for zara =',list2.count('zara'))
# print('Count for 65 =',list2.count(65))
# Output:
            # Count for 122 = 2
            # Count for abc = 0
            # count for zara = 1
            # Count for 65 = 0

#******************** Exercise 10: list.extend(seq) : is used to append the contents of seq to list.
# list1 = ['mathématique','physique','chimique','biologique']
# list2 = list(range(3)) # create lists of numbers between 0 to 4.
# list1.extend(list2)
# print('The list after extended is such that : ',list1)
##    The list after extended is such that :  ['mathématique', 'physique', 'chimique', 'biologique', 0, 1, 2]

# list3 = ['Biotechnologique','généralement']
# list1.append(list3)
# print(list1)
##    ['mathématique', 'physique', 'chimique', 'biologique', 0, 1, 2, ['Biotechnologique', 'généralement']]

#******************** Exercise 11: list.index(obj) : is used to return the lowest index in list that obj appears.
# list = ['physique','mathematic','mécaniquellement','chimique','thermodynamique','gestion','comptabilité']
# print('Index of chemistry is :',list.index('chimique'))
# print('Index of mathematic is :',list.index('mathematic'))
# print('Index of mécaniquellement is :',list.index('mécaniquellement'))
# Output:
            # Index of chemistry is : 3
            # Index of mathematic is : 1
            # Index of mécaniquellement is : 2

#******************** Exercise 12: list.insert(index,obj) : is used to insert object obj into list at offset index.
# list = ['physic','chemistry','math']
# list.insert(2,'Bilogy')
# list.insert(0,'History')
# print(list)
# # Output:   ['History', 'physic', 'chemistry', 'Bilogy', 'math']

# list1 = ['Senghort','Seyha','Saray',123,567,879,890]
# list1.insert(9,'dfdf')
# print(list1)
# # Output:    ['Senghort', 'Seyha', 'Saray', 123, 567, 879, 890, 'dfdf']

#******************** Exercise 13: list.pop() : is used to removes and returns last object or obj from list.
# list = ['physic','chemistry','biology','mathematic','biotechnology']
# list.pop()    # it used FIFO method (first in first out) like the queue operation.
# print('list now : ',list)  # list now :  ['physic', 'chemistry', 'biology', 'mathematic']
# list.pop(1)   # it delete or pop with specific index that is given.
# print('list after pop(1) is :',list)  # list after pop(1) is : ['physic', 'biology', 'mathematic']

# list.pop(2) 
# print(list)  #  ['physic', 'biology']

# list.pop(1)
# list.pop(0)
# print(list) # []

#******************** Exercise 14: list.remove(obj): is used to remove object obj from list.
# list = ['abc','xyz','mno',123,567,980,978,'ax+b']
# list.remove('abc')
# print('list now is such that :',list)   # list now is such that : ['xyz', 'mno', 123, 567, 980, 978, 'ax+b']

# list.remove(123) or list.remove('xyz') or list.remove('ax+b')   # we use or to sum the remove method on the same list.
# print('list now is such that :',list)   # list now is such that : ['mno', 567, 980, 978]

# list.remove('mno') or list.remove(567)
# print(list)     # [980, 978]

#******************** Exercise 15: list.reverse() : is used to reverses(បញ្ច្រាសធាតុ​ backward) objects of list.
# list = ['Senghort','Dina','Ramol','Leakhena','Kimhean','Soriya',4343,434,788,56,8998]
# list.reverse()
# print('list after reverse or backward is such that : \n',list)
# list after reverse or backward is such that : 
# [8998, 56, 788, 434, 4343, 'Soriya', 'Kimhean', 'Leakhena', 'Ramol', 'Dina', 'Senghort']

#******************** Exercise 16: list.sort([func]): is used to sorts objects of list, using compare function if given.
# list = ['physic','biology','chemistry','mathematic']
# list.sort()
# print(list)   # ['biology', 'chemistry', 'mathematic', 'physic']

# list = [1,9,7,99,0,7,5,90,78,69,45,23]
# list.sort()
# print(list)   #  [0, 1, 5, 7, 7, 9, 23, 45, 69, 78, 90, 99]

#******************** Exercise 16: Used the all above operation methods to analyze on list that is given below.














