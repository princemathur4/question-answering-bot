class RootException(Exception):
    def __init__(self, error_message=None):
        if error_message is not None:
            self.err_message = error_message

    error_message = "Something went wrong"
    http_code = 500


class InvalidInputParameter(RootException):
    err_message = "Invalid input params provided"


class InvalidRequestPayload(RootException):
    err_message = "Invalid request payload"
    http_code = 400

