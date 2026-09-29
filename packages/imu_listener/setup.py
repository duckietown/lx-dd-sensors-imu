from setuptools import setup, find_packages
import os
from glob import glob

package_name = 'imu_listener'

setup(
    name=package_name,
    version='0.0.1',
    packages=find_packages(),
    data_files=[
        ('share/ament_index/resource_index/packages', ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name, 'launch'), glob('launch/*.launch.py')),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Duckietown',
    maintainer_email='info@duckietown.com',
    description='Duckiedrone IMU listener node (reads /mavros/imu/data)',
    license='None',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'imu_listener_node = imu_listener.imu_listener_node:main',
        ],
    },
)
