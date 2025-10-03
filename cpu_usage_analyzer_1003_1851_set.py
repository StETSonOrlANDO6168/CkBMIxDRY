# 代码生成时间: 2025-10-03 18:51:46
import streamlit as st
import psutil
import time

"""
CPU Usage Analyzer using Streamlit
"""

# Function to fetch CPU usage
def get_cpu_usage():
    try:
        # Get CPU usage percentage
        cpu_usage = psutil.cpu_percent(interval=1)
        return cpu_usage
    except Exception as e:
        # Log any exceptions that occur
        st.error(f'Failed to fetch CPU usage: {e}')
        return None

# Streamlit app
def main():
    st.title('CPU Usage Analyzer')

    # Allow user to input the number of seconds to track CPU usage
    track_time = st.number_input('Track CPU usage for how many seconds?', min_value=1, max_value=60, value=10, step=1)

    # Display a button to start tracking
    if st.button('Start Tracking'):
        # Track CPU usage for the specified duration
        start_time = time.time()
        while time.time() - start_time < track_time:
            cpu_usage = get_cpu_usage()
            if cpu_usage is not None:
                st.write(f'CPU Usage: {cpu_usage}%')
            time.sleep(1)
        else:
            st.success('Tracking complete!')

if __name__ == '__main__':
    main()