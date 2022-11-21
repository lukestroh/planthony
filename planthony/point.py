"""
point.py
"""

import rospy
import sys

from geometry_msgs.msg import Vector3

def callback(msg):
    point = Point(msg.data)

    rospy.loginfo(f"Got point {point}")

    publisher.publish(point)
    return


if __name__ == "__main__":
    # Initialize the node
    rospy.init_node('point_generator', argv=sys.argv)

    # Set up a subscriber
    subscriber = rospy.Subscriber('request', Vector3, callback)

    # Set up a publisher
    publisher = rospy.Publisher("target_point", Vector3, queue_size=10)
    
    # Hand control over to ROS
    rospy.spin()