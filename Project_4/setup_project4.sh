source /opt/ros/kinetic/setup.bash

shutdown() {
  # Get our process group id
  PGID=$(ps -o pgid= $$ | grep -o [0-9]*)

  # Kill it in a new new process group
  setsid kill -- -$PGID
  exit 0
}

trap "shutdown" SIGINT SIGTERM

# export ROS_NODE_PORT=$(python get_free_port.py)
# export ROS_MASTER_URI=http://127.0.0.1:$ROS_NODE_PORT

lf="ros.log"
if [ -e $lf ]; then
  \rm $lf
fi
touch $lf

echo "Starting roscore with port = $ROS_NODE_PORT..."
roscore &
( ( (stdbuf -oL roscore -p $ROS_NODE_PORT) 1> >(stdbuf -oL sed 's/^/ROSCORE: /') 2>&1 ) | tee $lf ) &

sleep 1

cd catkin_ws
catkin_make
source devel/setup.bash
cd ..

rosparam set robot_description --textfile kuka_lwr_arm.urdf

echo "Launching robot_sim..."
( ( (stdbuf -oL rosrun robot_sim robot_sim_bringup) 1> >(stdbuf -oL sed 's/^/KUKA: /') 2>&1 ) >> $lf ) &

sleep 1

echo "Launching robot_state_publisher..."
( ( (stdbuf -oL rosrun robot_state_publisher robot_state_publisher) 1> >(stdbuf -oL sed 's/^/STATE_PUB: /') 2>&1 ) >> $lf ) &

sleep 1

echo "Launching marker_control..."
rosrun cartesian_control marker_control.py &

sleep 1

echo "Launching cartesian_control"
rosrun cartesian_control cartesian_control.py &

sleep 1

echo "Launching Rviz"
rosrun rviz rviz 