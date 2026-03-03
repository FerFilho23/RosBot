#include <rclcpp/rclcpp.hpp>
#include <std_msgs/msg/string.hpp>
#include <chrono>

using namespace std::chrono_literals;

// SimplePublisher publishes a "Hello, ROS2!" message with an incrementing count.
class SimplePublisher : public rclcpp::Node
{
public:
    // Construct the node and set up communication primitives.
    SimplePublisher(): Node("simple_publisher")
    {
        // Create a publisher on the "chatter" topic with queue depth 10.
        publisher_ = create_publisher<std_msgs::msg::String>("chatter", 10);
        // Trigger timer_callback once per second.
        timer_ = create_wall_timer(1s, std::bind(&SimplePublisher::timer_callback, this));

        // Log that the node is ready.
        RCLCPP_INFO(get_logger(), "Simple Publisher node has been started.");
    }

private:
    // Counter appended to each published message.
    unsigned int count_ = 0;
    // ROS 2 publisher for std_msgs/String messages.
    rclcpp::Publisher<std_msgs::msg::String>::SharedPtr publisher_;
    // Periodic timer used to publish at a fixed rate.
    rclcpp::TimerBase::SharedPtr timer_;

    // Compose and publish one message on each timer event.
    void timer_callback()
    {
        auto message = std_msgs::msg::String();
        message.data = "Hello, ROS2! Count: " + std::to_string(count_++);
        publisher_->publish(message);
    }
};

int main(int argc, char * argv[])
{
    // Initialize ROS 2, run the node, then shut down cleanly.
    rclcpp::init(argc, argv);
    auto node = std::make_shared<SimplePublisher>();
    rclcpp::spin(node);
    rclcpp::shutdown();
    return 0;
}
