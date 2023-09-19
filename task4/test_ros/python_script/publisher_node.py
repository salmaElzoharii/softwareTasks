#!/usr/bin/env python


import rospy
from std_msgs.msg import Int32
from  random import randint

def talker():
    pub = rospy.Publisher('talker1', Int32, queue_size=10)
    rospy.init_node('talker1', anonymous=True)
    rate = rospy.Rate(10) # 10hz
    while not rospy.is_shutdown():
        num1=randint(1,50)
        rospy.loginfo(num1)
        pub.publish(num1)
        rate.sleep()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass