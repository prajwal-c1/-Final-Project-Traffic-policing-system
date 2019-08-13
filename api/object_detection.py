
import tensorflow as tf
import csv
import cv2
import numpy as np
from utils import visualization_utils as vis_util
import time
from random import randint

# Variables
total_passed_vehicle = 0  # using it to count vehicles


def object_counting(input_video, detection_graph, category_index,bboxes,colors):
		


        # input video
        
        cap = cv2.VideoCapture(input_video)

        total_passed_vehicle = 0
  
   
        with detection_graph.as_default():
          with tf.Session(graph=detection_graph) as sess:
            # Definite input and output Tensors for detection_graph
            image_tensor = detection_graph.get_tensor_by_name('image_tensor:0')

            # Each box represents a part of the image where a particular object was detected.
            detection_boxes = detection_graph.get_tensor_by_name('detection_boxes:0')

            # Each score represent how level of confidence for each of the objects.
            # Score is shown on the result image, together with the class label.
            detection_scores = detection_graph.get_tensor_by_name('detection_scores:0')
            detection_classes = detection_graph.get_tensor_by_name('detection_classes:0')
            num_detections = detection_graph.get_tensor_by_name('num_detections:0')

            # for all the frames that are extracted from input video
            while(cap.isOpened()):

                ret, frame = cap.read()
                  	
                if not  ret:
                    print("end of the video file...")
                    break
                    
               
                input_frame = frame
                
             
              
                for i in range(len(bboxes)):
                	colors.append((randint(0, 255), randint(0, 255), randint(0, 255)))
                	upper_left = (bboxes[i][0],bboxes[i][1])
                	bottom_right = (bboxes[i][2]+bboxes[i][0],bboxes[i][1]+bboxes[i][3])
                	cv2.rectangle(frame, bottom_right, upper_left,colors[i], 2)
                # Expand dimensions since the model expects images to have shape: [1, None, None, 3]
                image_np_expanded = np.expand_dims(input_frame, axis=0)

                # Actual detection.
                (boxes, scores, classes, num) = sess.run(
                    [detection_boxes, detection_scores, detection_classes, num_detections],
                    feed_dict={image_tensor: image_np_expanded})

                # insert information text to video frame
                font = cv2.FONT_HERSHEY_SIMPLEX
                
                # Visualization of the results of a detection.        
                counter, csv_line, counting_mode ,count= vis_util.visualize_boxes_and_labels_on_image_array(bboxes,cap.get(1),
                                                                                                      input_frame,
                                                                                                      1,
                                                                                                      np.squeeze(boxes),
                                                                                                      np.squeeze(classes).astype(np.int32),
                                                                                                      np.squeeze(scores),
                                                                                                      category_index,
                                                                                                      use_normalized_coordinates=True,
                
                                                                                                    
                                                                                                      line_thickness=2)
                
                
                cv2.rectangle(frame, (10,10), (400,200),(255,255,255), -1)
                
                for i in range(len(bboxes)):
                	if(len(counting_mode) == 0 or count[i]==""):
                		cv2.putText(frame, "...", (10, 35), font, 0.8, (0,255,255),2,cv2.FONT_HERSHEY_SIMPLEX)                       
                	else:
                		cv2.putText(frame,str("Total :"+counting_mode), (10, 35), font, 0.8,  (0,255,255),2,cv2.FONT_HERSHEY_SIMPLEX)
                		cv2.putText(frame, count[i], (10, 70+(i*25)), font, 0.8, colors[i],2,cv2.FONT_HERSHEY_SIMPLEX) 
                
                
                #cv2.putText(frame, count[0], (10, 70), font, 0.8,  (0,255,235),2,cv2.FONT_HERSHEY_SIMPLEX)
                #cv2.putText(frame, count[1], (10, 100), font, 0.8,  (0,245,245),2,cv2.FONT_HERSHEY_SIMPLEX)  


         			
                cv2.imshow('object counting',input_frame)
      
		
                if cv2.waitKey(1) & 0xFF == ord('q'):
                        break

         

            cap.release()
            cv2.destroyAllWindows()


def object_counting_web(detection_graph, category_index):
		


        # input video
        cap = cv2.VideoCapture(0)

        total_passed_vehicle = 0
  
   
        with detection_graph.as_default():
          with tf.Session(graph=detection_graph) as sess:
            # Definite input and output Tensors for detection_graph
            image_tensor = detection_graph.get_tensor_by_name('image_tensor:0')

            # Each box represents a part of the image where a particular object was detected.
            detection_boxes = detection_graph.get_tensor_by_name('detection_boxes:0')

            # Each score represent how level of confidence for each of the objects.
            # Score is shown on the result image, together with the class label.
            detection_scores = detection_graph.get_tensor_by_name('detection_scores:0')
            detection_classes = detection_graph.get_tensor_by_name('detection_classes:0')
            num_detections = detection_graph.get_tensor_by_name('num_detections:0')

            # for all the frames that are extracted from input video
            while(cap.isOpened()):
            	
                ret, frame = cap.read()
                input_frame=frame
               
           
				
                if not  ret:
                    print("end of the video file...")
                    break
                
             
                
    
                image_np_expanded = np.expand_dims(input_frame, axis=0)

                # Actual detection.
                (boxes, scores, classes, num) = sess.run(
                    [detection_boxes, detection_scores, detection_classes, num_detections],
                    feed_dict={image_tensor: image_np_expanded})

                # insert information text to video frame
                font = cv2.FONT_HERSHEY_SIMPLEX
                
                # Visualization of the results of a detection.        
                counter, csv_line, counting_mode = vis_util.visualize_boxes_and_labels_on_image_array(cap.get(1),
                                                                                                      input_frame,
                                                                                                      1,
                                                                                                      np.squeeze(boxes),
                                                                                                      np.squeeze(classes).astype(np.int32),
                                                                                                      np.squeeze(scores),
                                                                                                      category_index,
                                                                                                      use_normalized_coordinates=True,
                
                                                                                                      line_thickness=2)
                if(len(counting_mode) == 0):
                    cv2.putText(input_frame, "...", (10, 35), font, 0.8, (0,255,255),2,cv2.FONT_HERSHEY_SIMPLEX)                       
                else:
                    cv2.putText(input_frame, counting_mode, (10, 35), font, 0.8, (0,255,255),2,cv2.FONT_HERSHEY_SIMPLEX)

                #output_movie.write(input_frame)
                
      
         		
                cv2.imshow('object counting',input_frame)
              
		
                if cv2.waitKey(1) & 0xFF == ord('q'):
                        break

         

            cap.release()
            cv2.destroyAllWindows()

