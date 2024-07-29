import error_handling
from error_handling import ErrorHandling
import file_handler


def main():
    file_path = input("Please enter file path: ")
    mode = input("Please enter file operation (r/w): ")
    file_handler.file_handler(file_path, mode)
    if mode == "w":
        content = input("Because of mode write, enter content: ")
        ErrorHandling.write_file(file_path, content)
    elif mode == "r":
        print(error_handling.ErrorHandling.read_file(file_path))




if __name__ == '__main__':
    main()