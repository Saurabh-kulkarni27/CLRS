'''
Question: leetcode
Given an array nums and a value val, remove all instances of that value in-place and return the new length.

Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

The order of elements can be changed. It doesn't matter what you leave beyond the new length.

Example 1:

Given nums = [3,2,2,3], val = 3,

Your function should return length = 2, with the first two elements of nums being 2.

It doesn't matter what you leave beyond the returned length.
'''


class Solution:
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        
        '''
        Solution logic:
        2-pointer technique. i pointer normal iteration, k pointer denotes last element of result array
        not making a new list and doing in-place changes in same list to save memory
        '''
        k = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] == nums[i]
                k += 1
        return(k,nums[0:k])
        
        
        
        '''
        Solution 2
        below mewthod uses built in remove() function of list
        '''
        while val in nums:
            nums.remove(val)
