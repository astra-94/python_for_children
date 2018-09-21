def weight_on_moon(m, d):
    i = 0
    for i in range(1, 16):
        m1 = (m) * 0.165
        print('вес в год №', i, ':', m1)
        i = i + 1
        m = m + d
