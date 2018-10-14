'''
Source: leetcode
Implement strStr().

Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

Example 1:

Input: haystack = "hello", needle = "ll"
Output: 2
Example 2:

Input: haystack = "aaaaa", needle = "bba"
Output: -1
Clarification:

What should we return when needle is an empty string? This is a great question to ask during an interview.

For the purpose of this problem, we will return 0 when needle is an empty string. This is consistent to C's strstr() and Java's indexOf().
'''

'''
Logic:  iterate in string using for loop, here we will require 1 for loops, when 1st letter in 'needle' match then check if needle is substring
'''

class Solution:
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        
        length = len(needle)
        
        #For the purpose of this problem, we will return 0 when needle is an empty string
        if(length == 0):
            return(0)
        
        first = needle[0]
        
        for i, letter in enumerate(haystack):
            if letter == first:
                if haystack[i:i+length] == needle:    #checking if subset of haystack is in needle. 
                    return (i)
                else:
                    pass
        
        return (-1)
