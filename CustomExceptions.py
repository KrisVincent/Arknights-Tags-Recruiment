class CustomException(Exception):
    def __init__(self, name, message="A custom exception occurred"):
        # Call the base class constructor with the error message
        super().__init__(message)
        # Set the custom attribute
        self.name = name
