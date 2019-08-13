# Imports
import tensorflow as tf

# Object detection imports
from utils import backbone
from api import object_detection
from Noinput import weather_report
import cv2
import sys
from random import randint




input_video = "./input_images_and_videos/t1.mp4"


cap = cv2.VideoCapture(input_video)

if cap.isOpened()== False:
	weather_report.weather("Delhi")
	sys.exit(1)


detection_graph, category_index = backbone.set_model('ssdlite_mobilenet_v2_coco_2018_05_09')

flag, frame = cap.read()

if(cap.get(cv2.CAP_PROP_POS_FRAMES)==1):
	i=cv2.imwrite('utils/first_frame.jpg', frame)

bboxes = []
colors = [] 
 
# OpenCV's selectROI function doesn't work for selecting multiple objects in Python
# So we will call this function in a loop till we are done selecting all objects
while True:
  # draw bounding boxes over objects
  # selectROI's default behaviour is to draw box starting from the center
  # when fromCenter is set to false, you can draw box starting from top left corner
  bbox = cv2.selectROI('MultiTracker', frame)
  bboxes.append(list(bbox))
  colors.append((randint(0, 255), randint(0, 255), randint(0, 255)))
  print("Press q to quit selecting boxes and start tracking")
  print("Press any other key to select next object")
  k = cv2.waitKey(0) & 0xFF
  if (k == 113):  # q is pressed
    cap.release()
    cv2.destroyAllWindows()
    break

object_detection.object_counting(input_video, detection_graph, category_index,bboxes,colors) # counting all the objects


