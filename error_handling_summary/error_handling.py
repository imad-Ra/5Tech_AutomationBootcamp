from error_handling_summary.custom_exceptions import FileProcessingError


class ErrorHandling:
    @staticmethod
    def read_file(file_path):
        try:
            with open(file_path, "r") as file:
                return file.read()

        except FileNotFoundError:
            raise FileProcessingError("FileNotFoundError try again")
        except IOError:
            raise FileProcessingError("IOError try again")
        except UnboundLocalError:
            raise FileProcessingError("UnboundLocalError try again")

    @staticmethod
    def write_file(file_path, content):
        try:
            with open(file_path, "w") as file:
                file.write(content)
        except IOError or PermissionError:
            raise FileProcessingError(f"{file_path} not found")
        else:
            print(f"Succeed in writing to {file_path}")