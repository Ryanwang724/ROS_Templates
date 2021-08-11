#include "ros/ros.h"
#include <iostream>
#include "std_msgs/String.h"

using namespace std;

void callback(const std_msgs::String::ConstPtr &msg) {
    cout << msg->data << endl;
}

int main(int argc, char **argv) {

    string node_name = "yourSubNode";
    string topic_name = "yourTopic";

    ros::init(argc, argv, node_name);
    ros::NodeHandle nh;
    ros::Subscriber sub = nh.subscribe(topic_name, 10, callback);
    ros::spin();
    return 0;
}