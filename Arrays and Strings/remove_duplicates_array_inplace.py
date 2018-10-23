'''
Question source: Leetcode
Given a sorted array nums, remove the duplicates in-place such that each element appear only once and return the new length.

Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

Example 1:

Given nums = [1,1,2],

Your function should return length = 2, with the first two elements of nums being 1 and 2 respectively.

It doesn't matter what you leave beyond the returned length.
Example 2:

Given nums = [0,0,1,1,1,2,2,3,3,4],

Your function should return length = 5, with the first five elements of nums being modified to 0, 1, 2, 3, and 4 respectively.

It doesn't matter what values are set beyond the returned length.
'''



class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
       Method1: compares i,i+1 th elements and removes if same. Works but slow
        '''
        i = 0
        while (i < len(nums)-1):
            if nums[i] == nums[i+1]:
                nums.remove(nums[i+1])
            else:
                i = i+1
        '''
        
        
        Method 2: 2 pointer method, here we are not removing elements instead swapping in-place
        count = 1
        left,right = 0,1
        
        if len(nums) < 2:
            return(len(nums))
        
        while (right < len(nums)):
            
            if nums[left] == nums[right]:      #if same then move right pointer
                right += 1
            else:                              #if not same then swap left+1 and right elements
                left += 1
                nums[left] = nums[right]
                count+=1
        return(count)                         #returning count so that subset of array till count i.e. with distinct element will be returned
        
