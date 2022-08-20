"""
Given two strings s and t, return true if t is an anagram of s, and false otherwise.
An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, 
typically using all the original letters exactly once.
"""


class Solution(object):
    def isAnagram(self, s, t):
        if len(s)!=len(t):
            return False
        dis={}
        dit={}
        for i in range(len(s)):
            dis[s[i]] = dis.get(s[i], 0) + 1
            dit[t[i]] = dit.get(t[i], 0) + 1
        print(dis)
        print(dit)
        if dis==dit:
            return True
        else:
            return False