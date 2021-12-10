# Creating a bubble sort function  
import numpy as np
from random import randint
import time

def bubble_sort(list1):  
    # Outer loop for traverse the entire list  
    for i in range(0,len(list1)-1):  
        for j in range(len(list1)-1):  
            if(list1[j]>list1[j+1]):  
                temp = list1[j]  
                list1[j] = list1[j+1]  
                list1[j+1] = temp  
    return list1  

def bubble_sort_tester(n):
  arr = array_gen(n)
  startTime = time.time()
  sorted_arr = bubble_sort(arr)
  stopTime = time.time()
  return stopTime - startTime

def array_gen(n):
  arr = []
  for i in range(n):
    arr.append(randint(0,n))
  return arr

print(bubble_sort_tester(1000))

#   steup_code = f"form_main_import{list}"
#   if list != "sorted" else ""
#   stmt = f"{list}({array})"
# times = repeat(setup = setup_code, stmt=stmt, repeat=3, number=10)

# list1 = np.random.randint(1,200000,20000)
# print("The unsorted list is: ", list)
# # Calling the bubble sort function  
# print("The sorted list is: ", bubble_sort(list){min(times)})  