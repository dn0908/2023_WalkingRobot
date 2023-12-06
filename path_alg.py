from imports import *
global flag


class Image_Test():
    def __init__(self):
        # self.flag = 0
        print("")

    def first_nonzero(self, arr, axis, invalid_val=-1):
        arr = np.flipud(arr)
        mask = arr!=0
        return np.where(mask.any(axis=axis), mask.argmax(axis=axis), invalid_val)

    # detect red
    def red_image(self,image):
        # red_detection = 'no_red'
        hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)    
        lower_range = np.array([150,150,0], dtype=np.uint8)
        upper_range = np.array([180,255,255], dtype=np.uint8)
        red_mask = cv2.inRange(hsv, lower_range, upper_range)
        
        min_pool=block_reduce(red_mask, block_size=(2,2), func=np.min)
        
        return red_mask, min_pool

    def crop(self, img,dx,dy):
        y,x,z = img.shape
        startx = x//2-(dx)
        starty = y-(dy)
        return img[starty:y,startx:startx+2*dx]
        
    # change white & black with threshold
    def select_white(self, image, white):
        lower = np.array([white,white,white])
        upper = np.array([255,255,255])
        white_mask = cv2.inRange(image, lower, upper)
        return white_mask
    
    def set_path1(self, image, upper_limit, fixed_center = 'False', sample = 10):
        # img = np.array(image)
        # height, width = image.shape[:2]
        # print(height, width)
        # height, width = image.shape # shape of array ex) 240,320
        height = 240
        width = 320
        height = height -1 # array starts from 0, so the last num is 319, not 320
        width = width -1
        center=int(width/2)
        left=0
        right=width
        
        white_distance = np.zeros(width)

        if not fixed_center: 
            #finding first white pixel in the lowest row and reconfiguring center pixel position
            for i in range(center):
                if image[height,center-i] > 200:
                    left = center-i
                    break            
            for i in range(center):
                if (image[height - j, i] > 200).any():
                    right = center+i
                    break    
            center = int((left+right)/2)   

        for i in range (left, right, sample):
            for j in range (upper_limit):
                if (image[height - j, i] > 200).any():
                    white_distance[i] = j
                    break

        
        left_sum = np.sum(white_distance[left:center]+1)
        right_sum = np.sum(white_distance[center:right]) 
        forward_sum = np.sum(white_distance[center-10:center+10])
        # print("--- left sum :",left_sum, 'right sum :', right_sum, 'forward sum :',forward_sum)

        if forward_sum > 160:
            result = 'forward'
        elif left_sum > right_sum + 100:
            result = 'left'
        elif left_sum < right_sum -100:
            result = 'right'
        else:
            result = 'forward'

        return result, forward_sum, left_sum, right_sum

    
if __name__ == "__main__":
    #flag =1
    KP = 0.15
    KI = 0
    KD = 0
    limit = 20
    output_min = 3
    from Motor_Class import Motor_Control
    Motor = Motor_Control()
    Image = Image_Test()
    cap = cv2.VideoCapture(0)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 320)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 240)
    while True :
        ret, frame = cap.read()
        if not ret:
            print('failed to grab frame ...')
            continue
        if ret:
            # crop = Image.crop(frame,120,160)
            crop = frame
            white_mask = Image.select_white(crop, 90)
            # height, width = white_mask.shape
            # center = int(width/2)
            result, forward_sum, left_sum, right_sum = Image.set_path1(crop, 120)
            print('result : ',result, "forward_sum", forward_sum, "left_sum", left_sum, 'right_sum', right_sum)

            if result == 'forward':
                Motor.go_forward(100)
            if result == 'left':
                Motor.turn_left(100)
            if result == 'right':
                Motor.turn_right(100)
            if result == 'stop':
                Motor.stop()  
            if result == 'backward':
                Motor.go_backward(100)
        #ctrl_output = Image.ctrl(result, forward_sum, left_sum, right_sum)
        #print("RESULT :      ",ctrl_output)
        cv2.imshow('white test', white_mask)
        cv2.imshow('original', crop)
        if cv2.waitKey(500) == ord('q'):
            Motor.stop()
            break
    cap.release()
    cv2.destroyAllWindows()