import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class SimplePublisher(Node):
    def __init__(self):
        super().__init__('simple_publisher')
        
        self.publisher_ = self.create_publisher(String, 'chatter', 10)
        self.counter = 0
        self.frequency = 1.0  # Publish at 1 Hz
        self.timer = self.create_timer(1 / self.frequency, self.timer_callback)

        self.get_logger().info('Chatter publisher started, publishing at %f Hz' % self.frequency)

    def timer_callback(self):
        msg = String()
        msg.data = 'Hello, world! #%d' % self.counter
        self.publisher_.publish(msg)
        self.counter += 1

def main():
    rclpy.init()
    simple_publisher = SimplePublisher()
    rclpy.spin(simple_publisher)
    simple_publisher.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()