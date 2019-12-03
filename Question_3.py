"""
Question 3
Please write a Python function, max_num_in_list to return the max number of a
given list. The first line of the code has been defined as below.

    def max_num_in_list(a_list):

"""

def max_num_in_list(a_list):
    max_num = max(a_list)
    return max_num
digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
highest_digit = max_num_in_list(digits)
print(highest_digit)
