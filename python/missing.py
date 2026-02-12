from typing import List


class Solution(object):
   def findMissingAndRepeatedValues(self, grid):
       """
       :type grid: List[List[int]]
       :rtype: List[int]
       """
       n = len(grid)
       N = n * n
       actualSum = 0
       actualSquareSum = 0


       # Compute the actual sum and sum of squares from the grid
       for i in range(n):
           for j in range(n):
               num = grid[i][j]
               actualSum += num
               actualSquareSum += num * num


       # Compute the expected sum and sum of squares for numbers from 1 to N
       expectedSum = (N * (N + 1)) // 2
       expectedSquareSum = (N * (N + 1) * (2 * N + 1)) // 6


       # Calculate the differences
       sumDifference = actualSum - expectedSum              # a - b
       squareSumDifference = actualSquareSum - expectedSquareSum  # a² - b²


       # Use derived equations to find repeated (a) and missing (b)
       sum_ab = squareSumDifference // sumDifference        # a + b
       repeated = (sum_ab + sumDifference) // 2
       missing = (sum_ab - sumDifference) // 2


       return [repeated, missing]


# Run the function with a sample grid
if __name__ == "__main__":
   # Example: 1 is repeated, 3 is missing
   grid = [
       [1, 2],
       [1, 4]
   ]


   sol = Solution()
   result = sol.findMissingAndRepeatedValues(grid)


   print("Repeated:", result[0])
   print("Missing:", result[1])


