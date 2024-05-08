# Problem Link: https://leetcode.com/problems/container-with-most-water/description/
# You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

# Find two lines that together with the x-axis form a container, such that the container contains the most water.

# Return the maximum amount of water a container can store.

# Notice that you may not slant the container.

 

# Example 1:


# Input: height = [1,8,6,2,5,4,8,3,7]
# Output: 49
# Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.
# Example 2:

# Input: height = [1,1]
# Output: 1
 

# Constraints:

# n == height.length
# 2 <= n <= 105
# 0 <= height[i] <= 104

# SOLUTION:

class Solution:
    def maxArea(self, height: List[int]) -> int:
        # Brute force 
        # maxArr = 0
        # for l in range(len(height)):
        #     for r in range(l+1, len(height)):
        #         arr = (r-l)*min(height[l], height[r])
        #         maxArr = max(maxArr, arr)
        # return maxArr

        l = 0
        r = len(height) - 1
        maxArr = 0
        while l<r:
            arr = (r-l)*min(height[l],height[r])
            maxArr = max(maxArr, arr)
            if height[l] == height[r]:
                if height[l+1] >= height[r-1]:
                    l = l+1
                else:
                    r = r-1
            else:
                if height[l] < height[r]:
                    l = l+1
                else:
                    r = r-1
        return maxArr
