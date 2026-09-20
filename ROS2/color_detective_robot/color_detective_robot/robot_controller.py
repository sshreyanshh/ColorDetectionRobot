import rclpy
from rclpy.node import Node
from std_msgs.msg import String
from geometry_msgs.msg import TwistStamped


class RobotController(Node):

    def __init__(self):
        super().__init__('robot_controller')

        self.subscription = self.create_subscription(
            String,
            'detected_color',
            self.color_callback,
            10
        )

        self.publisher = self.create_publisher(
            TwistStamped,
            'cmd_vel',
            10
        )

        self.get_logger().info('Color Robot Controller started.')

    def color_callback(self, msg):

        color = msg.data

        command = TwistStamped()

        if color == 'RED':
            command.twist.linear.x = 0.0
            command.twist.angular.z = 1.0

        elif color == 'GREEN':
            command.twist.linear.x = 0.2
            command.twist.angular.z = 0.0

        elif color == 'BLUE':
            command.twist.linear.x = 0.0
            command.twist.angular.z = -1.0

        else:
            command.twist.linear.x = 0.0
            command.twist.angular.z = 0.0

        self.publisher.publish(command)

        self.get_logger().info(
            'Color: ' + color + ' -> Robot command sent'
        )


def main(args=None):

    rclpy.init(args=args)

    node = RobotController()

    rclpy.spin(node)

    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
