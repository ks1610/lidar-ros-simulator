import os
from launch import LaunchDescription
from launch.actions import ExecuteProcess
from launch_ros.actions import Node

def generate_launch_description():
    # Lấy đường dẫn thư mục hiện tại (chứa file sdf và rviz)
    current_dir = os.getcwd()
    world_file = os.path.join(current_dir, 'lidar_world.sdf')
    rviz_config = os.path.join(current_dir, 'lidar.rviz')

    # 1. Khởi động Gazebo và TỰ ĐỘNG PLAY (cờ -r)
    gazebo = ExecuteProcess(
        cmd=['gz', 'sim', world_file, '-r'],
        output='screen'
    )

    # 2. Khởi động Bridge
    bridge = Node(
        package='ros_gz_bridge',
        executable='parameter_bridge',
        arguments=['/scan@sensor_msgs/msg/LaserScan@gz.msgs.LaserScan'],
        output='screen'
    )

    # 3. Khởi động Gắn hệ tọa độ (TF)
    tf_node = Node(
        package='tf2_ros',
        executable='static_transform_publisher',
        arguments=['0', '0', '0', '0', '0', '0', 'map', 'my_lidar/lidar_link/gpu_lidar'],
        output='screen'
    )

    # 4. Khởi động RViz2 (Tự động load file cấu hình nếu file tồn tại)
    rviz_args = []
    if os.path.exists(rviz_config):
        rviz_args = ['-d', rviz_config]
        
    rviz = Node(
        package='rviz2',
        executable='rviz2',
        arguments=rviz_args,
        output='screen'
    )

    return LaunchDescription([
        gazebo,
        bridge,
        tf_node,
        rviz
    ])