# Autonomous_Portable_Engine

## Description

Search and rescue is crucial during situations such as natural disasters to save lives. However, these natural disasters can pose a risk to the the safety of the search and rescue teams members. Autonomous_Portable_Engine is an autonomous search and rescue surveillance vehicle designed to map out its surroundings to help search and rescue teams assess the situation from a safe distance.


## What it does

When the autonomous vehicle is deployed to a natural disaster area, it will move around the area, ensuring that it avoids any obstacles in its way. While it's navigating around, it will provide a live feed of the area and either annotate the feed or take pictures that will be stitched together to a panoramic image. These two modes will be controlled from a remote device. There are 4 tasks that the main program does: collect data from the ultrasonic sensor and determine how the vehicle should navigate, use the arducam to take pictures of the area to stitch together, stream a live feed off the camera to another device, and annotate the video for object detection. The autonomous navigation and camera feed are are run simultaneously via threading to improve speeds and performance. For the object detection, we decided to use a YOLOv8 model to annotate what the camera sees. We used the socket library for the server-client connection for the arducam. 

## What's next
Next steps are to continue to improve the speed of the program to make the live feed and autonomous navigation more fluid and snappy. This autonomous vehicle can also be improved upon by adding extensions that can move debris or objects around to clear a path for itself or to help people that are stuck.   

## Requirements

The vehicle requires many python libraries to be installed.  
To install them, run:  
`pip3 install -r requirements.txt --break-system-packages`

## Installation

To install the repository, run `git clone <HTTPS URL>`
