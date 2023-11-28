from __future__ import print_function
import math
import RPi.GPIO as GPIO
import cv2
import numpy as np
import time
#from timer import Timer

from skimage.measure import block_reduce
# from picamera import PiCamera
# from picamera.array import PiRGBArray

global flag


class Stop:
    def __init__(self):
        # Path of train weights and lables 
        self.labelsPath = "/home/diana/2023_WalkingRobot/ex/edison.names"
        self.LABELS = open(self.labelsPath).read().strip().split("\n")
        
        weightsPath = "/home/diana/2023_WalkingRobot/ex/2nd_final.weights"
        configPath = "/home/diana/2023_WalkingRobot/ex/edison.cfg"

        # Loading the neural network
        self.net = cv2.dnn.readNetFromDarknet(configPath,weightsPath)

    # Detecting stopsign
    def detect_stop(self, image):
        # initialize a list of colors to represent each possible class label
        np.random.seed(42)
        COLORS = np.random.randint(0, 255, size=(len(self.LABELS), 3), dtype="uint8")
        (H, W) = image.shape[:2]
        
        # determine only the "ouput" layers name which we need from YOLO
        ln = self.net.getLayerNames()
        ln = [ln[i[0] - 1] for i in self.net.getUnconnectedOutLayers()]
        
        # construct a blob from the input image and then perform a forward pass of the YOLO object detector, 
        # giving us our bounding boxes and associated probabilities
        blob = cv2.dnn.blobFromImage(image, 1 / 255.0, (320, 224), swapRB=True, crop=False)
        self.net.setInput(blob)
        layerOutputs = self.net.forward(ln)
        
        boxes = []
        confidences = []
        classIDs = []
        threshold = 0.1 # parameter
        
        # loop over each of the layer outputs
        for output in layerOutputs:
            # loop over each of the detections
            for detection in output:
                # extract the class ID and confidence (i.e., probability) of
                # the current object detection
                scores = detection[5:]
                classID = np.argmax(scores)
                confidence = scores[classID]

                # filter out weak predictions by ensuring the detected
                # probability is greater than the minimum probability
                # confidence type=float, default=0.5
                
    #             text = 'labels: '+ str(LABELS[classID])+'//'+ str(confidence)
    #             cv2.putText(image, text, (10, 140), cv2.FONT_HERSHEY_SIMPLEX,1, (255,255,255), 2)
    #             print('/////////////////conf: {}'.format(confidence))
                
                if confidence > threshold:
                    # scale the bounding box coordinates back relative to the
                    # size of the image, keeping in mind that YOLO actually
                    # returns the center (x, y)-coordinates of the bounding
                    # box followed by the boxes' width and height
                    box = detection[0:4] * np.array([W, H, W, H])
                    (centerX, centerY, width, height) = box.astype("int")

                    # use the center (x, y)-coordinates to derive the top and
                    # and left corner of the bounding box
                    x = int(centerX - (width / 2))
                    y = int(centerY - (height / 2))

                    # update our list of bounding box coordinates, confidences,
                    # and class IDs
                    boxes.append([x, y, int(width), int(height)])
                    confidences.append(float(confidence))
                    classIDs.append(classID)

        # apply non-maxima suppression to suppress weak, overlapping bounding boxes
        idxs = cv2.dnn.NMSBoxes(boxes, confidences, threshold, 0.1)
    #     if confidences[0] is not None:
        # print('/////////////////conf: {}'.format(confidences))
        # ensure at least one detection exists
        if len(idxs) > 0:
            # flag = 0 for stopsign detection
            # print(width)
            # global flag
            # global stop_flag
            # flag =+ 1
            # stop_flag =+ 1
            print('STOP detected')
            
            # print(flag)
            # if stopsign detected, stop for 5secs
            # stop5()
            #stop_flag += 1 
    #         stop_time = time.time()
            # loop over the indexes we are keeping 
    #         for i in idxs.flatten():
    #             # extract the bounding box coordinates
    #             (x, y) = (boxes[i][0], boxes[i][1])
    #             (w, h) = (boxes[i][2], boxes[i][3])

    # #          draw a bounding box rectangle and label on the image
    #             color = (255,0,0)
    #             cv2.rectangle(image, (x, y), (x + w, y + h), color, 2)
    #             text = 'labels: '+ str(self.LABELS[classIDs[i]])+'//'+ str(confidences[i])
    #             cv2.putText(image, text, (10, 140), cv2.FONT_HERSHEY_SIMPLEX,1, (255,255,255), 2)
        
        return image


if __name__ == '__main__':
    stop = Stop()
    cap = cv2.VideoCapture('/dev/video0', cv2.CAP_V4L)

    while True:
        # start_time = time.time()
        ret, frame = cap.read()
        if ret :
            frame = cv2.resize(frame, (640, 480))
            # frame = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
            # results = yolo.detect_(frame, model = model)
            # frame = cv2.cvtColor(frame,cv2.COLOR_RGB2BGR)
            # yolo_frame = yolo.plot_boxes(results, frame,classes = classes)
            stop.detect_stop(frame)
            cv2.imshow("cam", frame)

            if cv2.waitKey(500) == ord('q'):
                break

    cap.release()
    cv2.destroyAllWindows()