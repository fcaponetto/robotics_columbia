#!/usr/bin/env python  
import rospy

import numpy

import tf
import tf2_ros
import geometry_msgs.msg

def message_from_trasform(T):
    msg = geometry_msgs.msg.Transform()

    rotation = tf.transformations.quaternion_from_matrix(T)
    translation = tf.transformations.translation_from_matrix(T)

    msg.translation.x = translation[0]
    msg.translation.y = translation[1]
    msg.translation.z = translation[2]
    msg.rotation.x = rotation[0]
    msg.rotation.y = rotation[1]
    msg.rotation.z = rotation[2]
    msg.rotation.w = rotation[3]
    return msg
    

def publish_transforms():
        # The transform from the 'base' coordinate frame to the 'object' coordinate frame consists of a 
        # rotation expressed as (roll, pitch, yaw) of (0.79, 0.0, 0.79) followed by a translation of 
        # 1.0m along the resulting y-axis and 1.0m along the resulting z-axis. 
    T1 = numpy.dot(tf.transformations.translation_matrix((0.0, 1.0, 1.0)),
                   tf.transformations.quaternion_matrix(
                        tf.transformations.quaternion_from_euler(0.79, 0.0, 0.79)))
    object_transform = geometry_msgs.msg.TransformStamped()
    object_transform.header.stamp = rospy.Time.now()
    object_transform.header.frame_id = "base_frame"
    object_transform.child_frame_id = "object_frame"
    object_transform.transform = message_from_trasform(T1)
    br.sendTransform(object_transform)

        # The transform from the 'base' coordinate frame to the 'robot' coordinate frame consists of a 
        # rotation around the z-axis by 1.5 radians followed by a translation along the resulting y-axis of -1.0m. 
    T2 = numpy.dot(tf.transformations.translation_matrix((0.0, -1.0, 0.0)),
                   tf.transformations.quaternion_matrix(
                        tf.transformations.quaternion_about_axis(1.5, (0,0,1))))
    robot_transform = geometry_msgs.msg.TransformStamped()
    robot_transform.header.stamp = rospy.Time.now()
    robot_transform.header.frame_id = "base_frame"
    robot_transform.child_frame_id = "robot_frame"
    robot_transform.transform = message_from_trasform(T2)
    br.sendTransform(robot_transform)
 
        # The transform from the 'robot' coordinate frame to the 'camera' coordinate frame must be defined as follows:
        # The translation component of this transform is (0.0, 0.1, 0.1)
        # The rotation component of this transform must be set such that the camera is pointing directly at the object. 
        # In other words, the x-axis of the 'camera'  coordinate frame must be pointing directly at the origin of the 'object' coordinate frame. 
    T3 = numpy.dot(tf.transformations.translation_matrix((0.0, 0.1, 0.1)),
                   tf.transformations.quaternion_matrix(
                        tf.transformations.quaternion_from_euler(0.79, 0.0, 0.79)))
    camera_transform = geometry_msgs.msg.TransformStamped()
    camera_transform.header.stamp = rospy.Time.now()
    camera_transform.header.frame_id = "robot_frame"
    camera_transform.child_frame_id = "camera_frame"
    camera_transform.transform = message_from_trasform(T3)
    br.sendTransform(camera_transform)

if __name__ == '__main__':
    rospy.init_node('project2_solution')

    br = tf2_ros.TransformBroadcaster()
    rospy.sleep(0.5)

    while not rospy.is_shutdown():
        publish_transforms()
        rospy.sleep(0.05)
