#include "ros/ros.h"
#include <iostream>
#include "std_msgs/String.h"

using namespace std;

int main(int argc, char **argv) {

    string node_name = "yourPubNode";
    string topic_name = "yourTopic";

    ros::init(argc, argv, node_name);
    ros::NodeHandle nh;
    ros::Publisher pub = nh.advertise<std_msgs::String>(topic_name, 10);

    int count = 0;
    ros::Rate rate(1); 

    while (ros::ok()) {
        std_msgs::String msg;

        msg.data = "hello " + to_string(count);
        pub.publish(msg);
        cout << msg.data << endl;
        rate.sleep();
        count++;
    }
    return 0;
}