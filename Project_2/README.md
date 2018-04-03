# Project 2
## Description
This project will introduce you to 'tf', the ROS framework for handling transforms. Please make sure you have read the entry on this package on the ROS wiki. In this project we consider a ROS ecosystem, which consists of a robot with a camera mounted on it as well as an object. To describe the poses of all these items, we define the following coordinate frames:

* A base coordinate frame called 'base'
* A robot coordinate frame  called 'robot'
* A camera coordinate frame called 'camera'
* An object coordinate frame 'object'

The following relationships are true:

1. The transform from the 'base' coordinate frame to the 'object' coordinate frame consists of a rotation expressed as (roll, pitch, yaw) of (0.79, 0.0, 0.79) followed by a translation of 1.0m along the resulting y-axis and 1.0m along the resulting z-axis. 
2. The transform from the 'base' coordinate frame to the 'robot' coordinate frame consists of a rotation around the z-axis by 1.5 radians followed by a translation along the resulting y-axis of -1.0m. 
3. The transform from the 'robot' coordinate frame to the 'camera' coordinate frame must be defined as follows:
4. The translation component of this transform is (0.0, 0.1, 0.1)

The rotation component of this transform must be set such that the camera is pointing directly at the object. In other words, the x-axis of the 'camera' coordinate frame must be pointing directly at the origin of the 'object' coordinate frame. 
In the provided solution.py write a ROS node that publishes the following transforms to TF:

* The transform from the 'base' coordinate frame to the 'object' coordinate frame 
* The transform from the 'base' coordinate frame to the 'robot' coordinate frame 
* The transform from the 'robot' coordinate frame to the 'camera' coordinate frame

## How do run this project in my own Ubuntu machine?
IGNORE all the files outside the catkin_ws folder. You do not need these in your local machine 
The downloaded files are structured as a catkin workspace. You can either use this structure directly (as downloaded) and build the workspace using the **catkin_make**.
``:
source /opt/ros/indigo/setup.bash
cd catkin
catkin_make
source devel/setup.bash
```
This way every time you open up a terminal, you will already have your workspace sourced, such that ROS will have knowledge of the packages there.
To run the project, open up a terminal and fire up:
```
roscore
```
On another **2 separate terminals** you need to run the scripts in each package:
```
rosrun marker_publisher marker_publisher 
rosrun project2_solution solution.py 
```
Now, to visualize the markers we need to launch rviz. In a new terminal type:
```
rosrun rviz rviz
```
First thing you need to do is change the Fixed Frame option on the left of the UI. Select "base_frame", and notice that the Global Status now reads "Ok". Now we need to add the information we want to be displayed. Click Add and on the popup screen select the tab "By topic". Here you will see the topic /visualization_marker>Marker. Select it and then you should be able to see the block, cylinder and arrow. You can also add the item "TF" if you want to see a visual representation of the frames.

## How to aim the camera?

Hint: There is a simple geometrical argument that can help you rotate the x-axis of the arrow to point at the cylinder. Calculate the vector pointing from the camera to the object, use the dot and cross products to deduce the angle and axis to rotate around.
