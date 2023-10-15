#!/usr/bin/env python

import rospy
from geometry_msgs.msg import Twist
from darknet_ros_msgs.msg import BoundingBoxes

class FollowMeYolo:
    def __init__(self):
        rospy.init_node('follow_me_yolo')
        self.cmd_pub = rospy.Publisher('/cmd_vel', Twist, queue_size=1)
        self.bbox_sub = rospy.Subscriber('/darknet_ros/bounding_boxes', BoundingBoxes, self.bbox_callback)
        self.following = False

    def bbox_callback(self, data):
        for bbox in data.bounding_boxes:
            if bbox.Class == 'person':
                self.follow_person(bbox.xmin, bbox.xmax)

    def follow_person(self, xmin, xmax):
        if self.following:
            mid_point = (xmin + xmax) / 2
            if mid_point < 320:
                self.turn_left()
            elif mid_point > 320:
                self.turn_right()
            else:
                self.move_forward()
        else:
            self.following = True

    def turn_left(self):
        move_cmd = Twist()
        move_cmd.angular.z = 0.5  # Velocità di rotazione a sinistra
        self.cmd_pub.publish(move_cmd)

    def turn_right(self):
        move_cmd = Twist()
        move_cmd.angular.z = -0.5  # Velocità di rotazione a destra
        self.cmd_pub.publish(move_cmd)

    def move_forward(self):
        move_cmd = Twist()
        move_cmd.linear.x = 0.2  # Velocità lineare costante
        self.cmd_pub.publish(move_cmd)

    def run(self):
        rate = rospy.Rate(10)  # Frequenza di aggiornamento
        while not rospy.is_shutdown():
            rate.sleep()

if __name__ == '__main__':
    try:
        follow_me_yolo = FollowMeYolo()
        follow_me_yolo.run()
    except rospy.ROSInterruptException:
        pass
