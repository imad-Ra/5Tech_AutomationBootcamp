from file_operations import read_file, write_file
from custom_exceptions import FileProcessingError

def file_processing_system():
    """
    Main function to run the file processing system.
    """
    while True:
        file_path = input("Enter the file path: ")
        operation = input("Choose an operation [r(read)/w(write)]: ").lower()

        try:
            if operation == 'r':
                content = read_file(file_path)
                if content:
                    print("File content:")
                    print(content)
            elif operation == 'w':
                content = input("Enter the content to write to the file: ")
                write_file(file_path, content)
            else:
                # Raise our custom exception for invalid operations
                raise FileProcessingError("Invalid operation. Please choose 'read' or 'write'.")
        except FileProcessingError as e:
            # Catch and handle our custom exception
            print(f"Error: {e.message}")



# Entry point of the program
if __name__ == "__main__":
    file_processing_system()