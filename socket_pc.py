# see__author__ = 'diana'

import threading
import SocketServer
import cv2
import numpy as np
import socket

# img=cv2.imread("frame.jpg",cv2.IMREAD_COLOR)
# cv2.imshow("TEST IMAGE",img)

class KeyboardControl(SocketServer.BaseRequestHandler):
    data=" "
    global img
    def handle(self):
        try:
            while self.data:
                key = cv2.waitKey(1) & 0xFF
                if key==255:
                    key="No Keyboard Input"
                elif key==ord('s'):
                    key="STOP"
                else:
                    key=chr(key)
                self.data = self.request.recv(1024)
                self.request.sendall(key)
                keyboard_data = self.data.decode()
                print(keyboard_data)
            cv2.destroyAllWindows()
        finally:
            print "Connection closed on thread 1"

class ThreadServer(object):
    def server_thread(host, port):
        server = SocketServer.TCPServer((host, port), KeyboardControl)
        server.serve_forever()
    
    ip=socket.gethostbyname(socket.getfqdn())
    keyboard_thread = threading.Thread(target=server_thread(ip, 9999))
    keyboard_thread.start()

if __name__ == '__main__':
    ThreadServer()
