import pickle
import numpy as np

with open('./Test_files/calibration.pkl', 'rb') as f:
    data = pickle.load(f)
    cameraMatrix = np.array(data[0])
    distortion = np.array(data[1])

print(f'cameraMatrix : {cameraMatrix}')
print(f'distortion : {distortion}')
