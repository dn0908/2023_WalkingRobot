import threading
import socketserver
import socket

class KeyboardControl(socketserver.BaseRequestHandler):
    def handle(self):
        while True:
            key = input("Enter a command: ")  # Wait for user input
            self.request.sendall(key.encode())  # Send the command to the Raspberry Pi

class ThreadServer(object):
    def server_thread(host, port):
        server = socketserver.TCPServer((host, port), KeyboardControl)
        server.serve_forever()

    ip = socket.gethostbyname(socket.getfqdn())
    print(ip)
    keyboard_thread = threading.Thread(target=server_thread, args=(ip, 9898))
    keyboard_thread.start()

if __name__ == '__main__':
    ThreadServer()
