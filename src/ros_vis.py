"""
simple service
"""

import rospy

from __future__ import print_function

class VisNode:
    def __init__(self):

        return

    def start(self, node_name="vis_node", service_name="vis"):

        rospy.init_node(node_name)

        service = rospy.Service(service_name, VisNode, self._node_request_handler)

        rospy.loginfo(f"vis_node running: {service.uri})")

        rospy.spin()


    def _node_request_handler(self):
        return

class ArmNode:
    def __init__(self):
        return

    def get_pos(self):
        rospy.wait_for_service("vis")


def main():
    vis = VisNode()
    


    vis.start()
    return

if __name__ == "__main__":
    main()