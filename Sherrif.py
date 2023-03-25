
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
def strategy3(state,per):
  actions = getValidActions(state)
  actions = np.where(actions == 1)[0]
  # hoi lo the trong tui
  # if 62 in actions:
  #   return 62,per
  # # hoi lo the done
  # if 46 in actions:
  #   return 46,per
  # # Hoi lo 1 coin
  # if 45 in actions:
  #   return 45,per
  actions_point = per[actions]
  return actions[np.argmax(actions_point)],per
per = np.array([3072.78446672, 2275.81537697, 4026.73107539, 4229.42424206,
       3950.69881352, 2819.3709458 , 5310.95286769, 2821.13117227,
       4084.14185025, 3185.68508295, 3189.09927581, 2671.61034121,
       3260.70386798, 3248.12814816, 3043.64911845, 1846.2837195 ,
       4068.20751977, 2534.51422929, 5186.30869811, 4271.40659015,
       3361.75631509, 3879.22118819, 3720.30978468, 3557.38860471,
       3453.2255582 , 3421.04140934, 4231.52865833, 3427.37316029,
       4288.45326252, 2380.3387198 , 3043.3061794 , 4101.73227284,
       4029.33359057, 3607.30764618, 2220.9227399 , 2717.94857346,
       1439.68656779, 3855.85388901, 3337.85454584, 2504.50037646,
       2478.02743352, 3222.77733846, 3445.88771272, 2137.53066425,
       3952.690724  , 2171.98179746, 3795.72618768, 3495.11014367,
       3744.3586831 , 4276.91290375, 3253.87644848, 3580.90617343,
       3204.76234701, 2639.72792517, 1821.34964516, 3570.42636318,
       3212.019844  , 3583.68886086, 2464.34143859, 3939.27075498,
       3138.967813  , 5533.34508788, 1726.48763214, 3244.50895032,
       3416.64024734, 4161.73302768, 2292.44598161, 1771.59299082,
       1932.27421567, 4084.82265037, 2300.87734671, 2652.76644206,
       3094.69325948, 2589.94187274, 2453.25550892, 3179.25886846,
       2486.11336782, 5170.76695875, 4074.3714663 , 2031.29446459,
       3265.01610287, 4253.26401114])
win,per = numba_main_2(strategy3,1000,per,1)
print(win)