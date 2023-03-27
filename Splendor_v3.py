# def getCardValue(state,per):
def getCardValue(state,card):
    card = np.array(card)
    if len(np.where(card > 0)[0]) == 0:
      return -999
    type_card = np.array(card[1:6])
    type_card = np.where(type_card == 1)[0][0]
    player_stock_const = state[6+6:6+6+5]
    had = player_stock_const[type_card]
    point = card[0]
    stock_require = card[-5:]
    result = player_stock_const -  stock_require
    need = sum(result[result < 0])

    value =   type_card/(had*1) * point/(need+1)
    return value
def MainAgent(state,per):
    actions = getValidActions(state)
    actions = np.where(actions == 1)[0]
    temp_cards = list(state[18:150]) + list(state[175:208])
    cards = []
    for i in range(0,15):
      temp_card = temp_cards[i*11:i*11+11]
      cards.append(temp_card)
    value_arr = [getCardValue(state,card) for card in cards]
    return np.argmax(value_arr),per
win,per = numba_main_2(MainAgent,10000,np.array([0.]),1)
print('win',win)