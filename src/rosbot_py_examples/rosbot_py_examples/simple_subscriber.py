import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class SimpleSubscriber(Node):
    """ROS 2 node that subscribes to greeting messages on /chatter."""

    def __init__(self):
        # Initialize the node with the ROS graph name `simple_subscriber`.
        super().__init__('simple_subscriber')

        # Create a String subscription:
        # - message type: std_msgs/String
        # - topic name: chatter
        # - callback: listener_callback
        # - queue depth: 10
        self.subscriber_ = self.create_subscription(
            String,
            'chatter',
            self.listener_callback,
            10
        )
        # Keep a reference to avoid an unused variable warning.
        self.subscriber_  # prevent unused variable warning

    def listener_callback(self, msg):
        # Log each received message to confirm subscription activity.
        self.get_logger().info('I heard: "%s"' % msg.data)

def main():
    # Standard ROS 2 lifecycle:
    # 1) initialize rclpy
    # 2) create and spin node (process callbacks)
    # 3) clean up node and shutdown rclpy on exit
    rclpy.init()
    simple_subscriber = SimpleSubscriber()
    rclpy.spin(simple_subscriber)
    simple_subscriber.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
