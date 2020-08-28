#!/usr/bin/env python3

from __future__ import print_function

import sys
import rospy
import time
from cross_check.srv import *

def request_check_and_call(x):
    print(x)
    rospy.wait_for_service("lyt_main")
    try:
        recieve_info = rospy.ServiceProxy('lyt_main', AskInfo)
        resp1 = recieve_info(x)
        return resp1
    except rospy.ServiceException as e:
        print("Service call failed: %s"%e)

if __name__ == "__main__":
    x = int( sys.argv[1] )
    print(request_check_and_call(x))
