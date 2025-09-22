# 代码生成时间: 2025-09-23 00:39:19
import streamlit as st
def add_item_to_cart(item, quantity):    """ Adds an item to the shopping cart and returns the updated cart. """    if item in cart:        cart[item] += quantity    else:        cart[item] = quantity    return cart
def remove_item_from_cart(item, quantity):    """ Removes an item from the shopping cart and returns the updated cart. """    if item in cart:        if cart[item] <= quantity:            del cart[item]        else:            cart[item] -= quantity    return cart\st.title('Shopping Cart Application')
# NOTE: 重要实现细节

# Initialize an empty cart
cart = {}

# Streamlit widgets for user input
item_input = st.text_input('Enter item name')
# 优化算法效率
quantity_input = st.number_input('Enter quantity', min_value=1, value=1)

# Add item to cart
if st.button('Add to Cart'):    if item_input:        add_item_to_cart(item_input, quantity_input)        st.success(f'Added {quantity_input} {item_input}(s) to cart')
# 改进用户体验

# Remove item from cart
remove_button = st.button('Remove from Cart')
if remove_button:    if item_input in cart:        remove_item_from_cart(item_input, quantity_input)        st.success(f'Removed {quantity_input} {item_input}(s) from cart')

# Display cart contents
if st.button('Show Cart'):    if cart:        st.write('Shopping Cart:')        for item, quantity in cart.items():            st.write(f'{item}: {quantity}')    else:        st.write('Your cart is empty')

# Streamlit session state for cart persistence
if 'cart' not in st.session_state:    st.session_state.cart = {}\
st.session_state.cart = cart