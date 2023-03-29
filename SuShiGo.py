def test1(state,per):
    actions = getValidActions(state)
    actions = np.where(actions == 1)[0]
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
    actions_point = per[actions]
    return actions[np.argmax(actions_point)],per

per = np.array([5,13,8,0,3,10,4,11,1,15,6,2,12,9])
win1, per = numba_main_2(test1, 10000,per , 1)
print('win',win1)
