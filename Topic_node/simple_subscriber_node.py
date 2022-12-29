
import rclpy #ROS2 python library
from rclpy.node import Node    #import Node module from rclpy.node
from std_msgs.msg import String

class MySubscriber(Node):
    def __init__(self):
        super().__init__('my_subscriber')
        self.subscriber = self.create_subscription(
            String,
            'topic_SWAhn',
            self.subscribe_topic_message,
            10
            )
    def subscribe_topic_message(self, msg):
        self.get_logger().info('I heard: %s' %msg.data)



def main():
    rclpy.init()
    print('Start subscribing a topic...')
    my_subscriber = MySubscriber()
    rclpy.spin(my_subscriber)
    rclpy.shutdown()


if __name__ == '__main__':
    main()
