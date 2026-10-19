# Duckiedrone IMU LX: theory answers

> Worked answers to the theory questions of each notebook.

## Notebook 1: IMU basics

1. What does an IMU measure, and what does it not measure?

2. How does proper acceleration differ from linear acceleration?

3. Why does the `linear_acceleration` field of `sensor_msgs/Imu` not hold linear acceleration on
   the Duckiedrone?

## Notebook 2: IMU estimation and drift

1. How can the stationary proper-acceleration measurement correct roll and pitch, and why does
   it not provide an absolute yaw reference?

2. What does integrating the proper-acceleration measurement twice give, and why is that estimate
   not usable by itself for position?

3. Why can a longer calibration reduce drift without eliminating it?

## Notebook 3: rotation representations

1. What do the body frame and the world frame describe, and how do they define the attitude of
   the Duckiedrone?

2. How do roll, pitch and yaw combine into one rotation in the ZYX convention?

3. What is gimbal lock, and which motion does it take away?

## Notebook 4: quaternions and rotation representations

1. What are the three common ways of writing a rotation, and what is each one good and bad at?

2. Why does the ROS 2 IMU message carry a quaternion rather than roll, pitch and yaw?

3. How is a quaternion converted into roll, pitch and yaw, and where does gimbal lock come back?

## Notebook 5: Duckiedrone IMU architecture

1. Which pieces of software touch the IMU data between the sensor chip and a subscriber?

2. What does each one add to, or remove from, the signal?

3. Where in the chain is the data still raw, and where is it already filtered?

## Notebook 6: IMU rates and configuration

1. Which setting decides how often each IMU topic is published?

2. Why does changing a PX4 IMU parameter leave the topic rate unchanged?

3. How does a stored parameter differ from a stream-rate request?

## Notebook 7: interfacing with the IMU

1. Which fields of `/mavros/imu/data` are sensor measurements, and which one is an estimate?

2. Why does pitch stay between $-90^\circ$ and $+90^\circ$ while roll covers the full circle?

3. Why can yaw drift while roll and pitch stay correct?
