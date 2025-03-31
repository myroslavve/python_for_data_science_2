import pytest
from app.io.input import read_file_builtin, read_file_pandas

@pytest.fixture
def sample_text_file(tmp_path):
    """Create a temporary text file with sample content."""
    file_path = tmp_path / "test.txt"
    content = "Line 1\nLine 2\nLine 3"
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
    return str(file_path)

def test_read_file_builtin(sample_text_file):
    """Test reading file using built-in methods."""
    content = read_file_builtin(sample_text_file)
    assert content == "Line 1\nLine 2\nLine 3"

def test_read_file_builtin_nonexistent():
    """Test reading non-existent file using built-in methods."""
    content = read_file_builtin("nonexistent.txt")
    assert content == ""

def test_read_file_pandas(sample_text_file):
    """Test reading file using pandas."""
    content = read_file_pandas(sample_text_file)
    expected = "Line 1\nLine 2\nLine 3"
    assert content == expected

def test_read_file_pandas_nonexistent():
    """Test reading non-existent file using pandas."""
    content = read_file_pandas("nonexistent.txt")
    assert content == ""