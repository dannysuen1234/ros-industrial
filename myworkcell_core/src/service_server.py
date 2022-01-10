#!/usr/bin/env python

import rospy
from fake_ar_publisher.msg import ARMarker
from myworkcell_core.srv import LocalizePart

last_message = None

def callback(msg):
	last_msg = msg
	rospy.loginfo(last_msg.pose.pose)

def server_callback(req):
	p = last_msg
	if not p:
		return None
	return p.pose.pose

def server():
	
	s = rospy.Service('localize_part', LocalizePart, server_callback)

if __name__ == '__main__':
	rospy.init_node('service_node')
	server()
	rospy.loginfo("service node starting")
	rospy.spin()

# backup below
#!/usr/bin/env python

import rospy
from fake_ar_publisher.msg import ARMarker


def callback(data):
	last_msg = data
	rospy.loginfo(data.pose.pose)

if __name__ == '__main__':
	
	rospy.init_node('vision_node')
	rospy.Subscriber("ar_pose_marker", ARMarker, callback)
	rospy.loginfo("Vision node starting")
	rospy.spin()
