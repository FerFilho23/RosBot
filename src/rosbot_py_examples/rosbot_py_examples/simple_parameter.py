import rclpy
from rclpy.node import Node
from rcl_interfaces.msg import SetParametersResult
from rclpy.parameter import Parameter

class SimpleParameter(Node):
    def __init__(self):
        super().__init__('simple_parameter')
        self.declare_parameter('simple_int_param', 28)
        self.declare_parameter('simple_string_param', "Fernando")

        self.add_on_set_parameters_callback(self.parameter_callback)

        self.get_logger().info(f"My parameter simple_int_param value: {self.get_parameter('simple_int_param').get_parameter_value().integer_value}")
        self.get_logger().info(f"My parameter simple_string_param value: {self.get_parameter('simple_string_param').get_parameter_value().string_value}")

    def parameter_callback(self, params):
        result = SetParametersResult()
        for param in params:
            if (param.name == 'simple_int_param' and param.type_ == Parameter.Type.INTEGER) or (param.name == 'simple_string_param' and param.type_ == Parameter.Type.STRING):
                self.get_logger().info(f"Parameter {param.name} changed to {param.value}")
                result.successful = True

        return result
    
def main():
    rclpy.init()
    node = SimpleParameter()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()