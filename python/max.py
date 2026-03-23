class Solution:
    def maxSubArray(self, nums):
        cur = max_sum = nums[0]
        for n in nums[1:]:
            cur = max(n, cur + n)
            max_sum = max(max_sum, cur)
        return max_sum
