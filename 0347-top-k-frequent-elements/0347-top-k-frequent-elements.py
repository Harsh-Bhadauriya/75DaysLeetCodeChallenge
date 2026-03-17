from collections import Counter

class Solution:
    def topKFrequent(self, nums, k):
        return [x for x, _ in Counter(nums).most_common(k)]
nums = [1,1,1,2,2,3]
k = 2
print(Solution().topKFrequent(nums, k))