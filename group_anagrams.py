"""
Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, 
typically using all the original letters exactly once.
"""


class Solution(object):
    def groupAnagrams(self, strs):
        # create a dictionary for each string and compare them
        # ideally have only one dictionary for all same strings and group them
        dic={}
        for i in strs:
            tem=''.join(sorted(i))
            if tem in dic:
                dic[tem].append(i)
            else:
                dic[tem]=[i]
        return dic.values()