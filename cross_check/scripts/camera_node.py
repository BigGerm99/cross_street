#!/usr/bin/env python
from __future__ import print_function
import rospy
import sys
import cv2
from cv_bridge import CvBridge
from cross_check.srv import AskImage, AskImageResponse 

bridge = CvBridge()

def request_check(req):
    print("received call + %s" %(req.Ask))
    img = cv2.imread( '/home/germ/python_test/CrossingRoad1.jpg' )
    imgMsg = bridge.cv2_to_imgmsg(img, "bgr8")
    return AskImageResponse(imgMsg)

def camera_node():
    rospy.init_node('camera_node')
    s = rospy.Service('camera_lyt', AskImage, request_check)
    print("ready to send")
    rospy.spin()

if __name__ == "__main__":
    camera_node()
