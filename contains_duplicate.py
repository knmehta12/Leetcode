"""
Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.
"""


class Solution(object):
    def containsDuplicate(self, nums):
        di={}
        for i in range(len(nums)):
            if nums[i] in di:
                return True
            else:
                di[nums[i]]=1
        return False