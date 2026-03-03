import rclpy
from rclpy.node import Node
from std_msgs.msg import String


class SimplePublisher(Node):
    """ROS 2 node that publishes incrementing greeting messages on /chatter."""

    def __init__(self):
        # Initialize the node with the ROS graph name `simple_publisher`.
        super().__init__('simple_publisher')

        # Create a String publisher:
        # - message type: std_msgs/String
        # - topic name: chatter
        # - queue depth: 10
        self.publisher_ = self.create_publisher(String, 'chatter', 10)

        # Internal state used to number each message.
        self.counter = 0

        # Publish once per second (1 Hz) using a periodic timer callback.
        self.frequency = 1.0  # Publish at 1 Hz
        self.timer = self.create_timer(1 / self.frequency, self.timer_callback)

        # Log startup status for visibility in the console.
        self.get_logger().info('Chatter publisher started, publishing at %f Hz' % self.frequency)

    def timer_callback(self):
        # Build and publish the next message, then increment the counter.
        msg = String()
        msg.data = 'Hello, world! #%d' % self.counter
        self.publisher_.publish(msg)
        self.counter += 1


def main():
    # Standard ROS 2 lifecycle:
    # 1) initialize rclpy
    # 2) create and spin node (process callbacks)
    # 3) clean up node and shutdown rclpy on exit
    rclpy.init()
    simple_publisher = SimplePublisher()
    rclpy.spin(simple_publisher)
    simple_publisher.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
