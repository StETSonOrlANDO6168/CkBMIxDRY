# 代码生成时间: 2025-10-08 02:23:27
import streamlit as st
from streamlit.components.v1 import html

"""
Drag and Drop Sorting Component Application using Streamlit.

This application demonstrates how to create a drag and drop sorting
component using Streamlit. The user can drag and drop items to sort them.
"""

# Define the initial list of items to be sorted
ITEMS = ["Apple", "Banana", "Cherry", "Date", "Elderberry"]

# Initialize the session state with the initial list
if 'sorted_items' not in st.session_state:
    st.session_state['sorted_items'] = ITEMS.copy()

def drag_and_drop_component(sorted_items):
    # Create the HTML for the drag and drop component
    html_string = """
    <div id='drag-and-drop-container'>
        {% for index, item in enumerate(sorted_items) %}
        <div class='drag-item' id='{{index}}' draggable='true' ondragstart='dragStart(event)' ondragend='dragEnd(event)'>
            {{item}}
        </div>
        {% endfor %}
    </div>
    <div id='dropzone' ondrop='drop(event)' ondragover='allowDrop(event)'>
        Drag and drop items here.
    </div>
    <style>
        .drag-item {
            padding: 10px;
            margin: 5px;
            background-color: #f0f0f0;
            border: 1px solid #ddd;
            cursor: move;
        }
        #dropzone {
            border: 2px dashed #ccc;
            padding: 20px;
            min-height: 50px;
            text-align: center;
        }
    </style>
    <script>
    function dragStart(event) {
        event.dataTransfer.setData('text/plain', event.target.id);
    }
    function allowDrop(event) {
        event.preventDefault();
    }
    function drop(event) {
        event.preventDefault();
        var data = event.dataTransfer.getData('text/plain');
        var dropZone = document.getElementById('dropzone');
        var draggedElement = document.getElementById(data);
        dropZone.appendChild(draggedElement);
        draggedElement.removeAttribute('draggable');
        draggedElement.style.cursor = 'default';
        // Update the list of sorted items
        var sortedItems = Array.from(document.querySelectorAll('.drag-item')).map(function(item) {
            return item.textContent;
        });
        window.streamlit.setComponentValue(sortedItems);
    }
    function dragEnd(event) {
        // Reset the drag and drop state
        var draggedElement = document.getElementById(event.dataTransfer.getData('text/plain'));
        draggedElement.style.cursor = 'move';
    }
    </script>""
    
    # Render the HTML component
    html(html_string, height=500, scrolling=True)

# Create the drag and drop component
drag_and_drop_component(st.session_state['sorted_items'])

# Display the sorted items
st.write('Sorted Items:', st.session_state['sorted_items'])

# Update the sorted items when the user interacts with the component
@st.cache(allow_output_mutation=True)
def update_sorted_items():
    return st.session_state['sorted_items']

# Register the update function as a callback for the component
st.experimental_component_query('drag-and-drop-container', update_sorted_items)
