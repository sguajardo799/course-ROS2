from setuptools import find_packages, setup

package_name = 'demo_nodos'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
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
            "simple_node = demo_nodos.simple_node:main",
            "simple_pub = demo_nodos.pub_node:main",
            "simple_sub = demo_nodos.sub_node:main",
        ],
    },
)
