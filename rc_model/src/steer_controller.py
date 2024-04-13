#!/usr/bin/env python
import rospy
from std_msgs.msg import Float64

class SteerController:
    def __init__(self):
        self.left_pub = rospy.Publisher("/left_wheel_mount_turn_controller/command", data_class=Float64, queue_size=10)
        self.right_pub = rospy.Publisher("/right_wheel_mount_turn_controller/command", data_class=Float64, queue_size=10)

        rospy.Subscriber("/steer_controller/command", data_class=Float64, callback=self.handle_command)


    def handle_command(self, data):
        self.left_pub.publish(data)
        self.right_pub.publish(data)

if __name__ == "__main__":
    rospy.init_node("steer_controller")
    steer_controller = SteerController()
    rospy.spin()
