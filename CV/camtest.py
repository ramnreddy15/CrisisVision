from picamera2 import Picamera2
import cv2
import time

time.sleep(1)
picam2 = Picamera2()
config = picam2.create_preview_configuration({'format': 'RGB888'})
picam2.configure(config)
picam2.start()
test = picam2.capture_array()
cv2.imwrite("test.jpg", test)
