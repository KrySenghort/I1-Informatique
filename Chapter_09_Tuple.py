#=====================================================================================================================================
#==================================================== Chapter 09: Tuple =============================================================
#=====================================================================================================================================
# tuple is a sequence of immutable python objects. it just like lists, but different just only with list such that tuple cannot be 
# changed element like list. On the other hand, tuple use parentheses whereas list use square brackets.

#********************* Exercise 01: Accessing values in the tuples.
# tuple1 = ('physic','chemistry',997,2000)
# tuple2 = (1,2,3,4,5)
# tuple3 = ('a','b','c','d')
# tuple4 = ()
# print(tuple1[0])     # physic
# print(tuple1[2])     # 1997
# print(tuple1[1:3])   # ('chemistry', 1997)

# print(tuple2[3])     # 4
# print(tuple2[4])     # 5
# print(tuple2[0:3])   # (1, 2, 3)

# print(tuple3[0])     # a
# print(tuple3[1])     # b
# print(tuple3[2:4])   # ('c', 'd')   
# # for tuple in case, we assign value of index 4-th in the list, it has no error that is not like the list. 

# print(tuple4[0])     # no result
# print(tuple4[1])     # no result     because of no element in the list.
# print(tuple4[2])     # no result    

#********************* Exercise 02: Update data in the tuple
# # Remark : we cannot change the value of element in the list but we can take portions of the existing tuples to create new tuples 
# # as the following example demonstrates.
# tup1 = (12,34,56)
# tup2 = ('abc','xyz')
# tup3 = tup1+tup2
# print(tup3)   # (12, 34, 56, 'abc', 'xyz')
# # this method is unavailable for tuples.  # tup1[0] = 100

#******************** Exercise 03: Delete data in the tuples.
# # Remark : Removing individual tuple elements is not possible. there is, of course, nothing wrong with putting together another 
# tuple with the undesired element discarded.
# tup = ('physics','chemistry',1997,2000)
# del tup
# print('After deletion tup : ')
# print(tup)
# # Output:  an exception is raised. this is because after del tup, tuple does not exist anymore.
         # After deletion tup :
         # Traceback (most recent call last):
         #   File "d:\Year 01\Informatique\Basic to Advance Python\Basic Python\Chapter_09_Tuple.py", line 44, in <module>
         #     print(tup)
         # NameError: name 'tup' is not defined

#********************* Exercise 04: Basic Tuple Operations.
# # Length method
# tuple = (1,2,3,4,5,6,7,8,9,10)
# print(len(tuple))    # 10
# tuple = ('Senghort','Daro','Darith','Sreyneang','Darith')
# print(len(tuple))    # 5

# # Concatenation method
# tuple1 = (1,2,3,4,5)
# tuple2 = (4,3,5,6,7,8)
# tuple3 = tuple1+tuple2
# print(tuple3)         #   (1, 2, 3, 4, 5, 4, 3, 5, 6, 7, 8)

# # Repetition method
# tuple = ('Hi','Seyha','How are','you doing ?')
# tuple2 = tuple*3
# print(tuple2)
# #   ('Hi', 'Seyha', 'How are', 'you doing ?', 'Hi', 'Seyha', 'How are', 'you doing ?', 'Hi', 'Seyha', 'How are', 'you doing ?')

# # tuple = (1,2,3,4,5,6,8,6,4)
# print(3 in tuple)    # True
# tuple = ('naro','nareth','khemarak','Senghy','Seyha','Kimhor','Sophy')
# string1 = 'Senghy'
# string2 = 'Nareth'
# s = string1 in tuple
# t = string2 in tuple
# print(s)       # True
# print(t)       # False
# print(s and t) # False 
# print(s or t)  # True

# # Iteration method
# for x in (1,2,3,4,5,5,8,9,6):
#    print(x,end=' ')     # 1 2 3 4 5 5 8 9 6 
# print('\n')
# tuple = ('Dareth','Daroth','yahoo',323,454,676,434,787)
# for y in tuple:
#    print(y,end=' ; ')   # Dareth ; Daroth ; yahoo ; 323 ; 454 ; 676 ; 434 ; 787 ;

# #********************* Exercise 05: Indexing, Slicing and Matrixes
# tuple = (1,2,3,4,5,6,7,'python','java','c#')
# print(tuple[7])     # python
# print(tuple[-3])    # python  # if negeative index, it will count from the right hand side.
# print(tuple[1:])    # (2, 3, 4, 5, 6, 7, 'python', 'java', 'c#')
# print(tuple[2:10])  # (3, 4, 5, 6, 7, 'python', 'java', 'c#')
# print(tuple[2:-2])  # (3, 4, 5, 6, 7, 'python')

#********************* Exercise 06: Minimum & Maximum value in the tuple.
# tuple1 = ('python','math','physic','chemistry')
# tuple2 = (256,700,34,55)
# print("Max value in tuple1 is : ",max(tuple1))       # Max value in tuple1 is :  python
# print('Minimum value in tuple1 is : ',min(tuple1))   # Minimum value in tuple1 is :  chemistry

# print("Max value in tuple2 is : ",max(tuple2))       # Max value in tuple2 is :  700
# print('Minimum value in tuple2 is : ',min(tuple2))   # Minimum value in tuple2 is :  34

#********************* Exercise 07: tuple() method is used convets a list of items into tuples.
# list = ['math','physic','chemistry',3,4,7,8,9]
# tuple = tuple(list)
# print(tuple)  # ('math', 'physic', 'chemistry', 3, 4, 7, 8, 9)















