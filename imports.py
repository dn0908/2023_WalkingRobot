import argparse
import cv2
import os
import time
import RPi.GPIO as GPIO
from pynput import keyboard
import numpy as np
from skimage.measure import block_reduce
import pickle
from __future__ import print_function
import sys