from setuptools import find_packages, setup
import os
from glob import glob

package_name = 'demo_launch'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        (
            'share/ament_index/resource_index/packages',
            ['resource/' + package_name]
        ),
        (
            'share/' + package_name, 
            ['package.xml']
        ),
        (
            os.path.join('share', package_name, 'launch/'), 
            glob('launch/*launch.[pxy][yma]*')
        ),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='ros2curso',
    maintainer_email='ros2curso@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            "simple_pub = demo_launch.pub_node:main",
            "simple_sub = demo_launch.sub_node:main",
            "pub_params = demo_launch.pub_node_params:main",
        ],
    },
)
