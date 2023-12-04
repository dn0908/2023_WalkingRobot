import cv2
import numpy as np
from skimage.measure import block_reduce


vidcap = cv2.VideoCapture(0)
success, image = vidcap.read()

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

while success:
    success, image = vidcap.read()
    frame = cv2.resize(image, (640,480))

    ## Choosing points for perspective transformation
    tl = (65,315)
    bl = (0 ,345)
    tr = (610,315)
    br = (640,345)

    cv2.circle(frame, tl, 5, (0,0,255), -1)
    cv2.circle(frame, bl, 5, (0,0,255), -1)
    cv2.circle(frame, tr, 5, (0,0,255), -1)
    cv2.circle(frame, br, 5, (0,0,255), -1)

    ## perspective transformation
    pts1 = np.float32([tl, bl, tr, br]) 
    pts2 = np.float32([[0, 0], [0, 480], [640, 0], [640, 480]]) 
    
    # Matrix to warp the image for birdseye window
    matrix = cv2.getPerspectiveTransform(pts1, pts2)
    white_mask = select_white(frame, 100) # white mask
    transformed_frame = cv2.warpPerspective(white_mask, matrix, (640,480))

    white_left = crop_left(transformed_frame, 100, 480)
    white_right = crop_right(transformed_frame, 380, 480)
    white_front = crop_front(transformed_frame)

    left_sum = int(np.sum(white_left) / 1000)
    right_sum = int(np.sum(white_right) / 1000)
    front_sum = int(np.sum(white_front) / 1000)

    print('left sum :', left_sum, 'right sum :', right_sum, 'front sum :', front_sum)
    
        
    cv2.imshow("Original", frame)
    cv2.imshow("Bird's Eye View", white_mask)
    cv2.imshow("White LEFT", white_left)
    cv2.imshow("white RIGHT", white_right)
    cv2.imshow("white FRONT", white_front)

    if cv2.waitKey(10) == 27:
        break