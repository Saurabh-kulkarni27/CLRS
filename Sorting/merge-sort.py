#Merge sort algorithm
'''
steps:
Divide -- divide array in two parts n/2   (function in code mergesort)
Combine: -- combine two arrays w.r.t to elements  (function : merge)
'''

def merge(arr,L,R):
    #combine Left and right subarray
    
    i = j = k = 0
    
    
    while i < len(L) and j < len(R):
        
        #if left subarray element is smaller
        if L[i] < R[j]:
            arr[k] = L[i]
            i += 1
            
        #if right subarray element is smaller
        else:
            arr[k] = R[j]
            j += 1
        k += 1
    
    #for all the remaining elements
    while i < len(L):
        arr[k] = L[i]
        i += 1
        k += 1
    
    while j < len(R):
        arr[k] = R[j]
        j += 1
        k += 1
        

def mergesort(arr):
    
    if len(arr) >1: 
    
        #step 1 divide 
        mid = len(arr) // 2
        L = arr[:mid]     #left subarray
        R = arr[mid:]     #right subarray

        #recursively call mergesort() to further divide down to 1 element list
        mergesort(L)
        print('L',L)
        mergesort(R)
        print('R',R)

        #combine step
        merge(arr,L,R)

def main():
    arr = [12,11,13,5,6,7]
    
    mergesort(arr)
    print('sorted',arr)

main()

#reference pseudo code -- CLRS book


'''
Example Input: [12,11,13,5,6,7]

Output of stack:
L [12]
L [11]
R [13]
R [11, 13]
L [11, 12, 13]
L [5]
L [6]
R [7]
R [6, 7]
R [5, 6, 7]

--------
Final sorted [5, 6, 7, 11, 12, 13]

'''
