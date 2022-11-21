"""
ros_arm.py
"""

import rospy
import sys

from planthony import point


class ArmNode:
    def __init__(self):
        rospy.init_node("arm_node", argv=sys.argv)

        rospy.wait_for_service("vis_node")
        
    def start(self, 


    def get_pos(self):
        return