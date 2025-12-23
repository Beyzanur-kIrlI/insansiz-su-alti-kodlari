#SONAR DÜĞÜMÜ – DETAYLI (ROS2)
#!/usr/bin/env python3
"""
SONAR DÜĞÜMÜ
- ROS2 üzerinden sonar mesafesini okur
- Engelden kaçınma sistemine veri sağlar
"""

import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Range


class SonarDugumu(Node):
    """
    Sonar sensöründen gelen mesafeyi dinleyen ROS2 düğümü
    """

    def __init__(self):
        super().__init__('sonar_dugumu')

        # Sonar verisini dinlediğimiz topic
        self.sonar_aboneligi = self.create_subscription(
            Range,              # Mesaj tipi
            '/sonar/mesafe',    # Topic adı
            self.sonar_callback,
            10
        )

        self.get_logger().info("Sonar düğümü başlatıldı.")

    def sonar_callback(self, mesaj):
        """
        Sonar sensöründen veri geldiğinde otomatik çağrılır
        """
        mesafe = mesaj.range

        # Negatif veya hatalı ölçüm kontrolü
        if mesafe <= 0:
            self.get_logger().warn("Geçersiz sonar verisi alındı!")
            return

        self.get_logger().info(
            f"Algılanan sonar mesafesi: {mesafe:.2f} metre"
        )


def main(args=None):
    rclpy.init(args=args)
    dugum = SonarDugumu()
    rclpy.spin(dugum)
    dugum.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
