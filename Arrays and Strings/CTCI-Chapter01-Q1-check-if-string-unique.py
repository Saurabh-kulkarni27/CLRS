'''
Problem Statement: Check If String has unique characters

Function is_unique(ip_list) : Return True if String is unique, else False

Input: 'stadfg'
Output: True

Input: 'stasfg'
Output: False  (character s is repeating)


Approach 1: Using Dictionary
Time Complexity : O(n)
Space Complexity: O(n)

Approach 2: without using additional Data structure
Time complexity : O(n * n)
Space complexity : --
'''
#---------------------
#Approach 1: using Dictionary, append character to dictionary and if is already there return False
def is_unique(input_string):
    dic = {}
    
    
    for x in input_string:
        if x not in dic:
            dic[x] = 1
        else:
            return False
    return True
#---------------------

#---------------------
#Approach 2: without additional data structure (like dictionary)
def is_unique_without_additional_ds(input_string):
    for x in range(0,len(input_string)):
        for y in range(x+1,len(input_string)):
            if input_string[x] == input_string[y]:
                print(x,y)
                return False
    return True
#---------------------


    
    


def main():
    input_string = 'satsgh'
    
    
    
    result1 = is_unique(input_string)
    
    result2 = is_unique_without_additional_ds(input_string)
    print(result1,result2)

main()
