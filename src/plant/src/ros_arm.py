#!/usr/bin/env python3
"""
ros_arm.py
"""

import rospy

from geometry_msgs.msg import Vector3


class ArmNode:
    def __init__(self):
        return
        
    def start(self, node_name="arm_node", service_name="vis"):

        # rospy.wait_for_service("vis_node")
    
        rospy.init_node(node_name)
        rospy.Subscriber("vis_node", Vector3, self._node_request_handler)
        rospy.spin()
        return


    def _node_request_handler(self, point):

        rospy.loginfo(f"Got point ({point.x}, {point.y}, {point.z})")

        return

def main():
    arm = ArmNode()
    arm.start()
    rospy.spin()


if __name__ == "__main__":
    main()





