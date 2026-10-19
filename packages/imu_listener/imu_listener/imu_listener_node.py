#!/usr/bin/env python3
"""Duckiedrone IMU listener that wraps the student solution.

The node simply constructs ``solution.imu_subscriber.ImuSubscriber`` and
spins it. Keeping the launchable node this thin lets students iterate on
their solution code without touching any launch plumbing.
"""

from solution.imu_subscriber import main as solution_main


def main(args: list[str] | None = None) -> None:
    """Run the IMU listener node."""
    solution_main(args=args)


if __name__ == "__main__":
    main()
