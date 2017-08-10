import sys
import pyocr
import pyocr.builders
import argparse
from PIL import Image

# setting args
parser = argparse.ArgumentParser(description='Extract words from input img')
parser.add_argument('img', help='image path')
args = parser.parse_args()

# setting ocr tool
tools = pyocr.get_available_tools()
if len(tools) == 0:
    print("No OCR tool found")
    sys.exit(1)
tool = tools[0]

# extract words (in english)
res = tool.image_to_string(
        Image.open(args.img),
        lang="jpn",
        # lang="eng",
        builder=pyocr.builders.TextBuilder(tesseract_layout=6)
)

print(res)
