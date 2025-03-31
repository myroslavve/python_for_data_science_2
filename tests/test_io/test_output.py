import pytest
import os
from app.io.output import write_to_file_builtin

@pytest.fixture
def output_dir(tmp_path):
    """Create a temporary directory for output files."""
    return str(tmp_path)

def test_write_to_file_builtin(output_dir):
    """Test writing to file using built-in methods."""
    file_path = os.path.join(output_dir, "test_output.txt")
    test_content = "Test content\nLine 2"
    
    write_to_file_builtin(test_content, file_path)
    
    assert os.path.exists(file_path)
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
    assert content == test_content

def test_write_to_file_builtin_invalid_path():
    """Test writing to file with invalid path."""
    file_path = "/nonexistent/dir/test.txt"
    write_to_file_builtin("test", file_path) # should not throw an error
