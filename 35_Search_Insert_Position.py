"""Given a sorted array and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You may assume no duplicates in the array."""

class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        try:
            return nums.index(target)
        except ValueError:
            if target > nums[-1]:
                return len(nums)
            elif target < nums[0]:
                return 0
            else:
                ll = 0
                rr = len(nums)
                while rr - ll > 1:
                    mid = (ll + rr) / 2
                    if target == nums[mid]:
                        return mid
                    elif target > nums[mid]:
                        ll = mid
                    else:
                        rr = mid
                return rr
