import cv2

cap = cv2.VideoCapture('/dev/video0', cv2.CAP_V4L)
while True :
    ret, frame = cap.read()
    if not ret:
        print('failed to grab frame ...')
        continue
    
    cv2.imshow('camera test', frame)
    if cv2.waitKey(500) == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()