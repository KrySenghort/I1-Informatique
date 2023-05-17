#=====================================================================================================================================
#==================================================== Chapter 07: String =============================================================
#=====================================================================================================================================
#===================================================== Part 01: Escape Character =====================================================
# a   : bell or alert
# b   : backspace
# \cx : control-x
# \e  : escape
# \f  : formfeed
# \n  : new line
# \nnn: octal notation, where n in the range 0.7
# \r  : carriage return 
# \s  : space
# \t  : tab
# \v  : vertical tab
# \x  : character x
#================================================= Part 02: String Special Operators =================================================
#  a = "Hello", b="Python"
#  +      : concatenate the strings. Ex: a+b ==> HelloPython
#  *      : repetition - create new strings, concatenating multiple copies of the same string. Ex: a*2 ==> HelloHello
#  []     : slice-gives the character from the given index. Ex: a[1] ==> e 
#  [:]    : range slice-gives the characters from the given range. Ex: a[1:4] ==> ell
#  in     : membership- returns true if a character exists in the given string. Ex: H in a ==> 1
#  not in : membership- returns true if a character does not exist in the given string. Ex: M not in a ==> 1
#  r/R    : raw string- supresses actual meaning of escape character
#================================================ Part 03: String Formatting Operators ==============================================  
# %c         : character
# %s         : string conversion via str() prior to formatting
# %i or %d   : signed decimal integer
# %u         : unsigned decimal integer
# %o         : octal integer
# %x         : hexadecimal integer(lowercase letters)
# %X         : hexadecimal integer(uppercase letters)
# %e         : exponential notation(with lowercase 'e')
# %E         : exponential notation(with uppercase 'e')
# %f         : floating point real number
# %g         : the shorter of %f and %e
# %G         : the shorter of %f and %E
#=============================================== Part 04: Built in String Methods ===================================================

# (1). capitalize() : is used to capitalize the first letter of string.

# (2). center(width,fillchar) : is used to return a string padded with fillchar with the original string centered to a total of width 
# columns. 

# (3). count(str,beg=0,end=len(string)) : counts how many times str occurs in string or in a substring of string if starting index 
# beg and ending index end are given.

# (4). decode(encoding='UTF-8',errors='strict') : convert form of code to information then display. Decode the string using the 
# codec registered for encoding. encoding defaults to the default string encoding.

# (5). encode(encoding = 'UTF-8',errors='strict') : convert data becoming code form or instruction. Return encoded string version of 
# string; on error, default is to raise a ValueError unless errors is given with 'ignore' or 'replace'.

#(6). endswith(suffix,beg=0,end=len(string)) : determine if string or a substring of string(if starting index beg and ending index 
# end are given) ends with suffix; returns true if so and false otherwise.

# (7). expandtabs(tabsize=8) : multiple spaces; default to 8 spaces per tab if tabsize not provided.

# (8). find(str,beg=0,end=len(string)) : determine if str occurs in string or in a substring of string if starting index beg and 
# ending index end are given return index if found and -1 otherwise.

# (9). index(str,beg=0,end=len(str)) : same as find() above but raise an exception if str not found.

# (10). isalnum() : return true if string has at least 1 character and all characters are alphanumeric and false otherwise.

# (11). isalpha() : return true if string has at least 1 character and all characters are alphabetic and false otherwise.

# (12). isdigit() : return true if the string contains only digits and false otherwise.

# (13). islower() : return the true if string has at least 1 case character and all cased characters are in lowercase and false 
# otherwise.

# (14). isnumeric() : return true if a unicode string has only numeric characters and false otherwise.

# (15). isspace() : return true if string has only whitespace characters and false otherwise.

# (16). istitle() : return true if string is properly "titlecased" and false otherwise.

# (17). isupper() : return true if string has at least one cased character and all cased character are in uppercase and false 
# otherwise.

# (18). join(seq) : merges(Concatenates) the string representations of elements in sequence seq into a string, with Separator.

# (19). len(string) : return the length of the string.

# (20). ljust(width[,fillchar]) : return a space-padded string with the original string left-justified to a total of width colums.

# (21). lower() : convert all uppercase letter in the string becoming lowercase at all.

# (22). lstrip() : removes all leading whitespace in string.

# (23). maketrans() : return a translation table to be used in translate function.

# (24). max(str) : return the max alphabetical Character from the string str.

# (25). min(str) : return the min alphabetical Character from the string str.

# (26). replace(old,new[,max]): replace all occurrences of old in string with new or at most max occurrences if max given. 

# (27). rfind(str,beg=0,end=len(str)) : same as find() but search backward in string.

# (28). rindex(str,beg=0,end=len(str)) : same as index() but search backward in string.

# (29). rjust(width,[,fillchar]) : return a space-padded string with the original stirng right-justified to a total of width columns.

# (30). rstrip() : remove all trailing whitespace of string.

# (31). spit(str="",num=string.count(str)) : spits string according to delimiter str(space if not provided) and returns of substrings; 
# split into at most num substrings if given.

# (32). splitlines(num=string.count('\n')) : splits string at all (or num) newline and returns a list of each line with newlines 
# removed.

# (33). startswidth(str,beg=0,end=len(string)) : determines if string or a substring of string(if starting index beg and ending index end 
# are given) start with substring str; return true if so and false otherwise.

# (34). strip([chars]) : performs both lstrip() and rstrip() on string.

# (35). swapcase() : inverts case for all letters in string.

# (36). title() : return "titlecased" version of string, that is, all words begin with uppercase and the rest are lowercase.

# (37). translate(table,deletechars="") : translate string according to translation table str(256 chars), removing those in the 
# del string.

# (38). upper() : converts lowercase letters in string to uppercase.

# (39). zfill(width) : return original string leftpadded with zeros to a total of width characters; intended for numbers, zfill() 
# retains any sign given(less one zero).

# (40). isdecimal() : return true if a unicode string has only decimal characters and false otherwise.

#====================================================== Practice ====================================================================
# print("I am a man who did it at the last day.\n Do you have any free time.")
# print("\t Do you have any meeting with another")
# # Analyze the string.
# print("Kry\Senghort")
# print("Kry\"Senghort")            # Kry"Senghort

#******************* Exercise 1: capitalize() : is used to capitalize the first letter of string.
# a = "kry senghort"
# b = 'cambodia kingdom of wonder !'
# c = "i am a data scientist in cambodia"
# x = str.capitalize(a)
# y = str.capitalize(b)
# z = str.capitalize(c)
# print("Capitalize begining word are such that:\n",x,'\n',y,'\n',z)
# Output:
# Capitalize begining word are such that: 
#  Kry senghort 
#  Cambodia kingdom of wonder !
#  I am a data scientist in cambodia

#********************* Exercise 2: center(width,fillchar) : is used to return a string padded with fillchar with the original string
# centered to a total of width columns. fillchar = fill character. 
# str = "This is string example...wow!!!"
# print("str.center(40,a) : ",str.center(40,'a'))
# print("str.center(40,a) : ",str.center(40,'b'))
# print("str.center(40,a) : ",str.center(40,'2'))
# print("str.center(40,a) : ",str.center(40,'#'))
# print("str.center(40,a) : ",str.center(40,'+'),'\n')

# print("str.center(60,a) : ",str.center(60,'a'))
# print("str.center(60,a) : ",str.center(60,'b'))
# print("str.center(60,a) : ",str.center(60,'2'))
# print("str.center(60,a) : ",str.center(60,'#'))
# print("str.center(60,a) : ",str.center(60,'+'),"\n")

# print("str.center(100,a) : ",str.center(100,'a'))
# print("str.center(100,a) : ",str.center(100,'b'))
# print("str.center(100,a) : ",str.center(100,'2'))
# print("str.center(100,a) : ",str.center(100,'#'))
# print("str.center(100,a) : ",str.center(100,'+'))

# Output:
        # str.center(40,a) :  aaaaThis is string example...wow!!!aaaaa
        # str.center(40,a) :  bbbbThis is string example...wow!!!bbbbb
        # str.center(40,a) :  2222This is string example...wow!!!22222
        # str.center(40,a) :  ####This is string example...wow!!!#####
        # str.center(40,a) :  ++++This is string example...wow!!!+++++

        # str.center(60,a) :  aaaaaaaaaaaaaaThis is string example...wow!!!aaaaaaaaaaaaaaa
        # str.center(60,a) :  bbbbbbbbbbbbbbThis is string example...wow!!!bbbbbbbbbbbbbbb
        # str.center(60,a) :  22222222222222This is string example...wow!!!222222222222222
        # str.center(60,a) :  ##############This is string example...wow!!!###############
        # str.center(60,a) :  ++++++++++++++This is string example...wow!!!+++++++++++++++

        # str.center(100,a) :  aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaThis is string example...wow!!!aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
        # str.center(100,a) :  bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbThis is string example...wow!!!bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        # str.center(100,a) :  2222222222222222222222222222222222This is string example...wow!!!22222222222222222222222222222222222
        # str.center(100,a) :  ##################################This is string example...wow!!!###################################
        # str.center(100,a) :  ++++++++++++++++++++++++++++++++++This is string example...wow!!!+++++++++++++++++++++++++++++++++++

#********************* Exercise 3: count(str,beg=0,end=len(string)) : counts how many times str occurs in string or in a substring of
# string if starting index beg and ending index end are given. syntax is : str.count(str,beg=0,end=len(string))
# str = "this is string example....wow!!!. Do you want to play this game with me ?"
# sub1 = 'i'
# print("str.count('i') : ",str.count(sub1))

# sub2 = 'exam'
# print("str.count('exam') : ",str.count(sub2))
# print("str.count('exam',10,40) : ",str.count(sub2,10,40))

# sub3 = 's'
# print("str.count('s',0,10) : ",str.count(sub3,0,7))

# sub4 = 'this'
# print("str.count('this',0,30) : ",str.count('this',0,30))

# Output:
                # str.count('i') :  5
                # str.count('exam') :  1
                # str.count('exam',10,40) :  1
                # str.count('s',0,10) :  2
                # str.count('this',0,30) :  1

#********************* Exercise 4: decode(encoding='UTF-8',errors='strict') : convert form of code to information then display. 
# (1). Decode the string using the codec registered for encoding. encoding defaults to the default string encoding.
# from base64 import decode
# (2). encode(encoding = 'UTF-8',errors='strict') : convert data becoming code form or instruction. Return encoded string version of 
# string; on error, default is to raise a ValueError unless errors is given with 'ignore' or 'replace'.

# from cgitb import text
# alphabet = ['a123','b5','3c','d78','9e','0f','7g','9h','5i','7j','9k','l7','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
# def encode(string):
#         returnText=""
#         for char in string:
#                 if not char in alphabet:
#                         returnText += char
#                 else:
#                         returnText += alphabet[(alphabet.index(char)+2)%26]
#         return returnText
# action = input("Would you like to encode or decode ? ")

# if action=='encode':
#         print((encode(action)))
# elif action=='decode':
#         print(decode(action))
# else:
#         print("no operation.")
#=================================
# import base64
# def main():
#         data = 'data to be encoded'
#         encoded = data.encode("utf-8")
#         b16encoded = base64.b16encode(encoded)
#         print(b16encoded)
#         print(base64.b16decode(b16encoded).decode("utf-8"))
# if __name__ == "__main__":
#         main()
# Output:
                # b'6461746120746F20626520656E636F646564'
                # data to be encoded

#********************* Exercise 5: endswith(suffix,beg=0,end=len(string)) : determine if string or a substring of string
# (if starting index beg and ending index end are given) ends with suffix; returns true if so and false otherwise.
# suffix : this could be a string or could also be a tuple of suffixes to look for 
# a = 'this is string example,.......wow!!!'
# suffix = '!!'
# print(a.endswith(suffix))      # True
# print(a.endswith(suffix,20))   # True  : for this case if we modify beg = arbitrary then it will display false, because of !! is not at the end. 
# suffix = 'exam'
# print(a.endswith(suffix))      # False
# print(a.endswith(suffix,0,19)) # True
# print(a.endswith(suffix,4,12)) # False
# suffix = 'wow' 
# print(a.endswith(suffix,2,7))  # False
# print(a.endswith(suffix))      # False
# b = 's'
# print(a.endswith(b,2,13))
# Output:
        # True
        # True
        # False
        # True
        # False
        # False
        # False

#********************* Exercise 6: expandtabs(tabsize = 8) : multiple spaces; default to 8 spaces per tab if tabsize not provided.
# a = "this is\tstring example....wow !!!" 
# print('Original String      :' + a)
# print("default expanded tab :" + a.expandtabs(8))
# print('Double expanded tab  :' + a.expandtabs(16))

# b = 'aaa\taadd\tfkdjdk\tfjdjfkgjfkgjf'
# print('Original String      :' + b)
# print("default expanded tab :" + b.expandtabs(20))
# print('Double expanded tab  :' + b.expandtabs(16))

# Output:
# Original String      :this is   string example....wow !!!
# default expanded tab :this is string example....wow !!!
# Double expanded tab  :this is         string example....wow !!!

# Original String      :aaa       aadd    fkdjdk  fjdjfkgjfkgjf
# default expanded tab :aaa                 aadd                fkdjdk              fjdjfkgjfkgjf
# Double expanded tab  :aaa             aadd            fkdjdk          fjdjfkgjfkgjf

#********************** Exercise 7: find(str,beg=0,end=len(string)) : determine if str occurs in string or in a substring of string 
# if starting index beg and ending index end are given if found it return index number, and if not found it return -1 .
# a = 'this is string example....wow!!!'
# b = 'exam'
# print(a.find(b))
# print(a.find(b,4))
# print(a.find(b,0,18))
# c = 'wow'
# print(a.find(c))
# print(a.find(c,9))
# print(a.find(c,9,15))
# Output:
        # 15
        # 15
        # -1
        # 26
        # 26
        # -1

#*********************** Exercise 8: index(str,beg=0,end=len(str)) : same as find() above but raise an exception if str not found.
# if not found it will display the error result. but if found it will display the index number of that substring in the string.
# a = "I am a single man who like to play the game with my brother."
# b = 'man'
# print(a.index(b))
# print(a.index("am",9))
# print(a.index("like to play the game"))
# c = "single"
# print(a.index(c))
# print(a.index('game'))
# d = 'play'
# print(a.index(d))
# print(a.index('brother'))

# phrase = 'Giraffe Academy'
# # return the length of string or number of characters.
# print(len(phrase))                
# # This section is used to return the letter that we want to know while we have already known their index.
# print(phrase[0])    # G
# print(phrase[1])    # i
# print(phrase[5])    # f
# print(phrase[9])    # A
# # index function is used to return the location or index of the letter or some part of string which# we want to modify.
# print(phrase.index("G"))    # 0
# print(phrase.index("a"))    # 3
# print(phrase.index("i"))    # 1
# print(phrase.index("r"))    # 2
# print(phrase.index('f'))    # 4
# print(phrase.index("Giraffe"))  # 0
# print(phrase.index("Academy"))  # 8
# print(phrase.index("raffe"))    # 2
# print(phrase.index("demy"))     # 11

# Output:
        # 14
        # 40
        # 22
        # 7
        # 39
        # 30
        # 52

#*********************** Exercise 9: isalnum() : return true if string has at least 1 character and all characters are alphanumeric 
# and false otherwise. if has no space it will return true, and otherwise it will return false.
# w = "this2016" # no space in this string
# print(w.isalnum()) # True

# x = 'this 2016'
# print(x.isalnum()) # False

# y = "this is my present that i want to send to you for the birthday."
# print(y.isalnum()) # False

# z = "ifyouareamaninthisplace"
# print(z.isalnum()) # True
# Output:
                # True
                # False
                # False
                # True

#************************ Exercise 10: isalpha() : return true if string has all character without including space, number and any
# symbol and false otherwise.
# a = 'this' # no space & digit in this string.
# print(a.isalpha())  # True

# b = 'yournameissenghortandhowaboutyou'
# print(b.isalpha())  # True

# c = "this is string example...wow!!!"
# print(c.isalpha())  # False

# d='thisisstringexample...wow' # if have any symbol such as: + - / * ! @ # and another symbols it will display error. despite no space
# print(d.isalpha())  # False

# e = 'dara2018'
# print(e.isalpha())  # False. if have no space but has string include the number it will display false.

# Output:
# True
# False

#************************ Exercise 11: isdigit() : return true if the string contains only digits and false otherwise.
# string = '123456' # only digit in this string.
# print(string.isdigit()) # True

# string = 'i am 34 years old.'
# print(string.isdigit())  # False

# string = "abcdef123456"
# print(string.isdigit())  # False

# string = 'this is string example...wow!!!'
# print(string.isdigit())  # False

# string = "059485948983902849584734873483943"
# print(string.isdigit())  # True

# string = '0594 85948 9839028 4958473 48734 83943'  # space is also a variable in the string so this case consist space and number.
# print(string.isdigit())  # False
# Output:
        # True
        # False
        # False
        # False
        # True 
        # False

#************************ Exercise 12: islower() Vs isupper() : are used to clarify that it is uppercase or lowercase.
# islower() : return true if string has at least 1 case character and all cased characters are in lowercase and false otherwise. 
# isupper() : return true if string has at least 1 cased character and all cased character are in uppercase and false otherwise.
# a = 'Hello i am a handsome man and today nice to meet you !'
# print(a.isupper()) # False
# print(a.islower()) # False

# b = 'MY NAME IS SENGHORT AND I WILL MAKE A PRESENTATION IN THIS ROOM.'
# print(b.isupper()) # True
# print(b.islower()) # False

# c = 'i am a best man in the world.'
# print(c.isupper()) # False
# print(c.islower()) # True

# d = 'I Am A Best Man In The World.'
# print(d.isupper()) # False
# print(d.islower()) # False

# phrase = "Giraffe Academy"        
# print(phrase+" is a cool man.")   # Giraffe is a cool man
# print(phrase.lower())             # giraffe academy
# print(phrase.upper())             # GIRAFFE ACADEMY
# # Modify it as lower or upper just one way.
# print(phrase.isupper())           # false
# print(phrase.islower())           # false
# # islower and isupper is used to check or exact on it. It will return true when islower or isupper are right based on the string.
# print(phrase.lower().islower())   # true : mean that first, it convert to lower and then check to modify it as lower 
# print(phrase.upper().isupper())   # true : 
# print(phrase.upper().islower())   # false: 
# print(phrase.lower().isupper())   # false: 

# Output:
        # False
        # False
        # True
        # False
        # False
        # True
        # False
        # False

#************************ Exercise 13: lower() Vs upper() are used to conver the string becoming lowercase or uppercase letter at all.
# lower() : convert all uppercase letter in the string becoming lowercase at all.
# upper() : converts lowercase letters in string to uppercase.
# a = 'Hello i am a handsome man and today nice to meet you !'
# print(a.upper()) 
# print(a.lower())
# print(a.capitalize()) 
# print('\n')
# b = 'MY NAME IS SENGHORT AND I WILL MAKE A PRESENTATION IN THIS ROOM.'
# print(b.upper()) 
# print(b.lower()) 
# print(a.capitalize()) 
# print('\n')
# c = 'i am a best man in the world.'
# print(c.upper()) 
# print(c.lower()) 
# print(a.capitalize()) 
# print('\n')
# d = 'I Am A Best Man In The World.'
# print(d.upper()) 
# print(d.lower()) 
# print(a.capitalize()) 

# Output:
        # HELLO I AM A HANDSOME MAN AND TODAY NICE TO MEET YOU !
        # hello i am a handsome man and today nice to meet you !
        # Hello i am a handsome man and today nice to meet you !

        # MY NAME IS SENGHORT AND I WILL MAKE A PRESENTATION IN THIS ROOM.
        # my name is senghort and i will make a presentation in this room.
        # Hello i am a handsome man and today nice to meet you !

        # I AM A BEST MAN IN THE WORLD.
        # i am a best man in the world.
        # Hello i am a handsome man and today nice to meet you !

        # I AM A BEST MAN IN THE WORLD.
        # i am a best man in the world.
        # Hello i am a handsome man and today nice to meet you !

#************************ Exercise 14: max(str) and min(str) are used to display the max or min character in string that comparison
# depends on the order of alphabet in english.
# max(str) : return the max alphabetical Character from the string str.
# min(str) : return the min alphabetical Character from the string str.
# a = 'Do you want to go here with me ?'
# print("The max character is :",max(a))
# print("The min character is :",min(a))

# b = 'zero is the number'
# print("The max character is :",max(b))
# print("The min character is :",min(b))

# c = 'i am a man and she is a girl'
# print("The max character is :",max(c))
# print("The min character is :",min(c))

# d = 'www.tutorialpoint.com'
# print("The max character is :",max(d))
# print("The min character is :",min(d))

# e = 'TUTORIALPOINT'
# print("The max character is :",max(e))
# print("The min character is :",min(e))

# f = '`~=-*/+><?\|@#$%^&*(),.'
# print("The max character is :",max(f))
# print("The min character is :",min(f))

# Output:
        # The max character is : y
        # The min character is :  
        # The max character is : z
        # The min character is :
        # The max character is : s
        # The min character is :
        # The max character is : w
        # The min character is : .
        # The max character is : U
        # The min character is : A
        # The max character is : ~
        # The min character is : #
# Remark : space is the minimum alphabet so, min(sting) will display empty or no result. In addition any symbols also consider as 
# min(string). but space is smaller than symbol.

#****************** Exercise 15: join(seq) Vs len(string) are used to merge and show the length of string which are given.
# join(seq) : merges(concatenates) the string representations of elements in sequence seq into a string, with separator.
# a = '-'
# seq = ('a','b','c','d','e','f','g','h')  # is sequence of the string.   
# print(a.join(seq))      #   a-b-c-d-e-f-g-h

# b = '+'
# seq = ('my','name','is','senghort','kry')
# print(b.join(seq))      #   my+name+is+senghort+kry

# c = '='
# string = ('data','science','is','a','best','department','in','ITC.') 
# print(c.join(string))   #   data=science=is=a=best=department=in=ITC.

# # len(string) : return the length of the string.
# x = 'i am a single man in ITC.'
# y = 'you are working hard'
# z = 'ITC is a best engineering institute in Cambodia.'
# print(len(x))   # 25
# print(len(y))   # 20
# print(len(z))   # 48

# Output:
        # a-b-c-d-e-f-g-h
        # my+name+is+senghort+kry
        # data=science=is=a=best=department=in=ITC.
        # 25
        # 20
        # 48

#****************** Exercise 16: isnumeric() : return true if a unicode of string has only numeric characters and false otherwise.
# a = 'this2016'
# print(a.isnumeric()) # False

# b = '234563434'
# print(b.isnumeric()) # True

# c = '34334 54544 6676'
# print(c.isnumeric()) # False
# Output:
        # False
        # True
        # False

#******************* Exercise 17: isspace() : return true if string has only whitespace characters and false otherwise.
# a = '    '
# print(a.isspace())   # True
# b = 'i am a handsome man in ITC.'
# print(b.isspace())   # False
# c = 'i am a cambodian data scientist.'
# print(c.isspace())   # False
# d = ''
# e = ' '
# print(d.isspace())   # False
# print(e.isspace())   # True
# Output:
        # True
        # False
        # False
        # False
        # True

#******************* Exercise 18: istittle() Vs tittle() are used to mention on the title line letters.
# istitle() : return true if string is properly "titlecased" and false otherwise.
# title() : return "titlecased" version of string, that is, all words begin with uppercase and the rest are lowercase.
# x = 'hello everyone! good afternoon welcome to the meeting.'
# y = 'dara Is a Doctor.'
# z = 'Nareth Like Playing Toy Car.'
# print(x.title())
# print(y.title())
# print(z.title())

# print(x.istitle())
# print(y.istitle())
# print(z.istitle())
# Output:
        # Hello Everyone! Good Afternoon Welcome To The Meeting.
        # Dara Is A Doctor.
        # Nareth Like Playing Toy Car.
        # False
        # False
        # True

#******************* Exercise 19: rstrip() Vs lstrip() are used to remove all leading or trailing whitespace in the string.
# rstrip() : remove all trailing whitespace of string or any symbol that we want to cut it out. 
# lstrip() : removes all leading whitespace in string or any symbol that we want to cut it out.
# strip([chars]) : performs both lstrip() and rstrip() on string.
# a = '     Hello my name is Kry Senghort !!!'
# print(a.lstrip())

# b = '*****Hello my name is Kry Senghort !!!*****'
# print(b.lstrip('*'))
# print(b.rstrip('*'))

# d = b.lstrip('*')
# c = d.rstrip('*')
# print(c)

# x = '*********Mathematician is a professional mathematic teacher.***************'
# print(x.strip('*'))  # Mathematician is a professional mathematic teacher.

# e = '&&&&&&  $$$$$$  =====Hello everyone today, welcome to the sport stadium.000000000    ######    @@@@@@@@@@'
# f = e.lstrip('&')
# g = f.rstrip('@')
# h = g.lstrip(' ')
# i = h.rstrip()
# j = i.lstrip('$')
# k = j.rstrip('#')
# l = k.lstrip()
# m = l.rstrip()
# n = m.lstrip('=')
# o = n.rstrip('0')
# print('The string after remove any symbol and space is such that : \n\t\t\t',o)
# Output:
# Hello my name is Kry Senghort !!!
# Hello my name is Kry Senghort !!!*****
# *****Hello my name is Kry Senghort !!!
# Hello my name is Kry Senghort !!!
# Mathematician is a professional mathematic teacher.
# The string after remove any symbol and space is such that :
#                          Hello everyone today, welcome to the sport stadium.

#******************** Exercise 20: ljust() Vs rjust() are used to return a space-padded string with left or right on original string.
# ljust(width[fillchar]) : return a space-padded string with the original string left-justified to a total of width colums.
# rjust(width,[fillchar]) : return a space-padded string with the original string right-justified to a total of width columns.
# a = 'My mother have lived in South Korea'  # it has 35 character in this string include the space.
# b = a.ljust(50,'*')
# print(b)            # My mother have lived in South Korea***************   the number of * is such that : #(*) = 50 - #character.
# c = a.rjust(50,'*')
# print(c)            # ***************My mother have lived in South Korea
# d = a.ljust(23,'=')
# print(d)            # My mother have lived in South Korea. It does not have = because 23-35 < 0
# e = a.ljust(35,'=')
# print(e)            # My mother have lived in South Korea. It does not have = because 35-35 = 0
# f = a.rjust(50,'=')
# print(f)            # ===============My mother have lived in South Korea
# g = a.rjust(74,'@')
# print(g)            # @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@My mother have lived in South Korea

#******************** Exercise 21: maketrans() Vs translate() are used to mention on the translate string which are given.
# maketrans(intab,outtab)         : return a translation table to be used in translate function.
# translate(table,deletechars="") : translate string according to translation table str(256 chars), removing those in the del string.
# intab = 'aeiou'
# outtab = '12345'
# str = 'this is string example...wow!!!'
# trantab = str.maketrans(intab,outtab)
# print(str.translate(trantab))
# # Output:
#         # th3s 3s str3ng 2x1mpl2...w4w!!!
# intab = 'aeiouxm'
# outtab = '1234512'
# str = 'this is string example...wow!!!'
# trantab = str.maketrans(intab,outtab)
# print(str.translate(trantab))
# # Output:
#         # th3s 3s str3ng 2112pl2...w4w!!!
# intab  = 'abyrweghi'
# outtab = 'llo mn He'
# str = 'hibaby,howareyoutoday?'
# str1 = 'Hello my name is Kry SengHort'
# trantab = str.maketrans(intab,outtab)
# print(str.translate(trantab))
# # Output:
#         # Helllo,Homl nooutodlo?

#******************** Exercise 22: replace(old,new,max): replace all occurrences of old in string with new or at most max 
# occurrences if max given. 
# old : refer to old substring to be replaced.
# new : refer to new substring, which would replace old substring
# max : if this optoinal argument max is given, only the first count occurrences are replaced.
# a = 'this is string example...wow!!! this is really string'
# b = a.replace('this','It',3)
# print(b)    # It is string example...wow!!! It is really string
# c = b.replace('string','doctor',3)
# print(c)
# d = c.replace('example','who')
# print(d)
# e = d.replace('...',' have two ')
# f = e.replace('wow','children')
# g = f.replace('!!!','.')

# phrase = 'Giraffe Academy'
# # replace funtion is used to replace the some part of string by another string. We can replace the full string.  
# print(phrase.replace("Giraffe","Elephant"))   # Elephant Academy
# print(phrase.replace("Academy","Senghort"))   # Giraffe Senghort
# print(phrase.replace(phrase,"Kry Senghort"))  # Kry Senghort

# print(g)
                # It is string example...wow!!! It is really string
                # It is doctor example...wow!!! It is really doctor      
                # It is doctor who...wow!!! It is really doctor
                # It is doctor who have two children. It is really doctor

#******************** Exercise 22: rfind(str, beg = 0, end = len(str)) : same as find() but search backward in string.
# string = 'this is really a string example...wow!!!'
# string2 = 'is'
# print(string.rfind(string2))             # 5
# print(string.rfind(string2,0,10))        # 5
# print(string.rfind(string2,10,0))        # -1
# print(string.rfind(string2))             # 5
# print(string.rfind(string2,7))           # -1
# print(string.rfind(string2,3,10))        # 5
# print(string.rfind(string2,9,7))         # -1
# print(string.rfind(string2,3,14))        # 5
# Output:
                # 5
                # 5 
                # -1
                # 5 
                # -1
                # 5 
                # -1
                # 5 

#******************** Exercise 22: rindex(str,beg=0,end=len(str)) : same as index() but search backward in string.
# x = 'hello my girlfriend, how are you doing ? '
# y = 'my'
# print(x.rindex(y))  #  6
# y = 'hello'
# print(x.rindex(y))  #  0

#******************** Exercise 22: split(str="",num=string.count(str)) : splits string according to delimiter str(space if not 
# provided) and returns of substrings; then split into at most num substrings if given.
# a = 'i love on listenig'
# print(a.split())
# print(a.split('i',1))
# b = 'Dara is a best student.'
# print(b.split('w'))
# Output:
        # 'i', 'love', 'on', 'listenig']
        # ['', ' love on listenig']
        # ['Dara is a best student.']

#******************** Exercise 23: splitlines(num=string.count('\n')) : splits string at all (or num) newline and returns a list of
# each line with newlines removed.
# x = 'this is\nstring example\n...wow!!!'  
# y = 'dara\nsenghort\ndavorn'              
# z = 'daro\nis\n a\n girl.'                
# print(x.splitlines())  # ['this is', 'string example', '...wow!!!']
# print(y.splitlines())  # ['dara', 'senghort', 'davorn']
# print(z.splitlines())  # ['daro', 'is', ' a', ' girl.']
# # startswidth(str,beg=0,end=len(string)) : determines if string or a substring of string(if starting index beg and ending index end 
# # are given) start with substring str; return true if so and false otherwise.
# x = 'this is string example...wow!!!'
# print(x.startswith('this',5))        # False
# print(x.startswith('string',8,15))   # True
# print(x.startswith('this',0,5))      # True

# y = 'dara senghort davorn'
# print(y.startswith('dara'))          # True
# print(y.startswith('dara',20))       # False
# print(y.startswith('senghort',5,12)) # False

# z = 'daro is a girl.'
# print(z.startswith('daro'))          # True
# print(z.startswith('daro',4,9))      # False
# print(z.startswith('is',4,6))        # False
# Output:
        # ['this is', 'string example', '...wow!!!']
        # ['dara', 'senghort', 'davorn']
        # ['daro', 'is', ' a', ' girl.']
        # False
        # True
        # True
        # True
        # False
        # False
        # True
        # False
        # False
#********************* Exercise 24: swapcase() : inverts case for all letters in string. if uppercase-->lowercase, lower-->upper. 
# w = 'hELLO EVERYONE, hOW ARE YOU TODAY ?'
# print(w.swapcase())     # Hello everyone, How are you today ?

# x = 'this is string example....wow!!!'
# print(x.swapcase())     # THIS IS STRING EXAMPLE....WOW!!!

# y = 'My name is Kry Senghort'
# print(y.swapcase())     # mY NAME IS kRY sENGHORT

# z = 'HELLO BABY, HOW ARE YOU TODAY.' 
# print(z.swapcase())     # hello baby, how are you today. 

#********************* Exercise 25: zfill(width) : return original string leftpadded with zeros to a total of width characters; 
# intended for numbers, zfill() retains any sign given(less one zero).
# a = 'this is string example...wow!!!'
# print(a.zfill(40))  #  000000000this is string example...wow!!!
# print(a.zfill(50))  # 0000000000000000000this is string example...wow!!!
# b = 'hello my name is Kry Senghort and today i will do a presentation with you so how do you fell ?'
# print(b.zfill(100)) # 000000hello my name is Kry Senghort and today i will do a presentation with you so how do you fell ?
# print(b.zfill(120)) 
# 00000000000000000000000000hello my name is Kry Senghort and today i will do a presentation with you so how do you fell ?

#********************** Exercise 26: isdecimal() : return true if a unicode string has only decimal characters and false otherwise.
# a = 'this2016'
# print(a.isdecimal())  # False
# b = '123456' 
# print(b.isdecimal())  # True

#==================================================== Part 5 : Additional Exercise ==================================================
#********************** Exercise 1: 

























