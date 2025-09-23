# 代码生成时间: 2025-09-24 00:49:25
import streamlit as st
def main():
    """
    Main function to create a responsive Streamlit application.
    This application demonstrates responsive layout design.
    """
    # Create a sidebar to demonstrate responsiveness
    st.sidebar.header('Responsive Sidebar')
    sidebar_option = st.sidebar.selectbox(
        "Choose an option:",
        ["Option 1", "Option 2", "Option 3"]
    )

    # Check the selected option from the sidebar
    if sidebar_option == "Option 1":
        st.title('Option 1 Selected')
        st.write('This is the content for Option 1.')
    elif sidebar_option == "Option 2":
        st.title('Option 2 Selected')
        st.write('This is the content for Option 2.')
    elif sidebar_option == "Option 3":
        st.title('Option 3 Selected')
        st.write('This is the content for Option 3.')

    # Create a responsive layout with columns
    col1, col2 = st.columns(2)

    # Content for the first column
    with col1:
        st.header('Column 1')
        user_input = st.text_input('Type something here:', 'Default value')
        if st.button('Submit'):
            st.write(f"You've entered: {user_input}")

    # Content for the second column
    with col2:
        st.header('Column 2')
        st.write('This is the content for the second column.')

    # Responsive table example
    data = {
        "Name": ["Alice", "Bob", "Charlie"],
        "Age": [25, 30, 35]
    }
    st.write(st.table(data))

    # Responsive image example
    st.image('https://via.placeholder.com/150', caption='Responsive Image', use_column_width=True)

# Run the main function
if __name__ == '__main__':
    main()