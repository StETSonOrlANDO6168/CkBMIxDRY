# 代码生成时间: 2025-09-21 19:47:28
import streamlit as st
# 优化算法效率

"""
Inventory Management System

This Streamlit app allows users to manage inventory items, including adding, updating, and deleting items.
"""

# Initialize the inventory as a dictionary
inventory = {}
# 优化算法效率

# Function to add a new item to the inventory
# 优化算法效率
def add_item(item_name, quantity):
    """Adds a new item to the inventory with the specified quantity."""
    if item_name in inventory:
        inventory[item_name] += quantity
    else:
        inventory[item_name] = quantity

# Function to update an existing item's quantity
# 改进用户体验
def update_item(item_name, quantity):
    """Updates the quantity of an existing item in the inventory."""
    if item_name in inventory:
        inventory[item_name] = quantity
    else:
        raise ValueError("Item not found in the inventory.")

# Function to delete an item from the inventory
def delete_item(item_name):
    """Removes an item from the inventory."""
    if item_name in inventory:
        del inventory[item_name]
    else:
        raise ValueError("Item not found in the inventory.")

# Streamlit app layout
# 增强安全性
st.title('Inventory Management System')

# Add item section
# 增强安全性
with st.form('add_item_form'):
    item_name = st.text_input('Item Name')
    quantity = st.number_input('Quantity', min_value=0, value=0)
    add_button = st.form_submit_button('Add Item')
    if add_button:
        if item_name and quantity > 0:
# 扩展功能模块
            add_item(item_name, quantity)
            st.success(f'Item {item_name} added/updated successfully.')
        else:
            st.error('Please enter a valid item name and quantity.')

# Display inventory section
st.header('Current Inventory')
st.write(inventory)

# Update item section
# 增强安全性
with st.form('update_item_form'):
# 扩展功能模块
    item_name = st.selectbox('Select Item', list(inventory.keys()) + ['Add New Item'], index=0)
    quantity = st.number_input('New Quantity', min_value=0, value=0)
    update_button = st.form_submit_button('Update Item')
    if update_button:
        if item_name == 'Add New Item':
            st.experimental_rerun()
        elif quantity > 0:
            update_item(item_name, quantity)
            st.success(f'Item {item_name} updated successfully.')
# TODO: 优化性能
        else:
# 扩展功能模块
            st.error('Please enter a valid quantity.')

# Delete item section
with st.form('delete_item_form'):
    item_name = st.selectbox('Select Item', list(inventory.keys()), key='delete_item_select')
    delete_button = st.form_submit_button('Delete Item')
    if delete_button:
        try:
            delete_item(item_name)
            st.success(f'Item {item_name} deleted successfully.')
        except ValueError as e:
            st.error(str(e))

# Clear button to reset inventory
# 扩展功能模块
clear_button = st.button('Clear Inventory')
if clear_button:
    inventory.clear()
    st.success('Inventory cleared successfully.')