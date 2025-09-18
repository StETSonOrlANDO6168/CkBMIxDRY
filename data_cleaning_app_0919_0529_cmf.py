# 代码生成时间: 2025-09-19 05:29:11
import streamlit as st
import pandas as pd

"""
数据清洗和预处理工具应用
"""

# Streamlit页面配置
st.set_page_config(page_title='Data Cleaning and Preprocessing Tool', page_icon='🔧')

"""
主应用程序函数
"""
def main():
    # 页面标题
    st.title('数据清洗和预处理工具')

    # 上传数据文件
    uploaded_file = st.file_uploader('选择数据文件', type=['csv', 'txt', 'xlsx'])
    if uploaded_file is not None:
        try:
            # 读取数据文件
            data = pd.read_csv(uploaded_file) if 'csv' in uploaded_file.name else pd.read_excel(uploaded_file)
            st.dataframe(data.head())  # 显示数据预览

            # 数据清洗选项
            clean_columns = st.multiselect('选择需要清洗的列', data.columns, default=data.columns)

            if clean_columns:
                # 清洗数据
                cleaned_data = clean_data(data, clean_columns)
                st.dataframe(cleaned_data.head())  # 显示清洗后的数据预览
        except Exception as e:
            st.error(f'数据读取失败: {e}')

"""
数据清洗函数
"""
def clean_data(data: pd.DataFrame, columns: list) -> pd.DataFrame:
    # 去除缺失值
    data = data.dropna(subset=columns)

    # 去除重复值
    data = data.drop_duplicates(subset=columns)

    # 转换数据类型
    for column in columns:
        try:
            data[column] = pd.to_numeric(data[column])
        except ValueError:
            pass

    # 其他数据清洗操作可以在这里添加

    return data

if __name__ == '__main__':
    main()