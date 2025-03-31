from app.io.input import get_text_from_console, read_file_builtin, read_file_pandas
from app.io.output import print_to_console, write_to_file_builtin

def main():
    console_text = get_text_from_console()
    print_to_console("Text from console:")
    print_to_console(console_text)
    write_to_file_builtin(console_text, "output/console_input.txt")

    input_path = "input/input.txt"
    file_text = read_file_builtin(input_path)
    print_to_console("\nText from file (built-in):")
    print_to_console(file_text)
    write_to_file_builtin(file_text, "output/file_input_builtin.txt")

    pandas_text = read_file_pandas(input_path)
    print_to_console("\nText from file (pandas):")
    print_to_console(pandas_text)
    write_to_file_builtin(pandas_text, "output/file_input_pandas.txt")

if __name__ == "__main__":
    main() 