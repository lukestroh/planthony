"""
main.py

"""

import planthony.ros_arm as arm
import planthony.ros_vis as vis

def main():
    
    vis_node = vis.VisNode()
    vis_node.start()
    return

if __name__ == "__main__":
    main()