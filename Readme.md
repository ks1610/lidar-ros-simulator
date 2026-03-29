# Lidar simulation guide

## Running process 

### Run Gazebo
```
gz sim lidar_world.sdf
```

### Open ROS-Gazebo Bridge
```
ros2 run ros_gz_bridge parameter_bridge /scan@sensor_msgs/msg/LaserScan@gz.msgs.LaserScan
```

### Static Transform
```
ros2 run tf2_ros static_transform_publisher 0 0 0 0 0 0 map my_lidar/lidar_link/gpu_lidar
```

### Start Rviz 
```
rviz2
```

## Run via launch file
```
ros2 launch lidar_launch.py
```