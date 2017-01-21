#!/usr/bin/env python
import rospy
from config import *
from std_msgs.msg import String
from geometry_msgs.msg import Twist

def callback(data):
    rate=50
    r=rospy.Rate(rate)
    rospy.loginfo(rospy.get_caller_id() + "I heard %s", data.data)
    twist = Twist()
    ticks=int(0.1*rate)
    if data.data == "F":
      twist.linear.x = 0.002
      twist.angular.z = 0
      for t in range(ticks):
          pub.publish(twist) 
          r.sleep()
      rospy.loginfo("forward")
      pub.publish(Twist())
    elif data.data == "B":
      twist.linear.x = -0.002
      twist.angular.z = 0
      for t in range(ticks):
          pub.publish(twist)
          r.sleep()       
      rospy.loginfo("backward")
      pub.publish(Twist())
    elif data.data == "L":
      twist.linear.x = 0
      twist.angular.z = -0.005
      for t in range(ticks)
          pub.publish(twist) 
          r.sleep()
      rospy.loginfo("Turn Left")
      pub.publish(Twist())
    elif data.data == "R":
      twist.linear.x = 0
      twist.angular.z = 0.005
      for t in range(ticks)
          r.sleep()
          pub.publish(twist)
      rospy.loginfo("Turn Right")
      pub.publish(Twist())
      
def stop():
    # Always stop the robot when shutting down the node.
    rospy.loginfo("Stopping the robot...")
    pub.publish(Twist())
    rospy.sleep(1)
    
def listener():
    rospy.init_node('listener', anonymous=False)
    rospy.on_shutdown(self.stop)
    global pub
    pub = rospy.Publisher('/RosAria/cmd_vel', Twist)
    rospy.Subscriber("receiver", String, callback)
    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':
    listener()
