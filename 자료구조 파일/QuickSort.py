# -*- coding: utf-8 -*-
"""
Created on Wed Apr  5 13:15:53 2023

@author: user
"""


def quickSort(A, p:int, r:int):
    if p <r:
        q = partition(A, p, r)
        quickSort(A, p, q-1)
        quickSort(A, q+1, r)
        
def partition(A, p:int, r:int) -> int:
    x = A[r]
    i = p-1
    for j in range(p, r):
        if A[j] < x:
            i += 1
            A[i], A[j] = A[j], A[i]
            
    A[i+1], A[r] = A[r], A[i+1]
    print(f"Partitioning array from index {p} to {r}: {A}")
    print(f"Current pivot: {x}")
    print(f"Swapping {A[i+1]} and {A[r]}")
    print(f"Result: {A}\n")
    return i+1        

def main():
    print("Quicksort test")
    A = [3,8,2,4,8,77,1,2,0,5,56,28]
    print("A[]:       ", A)
    quickSort(A, 0, len(A) -1)
    print("Sorted A[]", A)
     
if __name__ == "__main__":
    main()    