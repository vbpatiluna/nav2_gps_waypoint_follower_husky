from setuptools import find_packages, setup
import os
from glob import glob

package_name = 'nav2_gps_waypoint_follower_husky'

setup(
    name=package_name,
    version='1.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name, 'launch'), glob('launch/*.launch.py')),
        (os.path.join('share', package_name, 'config'), glob('config/*')),
        (os.path.join('share', package_name, 'urdf'), glob('urdf/*')),
        (os.path.join('share', package_name, 'meshes'), glob('meshes/*')),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Van Patiluna',
    maintainer_email='vpatilun@scsu.edu',
    description='Package for robot gps localization and navigation.',
    license='Apache-2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'logged_waypoint_follower = nav2_gps_waypoint_follower_husky.logged_waypoint_follower:main',
            'gps_waypoint_logger = nav2_gps_waypoint_follower_husky.gps_waypoint_logger:main'
        ],
    },
)
