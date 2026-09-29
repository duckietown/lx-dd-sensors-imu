# Duckiedrone IMU Sensors - Learning Experience

`Software: ente`; `Hardware: DD24-B`

An IMU provides the acceleration and angular-rate measurements a flight controller uses to estimate orientation. Small measurement errors accumulate when those readings are integrated. This Learning Experience covers what an IMU measures, how to describe the orientation it reports, how its readings reach a ROS 2 topic, and how to write the node that reads them.

## Intended learning outcomes

After completing this learning experience, learners will be able to:

1. Explain what an accelerometer and a gyroscope each measure, and predict what happens to a position estimate built by integrating acceleration over time.

2. Compare Euler angles, rotation matrices and quaternions as ways of writing an orientation, and identify the orientations at which Euler angles break down.

3. Trace an IMU reading from the sensor chip to a ROS 2 topic, naming what changes it at each step and what sets its rate.

4. Write, deploy, and run a ROS 2 node on a Duckiedrone that subscribes to the IMU topic and reports acceleration, angular velocity, and roll, pitch and yaw.

## Notebooks

Go through these in order:

| # | Notebook | Description |
| --- | --- | --- |
| 1 | `1-imu-basics.ipynb` | What an IMU measures, what it cannot, and how fast a position estimate drifts away |
| 2 | `2-rotation-representations.ipynb` | Euler angles, rotation matrices, gimbal lock, quaternions |
| 3 | `3-duckiedrone-imu-architecture.ipynb` | The path from the sensor chip to `/mavros/imu/data`, and where its settings live |
| 4 | `4-interfacing-with-imu.ipynb` | Write, deploy, and run a ROS 2 node that reads the IMU |

## What you need

A Duckiedrone, physical or virtual, running the standard software stack. Nothing here arms the Duckiedrone or flies it, so no propellers and no RC transmitter are needed. Notebook 4 walks through getting to a terminal on the Duckiedrone and deploying your code to it.
