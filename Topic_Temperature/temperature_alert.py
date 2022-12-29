import rclpy
from rclpy.node import Node
from std_msgs import String,Int8

class TemperatureAlert(Node):
    def __init__(self):
        super().__init__('temperature_alert')
        self.subscription = self.create_subscription(
            Int8,
            'temperature_Sungwoo',
            self.temp_alert,
            10
        )

    def temp_alert(self,msg):
        temp = msg.data
        alert = String()
        if temp > 25:
            alert.data = 'Temperature is %d .. too high!' %temp
        else:
            alert.data = 'Temperature is %d .. normal' %temp
        self.get_logger().info('%s' %alert.data)

def main():
    rclpy.init()
    node = TemperatureAlert()
    rclpy.spin(node)
    rclpy.shutdown()
