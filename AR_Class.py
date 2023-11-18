import cv2
from cv2 import aruco

class ARMarkerDetector:
    def __init__(self, camera_id=0):
        self.cap = cv2.VideoCapture(camera_id)
        self.dictionary = aruco.Dictionary_get(aruco.DICT_6X6_250)
        self.parameters = aruco.DetectorParameters_create()

    def detect_markers(self):
        while True:
            ret, frame = self.cap.read()

            if not ret:
                print("Failed to capture frame")
                break

            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            corners, ids, _ = aruco.detectMarkers(gray, self.dictionary, parameters=self.parameters)

            if ids is not None:
                aruco.drawDetectedMarkers(frame, corners, ids)

            cv2.imshow('AR Marker Detection', frame)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        self.cap.release()
        cv2.destroyAllWindows()

if __name__ == "__main__":
    marker_detector = ARMarkerDetector()
    marker_detector.detect_markers()