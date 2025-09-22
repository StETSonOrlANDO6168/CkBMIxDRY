# 代码生成时间: 2025-09-22 20:31:01
import streamlit as st
# 改进用户体验
import os
from pathlib import Path
# 添加错误处理

"""
Batch Renamer Tool
This Streamlit application allows users to batch rename files in a specified directory.
"""

# Define a function to rename files in a directory
def batch_rename(directory: str, file_pattern: str, new_name: str) -> None:
    try:
        # Convert the directory to a Path object
        dir_path = Path(directory)

        # Check if the directory exists
        if not dir_path.exists():
            st.error(f"The directory {directory} does not exist.")
            return

        # Find all files matching the file pattern
        files_to_rename = [file for file in dir_path.glob(file_pattern)]

        # If no files are found, inform the user
        if not files_to_rename:
            st.error(f"No files found matching the pattern {file_pattern} in {directory}.")
            return

        # Rename the files
        for file in files_to_rename:
            # Get the file's extension
            file_extension = file.suffix
            new_file_name = new_name + file_extension
            new_file_path = file.with_name(new_file_name)
            # Check if the new name already exists
            if new_file_path.exists():
                st.warning(f"File {new_file_name} already exists. Skipping...
                ")
                continue
            # Rename the file
            file.rename(new_file_path)
            st.success(f"Renamed {file.name} to {new_file_name}.")
    except Exception as e:
        st.error(f"An error occurred: {e}")
# 优化算法效率

# Streamlit interface
def main():
    # Set the title of the app
    st.title('Batch File Renamer Tool')

    # Create a sidebar to house the user input fields
    st.sidebar.header('Input Parameters')

    # User input for directory
# NOTE: 重要实现细节
    directory = st.sidebar.text_input('Directory Path', '/path/to/directory', key='dir')
# 扩展功能模块

    # User input for file pattern to match
# 增强安全性
    file_pattern = st.sidebar.text_input('File Pattern', '*.txt', key='pattern')

    # User input for new file name
    new_name = st.sidebar.text_input('New File Name', 'new_name', key='name')

    # Button to trigger the renaming process
    if st.sidebar.button('Rename Files'):
        batch_rename(directory, file_pattern, new_name)

if __name__ == '__main__':
    main()