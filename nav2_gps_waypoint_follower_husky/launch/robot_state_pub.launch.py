# Copyright 2025 South Carolina State University
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
# Author: Van Patiluna

import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    # get the launch directory
    gps_wpf_dir = get_package_share_directory(
        "nav2_gps_waypoint_follower_husky")
    #urdf_dir = os.path.join(gps_wpf_dir, 'urdf')
    
    # set the path of the URDF file
    urdf = os.path.join(gps_wpf_dir, 'urdf', 'husky_a200.urdf')
    # set URDF data to robot_description
    with open(urdf, 'r') as infp:
        robot_description = infp.read()

    # run the robot_state_publisher node
    start_robot_state_publisher_cmd = Node (
        package = 'robot_state_publisher',
        executable = 'robot_state_publisher',
        name = 'robot_state_publisher',
        output = 'both',
        parameters =[{'robot_description': robot_description}]
    )    

    # create the launch condition and populate
    ld = LaunchDescription()

    # robot_state_publisher launch
    ld.add_action(start_robot_state_publisher_cmd)

    return ld

