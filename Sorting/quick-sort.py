#Quick sort algorithm

'''
Divide and conquer approach

Divide based on pivot element 
Divide : divide array into 2 parts [(p .. q-1) < pivot] and  [(q+1 .. r) > pivot]
pivot is last element of array

Average case: o(nlog(n))

'''

def partition(arr,p,r):
    
    pivot = arr[r]  
    i = p - 1
    
    
    #loop traverses on array elements
    for j in range(p,r):
        
        #if current element less than pivot then add it to (p .. q-1)
        
        if arr[j] <= pivot:
            i += 1
            arr[i],arr[j] = arr[j],arr[i]
            
    #place the pivot in correct possition, (i+1) = qth position in array
    arr[i+1],arr[r] = arr[r],arr[i+1]
    return (i+1)



def quicksort(arr,p,r):
    if p < r:
        print(arr)
        
        #partition function to divide the array
        q = partition(arr,p,r)
        
        #all elements which are smaller than pivot 
        quicksort(arr,p,q-1)
        
        #here note: divsion is (p .. q-1) and (q+1 .. r), q is the pivot element
        
        #all elements which are greater than pivot
        quicksort(arr,q+1,r)
        
        
        
        



def main():
    arr = [2,8,7,1,3,5,6,4]
    
    p = 0
    r = len(arr) - 1
    
    
    quicksort(arr,p,r)
    
    print('sorted',arr)

main()


'''
input: arr = [2,8,7,1,3,5,6,4]

output: 
[2, 8, 7, 1, 1, 5, 6, 4]
[2, 1, 1, 4, 7, 5, 6, 8]
[1, 1, 2, 4, 7, 5, 6, 8]
[1, 1, 2, 4, 7, 5, 6, 8]
sorted [1, 1, 2, 4, 5, 6, 7, 8]
'''
