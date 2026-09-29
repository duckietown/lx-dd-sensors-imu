"""Duckiedrone IMU Sensors LX: student solution.

Subscribes to /<robot>/mavros/imu/data (sensor_msgs/Imu) and exposes the
latest reading through ``latest_reading``. A throttled logger prints the
values at ~1 Hz so students can verify the subscriber is working.

MAVROS2 already publishes IMU data for both the virtual and the physical Duckiedrone,
so this node is the only thing a student needs to write to access the
IMU.
"""

import math
from typing import Optional

import rclpy
from rclpy._rclpy_pybind11 import RCLError
from rclpy.executors import ExternalShutdownException
from rclpy.node import Node
from rclpy.qos import qos_profile_sensor_data
from sensor_msgs.msg import Imu

from solution.imu_math import ImuReading, quaternion_to_euler


class ImuSubscriber(Node):

    def __init__(self):
        super().__init__('imu_subscriber')

        self.declare_parameter('robot_namespace', '')
        self.declare_parameter('log_period_sec', 1.0)

        robot = self.get_parameter('robot_namespace').get_parameter_value().string_value
        log_period = self.get_parameter('log_period_sec').get_parameter_value().double_value

        prefix = f'/{robot}' if robot else ''
        topic = f'{prefix}/mavros/imu/data'
        self.get_logger().info(f'Subscribing to {topic}...')

        self.latest_reading: Optional[ImuReading] = None

        # ------------------------------------------------------------------
        # TO IMPLEMENT: ask ROS 2 for the messages. Notebook 4, Activity 1
        # explains why each argument is what it is.
        #
        #   self.sub_imu = self.create_subscription(<type>, <topic>, <cb>, <qos>)
        #
        #     <type>   Imu
        #     <topic>  the `topic` variable above
        #     <cb>     self.cb_imu, no parentheses
        #     <qos>    qos_profile_sensor_data
        #
        # Assign to self.sub_imu.
        # ------------------------------------------------------------------

        self.create_timer(log_period, self.cb_log)

    def cb_imu(self, msg: Imu) -> None:
        # ------------------------------------------------------------------
        # TO IMPLEMENT: unpack `msg` into self.latest_reading, which cb_log
        # reads when it prints. Notebook 4, Activity 1 explains the fields.
        #
        #   accel      msg.linear_acceleration.{x,y,z}          m/s^2
        #   gyro       msg.angular_velocity.{x,y,z}             rad/s
        #   rpy        quaternion_to_euler(msg.orientation.x, .y, .z, .w)
        #   stamp_sec  msg.header.stamp.sec + msg.header.stamp.nanosec * 1e-9
        #
        # Store them as ImuReading(stamp_sec=..., accel=..., gyro=..., rpy=...).
        # Do not print here.
        # ------------------------------------------------------------------
        pass

    def cb_log(self) -> None:
        r = self.latest_reading
        if r is None:
            self.get_logger().info('Waiting for IMU data...')
            return

        ax, ay, az = r.accel
        wx, wy, wz = r.gyro
        roll, pitch, yaw = r.rpy
        self.get_logger().info(
            f'accel=[{ax:+.2f} {ay:+.2f} {az:+.2f}] m/s^2 | '
            f'gyro=[{wx:+.2f} {wy:+.2f} {wz:+.2f}] rad/s | '
            f'rpy=[{math.degrees(roll):+6.1f} {math.degrees(pitch):+6.1f} {math.degrees(yaw):+6.1f}] deg'
        )


def main(args=None):
    rclpy.init(args=args)
    node = ImuSubscriber()
    try:
        rclpy.spin(node)
    except (KeyboardInterrupt, ExternalShutdownException):
        pass
    except RCLError:
        if rclpy.ok():
            raise
    finally:
        node.destroy_node()
        if rclpy.ok():
            rclpy.shutdown()


if __name__ == '__main__':
    main()
