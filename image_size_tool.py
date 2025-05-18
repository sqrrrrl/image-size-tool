import sys
import argparse
from errors import ImageToolError
from image import Image
from image_size import ImageSize

def setup_named_args() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", help="The image file to load", type=str, required=True)
    parser.add_argument("--output", help="Output file for the modified image", type=str, required=True)
    parser.add_argument("--width", help="Manually set the width of the image", type=int)
    parser.add_argument("--height", help="Manually set the height of the image", type=int)
    return parser


if __name__ == "__main__":
    args_parser = setup_named_args()
    args = args_parser.parse_args()
    try:
        image = Image(args.input)
        current_size = image.get_size()
        print(f"Image size: {current_size.width}x{current_size.height}")
        if args.width or args.height:
            width = args.width or current_size.width
            height = args.height or current_size.height
            image.set_size(ImageSize(width, height))
        else:
            print("Trying to fix image...")
            image.autofix_size()
            print("Success!")
        new_size = image.get_size()
        print(f"New image size: {new_size.width}x{new_size.height}")
        image.save(args.output)
    except ImageToolError as e:
        print(f"Error: {e.message}")
        sys.exit(1)
    except FileNotFoundError as e:
        print(f"Error: image file does not exist")
        sys.exit(1)
