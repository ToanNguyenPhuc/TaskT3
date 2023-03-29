def MachiKoro(state,per):
    actions = getValidActions(state)
    actions = np.where(actions == 1)[0]
    phase = state[122:129]
    phase = np.where(phase == 1)[0]   
    dice = state[117]

    if get10dCard(state) > 0:
      per[49] = 10
    if get22dCard(state) > 0:
      per[50] = 10
    if get16dCard(state) > 0  :
      per[52] = 10
    if  phase == 1:
      if dice != 4 and dice != 2:
          return 1,per
      elif dice == 4 or dice == 2:
        return 0,per
    if state[18] == 1  and getQuanAnGiaDinh(state) < 1 and 43 in actions:
      return 43,per
    if getQuanCaPhe(state) > 1:
      per[37] = -1
    if getReward(state) == 0 or getReward(state) == 1:
          per = np.array([ 0, 1, -1, -1, -1, -1, -1,-1, -1, -1,-1, -1, -1, -1, -1, -1, -1, -1,
  -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 10, 10,
  10, 10, 10, 10, -1, -1, -1, -1, -1, -1, -1, -1, -1,-1,-1,15,-1, 0])
    point_actions = per[actions]
    idx = np.argmax(point_actions)
    action = actions[idx]
    return action,per
policy = np.array([ 0, 1, -1, -1, -1, -1, -1,-1, -1, -1,-1, -1, -1, -1, -1, -1, -1, -1,
  -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 10, 10,
  10, 10, 10, 10, -1, -1, -1, -1, -1, -1, -1, -1, -1,-1,-1,15,-1, 0])