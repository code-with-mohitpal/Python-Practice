from typing import List


# Solution class containing the majorityElement method
class Solution(object):
   def majorityElement(self, nums):
       """
       :type nums: List[int]
       :rtype: int
       """
       n = len(nums)
       count = 1
       majority = nums[0]


       # Phase 1: Find potential majority candidate
       for i in range(1, n):
           if nums[i] == majority:
               count += 1
           else:
               count -= 1
               if count == 0:
                   majority = nums[i]
                   count = 1


       # Phase 2: Verify the candidate
       count = 0
       for i in range(n):
           if nums[i] == majority:
               count += 1


       # Return candidate if it occurs more than n/2 times
       if count > n // 2:
           return majority
       else:
           return -1  # No majority element found


# Run the logic directly
if __name__ == "__main__":
   # Hardcoded test input
   nums = [2, 2, 1, 1, 2, 2, 2]


   # Create object and call method
   sol = Solution()
   result = sol.majorityElement(nums)


   # Print result
   if result != -1:
       print("Majority element is:", result)
   else:
       print("No majority element found.")

