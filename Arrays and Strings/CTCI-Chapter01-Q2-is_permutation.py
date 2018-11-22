'''
Problem Statement: Given two string write a method to check if one is permutation of other

Example:
String 1: 'adf'
String 2: 'afd'

Note: strings of different length cannot be permutation i.e. here strings are of same length

Assumptions : 
1) permutation are case sensitive: i.e. 'god' permutation 'Dog' are different
2) No spaces (  )are involved i.e. 'god' and 'god   ' are different

Approach 1: Iterate over string and compute sum of ord() i.e. ASCII values
Time complexity : 2 * n  --> O(n)

Approach 2: Sort and then check if they are equal
Time complexity: O(n)
Space complexity: O(n)
'''

import unittest


#-----------------
#Approach 1: Iterate over string and compute sum of ord() i.e. ASCII values
def if_permutation(s1,s2):
    '''
    Function input (2 input strings)
    returns: True/False if they are permutations
    '''
    if len(s1) != len(s2):
        print('strings different lengths')
        return False
        
    
    sum1 = 0
    sum2 = 0
    for x in s1:
        
        sum1 = sum1 + ord(x)
    
    
    for y in s2:
        
        sum2 = sum2 + ord(y)
    
    if (sum1 == sum2):
        return True
    
    else:
        return False

#-----------------



    
#------------------
def if_permutation_approach2(s1,s2):
    
    if len(s1) != len(s2):
        print('strings different lengths')
        return False
    
    
    dic = {}
    #count = 0
    for x in s1:
        if x not in dic:
            dic[x] = 1
    
    for x in s2:
        if x in dic:
            del dic[x]
    
    return True if len(dic) == 0 else False
#--------------------


def main():
    s1 = 'dog'
    s2 = 'odg'
    result1 = if_permutation(s1,s2)
    result2 = if_permutation_approach2(s1,s2)
    print(result1,result2)
    
main()
