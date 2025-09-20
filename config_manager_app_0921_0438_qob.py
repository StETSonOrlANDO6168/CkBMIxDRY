# 代码生成时间: 2025-09-21 04:38:28
import streamlit as st
import json
import os
from typing import Any, Dict

"""
Config Manager Application
=========================

This application is designed to manage configuration files using Streamlit.
It provides functionality to load, view, create, and delete configuration files.
"""

# Define the configuration directory
CONFIG_DIR = 'configs'  # Directory to store configuration files

# Check if the configuration directory exists, if not create it
if not os.path.exists(CONFIG_DIR):
    os.makedirs(CONFIG_DIR)

@st.cache(allow_output_mutation=True)
def load_config(file_path: str) -> Dict[str, Any]:
    """
    Load a configuration file and return the contents as a dictionary.
    
    :param file_path: Path to the configuration file
    :return: Dictionary representation of the configuration file
    """
    try:
        with open(file_path, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        st.error(f'Configuration file {file_path} not found.')
        return {}
    except json.JSONDecodeError:
        st.error('Failed to parse JSON. Please check the file format.')
        return {}

def save_config(file_path: str, config: Dict[str, Any]) -> None:
    """
    Save a configuration to a file.
    
    :param file_path: Path to the configuration file
    :param config: Dictionary representation of the configuration
    """
    try:
        with open(file_path, 'w') as file:
            json.dump(config, file, indent=4)
    except Exception as e:
        st.error(f'Failed to save configuration: {e}')

def delete_config(file_path: str) -> None:
    """
    Delete a configuration file.
    
    :param file_path: Path to the configuration file
    """
    try:
        os.remove(file_path)
    except FileNotFoundError:
        st.error(f'Configuration file {file_path} not found.')
    except Exception as e:
        st.error(f'Failed to delete configuration: {e}')

def main():
    """
    Main function to run the Streamlit application.
    """
    st.title('Config Manager')
    
    # List all configuration files
    st.subheader('Configuration Files')
    files = os.listdir(CONFIG_DIR)
    if not files:
        st.write('No configuration files found.')
    for file in files:
        st.write(file)
        
    # Create a new configuration file
    new_file = st.text_input('New Configuration File Name (without extension):', key='new_file')
    if st.button('Create New Config', key='create_config'):
        if new_file:
            file_path = os.path.join(CONFIG_DIR, f'{new_file}.json')
            save_config(file_path, {})
            st.success(f'Created new configuration file: {file_path}')
        else:
            st.error('Please enter a file name.')
    
    # Load and view a configuration file
    selected_file = st.selectbox('Select a Configuration File:', files + [None], key='selected_file')
    if selected_file and selected_file != 'None':
        config_path = os.path.join(CONFIG_DIR, selected_file)
        config = load_config(config_path)
        st.subheader('Configuration Details')
        st.json(config)
        
        # Update the configuration file
        update_config = st.text_area('Update Configuration (JSON):', json.dumps(config, indent=4), height=300)
        if st.button('Save Changes', key='save_changes'):
            try:
                update_config = json.loads(update_config)
                save_config(config_path, update_config)
                st.success(f'Configuration updated successfully.')
            except json.JSONDecodeError:
                st.error('Invalid JSON format. Please check the input.')
        
        # Delete the configuration file
        if st.button('Delete Configuration', key='delete_config'):
            delete_config(config_path)
            st.success(f'Configuration file {config_path} deleted successfully.')
            # Remove the file from the list
            files.remove(selected_file)
    
if __name__ == '__main__':
    main()