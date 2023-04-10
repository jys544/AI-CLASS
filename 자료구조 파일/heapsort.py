jy# -*- coding: utf-8 -*-
"""
Created on Wed Apr  5 16:04:57 2023

@author: user
"""

def heapSort(A):
    buildHeap(A)
    for last in range(len(A) - 1, 0 ,-1):
        A[last], A[0] = A[0], a[last]
        percolateDown(A, 0, last-1)
        
def buildHeap(A):
    for i in range((len(A)-2) // 2, -1, -1):
        percolateDown(A, i, len(A)-1)
        
        
def percolateDown(A, k:int, end:int):
    child = 2 * k + 1  # left child
    right = 2 * k + 2  # right child
    if child <= end:
            if right <= end and A[child] < A[right]:
                    child = right
                
            if A[k] < A[child]:
                A[k], A[child] = A[child], A[k]
                percolateDown(A,child,END)     

def main():
    print("Heapsort ! ")
    A = [3,8, 2, 4, 8, 1, 2, 0, 5, 9]
    print("A[]:             ",A)
    heapSort(A)
    print("Sorted A[]:", A)

if __name__ == "__main__":
    main()                                                                               				