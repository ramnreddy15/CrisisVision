import threading
import psutil
import time

def print_cpu_usage():
    while True:
        cpu_usage = psutil.cpu_percent(interval=1)
        print(f"CPU Usage: {cpu_usage}%")
        time.sleep(5)

def print_memory_usage():
    while True:
        memory_usage = psutil.virtual_memory().percent
        print(f"Memory Usage: {memory_usage}%")
        time.sleep(5)

#Create threads
t1 = threading.Thread(target=print_cpu_usage)
t2 = threading.Thread(target=print_memory_usage)

#Start threads
t1.start()
t2.start()
