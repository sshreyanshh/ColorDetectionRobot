# Color Detective Robot

## Project pipeline

Windows webcam
-> OpenCV color detection
-> TCP
-> ROS 2 color_bridge
-> /detected_color
-> ROS 2 robot_controller
-> /cmd_vel
-> Webots e-puck

## Robot behavior

- RED -> turn left
- GREEN -> move forward
- BLUE -> turn right
- NO COLOR -> stop

## Project files

### OpenCV
`WINDOWS/color_detector.py`

This handles:
- webcam capture
- BGR to HSV conversion
- red/green/blue masks
- pixel counting
- color classification
- sending the detected color to the ROS 2 bridge

### ROS 2
`ROS2/color_detective_robot/color_detective_robot/color_bridge.py`

Receives color strings over TCP and publishes them on:
`/detected_color`

`ROS2/color_detective_robot/color_detective_robot/robot_controller.py`

Subscribes to `/detected_color` and publishes `TwistStamped` commands on:
`/cmd_vel`

`color_publisher.py`

A simple ROS 2 subscriber for testing/teaching the `/detected_color` topic.

## What is NOT included

The Webots R2025a application and the official Cyberbotics `webots_ros2` repository are not redistributed in this project folder. They should be installed/provided separately because they are external software.

## Current tested run sequence

### WSL / Ubuntu

First source the ROS 2 workspace:

```bash
source ~/webots_ws/install/setup.bash
```

Start the Webots e-puck:

```bash
ros2 launch webots_ros2_epuck robot_launch.py
```

In another WSL terminal:

```bash
source ~/webots_ws/install/setup.bash
ros2 run color_detective_robot color_bridge
```

In another WSL terminal:

```bash
source ~/webots_ws/install/setup.bash
ros2 run color_detective_robot robot_controller
```

### Windows PowerShell

```powershell
cd C:\Users\Kashvi\ColorDetectiveRobot
python color_detector.py
```

Hold a colored object in front of the webcam.

## ROS 2 package installation

Copy the `ROS2/color_detective_robot` folder into:

```text
~/webots_ws/src/
```

Then:

```bash
cd ~/webots_ws
colcon build --packages-select color_detective_robot
source install/setup.bash
```

## Important workshop note

The OpenCV and ROS 2 code is the educational part of the project.

The following are infrastructure/setup and can be preconfigured for students:
- WSL/Ubuntu
- ROS 2 installation
- Webots installation
- webots_ros2 installation
- e-puck world/configuration
- Python/system dependencies
- ROS 2 workspace creation and build
- Windows <-> WSL networking

The `WSL_IP` value in `WINDOWS/color_detector.py` is currently the tested WSL address from the development setup. For a student distribution, this should be replaced by an automatic WSL-IP discovery method or configured by the workshop setup script.
