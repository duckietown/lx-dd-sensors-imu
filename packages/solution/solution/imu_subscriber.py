"""Duckiedrone IMU Sensors LX: student solution.

Subscribes to /DUCKIEDRONE_NAME/mavros/imu/data (sensor_msgs/Imu) and exposes the
latest reading through ``latest_reading``. A throttled logger prints the
values at ~1 Hz so students can verify the subscriber is working.

MAVROS2 already publishes IMU data for virtual and physical
Duckiedrones, so this node is all a student needs to write to access the
IMU.
"""

import math

import rclpy
from rclpy.executors import ExternalShutdownException
from rclpy.node import Node
from rclpy.qos import qos_profile_sensor_data
from sensor_msgs.msg import Imu

from solution.imu_math import ImuReading, quaternion_to_euler


class ImuSubscriber(Node):
    """Store and periodically log the most recent IMU message."""

    def __init__(self) -> None:
        """Create the IMU subscriber and its timer-based logger."""
        super().__init__("imu_subscriber")

        self.declare_parameter("robot_namespace", "")
        self.declare_parameter("log_period_sec", 1.0)

        robot_parameter = self.get_parameter("robot_namespace")
        robot = robot_parameter.get_parameter_value().string_value
        log_period_parameter = self.get_parameter("log_period_sec")
        log_period = log_period_parameter.get_parameter_value().double_value

        prefix = f"/{robot}" if robot else ""
        topic = f"{prefix}/mavros/imu/data"
        self.get_logger().info(f"Subscribing to {topic}...")

        self.latest_reading: ImuReading | None = None

        # ------------------------------------------------------------
        # TO IMPLEMENT: subscribe to IMU messages.
        # Activity 1 in Notebook 7 explains each argument.
        #
        # - Message type: Imu.
        # - Topic: the `topic` variable above.
        # - Callback: self.cb_imu, with no parentheses.
        # - QoS profile: qos_profile_sensor_data.
        #
        # Assign the returned subscription to self.sub_imu.
        # ------------------------------------------------------------

        self.create_timer(log_period, self.cb_log)

    def cb_imu(self, msg: Imu) -> None:
        """Store an IMU message as the latest compact reading."""
        # ------------------------------------------------------------
        # TO IMPLEMENT: unpack msg into self.latest_reading.
        # Activity 1 in Notebook 7 explains the fields.
        #
        # - Acceleration: msg.linear_acceleration.x, .y, and .z,
        #   in m/s^2.
        # - Gyroscope: msg.angular_velocity.x, .y, and .z in rad/s.
        # - RPY: quaternion_to_euler applied to msg.orientation.
        # - Timestamp: seconds plus nanoseconds times 1e-9.
        #
        # Store an ImuReading with stamp_sec, accel, gyro, and rpy,
        # replacing the `pass` below. Do not print here.
        # ------------------------------------------------------------
        pass

    def cb_log(self) -> None:
        """Log the most recently received IMU reading."""
        reading = self.latest_reading
        if reading is None:
            self.get_logger().info("Waiting for IMU data...")
            return

        ax, ay, az = reading.accel
        wx, wy, wz = reading.gyro
        roll, pitch, yaw = reading.rpy
        roll_deg = math.degrees(roll)
        pitch_deg = math.degrees(pitch)
        yaw_deg = math.degrees(yaw)
        log_message = (
            f"accel=[{ax:+.2f} {ay:+.2f} {az:+.2f}] m/s^2 | "
            f"gyro=[{wx:+.2f} {wy:+.2f} {wz:+.2f}] rad/s | "
            f"rpy=[{roll_deg:+6.1f} "
            f"{pitch_deg:+6.1f} "
            f"{yaw_deg:+6.1f}] deg"
        )
        self.get_logger().info(log_message)


def main(args: list[str] | None = None) -> None:
    """Run the IMU subscriber node until ROS 2 shuts down."""
    rclpy.init(args=args)
    node = ImuSubscriber()
    try:
        rclpy.spin(node)
    except (KeyboardInterrupt, ExternalShutdownException):
        pass
    finally:
        node.destroy_node()
        if rclpy.ok():
            rclpy.shutdown()


if __name__ == "__main__":
    main()
