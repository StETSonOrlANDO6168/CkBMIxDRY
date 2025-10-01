# 代码生成时间: 2025-10-01 22:03:58
import streamlit as st

# 定义通知提示系统类
class NotificationSystem:
    def __init__(self, title="Notification"):
        self.title = title

    def show_notification(self, message, severity="info"):
        """显示通知提示信息

        参数：
        message (str): 通知消息内容
        severity (str): 通知消息的严重性，可选值："info", "warning", "error"
        """
        if severity == "info":
            st.info(message)
        elif severity == "warning":
            st.warning(message)
        elif severity == "error":
            st.error(message)
        else:
            st.info(message)  # 默认为 info 类型

# 主程序
def main():
    # 初始化通知提示系统
    notification = NotificationSystem(title="Notification System")

    # 显示不同严重性的通知消息
    notification.show_notification("This is an informational message.")
    notification.show_notification("This is a warning message.", severity="warning")
    notification.show_notification("This is an error message.", severity="error")

    # 添加用户输入框，允许用户自定义通知消息
    user_message = st.text_input("What would you like to say?", key="message")
    if user_message:
        severity = st.selectbox("Choose the severity of your message:",
                             ["info", "warning", "error"], key="severity")
        notification.show_notification(user_message, severity)

if __name__ == "__main__":
    main()