GivenList = [10, 501, 22, 37, 100, 999, 87, 351]


def is_prime(l1):
    prime_list = []
    count = 0
    for i in range(len(GivenList)):
        if i == 0 or i == 1:
            continue
        for j in range(2, (GivenList[i]//2) + 1):
            if GivenList[i] % j == 0:
                break
        else:
            prime_list.append(GivenList[i])
            count = count + 1
    return prime_list


print(is_prime(GivenList))

