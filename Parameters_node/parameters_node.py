import rclpy
from rclpy.node import Node
from rclpy.exceptions import ParameterAlreadyDeclaredException
from rcl_interfaces.msg import ParameterType

class MinimalParam(Node):
    def __init__(self):
        super().__init__('minimal_param_node')
        timer_period = 2
        self.timer = self.create_timer(timer_period, self.timer_callback)

        self.declare_parameter('my_parameter','world')

    def timer_callback(self):
        my_param = self.get_parameter('my_parameter').get_parameter_value().string_value

        self.get_logger().info('Hello %s! ' %my_param)

def main():
    rclpy.init()
    node = MinimalParam()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()
