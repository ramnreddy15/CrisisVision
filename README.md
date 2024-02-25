# CrisisVision

## Description

Search and rescue is crucial during situations such as natural disasters to save lives. However, these natural disasters can pose a risk to the the safety of the search and rescue teams members. CrisisVision is an autonomous search and rescue surveillance vehicle designed to map out its surroundings to help search and rescue teams assess the situation from a safe distance.


## Requirements

The vehicle requires many python libraries to be installed.  
To install them, run:  
`pip3 install -r requirements.txt --break-system-packages`

## Installation

To install the repository, run `git clone <HTTPS URL>`


## What it Does

When the autonomous vehicle is deployed to a natural disaster area, it will move around the area, ensuring that it avoids any obstacles in its way. While it's navigating around, it will provide a live feed of the area to another device. It will go through two modes, the first one is annotating the live feed, and the second one is taking pictures to stitch together as a panoramic image. These two modes will continuously run one after another. The autonomous navigation and camera feed are are run simultaneously via threading to improve speeds and performance. For the object detection, we decided to use a YOLOv8 model to annotate what the camera sees. We used the socket library for the server-client connection for the arducam. 

## Challenges

The first challenge was setting up all the hardware. Our Raspberry Pi often crashed when we were logged into it due to the network blocking it from accessing anything on the web. Luckily, we were able to resolve by using another network.

The second and biggest challenge was integrating the code and testing it on the Raspberry Pi. When we were working on the server-client connection to stream video, we were able to get it to work between Windows laptops. However, when we tested it on the Raspberry Pi, we ran into issues that had to be debugeed and resolved. We tried a lot of different methods to fix the issues, and while we were able to resolve it, it was a huge setback for us.

The third challenge was optimizing the code. The working draft of the code did not have a very high frame rate. For this to be used in a real natural disaster event, the feed must be able to have a higher frame rate. Therefore, we had to optimize the code to reduce the amount of computations.

## Accomplishments

We created a vehicle that could move and avoid obstacles autonomously. In addition, we got a live feed with the annotations from the YOLOv8 model to be sent and received by another device. 
The code was also optimized to the point where the arducam outputed a video that was at a respectable frame rate. 


## What We Learned

Do not delete and reinstall python
Compatability is very important between host-client connections.


## What's Next
Next steps are to continue to improve the speed of the program to make the live feed and autonomous navigation more fluid and snappy. This autonomous vehicle can also be improved upon by adding extensions that can move debris or objects around to clear a path for itself or to help people that are stuck.   
