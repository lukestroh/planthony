"""
simple service
"""

import rospy

from __future__ import print_function

from . import point



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




