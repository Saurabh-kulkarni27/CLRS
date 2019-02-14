'''
Quick Sort: CLRS style
Divide and conquer approach

Worst case: O(n * n) [can be avoided by choosing pivot]
Average case: O(n log n)  [high probabibility]

Also does this in-place so no extra space needed

Approach: last element selected as pivot
1) Divide the Array into two subsets, left subset will have elements less than equal to pivot,
right subset will have elements greater than pivot
2) Recursively sort left and right subset
'''



ip_array = [2, 8, 7, 1, 3, 5, 6, 4]


def partition(A, p, r):
    # last element choosen as pivot
    x = A[r]

    # pinter i used for inplace swap withing array
    i = p - 1

    for j in range(p, r):  # (r-1) as last element is pivot

        # if element is small, they are collected in left subset, i pointer keeps track of left subset
        if A[j] <= x:
            i += 1
            A[i], A[j] = A[j], A[i]

    # placing pivot in perfect place
    A[i + 1], A[r] = A[r], A[i + 1]
    return (i + 1)


def quicksort(A,p,r):
    print(A,p,r)


    if (p < r):
        q = partition(A, p, r)
        #left subset
        quicksort(A,p,q-1)
        #right subset
        quicksort(A,q+1,r)


quicksort(ip_array,0,len(ip_array)-1)
print(ip_array)


