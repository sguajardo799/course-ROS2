import rclpy
from rclpy.node import Node
from std_msgs.msg import Int16

class SimpleSub(Node):
    def __init__(self):
        super().__init__("simple_subscriber")
        self.get_logger().warning("Inicio de Nodo Suscriptor")

        self.number_sub_ = self.create_subscription(
            Int16, 
            "/number", 
            self.subscriber_callback, 
            10)


    def subscriber_callback(self, msg:Int16):
        self.get_logger().info(str(msg))


def main(args=None):
    rclpy.init(args=args)
    node = SimpleSub()

    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == "__main__":
    main()