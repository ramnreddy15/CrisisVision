
![Banner](banner.png)

## Description

There are some situations such as natural disasters and war zones where it's critical for them to gather information about the surroundings. However, these environments can pose a risk to the the safety of those involved. crisisvision is an autonomous surveillance vehicle designed to map out its surroundings to help those types of people assess the situation from a safe distance.


## Requirements

The vehicle requires many python libraries to be installed.  
To install them, run:  
`pip3 install -r requirements.txt --break-system-packages`

## Installation

To install the repository, run `git clone <HTTPS URL>`


## What it Does

* Vehicle will move around in the area while avoiding any obstacles
* Simultaneously, it will provide a live feed of the area to another device
* Annotate live feed using a YOLOv8 model
* After a certain time, it will spin around to take pictures and stitch them together
* Once it spins a full circle, it will go back to moving around and show a live feed


## Challenges

1) Raspberry Pi often crashed when trying to log in. This was a result of the network blocking it from accessing the web. 

2) Code integration and testing on Raspberry Pi. We got the server-client connection to stream video between Windows laptops, but when we tested it on the Raspberry Pi, we ran into issues that had to be debugged and resolved. 

3) Code optimization. The first working draft of the code did not output a very high frame rate, so opmizations had to be made to increase the frame rate for this to be able to be used in a real natural disaster event.

## Accomplishments

* Created a vehicle that could move and avoid obstacles autonomously.
* Created a live feed with the annotations from the YOLOv8 model to be sent and received by another device. 
* Optimized the code to where the arducam outputed a video that was at a respectable frame rate. 


## What We Learned

1) Version compatability is very important between server and client devices when using python sockets. This issue led to the second thing we learned.
2) Deleting and reinstalling python can create a lot of issues. We attempted to do that because of the version compatability, but it just caused more problems for our Raspberry Pi. 

## What's Next
Next steps are to continue to improve the speed of the program to make the live feed and autonomous navigation more fluid and snappy. This autonomous vehicle can also be improved upon by adding extensions that can move debris or objects around to clear a path for itself or to help people that are stuck.   

## Dependencies

* **Control System:** numpy, threading, time, sockets, struct
* **Computer Vision and Image Processing:** cv2, ultralytics, supervision, picamera2
* **Drivers:** Many thanks to [John Deere](https://github.com/jameskabbes/HackIllinois2024/tree/main)
