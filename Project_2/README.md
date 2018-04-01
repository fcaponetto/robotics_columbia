## How do run this project in my own Ubuntu machine?
IGNORE all the files outside the catkin_ws folder. You do not need these in your local machine 
The downloaded files are structured as a catkin workspace. You can either use this structure directly (as downloaded) and build the workspace using the **catkin_make**".
```
source /opt/ros/indigo/setup.bash
cd catkin
catkin_make
source ~/robotics_ws/devel/setup.bash
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
