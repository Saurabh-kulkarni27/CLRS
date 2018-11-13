#insertion sort algorithm

'''
Application
-- small array/list
-- algorithm sorts elements in place

Time Complexity: O(n*2)
Auxiliary Space: O(1)
'''

def sort(listinput):

    '''
    Sorting logic:
    insert the element in proper position

    i loop from 1st element to last of List
    pointer j traversed from i-1 to 0

    '''
    
    for i in range(1,len(listinput)):
        key = listinput[i]
        
        j = i-1

        #insert a[i] into sorted sequence of a[1 to i-1]
        while j >= 0 and listinput[j]>key:
            listinput[j+1] = listinput[j]
            j = j - 1
            print(listinput)
        listinput[j+1]  = key
                
        print('-----------')
    

def main():
    listinput = [5,2,4,6,1,3]
    sort(listinput)


main()

'''
code reference from: CLRS book
sample input and its sorting method on each step:

Input: [5,2,4,6,1,3]

Output:
[5, 5, 4, 6, 1, 3]
-----------
[2, 5, 5, 6, 1, 3]
-----------
-----------
[2, 4, 5, 6, 6, 3]
[2, 4, 5, 5, 6, 3]
[2, 4, 4, 5, 6, 3]
[2, 2, 4, 5, 6, 3]
-----------
[1, 2, 4, 5, 6, 6]
[1, 2, 4, 5, 5, 6]
[1, 2, 4, 4, 5, 6]
-----------
'''


