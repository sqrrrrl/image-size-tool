from errors import InvalidImageSizeError

MIN_AXIS_SIZE = 1
MAX_AXIS_SIZE = 2147483648

class ImageSize:
    def __init__(self, width: int, height: int):
        allowed_sizes = range(MIN_AXIS_SIZE, MAX_AXIS_SIZE + 1)
        if width in allowed_sizes and height in allowed_sizes:
            self.width = width
            self.height = height
        else:
            raise InvalidImageSizeError(f"Image width/height must be between {MIN_AXIS_SIZE} and {MAX_AXIS_SIZE} inclusively")
