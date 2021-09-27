import socket
import threading
from queue import Queue

target = socket.gethostbyname(socket.gethostname())
queue = Queue()

open_ports = []


def fill_que(port_list):
    for port in port_list:
        queue.put(port)


# try to connect with socket to a port, if port is open return true else return false
def port_scan(port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((target, port))
        return True
    except:
        return False


def worker():
    while queue.not_empty:
        # get one port from queue
        port = queue.get()
        if port_scan(port):
            print("PORT {} IS OPEN!".format(port))
            open_ports.append(port)


# for port in range(1, 1024):
#     result = port_scan(port)
#     if result:
#         print(f"PORT IS {port} OPEN!")
#     else:
#         print(f"Port {port} is closed")


port_list = range(1, 1024)

fill_que(port_list)

thread_list = []

# crating 100 threads and add to a thread list
for t in range(100):
    thrad = threading.Thread(target=worker)
    thread_list.append(thrad)

# run all thread from thread_list
for thread in thread_list:
    thread.start()

# join all threads and set order starting
for thread in thread_list:
    thread.join()

print("OPEN PORTS ARE: ", open_ports)
