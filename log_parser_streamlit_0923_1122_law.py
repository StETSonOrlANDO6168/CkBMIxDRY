# 代码生成时间: 2025-09-23 11:22:52
import streamlit as st
import pandas as pd
from datetime import datetime
import re

"""
日志文件解析工具，使用STREAMLIT框架实现图形界面交互。
允许用户上传日志文件，并解析显示日志内容。
"""

# 定义主函数
def main():
    """主函数，用于设置STREAMLIT界面"""
    st.title('日志文件解析工具')
    uploaded_file = st.file_uploader('选择一个日志文件', type=['log'])

    # 检查是否上传了文件
    if uploaded_file is not None:
        try:
            # 读取日志文件内容
            log_content = uploaded_file.read().decode('utf-8')
            st.text_area('日志内容', log_content, height=400)

            # 提供解析日志的选项
            st.subheader('解析日志')
            parse_log = st.checkbox('解析日志')
            if parse_log:
                # 解析日志文件
                parsed_logs = parse_log_file(log_content)
                st.dataframe(parsed_logs)
        except Exception as e:
            st.error(f'解析日志时发生错误: {e}')

# 解析日志文件
def parse_log_file(log_content):
    """解析日志文件内容，并返回DataFrame"""
    # 定义日志行的正则表达式
    log_pattern = re.compile(r'\[(.*?)\] (.*?): (.*)')
    # 定义日志行的列名
    log_columns = ['Timestamp', 'Level', 'Message']

    # 使用正则表达式匹配日志行
    logs = log_pattern.findall(log_content)
    # 将匹配结果转换为DataFrame
    logs_df = pd.DataFrame(logs, columns=log_columns)
    return logs_df

if __name__ == '__main__':
    main()