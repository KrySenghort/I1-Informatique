#=====================================================================================================================================
#==================================================== Chapter 11: Date&Time ==========================================================
#=====================================================================================================================================
#********************** Definition:
# Python programming can handle date and time in several ways. Converting between date formats is a common choice for computers. 
# python's time and calendar modules help track dates and times.
# Tick is time intervals that are floating point numbers in unit of seconds. Particular-instants in time are expressed in second since
# 12:00am, january 1 1970.(epoch)
# There is a popular time module available in python, which provides functions for working with times, and for converting between 
# representations. The function time.time() return the current system time in ticks since 12:00am, january 1970(epoch).

# import time
# ticks = time.time()
# print('Number of ticks since 12:00am, January 1, 1970 : ',ticks)
# # Number of ticks since 12:00am, January 1, 1970 :  1663581481.098766 (1970-now = 1663581481.098766s)

#********************** Time Tuple : many python's time function handle time as a tuple of 9 numbers, as shown below.
# tm_year   = 4-digit year       --> 2012      
# tm_month  = Month              --> 1 to 12   
# tm_day    = Day                --> 1 to 31
# tm_hour   = Hour               --> 0 to 23
# tm_min    = Minute             --> 0 to 59
# tm_sec    = Second             --> 0 to 61 (60 or 61 are leap-seconds)
# tm_wday   = Day of week        --> 0 to 6 (0 is monday)
# tm_yday   = Day of year        --> 1 to 366 (Julian day)
# tm_isdst  = Daylight savings   --> -1,0,1 means library determines DST.

# # Example : 
# import time
# print(time.localtime())
   # time.struct_time(tm_year = 2022, tm_mon = 9, tm_mday = 19, tm_hour=17, tm_min=13, tm_sec=32, tm_wday=0, tm_yday=262, tm_isdst=0)

#********************** Exercise 1: Getting current time.
# import time
# localtime = time.localtime(time.time())
# print(localtime)
#    #  time.struct_time(tm_year=2022, tm_mon=9, tm_mday=19, tm_hour=17, tm_min=41, tm_sec=33, tm_wday=0, tm_yday=262, tm_isdst=0)

#********************** Exercise 2: Getting formatted time.
# import time
# localtime = time.asctime(time.localtime(time.time()))
# print('Local current time : ',localtime)   # Local current time :  Mon Sep 19 17:48:30 2022

# import time
# localtime = time.asctime(time.localtime(time.time()))
# print('The time that is right now is : ',localtime)   # The time that is right now is :  Mon Sep 19 18:01:33 2022

#********************** Exercise 3: Getting calendar for a month
# import calendar
# a = calendar.month(2022,1)
# print('Calendar for :%s'%str(a))
                                    # Calendar for :     January 2022
                                    # Mo Tu We Th Fr Sa Su
                                    #                 1  2
                                    #  3  4  5  6  7  8  9
                                    # 10 11 12 13 14 15 16
                                    # 17 18 19 20 21 22 23
                                    # 24 25 26 27 28 29 30
                                    # 31
# b = calendar.month(2022,2)
# print('Calendar for :'+str(b))
                                    # Calendar for :   February 2022
                                    # Mo Tu We Th Fr Sa Su
                                    #     1  2  3  4  5  6
                                    #  7  8  9 10 11 12 13
                                    # 14 15 16 17 18 19 20
                                    # 21 22 23 24 25 26 27
                                    # 28
# c = calendar.month(2022,3)
# print('Calendar for :',c)
                                    # Calendar for :      March 2022
                                    # Mo Tu We Th Fr Sa Su
                                    #     1  2  3  4  5  6
                                    #  7  8  9 10 11 12 13
                                    # 14 15 16 17 18 19 20
                                    # 21 22 23 24 25 26 27
                                    # 28 29 30 31
# d = calendar.month(2022,4)
# print('calendar for :',d)
                                    # calendar for :      April 2022
                                    # Mo Tu We Th Fr Sa Su
                                    #              1  2  3
                                    #  4  5  6  7  8  9 10
                                    # 11 12 13 14 15 16 17
                                    # 18 19 20 21 22 23 24
                                    # 25 26 27 28 29 30

# import calendar
# for i in range(1,13):
#    a = calendar.month(2022,i)
#    print('Calendar for',a,end='')
# Output:
                              # Calendar for     January 2022
                              # Mo Tu We Th Fr Sa Su
                              #                 1  2
                              #  3  4  5  6  7  8  9
                              # 10 11 12 13 14 15 16
                              # 17 18 19 20 21 22 23
                              # 24 25 26 27 28 29 30
                              # 31
                              # Calendar for    February 2022
                              # Mo Tu We Th Fr Sa Su
                              #     1  2  3  4  5  6
                              #  7  8  9 10 11 12 13
                              # 14 15 16 17 18 19 20
                              # 21 22 23 24 25 26 27
                              # 28
                              # Calendar for      March 2022 
                              # Mo Tu We Th Fr Sa Su
                              #     1  2  3  4  5  6
                              #  7  8  9 10 11 12 13
                              # 14 15 16 17 18 19 20
                              # 21 22 23 24 25 26 27
                              # 28 29 30 31
                              # Calendar for      April 2022
                              # Mo Tu We Th Fr Sa Su
                              #              1  2  3
                              #  4  5  6  7  8  9 10
                              # 11 12 13 14 15 16 17
                              # 18 19 20 21 22 23 24
                              # 25 26 27 28 29 30
                              # Calendar for       May 2022
                              # Mo Tu We Th Fr Sa Su
                              #                    1
                              #  2  3  4  5  6  7  8
                              #  9 10 11 12 13 14 15
                              # 16 17 18 19 20 21 22
                              # 23 24 25 26 27 28 29
                              # 30 31
                              # Calendar for      June 2022
                              # Mo Tu We Th Fr Sa Su
                              #        1  2  3  4  5
                              #  6  7  8  9 10 11 12
                              # 13 14 15 16 17 18 19
                              # 20 21 22 23 24 25 26
                              # 27 28 29 30
                              # Calendar for      July 2022
                              # Mo Tu We Th Fr Sa Su
                              #              1  2  3
                              #  4  5  6  7  8  9 10
                              # 11 12 13 14 15 16 17
                              # 18 19 20 21 22 23 24
                              # 25 26 27 28 29 30 31
                              # Calendar for     August 2022
                              # Mo Tu We Th Fr Sa Su
                              #  1  2  3  4  5  6  7
                              #  8  9 10 11 12 13 14
                              # 15 16 17 18 19 20 21
                              # 22 23 24 25 26 27 28
                              # 29 30 31
                              # Calendar for    September 2022
                              # Mo Tu We Th Fr Sa Su
                              #           1  2  3  4
                              #  5  6  7  8  9 10 11
                              # 12 13 14 15 16 17 18
                              # 19 20 21 22 23 24 25
                              # 26 27 28 29 30
                              # Calendar for     October 2022
                              # Mo Tu We Th Fr Sa Su
                              #                 1  2
                              #  3  4  5  6  7  8  9
                              # 10 11 12 13 14 15 16
                              # 17 18 19 20 21 22 23
                              # 24 25 26 27 28 29 30
                              # 31
                              # Calendar for    November 2022
                              # Mo Tu We Th Fr Sa Su
                              #     1  2  3  4  5  6
                              #  7  8  9 10 11 12 13
                              # 14 15 16 17 18 19 20
                              # 21 22 23 24 25 26 27
                              # 28 29 30
                              # Calendar for    December 2022
                              # Mo Tu We Th Fr Sa Su
                              #           1  2  3  4
                              #  5  6  7  8  9 10 11
                              # 12 13 14 15 16 17 18
                              # 19 20 21 22 23 24 25
                              # 26 27 28 29 30 31

#********************** Exercise 4: time.altzone() method is the offset of the local DST timezone, in seconds west of UTC, if one is
# defined. This is negative if the local DST timezone is east of UTC(as in Western Europe, including the UK), Use this if the daylight
# is nonzero.  UTC​​ (Coordinate Universal Time ការសម្របសម្រួលពេលវេលាម៉ោងសកល)
# Offset is a zone that is the difference in hours and minutes between a particular time zone and UTC. In ISO 8601, the particular 
# zone offset can be indicated in a date or time value. The zone offset can be Z for UTC or it can be a value "+" or "-" from UTC.

# import time
# print('time zone is :',time.altzone)          # time zone is : -28800
# print('Hello everyone today welcome to the stadium at',time.altzone)

#********************** Exercise 5: time.asctime([tupletime]) is used to accept a time tuple and returns a readable 24-character 
# string such as 'Tue Dec 11 18:07:14 2008'.

# import time
# t = time.localtime()
# print('Asctime : ',time.asctime(t))                # Asctime :  Tue Sep 20 01:42:45 2022
# print('I am studying right now :',time.asctime(t)) # I am studying right now : Tue Sep 20 01:46:04 2022

#********************** Exercise 7: time.ctime([secs]) is like the asctime(localtime(secs)) and without arguments is like asctime().
# import time
# print('ctime : ',time.ctime())   # ctime :  Tue Sep 20 02:03:35 2022

#********************** Exercise 8: time.gmtime([secs]) accepts an instant expressed in seconds since the epoch and returns a time-t
# # tuple with the UTC time. Note tm_isdst is always 0.
# import time
# print('gmtime :',time.gmtime(1455508609.34375))
# # output:
# # gmtime : time.struct_time(tm_year=2016, tm_mon=2, tm_mday=15, tm_hour=3, tm_min=56, tm_sec=49, tm_wday=0, tm_yday=46, tm_isdst=0)

#********************** Exercise 9: time.localtime([sec]) accept an instant expressed in seconds since the epoch and returns a time-
# tuple t with local time(t.tm_isdst is 0 or 1, depending on whether DST applies to instant secs by local rules.)
# Epoch           : សម័យកាល
# Daylight Saving : DST is the practice of turning the clock ahead as warmer weather approaches and back as it becomes colder again.
# The goal of Daylight Saving Time is to make better use of daylight by prolonging(អូសបន្លាយ) the amount of time we can spend outside
# during daylight hours.

# import time
# a = time.localtime()
# print('this location : ',time.localtime())
# # this location :  
# # time.struct_time(tm_year=2022, tm_mon=9, tm_day=20, tm_hour=2, tm_min=10, tm_sec=35, tm_wday=1, tm_yday=263, tm_isdst=0

#********************** Exercise 10: time.mktime(tupletime) accept an instant expressed as a time-tuple in local time and return a
# floating point value with the instant expressed in seconds since the epoch.

# from email.utils import localtime
# import time
# tuple = (2016,2,15,10,13,38,1,48,0)
# d = time.mktime(tuple)
# print('time.mktime(t) is \t\t:%f' %d)
# print('asctime(localtime(secs))\t: %s' % time.asctime(time.localtime(d)))
# # time.mktime(t) is               :1455506018.000000
# # asctime(localtime(secs))        : Mon Feb 15 10:13:38 2016

#********************** Exercise 11: time.sleep(secs) is a method that suspends the calling thread for secs seconds.
# import time
# print('Start : %s'%time.ctime())
# time.sleep(3)
# print('End : %s'% time.ctime())
# # Start : Tue Sep 20 18:40:04 2022     
# # End : Tue Sep 20 18:40:07 2022    # it means that it sleep for 3 seconds then it will display end time.

#********************** Exercise 12: time.strftime(fmt,[tupletime]) accept an instant expressed as a time-tuple in local time and 
# # return a string representing the instant as specified by string fmt.
# import time
# t = {2015,12,31,10,39,45,1,48,0}
# t1 = time.mktime(t)
# print(time.strftime("%b %d %Y %H:%M:%S", time.localtime(t1)))

#********************** Exercise 13: time.strptime(str,fmt = '%a %b %d %H:%M:%S %Y') parses str according to format string fmt and
# # returns the instant in time-tuple format.
# import time
# struct_time = time.strptime('30 12 2015','%d %m %Y')
# print('tuple',struct_time)
# # tuple time.struct_time(tm_year=2015, tm_mon=12, tm_mday=30, tm_hour=0, tm_min=0, tm_sec=0, tm_wday=2, tm_yday=364, tm_isdst=-1)

#********************** Exercise 14: time.time() method is used to return the current time instant, a floating-point number of seconds
# # since we epoch.
# import time
# print("time.time() : %f" % time.time())            # time.time() : 1663690174.655056
# print(time.localtime(time.time()))
# # time.struct_time(tm_year=2022, tm_mon=9, tm_mday=20, tm_hour=23, tm_min=9, tm_sec=34, tm_wday=1, tm_yday=263, tm_isdst=0)
# print(time.asctime(time.localtime(time.time())))   # Tue Sep 20 23:09:34 2022

#********************** Exercise 15: time.ztime() method is used to resets the time conversion rules used by the library routines. 
# # The environmental variable TZ specifies how this is done.
# import time
# import os
# os.environ['TZ'] = 'EST+05EDT,M4.1.0,M10.5.0'
# print(time.strftime('%X %x %Z'))   # 11:27:54 09/20/22 EDT

# os.environ['TZ'] = 'AEST-10AEDT-11,M10.5.0,M3.5,0'
# print(time.strftime('%X %x %Z'))   # 11:27:54 09/20/22 EDT

#********************** Exercise 16: calendar.calendar(year,w=2,l=1,c=6) is used to return a multiline string with a calendar for
# # year formatted into three columns separated by c spaces. w is the width in characters of each date; each line has length 
# # 21*w+18+2*c. l is the number of lines for each week.
# # y is year
# # w is width
# # c is column space
# # l is number of line for each week.

# import calendar
# x = calendar.calendar(2022,2,1,6)
# print(x)
# # Output:
                              #                                   2022

                              #       January                   February                   March        
                              # Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su
                              #                 1  2          1  2  3  4  5  6          1  2  3  4  5  6
                              #  3  4  5  6  7  8  9       7  8  9 10 11 12 13       7  8  9 10 11 12 13
                              # 10 11 12 13 14 15 16      14 15 16 17 18 19 20      14 15 16 17 18 19 20
                              # 17 18 19 20 21 22 23      21 22 23 24 25 26 27      21 22 23 24 25 26 27
                              # 24 25 26 27 28 29 30      28                        28 29 30 31
                              # 31

                              #        April                      May                       June        
                              # Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su
                              #              1  2  3                         1             1  2  3  4  5
                              #  4  5  6  7  8  9 10       2  3  4  5  6  7  8       6  7  8  9 10 11 12
                              # 11 12 13 14 15 16 17       9 10 11 12 13 14 15      13 14 15 16 17 18 19
                              # 18 19 20 21 22 23 24      16 17 18 19 20 21 22      20 21 22 23 24 25 26
                              # 25 26 27 28 29 30         23 24 25 26 27 28 29      27 28 29 30
                              #                           30 31

                              #         July                     August                  September      
                              # Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su
                              #              1  2  3       1  2  3  4  5  6  7                1  2  3  4
                              #  4  5  6  7  8  9 10       8  9 10 11 12 13 14       5  6  7  8  9 10 11
                              # 11 12 13 14 15 16 17      15 16 17 18 19 20 21      12 13 14 15 16 17 18
                              # 18 19 20 21 22 23 24      22 23 24 25 26 27 28      19 20 21 22 23 24 25
                              # 25 26 27 28 29 30 31      29 30 31                  26 27 28 29 30

                              #       October                   November                  December
                              # Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su
                              #                 1  2          1  2  3  4  5  6                1  2  3  4
                              #  3  4  5  6  7  8  9       7  8  9 10 11 12 13       5  6  7  8  9 10 11
                              # 10 11 12 13 14 15 16      14 15 16 17 18 19 20      12 13 14 15 16 17 18
                              # 17 18 19 20 21 22 23      21 22 23 24 25 26 27      19 20 21 22 23 24 25
                              # 24 25 26 27 28 29 30      28 29 30                  26 27 28 29 30 31
                              # 31

#********************** Exercise 17: calendar.firstweekday() is used to return the current setting for the weekday that starts each
# # week. By default, when calendar is first imported, this is 0, meaning Monday.
# import calendar
# t = calendar.firstweekday()
# print(t)   # 0  mean that 0 or monday is the first week day.

#********************** Exercise 18: calendar.isleap(year) is used to return the current setting for the weekday that starts each 
# # week. By default, when calendar is first imported, this is 0, meaning Monday.
# import calendar
# for i in range(3):
#    print('Enter year#'+str(i)+' :',end=' ')
#    year = int(input())
#    c = calendar.isleap(year)
#    print(c)
# Output:
                  # Enter year#0 : 1904
                  # True
                  # Enter year#1 : 2024
                  # True
                  # Enter year#2 : 2022
                  # False
#********************** Exercise 19: calendar.leapdays(y1,y2) is used to return the total number of leap days in the years within 
# range(y1,y2).
# import calendar
# x = calendar.leapdays(2022,3000)
# print('The number of leap days between both years is : %s' % x)   # The number of leap days between both years is : 237

#********************** Exercise 20: calendar.month(year,month,w=2,l=1) is used to return a multiline string with a calendar for 
# # month of year, one line per week plus two header lines. w is the width in characters of each date; each line has length 7*w+6.
# # l is the number of lines for each week.
# import calendar
# x = calendar.month(2022,9,2,1)
# print(x)
# # Output:
                     #    September 2022
                     # Mo Tu We Th Fr Sa Su
                     #           1  2  3  4
                     #  5  6  7  8  9 10 11
                     # 12 13 14 15 16 17 18
                     # 19 20 21 22 23 24 25
                     # 26 27 28 29 30

# for i in range(1,13):
#    y = calendar.month(2023,i,2,1)
#    print('Calendar is such that : ',y)
# # Output:
                                          # Calendar is such that :      January 2023
                                          # Mo Tu We Th Fr Sa Su
                                          #                    1
                                          #  2  3  4  5  6  7  8
                                          #  9 10 11 12 13 14 15
                                          # 16 17 18 19 20 21 22
                                          # 23 24 25 26 27 28 29
                                          # 30 31

                                          # Calendar is such that :     February 2023
                                          # Mo Tu We Th Fr Sa Su
                                          #        1  2  3  4  5
                                          #  6  7  8  9 10 11 12
                                          # 13 14 15 16 17 18 19
                                          # 20 21 22 23 24 25 26
                                          # 27 28

                                          # Calendar is such that :       March 2023
                                          # Mo Tu We Th Fr Sa Su
                                          #        1  2  3  4  5
                                          #  6  7  8  9 10 11 12
                                          # 13 14 15 16 17 18 19
                                          # 20 21 22 23 24 25 26
                                          # 27 28 29 30 31

                                          # Calendar is such that :       April 2023
                                          # Mo Tu We Th Fr Sa Su
                                          #                 1  2
                                          #  3  4  5  6  7  8  9
                                          # 10 11 12 13 14 15 16
                                          # 17 18 19 20 21 22 23
                                          # 24 25 26 27 28 29 30

                                          # Calendar is such that :        May 2023
                                          # Mo Tu We Th Fr Sa Su
                                          #  1  2  3  4  5  6  7
                                          #  8  9 10 11 12 13 14
                                          # 15 16 17 18 19 20 21
                                          # 22 23 24 25 26 27 28
                                          # 29 30 31

                                          # Calendar is such that :       June 2023
                                          # Mo Tu We Th Fr Sa Su
                                          #           1  2  3  4
                                          #  5  6  7  8  9 10 11
                                          # 12 13 14 15 16 17 18
                                          # 19 20 21 22 23 24 25
                                          # 26 27 28 29 30

                                          # Calendar is such that :       July 2023
                                          # Mo Tu We Th Fr Sa Su
                                          #                 1  2
                                          #  3  4  5  6  7  8  9
                                          # 10 11 12 13 14 15 16
                                          # 17 18 19 20 21 22 23
                                          # 24 25 26 27 28 29 30
                                          # 31

                                          # Calendar is such that :      August 2023
                                          # Mo Tu We Th Fr Sa Su
                                          #     1  2  3  4  5  6
                                          #  7  8  9 10 11 12 13
                                          # 14 15 16 17 18 19 20
                                          # 21 22 23 24 25 26 27
                                          # 28 29 30 31

                                          # Calendar is such that :     September 2023
                                          # Mo Tu We Th Fr Sa Su
                                          #              1  2  3
                                          #  4  5  6  7  8  9 10
                                          # 11 12 13 14 15 16 17
                                          # 18 19 20 21 22 23 24
                                          # 25 26 27 28 29 30

                                          # Calendar is such that :      October 2023
                                          # Mo Tu We Th Fr Sa Su
                                          #                    1
                                          #  2  3  4  5  6  7  8
                                          #  9 10 11 12 13 14 15
                                          # 16 17 18 19 20 21 22
                                          # 23 24 25 26 27 28 29
                                          # 30 31

                                          # Calendar is such that :     November 2023
                                          # Mo Tu We Th Fr Sa Su
                                          #        1  2  3  4  5
                                          #  6  7  8  9 10 11 12
                                          # 13 14 15 16 17 18 19
                                          # 20 21 22 23 24 25 26
                                          # 27 28 29 30

                                          # Calendar is such that :     December 2023
                                          # Mo Tu We Th Fr Sa Su
                                          #              1  2  3
                                          #  4  5  6  7  8  9 10
                                          # 11 12 13 14 15 16 17
                                          # 18 19 20 21 22 23 24
                                          # 25 26 27 28 29 30 31

#********************** Exercise 21: calendar.monthcalendar(year,month) is used to return a list of ints. Each sublist denotes a week.
# Days outside month of year are set to 0; days within the month are set to their day of month, 1 and up.
# import calendar
# year = int(input('Enter year : '))
# month = int(input('Enter month : '))
# x = calendar.monthcalendar(year,month)
# print(x)

# Output:
# Enter year : 2022
# Enter month : 6
#[[0, 0, 1, 2, 3, 4, 5],[6, 7, 8, 9, 10, 11, 12],[13, 14, 15, 16, 17, 18, 19],[20, 21, 22, 23, 24, 25, 26],[27, 28, 29, 30, 0, 0, 0]]

# Enter year : 2023
# Enter month : 6
#[[0, 0, 0, 1, 2, 3, 4],[5, 6, 7, 8, 9, 10, 11],[12, 13, 14, 15, 16, 17, 18],[19, 20, 21, 22, 23, 24, 25],[26, 27, 28, 29, 30, 0, 0]]    

# Enter year : 2059
# Enter month : 9
#[[1, 2, 3, 4, 5, 6, 7],[8, 9, 10, 11, 12, 13, 14],[15, 16, 17, 18, 19, 20, 21],[22, 23, 24, 25, 26, 27, 28],[29, 30, 0, 0, 0, 0, 0]]    

#********************** Exercise 22: calendar.monthrange(year,month) is used to return two integers. The first one is the code of 
# weekday for the first day of the month in year; the second one is the number of days in the month. Weekday codes are 0 (Monday) to
# 6(sunday); month numbers are 1 to 12.

# import calendar
# y = input('Enter year : ')
# m = input('Enter month : ')
# z = calendar.monthrange(int(y),int(m))
# print("The day's code and the number of days in the month is ",z)

# # Output:
# # Enter year : 2022
# # Enter month : 6
# # The day's code and the number of days in the month is  (2, 30)

# # Enter year : 2043
# # Enter month : 8
# # The day's code and the number of days in the month is  (5, 31)

#********************** Exercise 23: calendar.prcal(year,w=2,l=1,c=6) is used to print calendar.calendar(year,w,l,c)   
# import calendar
# year = int(input("Enter year : "))
# x = calendar.prcal(year,2,1,6)
# print(x)

# Output:
                              # Enter year : 2056
                              #                                   2056

                              #       January                   February                   March
                              # Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su
                              #                 1  2          1  2  3  4  5  6             1  2  3  4  5
                              #  3  4  5  6  7  8  9       7  8  9 10 11 12 13       6  7  8  9 10 11 12
                              # 10 11 12 13 14 15 16      14 15 16 17 18 19 20      13 14 15 16 17 18 19
                              # 17 18 19 20 21 22 23      21 22 23 24 25 26 27      20 21 22 23 24 25 26
                              # 24 25 26 27 28 29 30      28 29                     27 28 29 30 31
                              # 31

                              #        April                      May                       June
                              # Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su
                              #                 1  2       1  2  3  4  5  6  7                1  2  3  4
                              #  3  4  5  6  7  8  9       8  9 10 11 12 13 14       5  6  7  8  9 10 11
                              # 10 11 12 13 14 15 16      15 16 17 18 19 20 21      12 13 14 15 16 17 18
                              # 17 18 19 20 21 22 23      22 23 24 25 26 27 28      19 20 21 22 23 24 25
                              # 24 25 26 27 28 29 30      29 30 31                  26 27 28 29 30

                              #         July                     August                  September
                              # Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su
                              #                 1  2          1  2  3  4  5  6                   1  2  3
                              #  3  4  5  6  7  8  9       7  8  9 10 11 12 13       4  5  6  7  8  9 10
                              # 10 11 12 13 14 15 16      14 15 16 17 18 19 20      11 12 13 14 15 16 17
                              # 17 18 19 20 21 22 23      21 22 23 24 25 26 27      18 19 20 21 22 23 24
                              # 24 25 26 27 28 29 30      28 29 30 31               25 26 27 28 29 30
                              # 31

                              #       October                   November                  December
                              # Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su
                              #                    1             1  2  3  4  5                   1  2  3
                              #  2  3  4  5  6  7  8       6  7  8  9 10 11 12       4  5  6  7  8  9 10
                              #  9 10 11 12 13 14 15      13 14 15 16 17 18 19      11 12 13 14 15 16 17
                              # 16 17 18 19 20 21 22      20 21 22 23 24 25 26      18 19 20 21 22 23 24
                              # 23 24 25 26 27 28 29      27 28 29 30               25 26 27 28 29 30 31
                              # 30 31
                              # None

#********************** Exercise 24: calendar.prmonth(year,month,w=2,l=1) is used to print calendar, month(year, month,w,l)
# import calendar
# x = int(input('Enter year : '))
# y = int(input('Enter month : '))
# a = calendar.prmonth(x,y,2,1)
# print(a)

# Output:
               # Enter year : 2036
               # Enter month : 8
               #     August 2036     
               # Mo Tu We Th Fr Sa Su
               #              1  2  3
               #  4  5  6  7  8  9 10
               # 11 12 13 14 15 16 17
               # 18 19 20 21 22 23 24
               # 25 26 27 28 29 30 31
               # None

#********************** Exercise 25: calendar.setfirstweekday(weekday) is used to set the first day of each week to weekday code
# # weekday. Wednesday codes are 0(monday) to 6(sunday).
# import calendar
# weekday = 1
# t = calendar.setfirstweekday(weekday)
# print(t)   # None

#********************** Exercise 26: calendar.timegm(tupletime) is used to accept a time instant in time-tuple form and return the
# # same instant as a floating-point number of seconds since the epoch.
# import calendar
# tupletime = (1,2,3,4,4,5,5,6)
# x = calendar.timegm(tupletime)
# print(x)    #  -62132730955

#********************** Exercise 27: calendar.weekday(year,month,day) is used to return weekday code for the given date. Weekday codes
# are 0 (monday)  to 6 (sunday); month numbers are 1(january) to 12(december).
# import calendar
# a = input('Enter year : ')
# b = input('Enter month : ')
# c = input('Enter day : ')
# d = calendar.weekday(int(a),int(b),int(c))
# print(d)

# Output:
            # Enter year : 2045
            # Enter month : 8
            # Enter day : 3
            # 3

            # Enter year : 2012
            # Enter month : 4
            # Enter day : 6
            # 4









