from setuptools import find_packages, setup

package_name = 'color_detective_robot'

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
    maintainer='kashvi',
    maintainer_email='kashvi@example.com',
    description='Color Detective Robot workshop package',
    license='Apache-2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'color_publisher = color_detective_robot.color_publisher:main',
            'color_bridge = color_detective_robot.color_bridge:main',
            'robot_controller = color_detective_robot.robot_controller:main',
        ],
    },
)
