class Solution:
    def lengthOfLongestSubstring(self, s):
        mp = {}
        l = 0
        ans = 0
        
        for r in range(len(s)):
            if s[r] in mp and mp[s[r]] >= l:
                l = mp[s[r]] + 1
            
            mp[s[r]] = r
            
            if r - l + 1 > ans:
                ans = r - l + 1
        
        return ans