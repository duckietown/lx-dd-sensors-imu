"""Pure-Python IMU math helpers.

This module has no ROS 2 dependency on purpose, so it can be imported
from a plain Python interpreter (e.g., from the notebook or the tests)
without needing ``rclpy``. The ROS 2 subscriber in
``imu_subscriber.py`` re-uses these helpers.
"""

import math
from dataclasses import dataclass


@dataclass
class ImuReading:
    """Decoded IMU sample in ROS-compatible units."""

    stamp_sec: float
    accel: tuple  # (ax, ay, az) in m/s^2
    gyro: tuple  # (wx, wy, wz) in rad/s
    rpy: tuple  # (roll, pitch, yaw) in rad


# How close |sin(pitch)| may get to 1 before the roll and yaw formulas
# below stop being usable. Past this point both arguments have collapsed
# to zero.
_POLE_TOL = 1e-12


def quaternion_to_euler(x: float, y: float, z: float, w: float) -> tuple:
    """Convert a unit quaternion to roll, pitch, and yaw in radians.

    The quaternion order is ``(x, y, z, w)``.
    It uses ZYX intrinsic rotations: yaw about Z, pitch about Y.
    It finishes with roll about X.
    """
    sinp = 2.0 * (w * y - z * x)
    # A non-unit quaternion can push this outside [-1, 1]. Clamping
    # prevents asin from raising.
    sinp = max(-1.0, min(1.0, sinp))
    pitch = math.asin(sinp)

    if abs(sinp) >= 1.0 - _POLE_TOL:
        # At pitch = +/-90 degrees, roll and yaw axes coincide.
        # Only their combined angle is defined.
        # Both atan2 arguments are zero, which would pick an arbitrary
        # split and describe a different rotation. Put the whole turn in
        # yaw to keep the returned angles faithful.
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
