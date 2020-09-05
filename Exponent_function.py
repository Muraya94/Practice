# FOR LOOP TO RAISE NUMBERS TO A GIVEN POWER
def raise_to_pwr(base_num, pwr_num):
    result = 1
    for index in range(pwr_num):
        result = result * base_num
    return result

print(raise_to_pwr(5, 2))

