import socket

import rclpy
from rclpy.node import Node
from std_msgs.msg import String


class ColorBridge(Node):

    def __init__(self):
        super().__init__('color_bridge')

        self.publisher = self.create_publisher(
            String,
            'detected_color',
            10
        )

        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.server.bind(('0.0.0.0', 5000))
        self.server.listen(1)

        self.get_logger().info('Color bridge listening on port 5000')

    def run_server(self):
        while rclpy.ok():
            self.get_logger().info('Waiting for Windows connection...')

            connection, address = self.server.accept()

            self.get_logger().info(
                'Connected to: ' + str(address)
            )

            while rclpy.ok():
                data = connection.recv(1024)

                if not data:
                    break

                color = data.decode().strip()

                msg = String()
                msg.data = color

                self.publisher.publish(msg)

                self.get_logger().info(
                    'Received color: ' + color
                )

            connection.close()

            # Safety: stop the robot if the Windows detector disconnects
            msg = String()
            msg.data = 'NO COLOR'

            self.publisher.publish(msg)

            self.get_logger().info(
                'Windows disconnected -> Robot stop command sent'
            )

        self.server.close()


def main(args=None):
    rclpy.init(args=args)

    node = ColorBridge()

    try:
        node.run_server()
    except KeyboardInterrupt:
        pass
    finally:
        node.server.close()
        node.destroy_node()
        rclpy.shutdown()


if __name__ == '__main__':
    main()
