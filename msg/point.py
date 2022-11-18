"""
point.py
"""

import rospy
import sys

from std_msgs.msg import Int64

def callback():
    
    return

if __name__ == "__main__":
    # Initialize the node
    rospy.init_node('point_generator', argv=sys.argv)

    # Set up a subscriber
    subscriber = rospy.Subscriber('request', Int64, callback)

    # Set up a publisher
    publisher = rospy.Publisher("target_point", Int64, queue_size=10)
    
    # Hand control over to ROS
    rospy.spin()