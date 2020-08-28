#!/usr/bin/env python3

from __future__ import print_function

import sys
import rospy
from cross_check.srv import *
from cv_bridge import CvBridge


import torch
import torchvision
import time
from lyt.LYTNet import LYTNet
from lyt.LYTNetV2 import LYTNetV2
import cv2
import numpy as np
from PIL import Image

import warnings

warnings.filterwarnings("ignore")

bridge = CvBridge()
net = LYTNetV2()
MODEL_PATH = '/home/germ/ros_catkin_ws/src/cross_check/src/lyt/TrainingResult/TrainingResult-V2-200/_final_weights'
checkpoint = torch.load(MODEL_PATH)
net.load_state_dict(checkpoint)
net.eval()
trans = torchvision.transforms.ToTensor()
 

def usage():
    return "%s [x]"%sys.argv[0]

def lyt_node():
    rospy.init_node('lyt_node')
    s = rospy.Service('lyt_main', AskInfo, request_check)
    print("ready")
    rospy.spin()

def request_check(req):
    print(req.Ask)
    coord = get_response(req.Ask)
    resp2 = AskInfoResponse()
    resp2.X1 = coord[0]
    resp2.Y1 = coord[1]
    resp2.X2 = coord[2]
    resp2.Y2 = coord[3]
    return resp2

def get_response(x):
    rospy.wait_for_service('camera_lyt')
    try:
        recieve_image = rospy.ServiceProxy('camera_lyt', AskImage)
        resp1 = recieve_image(x)
        orig = bridge.imgmsg_to_cv2(resp1.Image, "bgr8")
        orig = cv2.resize(orig, dsize=(768, 576), interpolation = cv2.INTER_AREA)
        return guess(orig)
    except rospy.ServiceException as e:
        print("Service call failed: %s"%e)

def guess(orig):
    image = cv2.cvtColor(orig, cv2.COLOR_BGR2RGB)
    img = Image.fromarray(image)

    img = trans(img).unsqueeze(0)
    img = img.type(torch.FloatTensor)
    img = img * 255
    
    with torch.no_grad():
        pred_classes, pred_direc = net(img)
        _, predicted = torch.max(pred_classes, 1)
        direc = np.array(pred_direc[0])

        return(direc)


if __name__ == "__main__":
    lyt_node()
