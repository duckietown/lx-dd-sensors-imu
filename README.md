<p align="center">
<a href="https://duckietown.com"><img src="./assets/images/dtlogo.png" alt="Duckietown Logo" width="30%"></a>
</p>

# Learning Experience (LX): Duckiedrone IMU Sensors

`Software: ente`; `Hardware: DD24-B`

The Duckiedrone uses inertial measurements to track rotation and estimate the attitude needed
for flight control. Making sense of those measurements starts with a stationary device: its
accelerometer reports support against gravity even though it is not moving, and small errors
in its readings can grow into large position errors when integrated.

This learning experience follows that connection from the accelerometer and gyroscope to the
values available in ROS 2. Recorded data and interactive examples develop the measurement and
rotation concepts before live activities trace the software path, change a message rate, and
use a subscriber to interpret a tilt-and-hold experiment.

## Intended learning outcomes

After completing this LX, learners will be able to:

1. Explain how the accelerometer and gyroscope produce their measurements, and interpret their readings for a stationary or tilted Duckiedrone.

2. Characterize a stationary acceleration recording and explain how residual errors accumulate in a dead-reckoned position estimate.

3. Compare Euler angles, rotation matrices, and unit quaternions, including frame conventions and Euler-angle singularities.

4. Trace the processing of IMU measurements into ROS 2, request a different MAVLink stream interval, and measure its effect on message arrival.

5. Complete or inspect the supplied subscriber, run it on a Duckiedrone, and relate its acceleration and attitude display to a known pose.

## Run this LX

Follow the Duckietown Manual's [LX General Instructions](https://docs.duckietown.com/ente/opmanual-dd24/50-learning-experiences/lx-general-procedure.html) to open this LX in a prepared environment. The notebooks provide the topic-specific activities; the prerequisites below describe the local setup.

## Notebooks

Start with [Notebook 1](./notebooks/1-imu-basics.ipynb) for the sensor measurements and a recorded
IMU message. [Notebook 2](./notebooks/2-imu-estimation-and-drift.ipynb) explores attitude estimation
and position drift. [Notebook 3](./notebooks/3-rotation-representations.ipynb) covers Euler angles,
rotation matrices, and gimbal lock; [Notebook 4](./notebooks/4-quaternions-and-rotation-representations.ipynb)
introduces quaternions. [Notebook 5](./notebooks/5-duckiedrone-imu-architecture.ipynb) follows the data
to ROS 2; [Notebook 6](./notebooks/6-imu-rates-and-configuration.ipynb) explores its rates and settings.
[Notebook 7](./notebooks/7-interfacing-with-imu.ipynb) builds and runs the subscriber.

| # | Notebook | Description |
| --- | --- | --- |
| 1 | [Notebook 1](./notebooks/1-imu-basics.ipynb) | Accelerometer, gyroscope, sensor frames, and a recorded IMU message |
| 2 | [Notebook 2](./notebooks/2-imu-estimation-and-drift.ipynb) | Attitude references, dead reckoning, and two drift experiments |
| 3 | [Notebook 3](./notebooks/3-rotation-representations.ipynb) | Euler angles, rotation matrices, and gimbal lock |
| 4 | [Notebook 4](./notebooks/4-quaternions-and-rotation-representations.ipynb) | Quaternions and converting back to Euler angles |
| 5 | [Notebook 5](./notebooks/5-duckiedrone-imu-architecture.ipynb) | The path from the sensor chip to `/mavros/imu/data` |
| 6 | [Notebook 6](./notebooks/6-imu-rates-and-configuration.ipynb) | PX4 and MAVLink rates, configuration, and MAVROS2 plugins |
| 7 | [Notebook 7](./notebooks/7-interfacing-with-imu.ipynb) | Write, deploy, and run a ROS 2 node that reads the IMU |

## Prerequisites

Complete the Duckietown Manual's [Initial Setup](https://docs.duckietown.com/ente/opmanual-dd24/10-duckiedrone-preliminaries/initial-setup.html#required-software-and-accounts)
so Docker and the Duckietown Shell (`dts`) are installed and configured on the base station.
Notebooks 1-5 need no live Duckiedrone. [Notebook 6](./notebooks/6-imu-rates-and-configuration.ipynb)
needs one only for its live rate-change example, and
[Notebook 7](./notebooks/7-interfacing-with-imu.ipynb) requires a virtual or physical Duckiedrone
running the `ente` software stack.

The base station is the computer running Docker and `dts`. The `dts code editor` terminal belongs
to a separate browser-editor environment: its filesystem and `localhost` are not the base station's.
Keep a separate base-station terminal available for device commands.

### Choose the terminal

| Task | Where to run it |
| --- | --- |
| Read notebooks, edit [imu_subscriber.py](./packages/solution/solution/imu_subscriber.py), and run local notebook activities | `dts code editor` |
| Run `dts duckiebot virtual connect`, `dts code build`, `dts code workbench`, or physical-device `ssh` | A separate base-station terminal, outside `dts code editor` |
| Inspect IMU topics, request stream intervals, and record data in Notebooks 6–7 | The Duckiedrone's MAVROS2 container shell, reached after connecting to the device |
| Watch subscriber output and stop a live run | The original workbench terminal; keep it ready for `Ctrl-C` |

### Local notebooks and checkpoints

Open the notebooks in `dts code editor`. Interactive checkpoints use the notebook path supplied
by that editor in execution-message metadata; this does not require saved notebook metadata.
A Jupyter/IPython kernel with `ipywidgets` alone is not sufficient. Work through the
first five notebooks without a live Duckiedrone. [Notebook 6](./notebooks/6-imu-rates-and-configuration.ipynb)
can be read offline, but its live rate-change example needs a disarmed Duckiedrone.

### Virtual or physical Duckiedrone

For a virtual Duckiedrone, start the Duckiematrix and attach the Duckiedrone to an entity before
expecting IMU data. For a physical Duckiedrone, check that its
`ente` services and MAVROS2 are running as described in [Notebook 7](./notebooks/7-interfacing-with-imu.ipynb).
This LX does not arm or fly the Duckiedrone; handle a physical device only while disarmed and clear
of the propellers.

## Complete the IMU subscriber

The two `TO IMPLEMENT` blocks in [imu_subscriber.py](./packages/solution/solution/imu_subscriber.py)
identify the subscription and message-decoding tasks. This solution repository includes their
implementations; a starter version leaves them for completion. Follow
[Notebook 7](./notebooks/7-interfacing-with-imu.ipynb) to inspect or complete the code and save edits
before building.
From the LX root in the base-station terminal, build and run the listener on the Duckiedrone:

```bash
dts code build -R amelia
dts code workbench -R amelia
```

Replace `amelia` with the configured Duckiedrone name. The workbench displays the listener's output; stop it with `Ctrl-C` when finished.

## Further reading

Each notebook's Further reading section is the primary reference for its lesson. These sources
cover the main stages of this LX:

- **IMU measurements:** [Duckiedrone sensor calibration](https://docs.duckietown.com/ente/opmanual-dd24/30-duckiedrone-setup-and-config/50-sensor-calibrations.html) explains the calibration behind the readings.

- **Orientation:** [ROS 2 quaternion fundamentals](https://docs.ros.org/en/jazzy/Tutorials/Intermediate/Tf2/Quaternion-Fundamentals.html) covers the rotation conventions used in Notebook 4.

- **ROS 2 subscriber:** The [sensor_msgs/Imu message definition](https://github.com/ros2/common_interfaces/blob/jazzy/sensor_msgs/msg/Imu.msg) specifies the fields unpacked in Notebook 7.

- **Notation:** The [notation reference](./assets/data/notation.md) collects the symbols used throughout the notebooks.

## For LX authors

Learner material is in `notebooks/` and `packages/`; checkpoint prompts and model answers are in
`checkpoint_data/`, and structural, checkpoint, and numerical-conversion checks are in `tests/`. Run checks from the LX root:

```bash
python3 -m pytest tests/
ruff check .
```
