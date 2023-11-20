from imports import *

class AR:
    def __init__(self):
        sys.path.insert(0, '/home/diana/2023_WalkingRobot/ar_detection')
        try:
            import cv2
            from ar_detection.detect import * #

        except ImportError:
            raise Exception('[ERROR] Import Error, Check Path...')
    
    def detect(self, frame):
        markers = detect_markers(frame)
        for marker in markers:
            marker.highlite_marker(frame)
            print("AR marker detected, ID : ", marker)
            return marker, frame
        
if __name__ == '__main__':
    AR = AR()
    capture = cv2.VideoCapture(0)
    frame_captured, frame = capture.read()
	markers, marker_frame = AR.detect(frame)
    cv2.imshow('AR Marker Frame', marker_frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    frame_captured, frame = capture.read()

	# When everything done, release the capture
	capture.release()
	cv2.destroyAllWindows()
