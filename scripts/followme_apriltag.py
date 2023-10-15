#!/usr/bin/env python
#apriltag_ros
import rospy
from geometry_msgs.msg import Twist
from apriltag_ros.msg import AprilTagDetectionArray


class FollowMe:
    def __init__(self):
        rospy.init_node('follow_me')
        self.cmd_pub = rospy.Publisher('/cmd_vel', Twist, queue_size=1)
        self.tag_sub = rospy.Subscriber('/tag_detections', AprilTagDetectionArray, self.tag_callback)
        self.tag_id_to_follow = 0  # ID del tag da seguire
        self.desired_distance = 1.0  # Distanza desiderata dall'oggetto
        self.linear_speed = 0.2  # Velocità lineare del robot

    def tag_callback(self, data):
        for detection in data.detections:
            if detection.id[0] == self.tag_id_to_follow:
                self.follow_tag(detection.pose.pose.position.x, detection.pose.pose.position.y)

    def follow_tag(self, x, y):
        distance = self.calculate_distance(x, y)
        if distance > self.desired_distance:
            self.move_forward()
        elif distance < self.desired_distance:
            self.move_backward()
        else:
            self.stop()

    def calculate_distance(self, x, y):
        return ((x ** 2) + (y ** 2)) ** 0.5

    def move_forward(self):
        move_cmd = Twist()
        move_cmd.linear.x = self.linear_speed
        self.cmd_pub.publish(move_cmd)

    def move_backward(self):
        move_cmd = Twist()
        move_cmd.linear.x = -self.linear_speed
        self.cmd_pub.publish(move_cmd)

    def stop(self):
        stop_cmd = Twist()
        stop_cmd.linear.x = 0.0
        self.cmd_pub.publish(stop_cmd)


if __name__ == '__main__':
    try:
        follow_me = FollowMe()
        rospy.spin()
    except rospy.ROSInterruptException:
        pass
