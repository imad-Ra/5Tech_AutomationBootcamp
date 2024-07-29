
class FileProcessingError(Exception):
    """
    Custom exception for file processing errors.

    Attributes:
    message (str): Explanation of the error.
    """

    def __init__(self, message):
        self.message = message
        super().__init__(self.message)