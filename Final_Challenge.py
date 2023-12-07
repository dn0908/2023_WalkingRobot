from imports import *
import cv2
import numpy as np
from skimage.measure import block_reduce

from Motor_Class import Motor_Control
Motor = Motor_Control()

from HC_Class import HC_SR04
HC_sensor = HC_SR04()

from AR_Class import AR
AR = AR()


cap = cv2.VideoCapture(0)
success, image = cap.read()

flag = 0
ar_114_count = 0
ar_1156_count = 0
stop_count = 0

# change white & black with threshold
def select_white(image, white):
    lower = np.array([white,white,white])
    upper = np.array([255,255,255])
    white_mask = cv2.inRange(image, lower, upper)
    return white_mask

def crop_left(img,dx,dy):
    y,x = img.shape
    startx = 0
    starty = y-(dy)
    return img[starty:y,startx:startx+2*dx]

def crop_right(img,dx,dy):
    y,x = img.shape
    startx = 640
    starty = y-(dy)
    return img[starty:y,dx:startx]

def crop_front(img):
    dx = 50
    dy = 50
    y = 315
    starty = y-(dy)
    img = img[starty:y,320-dx:320+dx]
    return img

def crop_1(img, startx, starty, dx,dy):
    # y,x = img.shape
    # startx = x//2-(dx)
    # starty = y-(dy)
    crop_img = img[starty:starty+dy,startx:startx+dx]
    return crop_img

def is_obstacle_detected():
    distance = HC_sensor.hc_get_distance()
    if distance <= 15:
        return True

def red_image(image):
    # red_detection = 'no_red'
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)    
    lower_range = np.array([150,150,0], dtype=np.uint8)
    upper_range = np.array([180,255,255], dtype=np.uint8)
    red_mask = cv2.inRange(hsv, lower_range, upper_range)
    
    min_pool=block_reduce(red_mask, block_size=(2,2), func=np.min)
    
    return red_mask, min_pool

while success:
    success, image = cap.read()
    frame = cv2.resize(image, (640,480))
    
    white_mask = select_white(frame, 90) # white mask
    
    # def crop_1(img, startx, starty, dx,dy):
    white_left = crop_1(white_mask, 0, 340, 100, 480-340)
    white_right = crop_1(white_mask, 585, 340, 640-585, 480-340)
    white_front = crop_1(white_mask, 200, 355, 300, 40)

    # sums
    left_sum = int(np.sum(white_left) / 10000)
    right_sum = int(np.sum(white_right) / 10000)
    front_sum = int(np.sum(white_front) / 10000)

    Stop_frame = frame
    red_mask = red_image(Stop_frame)
    

    # print('left sum :', left_sum, 'right sum :', right_sum, 'front sum :', front_sum)
    
    # markers, marker_frame, marker_ID = AR.detect(frame)
    # marker_id = AR_id(markers)
    # print('marker id',marker_id)

    # FLAG 0 : go forward & detect obstacle by hc
    if flag == 0:
        print("🚀 STARTING WITH FLAG 0 🚀")
        if left_sum > 5 and right_sum > 5:
            print('forward')
            Motor.go_forward(100)

        if left_sum < 10 and right_sum < 10:
            print("both low go front")
            Motor.go_forward(100)

        elif right_sum < 5:
            print('right')
            Motor.turn_left(100)

        elif left_sum < 5:
            print('left')
            Motor.turn_right(100)

        if is_obstacle_detected():
            print("--- OBSTACLE DETECTED, EMERGENCY STOP ---")
            Motor.stop()
            time.sleep(5)
            Motor.go_forward(100)
            time.sleep(1)
            flag = 1
            print('FLAGGGGGGGGGGGGGGGGGGGG 1')

    # FLAG 1 after obstacle, PART 1
    if flag ==1 :
        print("🚀   FLAG  1   🚀")
        markers, marker_frame, marker_ID = AR.detect(frame)
        front_count =0
        if left_sum > 5 and right_sum > 5:
            print('forward')
            Motor.go_forward(100)

        if left_sum < 10 and right_sum < 10:
            Motor.go_forward(100)

        elif right_sum < 5:
            print('right')
            Motor.turn_left(100)

        elif left_sum < 5:
            print('left')
            Motor.turn_right(100)

        elif front_sum > 100 and left_sum > 5 and right_sum >5 :
            print('Uturn')
            Motor.turn_left(100)

        # elif front_sum > 100:
        #     if front_count == 0:
        #         Motor.turn_right(100)
        #         front_count+=1
        #     if front_count ==1:
        #         Motor.turn_right(100)
        #         front_count+=1
        #     if front_count ==2:
        #         Motor.turn_left(100)
        #         front_count+=1
        #     if front_count ==3:
        #         Motor.turn_left(100)
        #         front_count +=1
        #     if front_count == 4:
        #         Motor.turn_right(100)
        #         front_count+=1
        #     if front_count ==5:
        #         Motor.turn_right(100)
        #         front_count+=1
        
        if marker_ID == 114:
            print('✅ [AR MARKER] MARKER ID : 114 DETECTED ✅')
            Motor.stop()
            time.sleep(3)
            Motor.go_forward(100)
            time.sleep(2)
            print('turning LEFT.... for 3 seconds')
            Motor.turn_right(100)
            time.sleep(1.5)
            marker_ID = 0
            flag = 1.5
            

    if flag == 1.5:
        count15 =0
        print("🚀   FLAG  1 .5   🚀")
        marker_ID = 0
        markers, marker_frame, marker_ID = AR.detect(frame)
        if left_sum > 5 and right_sum > 5:
            print('forward')
            Motor.go_forward(100)

        if left_sum < 10 and right_sum < 10:
            Motor.go_forward(100)

        elif right_sum < 5:
            print('right')
            Motor.turn_left(100)

        elif left_sum < 5:
            print('left')
            Motor.turn_right(100)

        elif front_sum > 100 and count15 == 0 :
            print('1st turn')
            Motor.turn_left(100)
            count15 += 1

        elif front_sum > 100 and left_sum > 5 and right_sum >5 :
            print('Uturn')
            Motor.turn_left(100)

        if marker_ID == 114:
            print('✅ [AR MARKER] MARKER ID : 114 DETECTED ✅')
            Motor.stop()
            time.sleep(3)
            Motor.go_forward(100)
            time.sleep(2)
            print('turning LEFT.... for 3 seconds')
            Motor.turn_right(100)
            time.sleep(1)
            marker_ID = 0
            flag = 2
    
    # FLAG 2 after 2 114 markers, PART 2
    if flag ==2 :
        print("🚀   FLAG  2   🚀")
        marker_ID = 0
        markers, marker_frame, marker_ID = AR.detect(frame)

        if np.any(red_mask):
            Motor.stop()
            print("STOP detected, ROBOT STOPPED !")
            text = "STOP DETECTED"
            time.sleep(5)
            Motor.go_forward(100)
            stop_count += 1

        if left_sum > 5 and right_sum > 5:
            print('forward')
            Motor.go_forward(100)

        if left_sum < 10 and right_sum < 10:
            Motor.go_forward(100)

        elif right_sum < 5:
            print('right')
            Motor.turn_left(100)

        elif left_sum < 5:
            print('left')
            Motor.turn_right(100)

        elif front_sum > 100 and left_sum > 5 and right_sum >5 :
            print('Uturn')
            Motor.turn_left(100)

        if marker_ID == 114:
            print('✅ [AR MARKER] MARKER ID : 114 DETECTED ✅')
            Motor.stop()
            time.sleep(3)
            print('turning LEFT.... for 2 seconds')
            Motor.go_forward(100)
            time.sleep(1)
            Motor.turn_right(100)
            time.sleep(1.5)
            Motor.go_forward(100)
            time.sleep(2)
            marker_ID = 0
            flag = 3

        # if ar_114_count == 3:
        #     flag = 3
        

    if flag == 3:
        print("🚀   FLAG  3   🚀")
        marker_ID = 0
        markers, marker_frame, marker_ID = AR.detect(frame)
        if marker_ID == 1156:
            print('✅ [AR MARKER] MARKER ID : 1156 DETECTED ✅')
            Motor.stop()
            time.sleep(2)
            Motor.go_forward(100)
            time.sleep(1)
            print('turning LEFT.... for 2 seconds')
            Motor.turn_left(100)
            time.sleep(2)
            ar_1156_count += 1
            marker_ID = 0

        if left_sum > 5 and right_sum > 5:
            print('forward')
            Motor.go_forward(100)

        if left_sum < 10 and right_sum < 10:
            Motor.go_forward(100)

        elif right_sum < 10 and right_sum > 3:
            print('right no line')
            Motor.turn_left(100)
            # Motor.go_forward(100)

        elif right_sum < 2:
            print('right no line but go forward')
            # Motor.turn_left(100)
            Motor.go_forward(100)

        elif left_sum < 5:
            print('left')
            Motor.turn_right(100)

        elif front_sum > 100 and left_sum > 5 and right_sum >5 :
            print('Uturn')
            Motor.turn_left(100)
            flag = 4

        # if ar_1156_count > 1:
        #     flag = 4

    if flag == 4:
        print("🚀   FLAG  4   🚀")
        marker_ID = 0
        markers, marker_frame, marker_ID = AR.detect(frame)
        if marker_ID == 923:
            print('✅ [AR MARKER] MARKER ID : 923 DETECTED ✅')
            Motor.stop()
            time.sleep(2)
            Motor.go_forward(100)
            time.sleep(1)
            print('turning LEFT.... for 2 seconds')
            Motor.turn_right(100)
            time.sleep(2)
            marker_ID = 0

        if left_sum > 5 and right_sum > 5:
            print('forward')
            Motor.go_forward(100)

        if left_sum < 10 and right_sum < 10:
            Motor.go_forward(100)

        elif right_sum < 5:
            print('right')
            Motor.turn_left(100)

        elif left_sum < 5:
            print('left')
            Motor.turn_right(100)

        elif front_sum > 100 and left_sum > 5 and right_sum >5 :
            print('Uturn')
            Motor.turn_left(100)

        if is_obstacle_detected():
            print("--- OBSTACLE DETECTED, EMERGENCY STOP ---")
            Motor.stop()
            time.sleep(5)
            Motor.go_forward(100)
            time.sleep(1)
            flag = 1
            print('FLAGGGGGGGGGGGGGGGGGGGG 1')

    ######## DEFAULT ############################
    # if left_sum > 5 and right_sum > 5:
    #     print('forward')
    #     Motor.go_forward(100)

    # if left_sum < 10 and right_sum < 10:
    #     Motor.go_forward(100)

    # elif right_sum < 5:
    #     print('right')
    #     Motor.turn_left(100)

    # elif left_sum < 5:
    #     print('left')
    #     Motor.turn_right(100)

    # elif front_sum > 100 and left_sum > 5 and right_sum >5 :
    #     print('Uturn')
    #     Motor.turn_left(100)
        
    if cv2.waitKey(500) == ord('q'):
        Motor.stop()
        break

    # cv2.imshow("Original", frame)
    # cv2.imshow("white mask", white_mask)
    # cv2.imshow('AR Marker Frame', marker_frame)
    # cv2.imshow("White LEFT", white_left)
    # cv2.imshow("white RIGHT", white_right)
    # cv2.imshow("white FRONT", white_front)

cap.release()
cv2.destroyAllWindows()