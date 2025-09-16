# 代码生成时间: 2025-09-17 04:01:08
import streamlit as st

"""
Streamlit application demonstrating various sorting algorithms.

This application allows users to input a list of numbers and choose a sorting algorithm to visualize how it works.
"""

# Define the sorting algorithms
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

def selection_sort(arr):
    for i in range(len(arr)):
        min_idx = i
        for j in range(i+1, len(arr)):
            if arr[min_idx] > arr[j]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        while j >= 0 and key < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key
    return arr

# Initialize the Streamlit app
def main():
    st.title('Sorting Algorithm Visualizer')

    # Input for the user
    input_list = st.text_input('label for the input list', 'Enter numbers separated by space')
    st.write('Choose a sorting algorithm:')
    algorithm = st.selectbox('', ('Bubble Sort', 'Selection Sort', 'Insertion Sort'))

    try:
        # Convert the input string to a list of integers
        numbers = list(map(int, input_list.split()))

        # Check for empty list
        if not numbers:
            st.error('Please enter at least one number.')
            return

        # Perform the sorting algorithm
        if algorithm == 'Bubble Sort':
            sorted_numbers = bubble_sort(numbers.copy())
        elif algorithm == 'Selection Sort':
            sorted_numbers = selection_sort(numbers.copy())
        elif algorithm == 'Insertion Sort':
            sorted_numbers = insertion_sort(numbers.copy())
        else:
            st.error('Unknown sorting algorithm.')
            return

        # Display the results
        st.write(f'Sorted list: {sorted_numbers}')
    except ValueError:
        st.error('Please enter valid integers separated by space.')

if __name__ == '__main__':
    main()