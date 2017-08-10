import sys
import pyocr
import pyocr.builders
import argparse
import cv2
from PIL import Image

# setting args
parser = argparse.ArgumentParser(description='Extract word boxes from input imgg')
parser.add_argument('img', help='image path')
args = parser.parse_args()

# setting ocr tool
tools = pyocr.get_available_tools()
if len(tools) == 0:
    print("No OCR tool found")
    sys.exit(1)
tool = tools[0]


# extract word boxes (in english)
res = tool.image_to_string(
        Image.open(args.img),
        # lang="jpn",
        lang="eng",
        builder=pyocr.tesseract.DigitBuilder()
    )

print(res)

# draw boxes to the original image
# img = cv2.imread(args.img)
# for box in res:
#     print(box.content)
#     print(box.position)
#     cv2.rectangle(img, box.position[0], box.position[1], (0, 0, 255), 2)

# display result
# cv2.imshow('result', img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
