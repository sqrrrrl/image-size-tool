class ImageToolError(BaseException):
    def __init__(self, message):
        super()
        self.message = message

class IncorrectImageTypeError(ImageToolError):
    pass

class InvalidImageSizeError(ImageToolError):
    pass
