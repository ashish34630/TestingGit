def min_heapify(A,k):
    l = left(k)
    r = right(k)
    if l < len(A) and A[l] < A[k]:
        smallest = l
    else:
        smallest = k
    if r < len(A) and A[r] < A[smallest]:
        smallest = r
    if smallest != k:
        A[k], A[smallest] = A[smallest], A[k]
        #we keep on heapfying if elements are exchanged and smallest still points to previous index which is now not smallest.So we need to again heapify on it.
        min_heapify(A, smallest)

def left(k):
    return 2 * k + 1

def right(k):
    return 2 * k + 2

def build_min_heap(A):
    #Here till n elements are non-leaf nodes and rest all further are leaf nodes
    n = int((len(A)//2)-1)
    for k in range(n, -1, -1):
        min_heapify(A,k)

A = [3,9,2,1,4,5]
build_min_heap(A)
print(A)


#IMPLINKS
#https://www.youtube.com/watch?v=cuL8gXCSA58
#Watch the link in fast mode
