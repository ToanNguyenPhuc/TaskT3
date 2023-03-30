@njit()
def getLuaMi(state):
    return state[1]
@njit()
def getNongTrai(state):
   return state[2]
@njit()
def getTiemBanh(state):
    return state[3]
@njit()
def getQuanCaPhe(state):
    return state[4]
@njit()
def getCuaHangTienLoi(state):
    return state[5]
@njit()
def getRung(state):
    return state[6]
def getNhaMayPhoMat(state):
    return state[7]
def getNhaMayNoiThat(state):
    return state[8]
def getMoQuang(state):
    return state[9]
@njit()
def getQuanAnGiaDinh(state):
    return state[10]
def getVuonTao(state):
    return state[11]
@njit()
def getChoTraiCay(state):
    return state[12]
def getSanVanDong(state):
    return state[13]
def getDaiTruyenHinh(state):
    return state[14]
def getTrungTamThuongMai(state):
    return state[15]
def get22dCard(state):
    return state[16]
def get16dCard(state):
    return state[17]
@njit()
def get10dCard(state):
    return state[18]
@njit()
def get4dCard(state):
    return state[19]
def getPlayerCoin(state):
  return state[0]
def getAllCardOnBoard(state):
  return state[80:92]
def getCardLuaMiOnBoard(state):
  card_on_board = getAllCardOnBoard(state)
  return card_on_board[0]
def getCardNongTraiOnBoard(state):
  card_on_board = getAllCardOnBoard(state)
  return card_on_board[1]
def getCardTiemBanhOnBoard(state):
    card_on_board = getAllCardOnBoard(state)
    return card_on_board[2]
def getCardQuanCaPheOnBoard(state):
    card_on_board = getAllCardOnBoard(state)
    return card_on_board[3]
def getCardCuaHangTienLoiOnBoard(state):
    card_on_board = getAllCardOnBoard(state)
    return card_on_board[4]
def getCardRungOnBoard(state):
  card_on_board = getAllCardOnBoard(state)
  return card_on_board[5]
def getCardNhaMayPhomatOnBoard(state):
  card_on_board = getAllCardOnBoard(state)
  return card_on_board[6]
def getCardNhaMayNoiThatOnBoard(state):
  card_on_board = getAllCardOnBoard(state)
  return card_on_board[7]
def getCardMoQuangOnBoard(state):
  card_on_board = getAllCardOnBoard(state)
  return card_on_board[8]
def getCardQuanAnGiaDinhOnBoard(state):
  card_on_board = getAllCardOnBoard(state)
  return card_on_board[9]
def getCardVuonTaoOnBoard(state):
  card_on_board = getAllCardOnBoard(state)
  return card_on_board[10]
def getCardChoTraiCayOnBoard(state):
  card_on_board = getAllCardOnBoard(state)
  return card_on_board[11]
def get4CardNeed(state,idCard):
    return state[16+20*idCard:16+20*idCard+4]
def get4PlayerCoin(state):
    return [state[0],state[20],state[40],state[60]]
def getTotalPlayerCard(state):
  return sum(state[1:20])
@njit()
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