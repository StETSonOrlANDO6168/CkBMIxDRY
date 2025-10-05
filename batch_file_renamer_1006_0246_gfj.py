# 代码生成时间: 2025-10-06 02:46:27
import streamlit as st
import os
import re

"""
Streamlit application for batch file renaming.
"""

# 设置Streamlit页面标题
st.title('Batch File Renamer Tool')

# 创建页面元素
st.header('Input Directory')
input_dir = st.text_input('Enter directory path:', '/path/to/your/directory')

st.header('Renaming Pattern')
rename_pattern = st.text_input('Enter renaming pattern (e.g., prefix_XXX.ext):', 'prefix_XXX.ext')

st.header('File Types')
file_types = st.text_input('Enter file types (e.g., *.txt, *.docx):', '*.txt, *.docx')

# 重命名按钮
rename_button = st.button('Rename Files')

# 检查目录是否存在
if rename_button and os.path.exists(input_dir):
    try:
        # 分割文件类型
        file_types_list = file_types.split(', ')
        
        # 遍历目录中的文件
        for file in os.listdir(input_dir):
            # 检查文件类型
            for file_type in file_types_list:
                if re.match(file_type.strip('*'), file):
                    # 生成新文件名
                    new_file_name = re.sub(r'(.*)(\.[^.]+)$', rename_pattern, file)
                    
                    # 原始文件路径和新文件路径
                    old_file_path = os.path.join(input_dir, file)
                    new_file_path = os.path.join(input_dir, new_file_name)
                    
                    # 重命名文件
                    os.rename(old_file_path, new_file_path)
                    st.write(f'Renamed {file} to {new_file_name}')
    except Exception as e:
        st.error(f'Error renaming files: {e}')
else:
    st.warning('Please enter a valid directory path and select file types.')
