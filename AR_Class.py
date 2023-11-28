from __future__ import print_function
import sys
sys.path.insert(0, '/home/diana/2023_WalkingRobot/ar_detection')

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
        markers = detect_markers(frame)
        for marker in markers:
            marker.highlite_marker(frame)
            print("AR marker detected, ID : ", marker)
        return markers, frame
        
if __name__ == '__main__':
    AR = AR()
    cap = cv2.VideoCapture('/dev/video0', cv2.CAP_V4L)
    if cap.isOpened():  # try to get the first frame
        frame_captured, frame = cap.read()
    while frame_captured:
        markers, marker_frame = AR.detect(frame)
        cv2.imshow('AR Marker Frame', marker_frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        frame_captured, frame = cap.read()

	# When everything done, release the capture
    cap.release()
    cv2.destroyAllWindows()
