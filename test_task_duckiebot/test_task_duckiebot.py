#!/usr/bin/env python3

"""
Simple exercise to construct a controller that controls the simulated Duckiebot using pose. 
"""

import time
import sys
import datetime
import argparse
import math
import numpy as np
import gym
from gym_duckietown.envs import DuckietownEnv

parser = argparse.ArgumentParser()
parser.add_argument('--env-name', default=None)
parser.add_argument('--map-name', default='udem1')
parser.add_argument('--no-pause', action='store_true', help="don't pause on failure")
args = parser.parse_args()

if args.env_name is None:
    env = DuckietownEnv(
        map_name = args.map_name,
        domain_rand = False,
        draw_bbox = False
    )
    buf_env = DuckietownEnv(
        map_name = args.map_name,
        domain_rand = False,
        draw_bbox = False
    )
else:
    env = gym.make(args.env_name)

obs = env.reset()
buf_env.reset()
env.render()
speed = 0.1
total_reward = 0

#circle radius
r = 0.07

#steering module
steering = speed / r

#to regulate the period
k_T = 0.75

#period
T = k_T * (2 * np.pi * r /  speed)

#to reverse the motor direction
k = 1

#to reverse the steering direction
steering_direction = -1

time = datetime.datetime.utcnow()  
start_time = time.second + time.microsecond / (10**len(str(time.microsecond)))
current_time = start_time

while current_time - start_time < 5:

    time = datetime.datetime.utcnow()  
    current_time = time.second + time.microsecond / (10**len(str(time.microsecond)))

    lane_pose = env.get_lane_pos2(env.cur_pos, env.cur_angle)
    distance_to_road_center = lane_pose.dist
    angle_from_straight_in_rads = lane_pose.angle_rad

    k_p = 10
    k_d = 1
    steering = k_p*distance_to_road_center + k_d*angle_from_straight_in_rads # TODO: You should overwrite this value

    obs, reward, done, info = env.step([0.2, steering])
    total_reward += reward

    env.render()


#without checking the position for staying on the road and  without checking reward
while True:
    
    time = datetime.datetime.utcnow()  
    start_time = time.second + time.microsecond / (10**len(str(time.microsecond)))
    current_time = 0

    steering = speed / r

    while current_time - start_time < T:

        time = datetime.datetime.utcnow()  
        current_time = time.second + time.microsecond / (10**len(str(time.microsecond)))
        
        #print('steering direction: ', steering_direction, sep = ' ')

        lane_pose = env.get_lane_pos2(env.cur_pos, env.cur_angle)
        angle_from_straight_in_rads = lane_pose.angle_rad
        obs, reward, done, info = env.step([k * speed, steering_direction * steering])
        #total_reward += reward
        env.render()
    steering_direction *= -1
    
