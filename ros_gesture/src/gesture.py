#! /usr/bin/env python

import cv2
import rospy
from std_msgs.msg import String
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError
import sys
##import numpy as np
##import mediapipe as mp
##import tensorflow as tf
##from tensorflow.keras.models import load_model


bridge= CvBridge()

def image_callback(ros_image):
    print ("got an image")
    global bridge
    try:
        frame=bridge.imgmsg_to_cv2(ros_image,"bgr8")
    except CvBridgeError as e:
        print(e)
    x, y, c = frame.shape
    if y>200 and x>200:
        cv2.circle(frame,(100,100),90,255)
    font=cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(frame,"Intel camera activated with opencv",(10,350),font,1,(255,255,255),2,cv2.LINE_AA)
    cv2.imshow("Video window",frame)
    cv2.waitKey(3)

def main(args):
    print("Main function")
    rospy.init_node("image_converter", anonymous=True)
    image_sub=rospy.Subscriber("/camera/color/image_raw",Image, image_callback)
    print("After sub")
    try:
        rospy.spin()
    except KeyboardInterrupt:
        print("Shutting down")
    cv2.destroyAllWindows()

if __name__=="__main__":
    main(sys.argv)
