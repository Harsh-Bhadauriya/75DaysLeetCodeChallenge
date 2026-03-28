class Solution:
    def characterReplacement(self, s, k):
        count = [0] * 26
        l = 0
        maxf = 0
        ans = 0
        
        for r in range(len(s)):
            idx = ord(s[r]) - ord('A')
            count[idx] += 1
            if count[idx] > maxf:
                maxf = count[idx]
            
            if (r - l + 1) - maxf > k:
                count[ord(s[l]) - ord('A')] -= 1
                l += 1
            
            if r - l + 1 > ans:
                ans = r - l + 1
        
        return ans
print(Solution().characterReplacement("AABABBA", 1))