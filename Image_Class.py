from imports import *
global flag


class Image_Processing():
    def __init__(self):
        self.flag = 0

    def first_nonzero(self, arr, axis, invalid_val=-1):
        arr = np.flipud(arr)
        mask = arr!=0
        return np.where(mask.any(axis=axis), mask.argmax(axis=axis), invalid_val)

    # detect red
    def red_image(image):
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

    # integration path algorithm, returns final action and integrated numbers
    '''
    flag = 0 for just driving 
    flag = 1 for stopsign detection
    # flag = 2 for ar marker detection
    '''
    def set_path1(self, image, upper_limit, fixed_center = 'False'):
        height, width = image.shape # shape of array ex) 240,320
        height = height-1 # array starts from 0, so the last num is 319, not 320
        width = width-1
        center=int(width/2)
        left=0
        right=width

        # for integration of left, right road
        white_distance = np.zeros(width)
        delta_w = 8
        delta_h = 3  
        
        if not fixed_center: 
            #finding first white pixel in the lowest row and reconfiguring center pixel position
            for i in range(center):
                if image[height,center-i] > 200:
                    left = center-i
                    break            
            for i in range(center):
                if image[height,center+i] > 200:
                    right = center+i
                    break    
            center = int((left+right)/2)      

        # integrating area of left, right road
        for i in range(int((center-left)/delta_w)+1):
            for j in range(int(upper_limit/delta_h)):
                if image[height-j*delta_h, center-i*delta_w]>200 or j==int(upper_limit/delta_h)-1: 
                    white_distance[center-i*delta_w] = j*delta_h
                    break        
        for i in range(int((right-center-1)/delta_w)+1):
            for j in range(int(upper_limit/delta_h)):
                if image[height-j*delta_h, center+1+i*delta_w] > 200 or j==int(upper_limit/delta_h)-1:
                    white_distance[center+1+i*delta_w] = j*delta_h
                    break
        
        left_sum = np.sum(white_distance[left:center]+1)
        right_sum = np.sum(white_distance[center:right]) 
        forward_sum = np.sum(white_distance[center-10:center+10])
        
        if flag == 0:
            if left_sum > right_sum + 600: 
                result = 'left'
            elif left_sum < right_sum - 600:
                result = 'right'
            elif forward_sum > 260:
                result = 'forward'
            elif forward_sum > 100: 
                if left_sum > right_sum + 100:
                    result = 'left'
                elif left_sum < right_sum - 100:
                    result = 'right'
                else:
                    result = 'forward'
            else: 
                result = 'backward'
    #     
        if flag == 1:
            if left_sum > right_sum + 600: 
                    result = 'left'
            elif left_sum < right_sum - 600:
                result = 'right'
            elif forward_sum > 300: 
                result = 'forward'
            elif forward_sum > 100: 
                if left_sum > right_sum + 100: 
                    result = 'left'
                elif left_sum < right_sum - 100:
                    result = 'right'
                else:
                    result = 'forward'
            else: 
                result = 'backward'
        
        if flag == 2:
            if left_sum > right_sum + 600: 
                    result = 'left'
            elif left_sum < right_sum - 600:
                result = 'right'
            elif forward_sum > 30: 
                result = 'forward'
    #         elif forward_sum > 100: 
    #             if left_sum > right_sum + 100: 
    #                 result = 'left'
    #             elif left_sum < right_sum - 100:
    #                 result = 'right'
    #             else:
    #                 result = 'forward'
            else:
                result = 'stop'
        return result, forward_sum, left_sum, right_sum
    
if __name__ == "__main__":
    Image = Image_Processing()
    cap = cv2.VideoCapture('/dev/video0', cv2.CAP_V4L)
    while True :
        ret, frame = cap.read()
        if not ret:
            print('failed to grab frame ...')
            continue
        crop = Image.crop(frame,160,120)
        white_mask = Image.select_white(crop, 140)
        cv2.imshow('white test', white_mask)
        cv2.imshow('original', crop)
        if cv2.waitKey(500) == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()