from imports import *
from Image_Class import Image_Processing
from Motor_Class import Motor_Control
from HC_Class import HC_SR04

flag =1
KP = 0.15
KI = 0
KD = 0
limit = 20
output_min = 3

Image = Image_Processing()
Motor = Motor_Control()

cap = cv2.VideoCapture('/dev/video0', cv2.CAP_V4L)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 320)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 240)
while True :
    ret, frame = cap.read()
    if not ret:
        print('failed to grab frame ...')
        continue
    crop = Image.crop(frame,160,120)
    white_mask = Image.select_white(crop, 140)
    # height, width = white_mask.shape
    # center = int(width/2)
    result, forward_sum, left_sum, right_sum = Image.set_path1(crop, 120)
    print('result : ',result)

    if result == 'forward':
        Motor.go_forward(100)
    
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
    cv2.imshow('white test', white_mask)
    cv2.imshow('original', crop)
    if cv2.waitKey(500) == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()