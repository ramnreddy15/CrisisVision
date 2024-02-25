import cv2
import matplotlib.pyplot as plt
import time

cap = cv2.VideoCapture(0) #webcam

images = []
#iterate through the images and then append to images

for i in range(5):
    print("taking image number", i+1)
    ret, frame = cap.read()
    
    images.append(frame)

    time.sleep(.5)

cap.release()
print(images)

stitcher = cv2.Stitcher_create()
status, result = stitcher.stitch(images) # images is list of images
if status == 0:
    result = cv2.cvtColor(result, cv2.COLOR_BGR2RGB)
    plt.figure(figsize = [30,10])
    plt.imshow(result)
    plt.show()