'''
Question : Leetcode
Say you have an array for which the ith element is the price of a given stock on day i.

If you were only permitted to complete at most one transaction (i.e., buy one and sell one share of the stock), design an algorithm to find the maximum profit.

Note that you cannot sell a stock before you buy one.

Example 1:

Input: [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
             Not 7-1 = 6, as selling price needs to be larger than buying price.
             
Input: [7,6,4,3,1]
Output: 0
Explanation: In this case, no transaction is done, i.e. max profit = 0.
'''

class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        
        '''
        Method 1: brute force, used 2 loops
        Time complexity: O(n*n)
        
        buy = 0
        sell = len(prices)-1 
        diff = 0
        x = 0
        
        
        for i in range(len(prices)-1):
            print('i',i)
            buy = prices[i]
            for j in range(i+1,len(prices)):
                sell = prices[j]
                x = sell - buy
                if x>0 and x> diff:
                    diff = x
        return(diff)     
        '''
        
        Method 2: Time complexity : O(n)
        
        
        if len(prices) == 0:
            return 0
        
        buy = prices[0]
        difference = 0
        
        
        
        for i in range(len(prices)):     
            if buy > prices[i]:                 #swap if sell(prices[i]) > buy
                buy = prices[i]
            elif difference < (prices[i] - buy):    
                difference = prices[i] - buy
        return difference
        
