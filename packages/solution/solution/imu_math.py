"""Pure-Python IMU math helpers.

This module has no ROS 2 dependency on purpose, so it can be imported
from a plain Python interpreter (e.g. from the notebook or the tests)
without needing ``rclpy``. The ROS 2 subscriber in
``imu_subscriber.py`` re-uses these helpers.
"""

import math
from dataclasses import dataclass


@dataclass
class ImuReading:
    stamp_sec: float
    accel: tuple  # (ax, ay, az) in m/s^2
    gyro: tuple   # (wx, wy, wz) in rad/s
    rpy: tuple    # (roll, pitch, yaw) in rad


# How close |sin(pitch)| may get to 1 before the roll and yaw formulas below stop
# being usable. Past this point both of their arguments have collapsed to zero.
_POLE_TOL = 1e-12


def quaternion_to_euler(x: float, y: float, z: float, w: float) -> tuple:
    """Convert a unit quaternion (x, y, z, w) to roll / pitch / yaw (rad).

    Uses the standard ZYX intrinsic convention (yaw about Z, then pitch
    about Y, then roll about X), which matches what MAVROS2 publishes in
    the ROS frame.
    """
    sinp = 2.0 * (w * y - z * x)
    # A quaternion that is not exactly unit length can push this a hair outside
    # [-1, 1], which would make asin raise.
    sinp = max(-1.0, min(1.0, sinp))
    pitch = math.asin(sinp)

    if abs(sinp) >= 1.0 - _POLE_TOL:
        # Gimbal lock: at pitch = +/-90 degrees the roll and yaw axes coincide, so
        # only their combination is defined and the two cannot be separated. Both
        # atan2 arguments below are zero here, which would return an arbitrary
        # split of that combination and so describe a different rotation. Put the
        # whole turn into yaw instead, which keeps the returned angles faithful.
        roll = 0.0
        yaw = -math.copysign(2.0, sinp) * math.atan2(x, w)
        return roll, pitch, yaw

    sinr_cosp = 2.0 * (w * x + y * z)
    cosr_cosp = 1.0 - 2.0 * (x * x + y * y)
    roll = math.atan2(sinr_cosp, cosr_cosp)

    siny_cosp = 2.0 * (w * z + x * y)
    cosy_cosp = 1.0 - 2.0 * (y * y + z * z)
    yaw = math.atan2(siny_cosp, cosy_cosp)

    return roll, pitch, yaw
