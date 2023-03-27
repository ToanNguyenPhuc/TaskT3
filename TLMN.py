def getTypeAction(action):
  return __ACTIONS__[action][0]
def getValueActions(action):
  return __ACTIONS__[action][1]
def agentMain(state,per):
  actions = getValidActions(state)
  actions = np.where(actions == 1)[0]
  type_action = [getTypeAction(action) for action in actions]
  id = np.argmax(type_action)
  return actions[id],per

win,per = numba_main_2(agentMain,1000,np.array([0.]),1)
print('win',win)