from wsgiref.util import request_uri
import rclpy
from rclpy.node import Node
from my_interfaces.srv import AddThreeInts

class MyServiceServer(Node):
    def __init__(self):
        super().__init__('server_node')
        self.srv = self.create_service(
            AddThreeInts,
            'add_three_ints_Sungwoo',
            self.add_three_ints_callback
        )
    def add_three_ints_callback(self,request,response):
        response.sum = request.a + request.b + request.c
        self.get_logger().info('Incoming request.. a: %d, b: %d, c: %c' %(request.a, request.b, request.c))
        return response

def main():
    rclpy.init()
    node = MyServiceServer()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()