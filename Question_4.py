"""
Question 4
Write a function to return if the given year is a leap year. A leap year is
divisible by 4, but not divisible by 100, unless it is also divisible by 400. 
The return should be boolean Type (true/false).

def is_leap_year(a_year):

"""
def is_leap_year(a_year):
    if(a_year % 4 == 0):
        if(a_year % 100 == 0 and a_year % 400 == 0):
            return "true"
        elif(a_year % 100 != 0):
            return "true"
        else:
            return "false"
    else:
       return "false"

year = int(input("enter a year: "))
print(is_leap_year(year))



#if a_year % 4 == 0 and (a_year % 400 == 0 or a_year % 100 != 0):
#       return "true"
#   else:
#       return "false"

