import os

def print_to_console(text: str) -> None:
    """
    Print text to the console.
    
    Args:
        text (str): Text to be printed to the console.
    """
    print(text)

def write_to_file_builtin(text: str, file_path: str) -> None:
    """
    Write text to a file using Python's built-in file operations.
    
    Args:
        text (str): Text to be written to the file.
        file_path (str): Path to the file where text should be written.
    """
    try:
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(text)
            print(f"Successfully wrote to file: {file_path}")
    except Exception as e:
        print(f"Error writing to file: {str(e)}")
