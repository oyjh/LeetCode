"""
A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

How many possible unique paths are there?
"""
class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        if m < n:
            return self.uniquePaths(n, m)
        ways = [1] * n
        for i in xrange(1, m):
            for j in xrange(1,n):
                ways[j] += ways[j-1]
        
        return ways[n - 1]
