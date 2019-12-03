"""
Question 5
Write a function to check to see if all numbers in list are consecutive
numbers. For example, [2,3,4,5,6,7] are consecutive numbers, but [1,2,4,5] are
not consecutive numbers. The return should be boolean Type.

    def is_consecutive(a_list):

"""

def is_consecutive(a_list):
    for i in range(1, len(a_list)):
        if(a_list[i] + 1 ==  a_list[i + 1]):
            return "true" 
        else:
            return "false"
numbers = [6, 7, 8, 9]
print(is_consecutive(numbers))

       
     
     

