#!/usr/bin/env python

import rospy
from myworkcell_core.srv import LocalizePart


def client ():
	rospy.wait_for_service('localize_part')
	try:
		call_service = rospy.ServiceProxy('localize_part', LocalizePart)
		result = call_service()
		print(result)
	except:
		print('failed')


if __name__ == "__main__":
	rospy.set_param('base_frame' , 'world')
	client()
	



