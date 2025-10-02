# 代码生成时间: 2025-10-02 23:31:10
import streamlit as st
import os
import hashlib
from typing import List, Dict

"""
重复文件检测器
这个程序使用STREAMLIT框架，允许用户上传一个文件夹，
然后扫描文件夹中的所有文件，找出重复的文件。
"""

def file_hash(filepath: str) -> str:
    """
    计算文件的哈希值
    :param filepath: 文件路径
    :return: 文件的哈希值
    """
    hash_md5 = hashlib.md5()
    with open(filepath, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()

def scan_files(directory: str) -> Dict[str, List[str]]:
    """
    扫描目录中的所有文件，并找出重复文件
    :param directory: 目录路径
    :return: 一个字典，键是文件哈希值，值是具有相同哈希值的所有文件路径列表
    """
    files_dict = {}
    for root, dirs, files in os.walk(directory):
        for file in files:
            filepath = os.path.join(root, file)
            if os.path.isfile(filepath):
                file_hash_value = file_hash(filepath)
                if file_hash_value in files_dict:
                    files_dict[file_hash_value].append(filepath)
                else:
                    files_dict[file_hash_value] = [filepath]
    return {k: v for k, v in files_dict.items() if len(v) > 1}

def main():
    """
    程序的主入口
    """
    st.title("重复文件检测器")
    # 请求用户上传文件夹
    uploaded_file = st.file_uploader("上传文件夹