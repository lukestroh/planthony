#!/usr/bin/env python3
"""
simple service
"""
"""
need catkin create package
need workspace
"""
import rospy
import random

from geometry_msgs.msg import Vector3


class VisNode:
    def __init__(self):

        return

    def start(self, node_name="vis_node", service_name="vis"):

        pub = rospy.Publisher(node_name, Vector3, queue_size=10)
        rospy.init_node(node_name)
        rospy.loginfo(f"vis_node running: {pub.name})")

        r = rospy.Rate(10)
        msg = Vector3()
        msg.x = random.randint(0,10)
        msg.y = random.randint(0,10)
        msg.z = random.randint(0,10)

        while not rospy.is_shutdown():
            msg.x = random.randint(0,10)
            msg.y = random.randint(0,10)
            msg.z = random.randint(0,10)
            rospy.loginfo(msg)
            pub.publish(msg)
            r.sleep()       
        return


    # def _node_request_handler(self, msg):
    #     return
    #     # return pointResponse(msg.request)


    def get_rand_int():
        return 

def main():
    vis = VisNode()
    vis.start()
    rospy.spin()


if __name__ == "__main__":
    main()





