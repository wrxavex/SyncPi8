



def button_check(k):
    global button_pre
    global count1
    global count2
    global count3
    global count4
    if k == 23 and button_pre != 23:
        count1 = count1 + 1
        return count1
    if k == 22 and button_pre != 22:
        count2 = count2 + 1
        return count2
    if k == 24 and button_pre != 24:
        count3 = count3 + 1
        return count3
    if k ==  5 and button_pre != 5:
        count4 = count4 + 1
        return count4
    else:
        return count