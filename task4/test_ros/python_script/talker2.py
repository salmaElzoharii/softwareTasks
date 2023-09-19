#!/usr/bin/env python


import rospy
from std_msgs.msg import Int32
from  random import randint

def talker2():
    pub = rospy.Publisher('talker2', Int32, queue_size=10)
    rospy.init_node('talker2', anonymous=True)
    rate = rospy.Rate(10) # 10hz
    while not rospy.is_shutdown():
        num2=randint(1,50)
        rospy.loginfo(num2)
        pub.publish(num2)
        rate.sleep()

if __name__ == '__main__':
    try:
        talker2()
    except rospy.ROSInterruptException:
        pass