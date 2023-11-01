import time
import cv2
import numpy as np
from socket import *
import argparse

# create a socket and bind socket to the host
parser = argparse.ArgumentParser(description='Press IP adress and Port number')
parser.add_argument('-ip', type=str ,default = '172.30.1.88')
parser.add_argument('-port', type=int, default = 9898)

a = parser.parse_args()
ip = a.ip
port = a.port

client_socket = socket(AF_INET, SOCK_STREAM)
client_socket.connect((ip, port))

try:
	while True:
		client_socket.send("Fine Connection")		
		data = client_socket.recv(1024)
		print(data)
		time.sleep(0.05)
finally:
	client_socket.close()
