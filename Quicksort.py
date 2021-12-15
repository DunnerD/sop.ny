

import numpy as np
from random import randint
import time

def partition(start, end, array):
	
	
	pivot_index = start
	pivot = array[pivot_index]
	
	
	while start < end:
		
		
		while start < len(array) and array[start] <= pivot:
			start += 1
			
		
		while array[end] > pivot:
			end -= 1
		
		
		if(start < end):
			array[start], array[end] = array[end], array[start]
	
	
	array[end], array[pivot_index] = array[pivot_index], array[end]
	
	
	return end
	

def quick_sort(start, end, array):
	
	if (start < end):
		
	
		p = partition(start, end, array)
		
		
		quick_sort(start, p - 1, array)
		quick_sort(p + 1, end, array)
		
	
def quick_sort_tester(n):
  arr = array_gen(n)
  startTime = time.time()
  sorted_arr = quick_sort(0,n-1,arr)
  stopTime = time.time()
  return stopTime - startTime

def array_gen(n):
  arr = []
  for i in range(n):
    arr.append(randint(0,n))
  return arr

print(quick_sort_tester(10000))