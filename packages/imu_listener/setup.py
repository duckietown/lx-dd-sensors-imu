from pathlib import Path

from setuptools import find_packages, setup

package_name = "imu_listener"
launch_files = [str(path) for path in Path("launch").glob("*.launch.py")]

setup(
    name=package_name,
    version="0.0.1",
    packages=find_packages(),
    data_files=[
        (
            "share/ament_index/resource_index/packages",
            ["resource/" + package_name],
        ),
        ("share/" + package_name, ["package.xml"]),
        (str(Path("share") / package_name / "launch"), launch_files),
    ],
    install_requires=["setuptools"],
    zip_safe=True,
    maintainer="Duckietown",
    maintainer_email="info@duckietown.com",
    description="Duckiedrone IMU listener node (reads /mavros/imu/data)",
    license="None",
    tests_require=["pytest"],
    entry_points={
        "console_scripts": [
            "imu_listener_node = imu_listener.imu_listener_node:main",
        ],
    },
)
