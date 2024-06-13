from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node

def generate_launch_description():
    
    number_arg = DeclareLaunchArgument(
        'number',
        default_value = '0',
        description = "Numero a publicar"
    )

    pub = Node(
        package="demo_launch",
        executable="pub_params",
        name="Int16_publisher_Node",
        #parameters={"number": 10},
        parameters=[{'number': LaunchConfiguration('number')}]
    )

    sub = Node(
        package="demo_launch",
        executable="simple_sub",
        name="Int16_subscriber_Node"
    )

    return LaunchDescription([
        number_arg,
        pub,
        sub
    ])