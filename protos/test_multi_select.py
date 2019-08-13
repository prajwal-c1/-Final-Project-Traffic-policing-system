import cv2
import numpy as np
from random import randint



input_video = "./input_images_and_videos/stmarc_video.avi"


cap = cv2.VideoCapture(input_video)

flag, frame = cap.read()

if not flag:
  print('Failed to read video')
  sys.exit(1)
## Select boxes
bboxes = []
colors = [] 
 
# OpenCV's selectROI function doesn't work for selecting multiple objects in Python
# So we will call this function in a loop till we are done selecting all objects
while True:
  # draw bounding boxes over objects
  # selectROI's default behaviour is to draw box starting from the center
  # when fromCenter is set to false, you can draw box starting from top left corner
  bbox = cv2.selectROI('MultiTracker', frame)
  bboxes.append(bbox)
  colors.append((randint(0, 255), randint(0, 255), randint(0, 255)))
  print("Press q to quit selecting boxes and start tracking")
  print("Press any other key to select next object")
  k = cv2.waitKey(0) & 0xFF
  if (k == 113):  # q is pressed
    break
 
print('Selected bounding boxes {}'.format(bboxes))
 	
 	
"""
# Note this code does not work. 
# Specify a vector of rectangles (ROI) 
fromCenter = False
im = cv2.imread("first_frame.jpg")
r=cv2.selectROI("image", im,True,True)

imCrop = im[int(r[1]):int(r[1]+r[3]), int(r[0]):int(r[0]+r[2])]

r2=cv2.selectROI("image", im,True,True)
imCrop2 = im[int(r2[1]):int(r2[1]+r2[3]), int(r2[0]):int(r2[0]+r2[2])]
print(r,r2)

cv2.waitKey(0) """

