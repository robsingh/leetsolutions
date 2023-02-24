"""
Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

I can be placed before V (5) and X (10) to make 4 and 9. 
X can be placed before L (50) and C (100) to make 40 and 90. 
C can be placed before D (500) and M (1000) to make 400 and 900.
Given a roman numeral, convert it to an integer.
"""

# class Solution:
    # def romanToInt(self, s: str) -> int:
    #             roman_dict = {'I':1,'V': 5,'X':10,'L':50,'C':100,'D':500,'M':1000}
    #             result = 0

    #             for x,y in zip(s,s[1:]):
    #                     if roman_dict[x] < roman_dict[y]:
    #                             result -= roman_dict[x]
    #                     else:
    #                             result += roman_dict[x]
    #             return result + roman_dict[s[-1]]
    

# another way
class Solution:
        def romanToInt(self, s: str) -> int:
                roman = {'I':1,'V': 5,'X':10,'L':50,'C':100,'D':500,'M':1000}
                result = 0
                prev_value = 0
                for i in range(len(s)):
                        # getting the integer value of the current roman numeral from dictionary(roman)
                        curr_value = roman[s[i]]
                        if curr_value > prev_value:
                                result -= prev_value
                        else:
                                result += prev_value
                        # store the current value in the prev_value variable so use it in the next iteration
                        prev_value = curr_value
                # add the value of the last numeral to the result
                result += prev_value
                return result


sol = Solution()
print(sol.romanToInt('IV'))
print(sol.romanToInt('LVIII'))
