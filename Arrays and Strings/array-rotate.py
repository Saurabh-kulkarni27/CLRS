'''
Algorithm to rotate the array (python list) by factor n
Example:
input_list = [1,2,3,4,5,6,7]
Rotation factor = 2

Rotation logic:
Step 1 rotate: input_list[0 to factor-1 ]
output of step 1: [2, 1, 3, 4, 5, 6, 7]   (only elements at position 0,1 rotated as factor is 2)

Step 2 rotate: input_list[factor-1  to len(input_list)-1 ]
output of step 2: [2, 1, 7, 6, 5, 4, 3]   (now all remaining elements are rotated)

Step 3: rotate entire list
output of step 3: [3, 4, 5, 6, 7, 1, 2]   (correct output after rotation by 2 positions)

As modification are don on list in place the time complexity is O(n)

'''


#function to rotate list in place. 2 pointers technique used
def rotate(input_list, start, end):
    while start < end:
        input_list[start],input_list[end] = input_list[end],input_list[start]
        start+=1
        end-=1



def array_rotate(input_list,factor):

    #check for edge case where factor is greater than len(input_list)
    if factor > len(input_list):
        factor = factor % len(input_list)
    
    #Step1 as described above
    rotate(input_list,0,factor-1)
    print(input_list)
    
    #Step2
    rotate(input_list,factor,len(input_list)-1)
    print(input_list)
    
    #Step3
    rotate(input_list,0,len(input_list)-1)
    print(input_list)
    



def main():
    input_list = [1,2,3,4,5,6,7]
    factor = 2
    
    array_rotate(input_list,factor)
    

main()
