#include <rclcpp/rclcpp.hpp>
#include <std_msgs/msg/string.hpp>

using std::placeholders::_1;

// SimpleSubscriber listens for messages on the "chatter" topic.
class SimpleSubscriber : public rclcpp::Node
{
public:
    // Construct the node and set up the subscription.
    SimpleSubscriber(): Node("simple_subscriber")
    {
        // Subscribe to the "chatter" topic with queue depth 10.
        subscriber_ = create_subscription<std_msgs::msg::String>(
            "chatter", 10, std::bind(&SimpleSubscriber::topic_callback, this, _1));

        // Log that the node is ready.
        RCLCPP_INFO(get_logger(), "Simple Subscriber node has been started.");
    }

private:
    // ROS 2 subscription for std_msgs/String messages.
    rclcpp::Subscription<std_msgs::msg::String>::SharedPtr subscriber_;

    // Handle each incoming message from the subscribed topic.
    void topic_callback(const std_msgs::msg::String::SharedPtr msg) const
    {
        RCLCPP_INFO_STREAM(get_logger(), "I heard: " << msg->data);
    }
};

int main(int argc, char * argv[])
{
    // Initialize ROS 2, run the node, then shut down cleanly.
    rclcpp::init(argc, argv);
    auto node = std::make_shared<SimpleSubscriber>();
    rclcpp::spin(node);
    rclcpp::shutdown();
    return 0;
}
