#!/usr/bin/env python
#coding:ust-8

# 以搖桿程式為例

import rospy
from sensor_msgs.msg import Joy
from geometry_msgs.msg import Twist

def callback(data):
	cmd = Twist()
	cmd.linear.x = data.axes[5] * 2
	cmd.angular.z = data.axes[4] * 2
	global cmd_pub
	cmd_pub.publish(cmd)
	print('linear:%s,angular:%s' %(cmd.linear.x,cmd.angular.z))

def joy_node():
	rospy.init_node('joy11')
	global cmd_pub
	cmd_pub = rospy.Publisher('/turtle1/cmd_vel',Twist,queue_size=1)
	rospy.Subscriber('joy',Joy,callback)

if __name__ == '__main__':
	joy_node()
	rospy.spin()