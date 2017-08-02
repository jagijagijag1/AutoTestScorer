import argparse
import cv2

parser = argparse.ArgumentParser(description='OpenCV test: display input img')
parser.add_argument('img', help='image path')
args = parser.parse_args()

img = cv2.imread(args.img)
cv2.imshow("result", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
