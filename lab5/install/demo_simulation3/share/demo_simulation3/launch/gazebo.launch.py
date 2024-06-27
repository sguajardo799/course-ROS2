from launch import LaunchDescription
from launch.actions import ExecuteProcess
from launch.substitutions import Command
from launch_ros.actions import Node

def generate_launch_description():

    urdf_path = '/home/ros2curso/curso/lab4/demo_simulation_2/urdf/differential-robot.urdf'

    pub = Node(
        package="robot_state_publisher",
        executable="robot_state_publisher",
        parameters=[{
            'robot_description': Command(['xacro ', urdf_path])
        }]
    )

    spawn_entity = Node(
        package="gazebo_ros",
        executable="spawn_entity.py",
        arguments=['-entity', 'robot', '-topic','robot_description'],
        output='screen'
    )

    gazebo = ExecuteProcess(
        cmd=[
            'gazebo',
            '--verbose',
            '-s',
            'libgazebo_ros_init.so',
            '-s',
            'libgazebo_ros_factory.so'
            ],
            output= 'screen'
    )

    teleop = Node(
        package="teleop_twist_keyboard",
        executable="teleop_twist_keyboard"
    )

    rviz = ExecuteProcess(
        cmd=['rviz2'],
        output='screen'
    )

    return LaunchDescription([
        gazebo,
        pub,
        spawn_entity,
        rviz
    ])