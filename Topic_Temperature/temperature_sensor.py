import rclpy
from rclpy.node import Node
from std_msgs import String,Int8
import random

class TemperatureSensor(Node):
    def __init__(self):
        super().__init__('temperature_sensor')
        self.publisher = self.create_publisher(
            Int8,
            'tmperature_Sungwoo',
            10
        )
        self.timer = self.create_timer(1,self.publish_temperature)
    def publish_temperature(self):
        temperature = random.randint(20,30)
        msg = Int8()
        msg.data = temperature
        self.publisher.publish(msg)
        self.get_logger().info('Temperature is %d' %msg.data)

def main():
    rclpy.init
    node = TemperatureSensor()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()
