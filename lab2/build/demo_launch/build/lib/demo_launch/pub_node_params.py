import rclpy
from rclpy.node import Node
from std_msgs.msg import ColorRGBA, Int16

class SimplePubParam(Node):
    def __init__(self):
        super().__init__("simple_publisher")
        self.get_logger().warning("Inicio de Nodo Publicador")

        self.declare_parameter('number',0)
        self.color_pub_ = self.create_publisher(Int16, "/number", 10)

        self.number = self.get_parameter('number').get_parameter_value().integer_value

        self.create_timer(1.5, self.publish_callback)

    def publish_callback(self):
        msg = Int16()
        msg.data = self.number

        self.color_pub_.publish(msg)
        self.get_logger().info("dato: " + str(msg.data))
        self.number += 1


def main(args=None):
    rclpy.init(args=args)
    node = SimplePubParam()

    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == "__main__":
    main()