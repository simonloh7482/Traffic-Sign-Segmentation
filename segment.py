import argparse
import os
import cv2 as cv
import numpy as np

# os.chdir("C:\\Users\\Simon Loh\\iCloudDrive\\UTAR\\Y3S1\\mini project\\Week 11")

# argument parser
parser = argparse.ArgumentParser(description = "traffic sign segmentation")
parser.add_argument('--input', help = "path to input image", default = '005_0026.png')
args = parser.parse_args()

blue_low = (80, 150, 60)
blue_high = (140, 255, 255)

red_low = (0, 70, 50)
red_high = (10, 255, 255)

red_low2 = (170, 70, 50)
red_high2 = (179, 255, 255)

yellow_low = (5, 105,65)
yellow_high = (40, 255, 255)

img = cv.imread(cv.samples.findFile(args.input))

kernel = np.ones((5,5), np.uint8)
colour_results = []

#Apply median blur
blur = cv.medianBlur(img, 5)
    
#HSV
hsv = cv.cvtColor(blur, cv.COLOR_BGR2HSV)

#mask
mask_blue = cv.inRange(hsv, blue_low, blue_high)
mask_red = cv.inRange(hsv, red_low, red_high)
mask_red2 = cv.inRange(hsv, red_low2, red_high2)
mask_yellow = cv.inRange(hsv, yellow_low, yellow_high)
mask2 = cv.add(mask_blue, mask_yellow)
mask3 = cv.add(mask_red, mask_red2)
#final mask
final_mask = cv.add(mask2, mask3)
#segment using color mask
res = cv.bitwise_and(img, img, mask = final_mask)
    
#find edges and contour to draw bounding box
res_blur = cv.GaussianBlur(res, (5, 5), 0)
    
canny = cv.Canny(res_blur, 50, 250, apertureSize = 3)
    
contours, hierarchy = cv.findContours(canny, cv.RETR_EXTERNAL,cv.CHAIN_APPROX_SIMPLE)
    
length = []
if len(contours) > 0:
    for i in contours:
        length.append(len(i))

    Idx_max = np.argmax(length)
    cnt = contours[Idx_max]

    x, y, w, h = cv.boundingRect(cnt)
else: #no contours
    x=0
    y=0
    w=0
    h=0
#draw bounding box    
cv.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 1, cv.LINE_AA)

cv.namedWindow('image', cv.WINDOW_NORMAL)
cv.imshow('image', img)
cv.waitKey(0)
cv.destroyAllWindows()
