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
        # s_lower = s.lower()   (O(n(logn)))
        # t_lower = t.lower()

        # if len(s_lower) == len(t_lower):
        #     sorted_s = sorted(s_lower)
        #     sorted_t = sorted(t_lower)

        #     if sorted_s == sorted_t:
        #         return True
        #     else:
        #         return False

    #if inputs contains Unicode characters
    def isAnagram(self, s:str, t:str) -> bool:
        if len(s.lower()) != len(t.lower()):
            return False
        
        #create a dictionary to count the occurrences of each Unicode
        char_count = {}
        for char in s:
            code_point = ord(char)
            if code_point in char_count:
                char_count[code_point] += 1
            else:
                char_count[code_point] = 1
            # print(char_count)

        #check if each character in t appears same times as that in s
        for char in t:
            code_point = ord(char)
            if code_point in char_count:
                char_count[code_point] -= 1
                if char_count[code_point] < 0:
                    return False
            else:
                return False
        
        return True


sol = Solution()
print(sol.isAnagram(s="rat",t="car"))
