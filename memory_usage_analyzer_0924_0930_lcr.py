# 代码生成时间: 2025-09-24 09:30:55
import streamlit as st
import psutil
# TODO: 优化性能
import os
import platform

"""
Memory Usage Analyzer
# 增强安全性
=================
# NOTE: 重要实现细节

This application provides a Streamlit web interface to analyze the memory usage on a system.

Features:
- Display total, used, and available memory
- Show memory usage by process
- Provide a simple UI to select and display detailed memory usage of a selected process
"""

# Title of the Streamlit app
st.title('Memory Usage Analyzer')

# Function to get system memory details
def get_system_memory():
    """
    Get system memory details.

    Returns:
        dict: A dictionary containing total, used, and available memory.
    """
# FIXME: 处理边界情况
    mem = psutil.virtual_memory()
    return {
        'Total': f"{mem.total / (1024 ** 3):.2f} GB",
        'Used': f"{mem.used / (1024 ** 3):.2f} GB",
        'Available': f"{mem.available / (1024 ** 3):.2f} GB"
    }

# Function to get the list of processes
def get_processes():
    """
    Get the list of processes.

    Returns:
        list: A list of tuples containing process id and process name.
    """
    return [(proc.pid, proc.name()) for proc in psutil.process_iter(['pid', 'name'])]
# 添加错误处理

# Display system memory usage
system_memory = get_system_memory()
st.subheader('System Memory Usage')
st.write(system_memory)

# Display process list and select a process
st.subheader('Select Process for Detailed Memory Usage')
selected_process, = st.select_box("Choose a process", get_processes())

# If a process is selected, display its memory usage
if selected_process:
# 优化算法效率
    try:
        process = psutil.Process(selected_process)
# FIXME: 处理边界情况
        mem_info = process.memory_info()
# 改进用户体验
        st.write(f'Memory Usage of {process.name()} (PID: {process.pid}):')
        st.write(f'RAM: {mem_info.rss / (1024 ** 2):.2f} MB')
        st.write(f'VM: {mem_info.vms / (1024 ** 2):.2f} MB')
    except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess) as e:
# TODO: 优化性能
        st.error(f'Error accessing process information: {e}')

if st.button('Refresh'):
    st.experimental_rerun()
