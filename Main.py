from __future__ import print_function
from imports import *
from Image_Class import Image_Processing
from Motor_Class import Motor_Control
from HC_Class import HC_SR04
from Stop_Class import Stop

import sys
sys.path.insert(0, '/home/diana/2023_WalkingRobot/ar_detection')

try:
	import cv2
	from ar_detection.detect import * #

except ImportError:
	raise Exception('[ERROR] Import Error, Check Path...')

flag =1
KP = 0.15
KI = 0
KD = 0
limit = 20
output_min = 3

Image = Image_Processing()
Motor = Motor_Control()

cap = cv2.VideoCapture(0, cv2.CAP_V4L)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 320)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 240)
while True :
    ret, frame = cap.read()
    if not ret:
        print('failed to grab frame ...')
        continue

    AR_frame = frame
    markers = detect_markers(AR_frame)
    print("AR MARKERS :", markers)
    for marker in markers:
        marker.highlite_marker(AR_frame)
        Motor.stop()
    cv2.imshow('AR Frame', AR_frame)

    Stop_frame = frame
    red_mask = Image.red_image(Stop_frame, 130)
    if np.any(red_mask):
        print("STOP detected, ROBOT STOPPED !")
        text = "STOP DETECTED"
        Motor.stop()
        cv2.putText(Stop_frame, text, (10, 140), cv2.FONT_HERSHEY_SIMPLEX,1, (255,255,255), 2)
    cv2.imshow('Stop frame', Stop_frame)
    # Stop.detect_stop(Stop_frame)
    # if stop_flag == 1:
    #      text = "STOP DETECTED"
    #      cv2.putText(Stop_frame, text, (10, 140), cv2.FONT_HERSHEY_SIMPLEX,1, (255,255,255), 2)
    # cv2.imshow('Stop Frame', Stop_frame)

    crop = Image.crop(frame,160,120)
    white_mask = Image.select_white(crop, 90)
    # height, width = white_mask.shape
    # center = int(width/2)
    result, forward_sum, left_sum, right_sum = Image.set_path1(crop, 120)
    print('line result : ',result)

    if result == 'forward':
        Motor.go_forward(100)

        if np.any(red_mask):
             Motor.stop()
    
    if result == 'left':
        Motor.turn_left(100)

    if result == 'right':
        Motor.turn_right(100)

    if result == 'stop':
        Motor.stop()
    
    if result == 'backward':
        Motor.go_backward(100)

    #ctrl_output = Image.ctrl(result, forward_sum, left_sum, right_sum)
    #print("RESULT :      ",ctrl_output)
    cv2.imshow('White test', white_mask)
    cv2.imshow('Cropped Frame', crop)

    if cv2.waitKey(500) == ord('q'):
        Motor.stop()
        break
cap.release()
cv2.destroyAllWindows()