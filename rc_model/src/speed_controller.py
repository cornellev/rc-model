#!/usr/bin/env python
import rospy
from std_msgs.msg import Float64

class SpeedController:
    def __init__(self):
        self.left_pub = rospy.Publisher("/back_left_wheel_controller/command", data_class=Float64, queue_size=10)
        self.right_pub = rospy.Publisher("/back_right_wheel_controller/command", data_class=Float64, queue_size=10)

        rospy.Subscriber("/speed_controller/command", data_class=Float64, callback=self.handle_command)

    def handle_command(self, data):
        self.left_pub.publish(data)
        self.right_pub.publish(-data.data)

if __name__ == "__main__":
    rospy.init_node("speed_controller")
    steer_controller = SpeedController()
    rospy.spin()
