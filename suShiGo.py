
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
#----------------------------------------------------------------
def MainAgent(state,per):
    actions = getValidActions(state)
    actions = np.where(actions ==1)[0]
    index_1 = 14*(0 + 1)
    cards_on_hand = state[index_1+2:index_1+14]
    turn = state[1:2] % 7
    # reset per
    if turn == 1:
        per = np.array([5,13,8,0,3,10,4,11,1,15,6,2,12,9])
    #--------------#--------------#--------------#--------------#--------------
    if  cards_on_hand[1] == 3:
        per[1] = 0
    if cards_on_hand[10] == 1:
        per[7] = 15    
    if cards_on_hand[9] == 3:
        per[9] = 0
    if turn > 4 and cards_on_hand[1] < 1:
        per[1] = 0
    if 9 in actions:
      return 9,per
    elif 1 in actions:
      return 1,per
    elif 12 in actions:
      return 12,per
    elif 7 in actions:
      return 7,per
    elif 5 in actions:
      return 5,per
    elif 13 in actions:
      return 13,per
    elif 2 in actions:
      return 2,per
    elif 10 in actions:
      return 10,per
    elif 0 in actions:
      return 0,per
    elif 6 in actions:
      return 6,per
    elif 4 in actions:
      return 4,per 
    elif 11 in actions:
      return 11,per
    elif 8 in actions:
      return 8,per
    elif 3 in actions:
      return 3,per
    return np.random.choice(actions),per
win,per = numba_main_2(MainAgent,10000,np.array([0]),1)
print('win',win)