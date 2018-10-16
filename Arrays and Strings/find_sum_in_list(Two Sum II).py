'''
Question source: leetcode
Given an array of integers that is already sorted in ascending order, find two numbers such that they add up to a specific target number.

The function twoSum should return indices of the two numbers such that they add up to the target, where index1 must be less than index2.

Note:

Your returned answers (both index1 and index2) are not zero-based.
You may assume that each input would have exactly one solution and you may not use the same element twice.
Example:

Input: numbers = [2,7,11,15], target = 9
Output: [1,2]
Explanation: The sum of 2 and 7 is 9. Therefore index1 = 1, index2 = 2
'''



class Solution:
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        #print(numbers)
        
        
        #brute-force algorithm, using 2 loops, compares every element with each other. 
        '''
        if len(numbers) == 0:
            print('no length')
        
        for i in range(len(numbers)-1):
            for j in range(i+1,len(numbers)):    
                if numbers[i] + numbers[j] == target:
                    return ([i+1,j+1])
        
        
        return ('no match')
        ------------------
        '''
        #2 pointer method
        '''
        logic: uses 2 pointers as name suggests
        left_ptr starts from beginning
        right_ptr starts from end
        compute sum of both ptr, move pointers according to sum to target
        '''
        left_ptr,right_ptr = 0,len(numbers)-1
        print(left_ptr, right_ptr )
        
        while(left_ptr < right_ptr):
            
            sum_elements = numbers[left_ptr] + numbers[right_ptr]
            print(sum_elements)
            if (sum_elements == target):
                return([left_ptr+1,right_ptr+1])
            
            elif (sum_elements < target):   # sum is less hence increase left_ptr
                left_ptr += 1
            
            else:
                right_ptr -= 1           # sum is more hence reduce right_ptr    
