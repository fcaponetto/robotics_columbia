[img01]: ../imgs/proj_4.png

# Cartesian controller for Kuka LWR
This controller will allow you to interactively move the end-effector by dragging around an interactive marker. It is done by implementing **Differential Kinematics** and therefore the numerical computation of the **Jacobian**

![alt text][img01]

## Algorithm overview

The problem we are aiming to solve with a Cartesian controller is the following:

*If we have a robot that allows us to directly set joint velocities, what velocities do we set such that the robot achieves a desired end-effector position?*

* Compute the desired change in end-effector pose from b_T_ee_current to b_T_ee_desired. The desired pose change of the end-effector expressed in its own coordinate frame, not in the base frame.
* Convert the desired change into a desired end-effector velocity. This is essentially a **velocity controller** in end-effector space. The simplest form could be a proportional controller, where the velocity is equal to the desired change scaled by a constant. **The more difference in posision, the more velocity**.
* Numerically compute the robot Jacobian. For each joint compute the matrix that relates the velocity of that joint to the velocity of the end-effector in its own coordinate frame. Assemble the last column of all these matrices to construct the Jacobian
* Compute the pseudo-inverse of the Jacobian
* Use the pseudo-inverse of the Jacobian to map from end-effector velocity to joint velocities. The result will be the resulting joint velocities, which will then be sent to the robot.

## How do run this project in my own Ubuntu machine?
Install the needed ROS package(s). Run the following lines on your terminal:
sudo apt-get update
sudo apt-get install ros-kinetic-urdfdom-py

Replace **kinetic** with the ROS version that you are running on your local machine.

IGNORE all the files other than catkin_ws and kuka_lwr_arm.urdf. Copy the folder catkin_ws to your home directory (you can rename it project3 if you want). Also put the file kuka_lwr_arm.urdf in the home directory.
You can either use this structure directly (as downloaded) and build the workspace using the **catkin_make**:
```
source /opt/ros/indigo/setup.bash
cd catkin
catkin_make
source devel/setup.sh 
```
If catkin_make gives out an error, you will need to modify the file located in catkin_ws/src/robot_sim/CMakeLists.txt
```
# replace line 34
link_directories(/opt/ros/indigo/lib/)
# with
link_directories(/opt/ros/kinetic/lib/)
```

To run the project, first open up a terminal and type:
```
roscore
```
 In the second terminal run:
```
rosparam set robot_description --textfile kuka_lwr_arm.urdf
rosrun robot_sim robot_sim_bringup
```

On another 3 separate terminals you need to run the scripts for the robot mover and the your solution in forward kineamtics :
```
rosrun robot_state_publisher robot_state_publisher
rosrun cartesian_control marker_control.py
rosrun cartesian_control cartesian_control.py
```

Now we can open up Rviz using:
```
rosrun rviz rviz
```
Inside Rviz, first change the Fixed Frame to **"world_link"**.
Then click **Add** and select **RobotModel** from the list of options. At this point you should see the robot arm standing straight up. 
To add the interactive marker needed to command the robot around, click **Add** and select **"InteractiveMarkers"** from the list. 
Then on the left navigation plane, expand the **InteractiveMarkers object**, and click on **Update Topic > /control_markers/update**.
Now you should see the robot in Rviz, along with an interactive marker to command different positions for the end effect. Once your code works, the robot will follow whatever command is issued by moving this marker around. 
