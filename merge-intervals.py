# Problem Link: https://leetcode.com/problems/merge-intervals/description/
# Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.

 

# Example 1:

# Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
# Output: [[1,6],[8,10],[15,18]]
# Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6].
# Example 2:

# Input: intervals = [[1,4],[4,5]]
# Output: [[1,5]]
# Explanation: Intervals [1,4] and [4,5] are considered overlapping.
 

# Constraints:

# 1 <= intervals.length <= 104
# intervals[i].length == 2
# 0 <= starti <= endi <= 104

# SOLUTION:

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        output = [intervals[0]]
        for i in range (1, len(intervals)):
            if intervals[i][0] > output[-1][1] or intervals[i][1] < output[-1][0]:
                output.append(intervals[i])
            else:
                if intervals[i][1] >= output[-1][1]:
                    output[-1][1] = intervals[i][1]
                if intervals[i][0] <= output[-1][0]:
                    output[-1][0] = intervals[i][0]           
        return output
