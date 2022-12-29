
import rclpy #ROS2 python library
from rclpy.node import Node    #import Node module from rclpy.node
from std_msgs.msg import String

class MyPublisher(Node):
    def __init__(self):
        super().__init__('my_publisher')
        self.publisher = self.create_publisher(
            String,
            'topic_SWAhn',
            10
            )
        timer_period = 1  #Seconds

        self.timer = self.create_timer(
            timer_period,
            self.timer_callback
        )

        self.i = 0
    def timer_callback(self):
        msg = String() #string data
        msg.data = 'Hello ROS2: %d' %self.i
        self.publisher.publish(msg)
        self.get_logger().info('Publishing : "%s" ' %msg.data)
        self.i += 1


def main():
    rclpy.init()
    print('Hi from my_second_package. I am Seoung Woo Ahn')
    node = MyPublisher()
    rclpy.spin(node)
    rclpy.shutdown()


if __name__ == '__main__':
    main()
