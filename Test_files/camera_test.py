import cv2

cap = cv2.VideoCapture('/dev/video0', cv2.CAP_V4L)
width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
fps = cap.get(cv2.CAP_PROP_FPS)
print('original size: %d, %d' %(width, height))
print('original FPS : ', fps)
cap.set(cv2.CAP_PROP_FPS, 60)
new_fps = cap.get(cv2.CAP_PROP_FPS)
print('set fps :', new_fps)
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