# Given two strings s and t, 
# return true if t is an anagram of s, and false otherwise.
# https://leetcode.com/problems/valid-anagram/

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if sorted(s) == sorted(t):
            return True
        else:
            return False

sol = Solution()

s = "anagram"
t = "nagaram"
print(sol.isAnagram(s, t))

s = "rat"
t = "car"
print(sol.isAnagram(s, t))

