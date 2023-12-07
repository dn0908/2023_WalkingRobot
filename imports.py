import argparse
import cv2
import os
import time
import RPi.GPIO as GPIO
# from pynput import keyboard
import numpy as np
from skimage.measure import block_reduce
import pickle
import re

import sys

sys.path.insert(0, '/home/diana/2023_WalkingRobot/ar_detection')
from ar_detection.detect import * #