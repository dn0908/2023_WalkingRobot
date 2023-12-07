from __future__ import print_function
import sys
sys.path.insert(0, '/home/diana/2023_WalkingRobot/ar_detection')

from Motor_Class import Motor_Control
Motor = Motor_Control()
try:
	import cv2
	from ar_detection.detect import * #

except ImportError:
	raise Exception('[ERROR] Import Error, Check Path...')
from imports import *
# from __future__ import print_function

class AR:
    def __init__(self):
        A = 0
    
    def detect(self, frame):
        markers, marker_ID = detect_markers(frame)
        for marker in markers:
            marker.highlite_marker(frame)
            # print("AR marker detected, ID : ", marker)
        return markers, frame, marker_ID
        
if __name__ == '__main__':
    AR = AR()
    cap = cv2.VideoCapture(0)
    if cap.isOpened():  # try to get the first frame
        frame_captured, frame = cap.read()
    while frame_captured:
        markers, marker_frame, marker_ID = AR.detect(frame)
        print(markers)
        # print('marker id',marker_id)
        cv2.imshow('AR Marker Frame', marker_frame)
        print("MARKER ID : ", marker_ID)

        if marker_ID == 923:
            print('yes 114')
        # if 'Marker id=114' in markers:
        #     print('✅ [AR MARKER] MARKER ID : 114 DETECTED ✅')
        #     print('turning LEFT.... for 3 seconds')
        #     Motor.turn_left(100)
        #     time.sleep(3)
        #     # ar_114_count += 1

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        frame_captured, frame = cap.read()

	# When everything done, release the capture
    cap.release()
    cv2.destroyAllWindows()
