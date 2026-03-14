class Solution:
    def isAnagram(self, s, t):
        return sorted(s) == sorted(t)
        print(Solution().isAnagram("rat", "tar"))