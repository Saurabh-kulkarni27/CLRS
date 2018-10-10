class Solution:
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        
        '''
        Logic: (not using Python built in add method)
        1. For binary addition both strings shoul be of equal length. hence used zfill method to match len(smaller string) with bigger string. 
        2. Addition done from last bit hence a reverse for loop.
        3. maintain a carry bit if sum is greater than 1
        '''
        #Step 1: matching string length
        max_ln = max(len(a), len(b))
        
        a = a.zfill(max_ln)
        b = b.zfill(max_ln)
        
        result = ''
        carry = 0
        #Step 2 and 3: reverse loop 
        for i in range(max_ln-1,-1,-1):   #loop from max_ln --> max_ln -1 --> 0
            r = carry
            
            r+=1   if a[i]=='1' else 0
            r+=1   if b[i]=='1' else 0
            result = ('1' if r % 2 ==1 else '0') + result
            carry = 0 if r< 2 else 1
            
        if carry != 0:
            result = '1' + result
        
        return (result)
