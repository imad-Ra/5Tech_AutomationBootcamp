def read_file(file_path):
    """
    Reads the content of a file.
    """
    try:
        with open(file_path, 'r') as file:
            content = file.read()
        return content
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
    except IOError:
        # This exception for input/output related errors
        print(f"Error: There was an issue reading the file '{file_path}'.")
    finally:
        # This block always executes, regardless of whether an exception occurred
        print("File reading operation completed.")


def write_file(file_path, content):
    """
    Writes content to a file.
    """
    try:
        with open(file_path, 'w') as file:
            file.write(content)
    except IOError:
        print(f"Error: There was an issue writing to the file '{file_path}'.")
    except PermissionError:
        # This exception is raised when the user doesn't have write permissions
        print(f"Error: You don't have permission to write to '{file_path}'.")
    finally:
        # This block always executes, regardless of whether an exception occurred
        print("File writing operation completed.")

