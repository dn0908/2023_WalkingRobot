import time
import cv2
import numpy as np
from socket import *
import argparse

# create socket & bind socket to host
parser = argparse.ArgumentParser(description='Press IP adress and Port number')
parser.add_argument('-ip', type=str ,default = '192.168.56.1')
parser.add_argument('-port', type=int, default = 9898)

a = parser.parse_args()
ip = a.ip
port = a.port

client_socket = socket(AF_INET, SOCK_STREAM)
client_socket.connect((ip, port))

try:
	while True:
		client_socket.send("Socket Connection Success !")		
		data = client_socket.recv(1024)
		print(data)
		time.sleep(0.05)
finally:
	client_socket.close()