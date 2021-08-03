#!/usr/bin/env python
#coding:utf-8

import rospy
from std_msgs.msg import String 

if __name__=='__main__':
    node_name = 'yourPubNode'
    topic_name = 'yourTopic'

    rospy.init_node(node_name,anonymous=True)
    pub = rospy.Publisher(topic_name,String,queue_size=10)
    rate = rospy.Rate(10)
    count = 0

    while not rospy.is_shutdown():
        pub.publish('hello %d' %count)
        print('hello %d' %count)
        rate.sleep()
        count += 1