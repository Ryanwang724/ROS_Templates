#!/usr/bin/env python
#coding:utf-8

import rospy
from std_msgs.msg import String 

def callback(msg):
	print('I heard %s' % msg.data)

if __name__ == '__main__':
	node_name = 'yourSubNode'
	topic_name = 'yourTopic'
	
	rospy.init_node(node_name,anonymous=True)
	rospy.Subscriber(topic_name,String,callback)
	rospy.spin()