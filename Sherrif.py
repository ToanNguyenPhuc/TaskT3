
# Check hệ thống

# import Base.MachiKoro.env as env
# from CheckEnv import check_env
# print(check_env(env))

import numpy as np
import random as rd
from numba import njit, jit
import sys, os
from setup import SHORT_PATH
import importlib.util
game_name = 'Sheriff'

def add_game_to_syspath(game_name):
    if len(sys.argv) >= 2:
        sys.argv = [sys.argv[0]]
    sys.argv.append(game_name)

def setup_game(game_name):
    spec = importlib.util.spec_from_file_location('env', f"{SHORT_PATH}Base/{game_name}/env.py")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module 
    spec.loader.exec_module(module)
    return module

add_game_to_syspath(game_name)
env = setup_game(game_name)

getActionSize = env.getActionSize
getStateSize = env.getStateSize
getAgentSize = env.getAgentSize

getValidActions = env.getValidActions
getReward = env.getReward
numba_main_2 = env.numba_main_2

@njit()
def bot_lv0(state, perData):
    validActions = getValidActions(state)
    arr_action = np.where(validActions==1)[0]
    idx = np.random.randint(0, arr_action.shape[0])
    return arr_action[idx], perData
#----------------------#----------------------#----------------------#----------------------#----------------------#----------------------
def strategy4(state,per):
  actions = getValidActions(state)
  actions = np.where(actions == 1)[0]
  if 2 in actions:
    return 2,per
  elif 3 in actions:
    return 3,per
  elif 6 in actions:
    return 6,per
  elif 8 in actions:
    return 8,per
  elif 18 in actions:
    return 18,per
  elif 19 in actions:
    return 19,per
  elif 26 in actions:
    return 26,per
  elif 28 in actions:
    return 28,per
  elif 31 in actions:
    return 31,per
  elif 32 in actions:
    return 32,per
  elif 49 in actions:
    return 49,per
  elif 61 in actions:
    return 61,per
  elif 65 in actions:
    return 65,per
  elif 69 in actions:
    return 69,per
  elif 77 in actions:
    return 77,per
  elif 78 in actions:
    return 78,per
  elif 81 in actions:
    return 81,per
  else:
    return np.random.choice(actions),per
win,per = numba_main_2(strategy4,10000,np.array([0.]),1)
print(win)