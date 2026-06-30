"""
Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, 
typically using all the original letters exactly once.

Input: s = "anagram", t = "nagaram"
Output: true

Input: s = "rat", t = "car"
Output: false

--->>> what if the inputs contain Unicode characters? How would you adapt your solution to such a case?
"""

class Solution:
    # def isAnagram(self, s:str, t:str) -> bool:
        # if len(s) == len(t):
        #     sorted_s = sorted(s)
        #     sorted_t = sorted(t)

        #     if sorted_s == sorted_t:
        #         return True
        #     else:
        #         return False

    #if inputs contains Unicode characters
    # Time - O(n), Space - O(n)
    def isAnagram(self, s:str, t:str) -> bool:
        if len(s) != len(t):
            return False
        
        #create a dictionary to count the occurrences of each Unicode
        char_count = {}
        for char in s:
            if char in char_count:
                char_count[char] += 1
            else:
                char_count[char] = 1
            # print(char_count)

        #check if each character in t appears same times as that in s
        for char in t:
            if char in char_count:
                char_count[char] -= 1
                if char_count[char] < 0:
                    return False
            else:
                return False
        
        return True


sol = Solution()
print(sol.isAnagram(s="rat",t="car"))
