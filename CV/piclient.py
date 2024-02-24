from picamera2 import Picamera2
import cv2
import time

time.sleep(1)
picam2 = Picamera2()
picam2.create_preview_configuration({"format": "YUV420"})
picam2.start()
yuv420 = picam2.capture_array()
cv2.imwrite("test.jpg", yuv420)
