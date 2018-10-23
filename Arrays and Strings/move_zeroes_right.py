'''
Question source: Leetcode
Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Example:

Input: [0,1,0,3,12]
Output: [1,3,12,0,0]
Note:

You must do this in-place without making a copy of the array.
Minimize the total number of operations.
'''



class Solution:
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        '''
        explanation: swap 0 to right, used 2 pointer left,right
        swap only when left element is zero and right is not
        '''
        left,right = 0,1
        
        while(right < len(nums)):
            if nums[left] == 0 and nums[right] != 0:
                temp = nums[left]
                nums[left] = nums[right]
                nums[right] = temp
                
                left += 1
                right += 1
            elif nums[left] != 0 and nums[right] == 0:
                    left = right
                    right += 1
            else:
                right += 1
