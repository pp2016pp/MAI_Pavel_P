def burner(c, h, o):
    if h//2 < o:
        water = h//2
    else:
        water = o
    water_h = water * 2
    water_o = water

    if (o-water_o)//2 <= c:
        co2 = (o-water_o)//2
    else:
        co2 = c
    co2_o = co2 * 2
    co2_c = co2

    if (h-water_h)//4 < (c - co2_c):
        methane = (h-water_h)//4
    else:
        methane = c - co2_c
    return water, co2, methane


burner(45, 11, 100)  # (5,45,0)
burner(354, 1023230, 0)  # (0,0,354)
burner(939, 3, 694)  # (1,346,0)
