#!/usr/bin/env python

import rospy
from fake_ar_publisher.msg import ARMarker
from myworkcell_core.srv import LocalizePart
from tf2_ros import Buffer
from tf2_ros import TransformListener
from geometry_msgs.msg import PoseStamped
import tf2_geometry_msgs

def callback(msg):
	global last_msg
	last_msg = msg
	

def server_callback(req):
	p = last_msg
	if p ==None:	
		return None

	target_pose_from_cam = PoseStamped()
	
	target_pose_from_cam.header = p.header
	target_pose_from_cam.pose = p.pose.pose
	
	target_pose_from_req = 	tfBuffer.lookup_transform('base_link', 'camera_frame', rospy.Time(0), rospy.Duration(1.0))

	print(target_pose_from_req)

	
	
	
	

def server():
	
	s = rospy.Service('localize_part', LocalizePart, server_callback)
	rospy.loginfo('service ready')
	rospy.spin()

if __name__ == '__main__':

	

	last_msg = None
	rospy.init_node('vision_node')
	#rospy.loginfo("Hello World")
	rospy.Subscriber("ar_pose_marker", ARMarker, callback)
	tfBuffer = Buffer()
	listener = TransformListener(tfBuffer)
	server()
	rospy.loginfo("service node starting")
	rospy.spin()
