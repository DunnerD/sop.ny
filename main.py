
import bubblesort as bs
import Quicksort as qs
import Mergesortv2 as mg
import Quicksort as qs
import insertionsort as io
import streamlit as st


st.title("Sorteringsalgoritmer")

result = st.button("Run all")


st.title("Bubblesort")

st.write (bs.bubble_sort_tester(1000))

st.title("Mergesort")

st.write (mg.merge_sort_tester(1000))


st.title("Quicksort")

st.write (qs.quick_sort_tester(1000))

st.title("Insertionsort")

st.write (io.insertion_sort_tester(1000))

