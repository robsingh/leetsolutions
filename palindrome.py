"""
Given an integer x, return true if x is a palindrome, and false otherwise.
An integer is a palindrome when it reads the same forward and backward.

Do a minor tweak and solve it without converting the integer to a string. 
"""

# def palindrome_str(x):
#     con_string = str(x)
#     if con_string == con_string[::-1]:
#         return True
#     else:
#         return False
    
# print(palindrome_str(10))

def check_palindrome(x):
    if x < 0:
        return False
    
    original_num = x
    reverse_num = 0

    while x > 0:
        remainder = x % 10
        reverse_num = (reverse_num * 10) + remainder
        x //= 10

    if original_num == reverse_num:
        return True
    return False

    
print(check_palindrome(121))  # Output: True
print(check_palindrome(675))  # Output: False
print(check_palindrome(1667)) # Output: False