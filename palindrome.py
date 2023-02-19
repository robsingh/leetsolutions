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
    
    # Counting the number of digits in x
    num_digits = 0
    temp = x
    while temp > 0:
        num_digits += 1
        temp = temp // 10

    # Compare the leftmost and rightmost digits
    left = 10 ** (num_digits - 1)
    right = 1
    while left > right:
        if (x//left) % 10 != (x//right) % 10:
            return False
        
        left = left // 10
        right = right * 10

    return True



print(check_palindrome(121))  # Output: True
print(check_palindrome(675))  # Output: False
print(check_palindrome(1667)) # Output: False