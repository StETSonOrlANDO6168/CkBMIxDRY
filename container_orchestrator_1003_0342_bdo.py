# 代码生成时间: 2025-10-03 03:42:24
import streamlit as st
import subprocess
import json
import os

# 定义全局变量
CONTAINERS = {}

"""
容器编排工具，使用Streamlit框架实现
"""

@st.cache
def get_docker_info(container_name=None):
    """
    获取Docker容器信息
    :param container_name: 容器名称
    :return: JSON格式的容器信息
    """
    try:
        cmd = ['docker', 'inspect', container_name] if container_name else ['docker', 'ps', '-a']
        result = subprocess.run(cmd, check=True, stdout=subprocess.PIPE, text=True)
        return json.loads(result.stdout)
    except subprocess.CalledProcessError as e:
        st.error(f"获取容器信息失败: {e}")
        return []

"