'''
Given a string s, reverse only all the vowels in the string and return it.

The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.
'''

'''
My approach: (2 pointer approach)
1. Iterate through all the elements in the string. 
2. To accomplish this, we will use two pointers to traverse the string from both the ends. 
3. We move the pointers until vowels are found, then swap them.
'''

class Solution:
    def reverseVowels(self, s:str) -> str:
        vowels = set('aeiouAEIOU') #set of vowels including uppercase
        s = list(s) # str is immutable hence we convert it to list so it can be modified later
        left, right = 0, len(s) - 1

        while left < right:
            # moving left pointer until a vowel is found
            if s[left] not in vowels:
                left += 1
            # moving right pointer until a vowel is found
            elif s[right] not in vowels:
                right -= 1
            else:
            # when vowels are found, we swap them
                s[left], s[right] = s[right], s[left]
                left += 1
                right -= 1

        # convert the list back to string
        return ''.join(s)


sol = Solution()
s = "hello"
print(sol.reverseVowels(s))