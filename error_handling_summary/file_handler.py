from contextlib import contextmanager

from error_handling_summary.custom_exceptions import FileProcessingError


@contextmanager
def file_handler(file_path, mode):
    try:
        file = open(file_path, mode)
        yield file

    except FileNotFoundError:
        raise FileProcessingError(f"File not found: {file_path}")
    except PermissionError:
        raise FileProcessingError(f"Permission error occurred while accessing the file: {file_path}")
    except IOError:
        raise FileProcessingError("IO error occurred while accessing the file")
    except ValueError:
        raise FileProcessingError("error value error")
    except UnboundLocalError:
        raise FileProcessingError("last error")

    finally:
        file.close()