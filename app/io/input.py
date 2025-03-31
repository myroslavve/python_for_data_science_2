import pandas as pd

def get_text_from_console() -> str:
    """
    Get text input from the console.
    
    Returns:
        str: Text entered by the user from the console.
    """
    line = input("Enter your text: ")
    return line

def read_file_builtin(file_path: str) -> str:
    """
    Read text from a file using Python's built-in file operations.
    
    Args:
        file_path (str): Path to the file to read.
        
    Returns:
        str: Content of the file as text.
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return file.read()
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        return ""
    except Exception as e:
        print(f"Error reading file: {str(e)}")
        return ""

def read_file_pandas(file_path: str) -> str:
    """
    Read text from a file using pandas library.
    
    Args:
        file_path (str): Path to the file to read.
        
    Returns:
        str: Content of the file as text.
    """
    try:
        df = pd.read_csv(file_path, header=None)
        rows = []
        for _, row in df.iterrows():
            rows.append(','.join(row.astype(str)))
        return '\n'.join(rows)
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        return ""
    except Exception as e:
        print(f"Error reading file with pandas: {str(e)}")
        return ""
