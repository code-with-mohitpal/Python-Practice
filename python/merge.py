class Solution(object):
   def merge(self, nums1, m, nums2, n):
       """
       :type nums1: List[int]
       :type m: int
       :type nums2: List[int]
       :type n: int
       :rtype: None. Do not return anything, modify nums1 in-place instead.
       """
       size = m + n
       index = size - 1
       i = m - 1
       j = n - 1


       # Merge from the end of both lists
       while i >= 0 and j >= 0:
           if nums1[i] <= nums2[j]:
               nums1[index] = nums2[j]
               j -= 1
           else:
               nums1[index] = nums1[i]
               i -= 1
           index -= 1


       # Copy remaining elements from nums2 (if any)
       while j >= 0:
           nums1[index] = nums2[j]
           j -= 1
           index -= 1




# Run the test
if __name__ == "__main__":
   # Example input
   nums1 = [1, 2, 3, 0, 0, 0]
   m = 3
   nums2 = [2, 5, 6]
   n = 3


   # Call the optimized merge function
   sol = Solution()
   sol.merge(nums1, m, nums2, n)


   # Print the result
   print("Merged array:", nums1)
