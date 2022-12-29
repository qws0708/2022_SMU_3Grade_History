from wsgiref.util import request_uri
import rclpy
from rclpy.node import Node
from my_interfaces.srv import AddThreeInts
import random

class MyServiceClient(Node):
    def __init__(self):
        super().__init__('client_node')
        self.client = self.create_client(
            AddThreeInts,
            'add_three_ints_Sungwoo'
        )
        while not self.client.wait_for_service(timeout_sec = 1.0):
            self.get_logger().info('Service not available, waiting again...')

    def send_request(self):
        self.service_request = AddThreeInts.Request()
        self.service_request.a = random.randint(1,10)
        self.service_request.b = random.randint(1,10)
        self.service_request.c = random.randint(1,10)
        self.future = self.client.call_async(self.service_request)
        return self.future


def main():
    rclpy.init()
    sum_client = MyServiceClient()
    future = sum_client.send_request()

    while rclpy.ok():
        rclpy.spin_once(sum_client)
        if future.done():
            try:
                response = sum_client.future.result()
            except Exception as e:
                sum_client.get_logger().info('Service call failed')
            else:
                sum_client.get_logger().info('Result of add_three_ints_Sungwoo for %d + %d +%d = %d' %(sum_client.service_request.a, sum_client.service_request.b, sum_client.service_request.c, response.sum))
            break
    sum_client.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()