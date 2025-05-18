# Image size tool

## What is this?
This tool changes the metadata of a PNG file to alter the image size without altering the image itself. There is a manual
mode, which allows you to adjust the image size as desired, and an automatic mode that attempts to fix images that have 
been altered by a tool like this one.

My cybersecurity class of 2024 gave me the idea to make this tool. Some of our assignments were CTF challenges and one of
them required us to fix an image in order to get a flag. Once we found the issue with the image we simply asked ChatGPT to
change the size metadata of the image and it worked. During my internship I often worked with raw data and thought it would
be a fun project to make a tool that could solve this challenge automatically.

## Requirements
- [Python 3](https://www.python.org/)

## Installation
1. Clone the repository

    ```bash
   git clone https://github.com/sqrrrrl/image-size-tool.git
    ```
   
## Usage
1. Automatic mode

    ```bash
    python3 image_size_tool.py --input <input_file> --output <output_file>
    ```

2. Manual mode

    ```bash
    python3 image_size_tool.py --input <input_file> --output <output_file> --width <width> --height <height>
    ```

## License
This project is licensed under the GPL-3.0 License - see the [LICENSE](LICENSE) file for details.