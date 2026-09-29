# Duckiedrone IMU LX: theory answers

> Answers to the theory questions from notebooks 1 to 4.

## Notebook 1: IMU basics

1. What does an IMU measure, and what does it **not** measure?

2. How can gravity correct roll and pitch, and why does it not provide an absolute yaw reference?

3. If you integrate the accelerometer output twice over time, what do you get, and why is this
   estimate not usable by itself for position?

## Notebook 2: rotation representations

1. What are the three common ways of writing a rotation, and what is each one good and bad at?

2. What is gimbal lock, and which motion does it take away?

3. Why does the ROS 2 IMU message carry a quaternion rather than roll, pitch and yaw?

4. How is a quaternion converted into roll, pitch and yaw, and where does gimbal lock come back?

## Notebook 3: the Duckiedrone IMU data flow

1. Which pieces of software touch the IMU data between the sensor chip and a subscriber?

2. What does each one add to, or remove from, the signal?

3. Where in the chain is the data still raw, and where is it already filtered?

## Notebook 4: interfacing with the IMU from ROS 2

1. `/mavros/imu/data` publishes a `sensor_msgs/Imu`. Which of its fields are populated on your
   Duckiedrone? How does the message represent an unknown covariance, and how does it represent
   an unavailable orientation estimate? Do the same for `/mavros/imu/data_raw`.

2. Your callback stores the reading and a timer prints it. What would go wrong if you printed
   inside the callback instead?

3. Roll and pitch stayed put while yaw did not. What did yaw do over the minute you watched it,
   and what does the Duckiedrone have for roll and pitch that it does not have for yaw?
