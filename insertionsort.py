import numpy as np
from random import randint
import time

def insertion_Sort(arr):
  
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        while j >=0 and key < arr[j] :
                arr[j+1] = arr[j]
                j -= 1
        arr[j+1] = key

def insertion_sort_tester(n):
  arr = array_gen(n)
  startTime = time.time()
  sorted_arr = insertion_Sort(arr)
  stopTime = time.time()
  return stopTime - startTime

def array_gen(n):
  arr = []
  for i in range(n):
    arr.append(randint(0,n))
  return arr

print(insertion_sort_tester(10000))