# 代码生成时间: 2025-09-22 07:58:56
import streamlit as st
def format_api_response(data, status_code):
    """Formats API response with given data and status code.

    Args:
        data (dict): The API response data.
        status_code (int): The HTTP status code of the API response.
    
    Returns:
        str: A formatted string representing the API response.
    """
    try:
        # Validate the input data
        if not isinstance(data, dict):
            raise ValueError("Data must be a dictionary.")
        if not isinstance(status_code, int) or not 100 <= status_code <= 599:
            raise ValueError("Status code must be an integer between 100 and 599.")
    
        # Create a formatted response string
        formatted_response = f"Status Code: {status_code}
Data: {data}
"
        return formatted_response
    except Exception as e:
        # Handle any unexpected errors
        error_message = f"An error occurred: {str(e)}
"
        return error_message

def main():
    st.title('API Response Formatter Tool')
    st.write('Enter the API response data and status code to format the response:')
    data = st.text_input('API Data (JSON)', value='{}')
    status_code_input = st.text_input('Status Code (integer)', value='200', type='number')
    
    try:
        # Parse the input data as JSON
        data = json.loads(data)
        status_code = int(status_code_input)
        
        # Format the API response and display it
        formatted_response = format_api_response(data, status_code)
        st.code(formatted_response)
    except json.JSONDecodeError as e:
        st.error(f'Invalid JSON input: {str(e)}')
    except ValueError as e:
        st.error(f'Input error: {str(e)}')
    except Exception as e:
        st.error(f'An unexpected error occurred: {str(e)}')

if __name__ == '__main__':
    main()