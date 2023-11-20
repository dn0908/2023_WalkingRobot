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
            return marker, frame
        
if __name__ == '__main__':
    AR = AR()
    capture = cv2.VideoCapture(0)
    if capture.isOpened():  # try to get the first frame
        frame_captured, frame = capture.read()
    while frame_captured:
        markers, marker_frame = AR.detect(frame)
        cv2.imshow('AR Marker Frame', marker_frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        frame_captured, frame = capture.read()

	# When everything done, release the capture
    capture.release()
    cv2.destroyAllWindows()
