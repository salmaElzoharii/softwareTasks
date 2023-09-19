#!/usr/bin/env python


import rospy
from std_msgs.msg import Int32
sum=0
def callback1(data):
     global sum
     sum+=data.data
def callback2(data):
     global sum
     sum+=data.data
def listener():
   while not rospy.is_shutdown():
        rospy.init_node('listener', anonymous=True)
        rospy.Subscriber('talker1', Int32, callback1)
        rospy.Subscriber('talker2', Int32, callback2)
        rospy.spin()
        rospy.loginfo("Sum of numbers: %d", sum)


if __name__ == '__main__':
    listener()