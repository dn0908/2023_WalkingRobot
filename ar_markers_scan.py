from __future__ import print_function
import sys
sys.path.insert(0, '/home/diana/2023_WalkingRobot/ar_detection')

try:
	import cv2
	from ar_detection.detect import * #

except ImportError:
	raise Exception('[ERROR] Import Error, Check Path...')


if __name__ == '__main__':
	from imports import *
	print('Press "q" to quit')
	capture = cv2.VideoCapture(0)
	with open('./Test_files/calibration.pkl', 'rb') as f:
		data = pickle.load(f)
		cameraMatrix = np.array(data[0])
		distortion = np.array(data[1])
		print(cameraMatrix)
	
	
	if capture.isOpened():  # try to get the first frame
		frame_captured, frame = capture.read()
		h, w = frame.shape[:2]
		newCameraMatrix, roi = cv2.getOptimalNewCameraMatrix(cameraMatrix, distortion, (w,h), 1, (w,h))
		dst = cv2.undistort(frame, cameraMatrix, distortion, None, newCameraMatrix)
		x, y, w, h = roi
		frame = dst[y:y+h, x:x+w]

	else:
		frame_captured = False
	while frame_captured:
		markers = detect_markers(frame)
		for marker in markers:
			marker.highlite_marker(frame)
		cv2.imshow('Test Frame', frame)
		if cv2.waitKey(1) & 0xFF == ord('q'):
			break
		frame_captured, frame = capture.read()

	# When everything done, release the capture
	capture.release()
	cv2.destroyAllWindows()
