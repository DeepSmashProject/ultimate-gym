
from ultimate_gym import UltimateEnv
from yuzulib.game.ssbu import Action
import time
import random
import argparse
import os

action_list = [
    Action.ACTION_JAB,
    Action.ACTION_RIGHT_TILT,
    Action.ACTION_LEFT_TILT,
    Action.ACTION_UP_TILT,
    Action.ACTION_DOWN_TILT,
    Action.ACTION_RIGHT_SMASH,
    Action.ACTION_LEFT_SMASH,
    Action.ACTION_UP_SMASH,
    Action.ACTION_DOWN_SMASH,
    Action.ACTION_NEUTRAL_SPECIAL,
    Action.ACTION_RIGHT_SPECIAL,
    Action.ACTION_LEFT_SPECIAL,
    Action.ACTION_UP_SPECIAL,
    Action.ACTION_DOWN_SPECIAL,
    Action.ACTION_UP_RIGHT_SPECIAL,
    Action.ACTION_UP_LEFT_SPECIAL,
    Action.ACTION_GRAB,
    Action.ACTION_SHIELD,
    Action.ACTION_JUMP,
    Action.ACTION_RIGHT_JUMP,
    Action.ACTION_LEFT_JUMP,
    Action.ACTION_SHORT_HOP,
    Action.ACTION_RIGHT_SHORT_HOP,
    Action.ACTION_LEFT_SHORT_HOP,
    #Action.ACTION_UP_TAUNT,
    #Action.ACTION_DOWN_TAUNT,
    #Action.ACTION_LEFT_TAUNT,
    #Action.ACTION_RIGHT_TAUNT,
    Action.ACTION_SPOT_DODGE,
    Action.ACTION_RIGHT_ROLL,
    Action.ACTION_LEFT_ROLL,
    #Action.ACTION_RIGHT_DASH,
    #Action.ACTION_LEFT_DASH,
    #Action.ACTION_RIGHT_WALK,
    #Action.ACTION_LEFT_WALK,
    #Action.ACTION_CROUCH,
    #Action.ACTION_RIGHT_CRAWL,
    #Action.ACTION_LEFT_CRAWL,
    Action.ACTION_RIGHT_STICK,
    Action.ACTION_LEFT_STICK,
    Action.ACTION_UP_STICK,
    Action.ACTION_DOWN_STICK,
    #Action.ACTION_NO_OPERATION
]
action_list2 = [
    Action.ACTION_JUMP,
    Action.ACTION_RIGHT_JUMP,
    Action.ACTION_LEFT_JUMP,
    Action.ACTION_SHORT_HOP,
    Action.ACTION_RIGHT_SHORT_HOP,
    Action.ACTION_LEFT_SHORT_HOP,
]
env = UltimateEnv(fps=6)
for k in range(10):
    done = False
    obs = env.reset()
    step = 0
    while not done:
        action = random.choice(action_list)
        next_obs, reward, done, info = env.step(action)
        print("episode: {}, step: {}, action: {}, obs: {}, done: {}, reward: {}, damage: {}, diff_damage: {}, kill: {}".format(k, step, action["name"], next_obs[100][100], done, reward, info["damage"], info["diff_damage"], info["kill"]))
        step += 1
print("finished!")