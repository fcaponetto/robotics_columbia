#!/usr/bin/env python  
import rospy

from std_msgs.msg import Int16
from project1_solution.msg import TwoInts

def talker(a, b):
    pub = rospy.Publisher('sum', Int16, queue_size=10)
    sum_int = a + b
    rospy.loginfo(sum_int)
    pub.publish(sum_int)

def callback(data):
    rospy.loginfo(rospy.get_caller_id() + 'I heard %d %d', data.a, data.b)
    talker(data.a, data.b)

def listener():
    rospy.Subscriber('two_ints', TwoInts, callback)
    rospy.spin()

if __name__ == '__main__':
    rospy.init_node('listener_and_talker', anonymous=True)
    listener()