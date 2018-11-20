'''
Append zero to end of array
Logic:
-- maintain count pointer
-- for every non-zero element append element to array[count]

Input: [0, 2, 4, 0, 0, 3, 6]
Output: [2, 4, 3, 6, 0, 0, 0]

Time complexity: O(n)
'''

def zeroes_to_end(input_list):
    count = 0
    n = 0
    
    #traverse the array
    for x in input_list:
        #if element not zero
        if x != 0:
            print('element',x,count)
            input_list[count] = x
            count += 1
        else:
            n += 1
    print(n,count)
    
    #appending 0s to end of array. Start position is count, i.e. after all non-zero elements 
    for i in range(count,len(input_list)):
        input_list[count] = 0
        count+=1
        

def main():
    input_list = [0, 2, 4, 0, 0, 3, 6]
    
    
    zeroes_to_end(input_list)
    print(input_list)
    


    
main()
