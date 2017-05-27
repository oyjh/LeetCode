"""You are climbing a stair case. It takes n steps to reach to the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
"""
class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        logStairs = [1,2]
        for i in xrange(n):
            logStairs.append(logStairs[i] + logStairs[i+1] )
            
        if n == 1:
            return 1
        if n == 2:
            return 2
        else:
            return logStairs[i]
