"""Given an integer, write a function to determine if it is a power of three.
"""


import math


class Solution(object):
    def __init__(self):
        self.__maxLog3 = int(math.log(0x7fffffff) / math.log(3))
        self.__maxPow3 = 3 ** self.__maxLog3

    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        return n > 0 and self.__maxPow3 % n == 0
