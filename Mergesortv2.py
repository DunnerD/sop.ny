# Merges two subarrays of arr[].
# First subarray is arr[l..m]
# Second subarray is arr[m+1..r]
from random import randint
import time
 
def merge(arr, l, m, r):
    n1 = m - l + 1
    n2 = r - m
 

    L = [0] * (n1)
    R = [0] * (n2)
 
  
    for i in range(0, n1):
        L[i] = arr[l + i]
 
    for j in range(0, n2):
        R[j] = arr[m + 1 + j]
 
    
    i = 0     
    j = 0     
    k = l     
 
    while i < n1 and j < n2:
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1
 
    # Copy the remaining elements of L[], if there
    # are any
    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1
 
    # Copy the remaining elements of R[], if there
    # are any
    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1
 
# l is for left index and r is right index of the
# sub-array of arr to be sorted
 
 
def mergeSort(arr, l, r):
    if l < r:
 

        m = l+(r-l)//2
 
        mergeSort(arr, l, m)
        mergeSort(arr, m+1, r)
        merge(arr, l, m, r)
 
 


def merge_sort_tester(d):
  arr = array_gen(d)
  n = len(arr)
  startTime = time.time()
  sorted_arr = mergeSort(arr,0,n-1)
  stopTime = time.time()
  return stopTime - startTime

def array_gen(d):
  arr = []
  for i in range(d):
    arr.append(randint(0,d))
  return arr

print(merge_sort_tester(10000))