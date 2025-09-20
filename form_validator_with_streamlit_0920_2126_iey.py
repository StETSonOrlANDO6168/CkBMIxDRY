# 代码生成时间: 2025-09-20 21:26:50
import streamlit as st
def validate_email(email):\
    """验证邮箱是否合法"""\
    from re import fullmatch\
    pattern = r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"\
    if fullmatch(pattern, email) is None: raise ValueError("无效的邮箱地址")\
    else: return True\

def validate_password(password):\
    """验证密码强度"""\
    if len(password) < 8: raise ValueError("密码长度至少为8位")\
    if not any(char.isdigit() for char in password): raise ValueError("密码必须包含数字")\
    if not any(char.isupper() for char in password): raise ValueError("密码必须包含大写字母")\
    if not any(char.islower() for char in password): raise ValueError("密码必须包含小写字母")\
    if not any(char in "!@#$%^&*()" for char in password): raise ValueError("密码必须包含特殊字符")\
    return True\

def main():\
    st.title("表单数据验证器")\
    \
    # 收集用户输入\
    email = st.text_input("输入邮箱")\
    password = st.text_input("输入密码", type="password")\
    \
    try:\
        # 验证表单数据\
        validate_email(email)\
        validate_password(password)\
        st.success("表单验证成功")\
    except ValueError as e:\
        # 处理验证错误\
        st.error(e)\
\
if __name__ == '__main__':\
    main()