import rclpy
from rclpy.action import ActionClient
from rclpy.node import Node
from my_interfaces.action import Fibonacci

class FibonacciActionClient(Node):
    def __init__(self):
        super().__init__('fibonacci_action_client')
        self.action_client = ActionClient(
            self,
            Fibonacci,
            'fibonacci_asw'
        )

    def send_goal(self, order):
        goal_msg = Fibonacci.Goal()
        goal_msg.order = order
        self.action_client.wait_for_server()
        self.send_goal_future = self.action_client.send_goal_async(goal_msg, feedback_callback = self.feedback_callback)

        self.send_goal_future.add_done_callback(self.goal_response_callback)

    def feedback_callback(self, feedback_msg):
        feedback = feedback_msg.feedback
        self.get_logger().info('Receive feedback: {0}'.format(feedback.partial_sequence))
    def goal_response_callback(self, future):
        goal_handle = future.result()
        self.get_logger().info('Goal accepted.')
        self.get_result_future = goal_handle.get_result_async()
        self.get_result_future.add_done_callback(self.get_result_callback)
    def get_result_callback(self, future):
        result = future.result().result
        self.get_logger().info('Result_SeoungWoo: {0}'.format(result.sequence))

def main():
    rclpy.init()
    action_client = FibonacciActionClient()
    action_client.send_goal(5)
    rclpy.spin(action_client)

if __name__ == '__main__':
    main()