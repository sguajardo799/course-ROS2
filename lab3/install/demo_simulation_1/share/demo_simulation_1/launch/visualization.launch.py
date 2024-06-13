from launch import LaunchDescription
from launch.actions import ExecuteProcess
from launch_ros.actions import Node

def generate_launch_description():

    urdf_path = '/home/ros2curso/curso/lab3/demo_simulation_1/urdf/differential-robot.urdf'

    with open(urdf_path,'r') as i:
        robot_desc = i.read()

    pub = Node(
        package="robot_state_publisher",
        executable="robot_state_publisher",
        name="robot_state_publisher",
        output='screen',
        parameters=[{
            'robot_description': robot_desc
        }]
    )

    joint = Node(
        package="joint_state_publisher",
        executable="joint_state_publisher",
        name="joint_state_publisher",
        output='screen'
    )

    rviz = ExecuteProcess(
        cmd=['rviz2', '-d', '/home/ros2curso/curso/lab3/demo_simulation_1/rviz/config.rviz'],
        output='screen'
    )

    return LaunchDescription([
        pub,
        rviz
    ])