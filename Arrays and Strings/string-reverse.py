'''
Write a function that takes a string as input and returns the string reversed.

Example 1:

Input: "hello"
Output: "olleh"
Example 2:

Input: "A man, a plan, a canal: Panama"
Output: "amanaP :lanac a ,nalp a ,nam A"
'''

'''
Logic 2 pointer technique:
start: start index, end: end index, swap elements of start and end at each iteration

Python string is immutable hence object assignment str[0] = str[2] is not possible, hence string is first converted to list, reversed --> converted back to string
'''


class Solution:
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        
        length = len(s)
        iterate = len(s)/2 + 1
        
        start = 0
        end = len(s) - 1
        
        lis = list(s)
        
        while start<end:
            temp = lis[start]
            lis[start] = lis[end]
            lis[end] = temp
            start = start + 1
            end = end-1
        s = ''.join(lis)
        return(s)
