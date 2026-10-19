#!/usr/bin/env python3
"""Launch the Duckiedrone IMU listener node.

Usage
-----
ros2 launch imu_listener imu_listener_node.launch.py \
    robot_namespace:=DUCKIEDRONE_NAME

Parameters
----------
robot_namespace : str
    Duckiedrone hostname for the MAVROS2 topic namespace. Defaults to an
    empty string when MAVROS2 publishes at the root of the Duckiedrone.
log_period_sec : float
    Seconds between printed listener summaries. Defaults to 1.0.

"""

from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node


def generate_launch_description() -> LaunchDescription:
    """Create the launch description for the IMU listener."""
    robot_namespace_arg = DeclareLaunchArgument(
        "robot_namespace",
        default_value="",
        description=(
            "Namespace used by MAVROS2, such as the Duckiedrone hostname."
        ),
    )

    log_period_arg = DeclareLaunchArgument(
        "log_period_sec",
        default_value="1.0",
        description="Seconds between summary log lines.",
    )

    imu_listener_node = Node(
        package="imu_listener",
        executable="imu_listener_node",
        name="imu_listener_node",
        output="screen",
        emulate_tty=True,
        parameters=[
            {
                "robot_namespace": LaunchConfiguration("robot_namespace"),
                "log_period_sec": LaunchConfiguration("log_period_sec"),
            }
        ],
    )

    return LaunchDescription(
        [
            robot_namespace_arg,
            log_period_arg,
            imu_listener_node,
        ]
    )
