import streamlit as st
import bubblesort as bs
import Mergesortv2 as mg
import Quicksort as qs
import time
import random
#buble as class import
#merge as class impoert
#buttnes



#array_gen = []
#start = time.time()
#bubble_sort([array_gen])
#end = time.time()

#print("It took " + str(end - start) + " seconds")



st.title("Sorteringsalgoritmer")

result = st.button("Run all")

st.write(result)

st.title("Bubblesort")

st.write (bs.bubble_sort_tester(1000))

st.title("Mergesort")

st.write (mg.merge_sort_tester(1000))

st.title("Quicksort")

st.write (qs.quick_sort_tester(1000))