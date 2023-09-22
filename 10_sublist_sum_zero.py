# function to check for sublist with sum equal to zero

def sublist_sum_zero(l1):
    for i in range(len(l1)):
        sl_sum = 0
        for j in range(i, len(l1)):
            sl_sum = sl_sum + l1[j]
            if sl_sum == 0:
                return l1[i:j+1]
    return None


given_list = [4, 2, -3, 1, 6]
result = sublist_sum_zero(given_list)
if result is not None:
    print(result)
else:
    print('No sublist with sum equal to zero found')