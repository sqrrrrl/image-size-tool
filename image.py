import zlib
from io import BytesIO
from errors import IncorrectImageTypeError
from image_size import ImageSize

MIN_AXIS_SIZE = 1
MAX_AXIS_SIZE = 2147483648
PNG_MAGIC_NUMBER = bytes([0x89, 0x50, 0x4e, 0x47, 0x0d, 0x0a, 0x1a, 0x0a])
IDHR_CHUNK_HEADER = bytes([0x49, 0x48, 0x44, 0x52])

IDHR_CHUNK_DATA_OFFSET = 16

IDHR_WIDTH_LEN = 4
IDHR_HEIGHT_LEN = 4
IDHR_CRC_LEN = 4
IDHR_CHUNK_DATA_LEN = 13

def read_image_file(image_path: str) -> BytesIO:
    with open(image_path, "rb") as file:
        buffer = BytesIO(file.read())
        magic_number = buffer.read(len(PNG_MAGIC_NUMBER))
        if magic_number != PNG_MAGIC_NUMBER:
            raise IncorrectImageTypeError("Image is not a png")
        buffer.seek(0)
        return buffer

class Image:
    def __init__(self, path: str):
        self.image = read_image_file(path)

    def save(self, image_path: str):
        self.image.seek(0)
        with open(image_path, "wb") as file:
            file.write(self.image.read())

    def set_size(self, size: ImageSize):
        width = size.width.to_bytes(IDHR_WIDTH_LEN, "big")
        height = size.height.to_bytes(IDHR_HEIGHT_LEN, "big")
        self.image.seek(IDHR_CHUNK_DATA_OFFSET)
        self.image.write(width)
        self.image.write(height)

    def get_size(self) -> ImageSize:
        self.image.seek(IDHR_CHUNK_DATA_OFFSET)
        width = self.image.read(IDHR_WIDTH_LEN)
        height = self.image.read(IDHR_HEIGHT_LEN)
        return ImageSize(int.from_bytes(width, "big"), int.from_bytes(height, "big"))

    def autofix_size(self):
        self.image.seek(IDHR_CHUNK_DATA_OFFSET)
        crc_data = bytearray(IDHR_CHUNK_HEADER + self.image.read(IDHR_CHUNK_DATA_LEN))
        crc_checksum = int.from_bytes(self.image.read(IDHR_CRC_LEN), "big")

        for range_stop in range(MIN_AXIS_SIZE, MAX_AXIS_SIZE + 1):
            check_range = range(MIN_AXIS_SIZE, range_stop + 1)
            height_check_range = [range_stop]
            for width in check_range:
                if width == range_stop:
                    height_check_range = check_range
                for height in height_check_range:
                    crc_data[4:4 + IDHR_WIDTH_LEN] = width.to_bytes(IDHR_WIDTH_LEN, "big")
                    crc_data[8:8 + IDHR_HEIGHT_LEN] = height.to_bytes(IDHR_HEIGHT_LEN, "big")
                    if zlib.crc32(crc_data) == crc_checksum:
                        self.set_size(ImageSize(width, height))
                        return

        raise Exception("You waited all these years and got nothing LMAO")
