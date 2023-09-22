pl = [10, 20, 30, 9]


def find_numbers(l1, t_sum):
    result = []
    for i in range(len(l1)):
        for j in range(i + 1, len(l1)):
            for k in range(j + 1,len(l1)):
                if l1[i] + l1[j] + l1[k] == t_sum:
                    result.append((l1[i], l1[j],l1[k]))
    return result


print(find_numbers(pl, 59))







