import rclpy
from rclpy.node import Node
from std_msgs.msg import Int16

class SimplePub(Node):
    def __init__(self):
        super().__init__("simple_publisher")
        self.get_logger().warning("Inicio de Nodo Publicador")

        self.number_pub_ = self.create_publisher(Int16, "/number", 10)

        self.create_timer(1.5, self.publish_callback)

    def publish_callback(self):
        msg = Int16()
        msg.data = 100

        self.number_pub_.publish(msg)
        self.get_logger().info("dato: " + str(msg.data))
        msg.data += 1


def main(args=None):
    rclpy.init(args=args)
    node = SimplePub()

    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == "__main__":
    main()