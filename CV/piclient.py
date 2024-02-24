from picamera2 import Picamera2
import cv2
import time

time.sleep(1)
picam2 = Picamera2()
picam2.start()
test = picam2.capture_array()
cv2.imwrite("test.jpg", test)
