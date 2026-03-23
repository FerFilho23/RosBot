#include <rclcpp/rclcpp.hpp>
#include <rcl_interfaces/msg/set_parameters_result.hpp>
#include <memory>

using std::placeholders::_1;

class SimpleParameter : public rclcpp::Node
{
public:
  SimpleParameter() : Node("simple_parameter")
  {
    // Declare a parameter with a default value
    this->declare_parameter<std::string>("simple_string_param", "Fernando");
    this->declare_parameter<int>("simple_int_param", 28);

    param_callback_handle_ = this->add_on_set_parameters_callback(
      std::bind(&SimpleParameter::parameters_callback, this, _1));

    // Get the parameter value
    std::string string_param_value;
    int int_param_value;
    this->get_parameter("simple_string_param", string_param_value);
    this->get_parameter("simple_int_param", int_param_value);

    RCLCPP_INFO(this->get_logger(), "My parameter simple_string_param value: %s", string_param_value.c_str());
    RCLCPP_INFO(this->get_logger(), "My parameter simple_int_param value: %d", int_param_value);

  }

private:
  OnSetParametersCallbackHandle::SharedPtr param_callback_handle_;

  rcl_interfaces::msg::SetParametersResult parameters_callback(const std::vector<rclcpp::Parameter> & parameters)
  {
    rcl_interfaces::msg::SetParametersResult result;
    result.successful = true;

    for (const auto & param : parameters) {
        if((param.get_name() == "simple_string_param" && param.get_type() == rclcpp::ParameterType::PARAMETER_STRING) ||
           (param.get_name() == "simple_int_param" && param.get_type() == rclcpp::ParameterType::PARAMETER_INTEGER)) {
            RCLCPP_INFO(this->get_logger(), "Parameter '%s' changed to '%s'", param.get_name().c_str(), param.value_to_string().c_str());
        }
        
    }

    return result;
  }

};

int main(int argc, char * argv[])
{
  rclcpp::init(argc, argv);
  auto node = std::make_shared<SimpleParameter>();
  rclcpp::spin(node);
  rclcpp::shutdown();
  return 0;
}
