l1 = [1, 2, 3, 3, 4, 10]
l2 = [6, 7, 3, 2, 2, 10]
l3 = [99, 1, 22, 3, 6, 12, 3]
l4 = l1 + l2 + l3
new_list = []
dup_list = []
for i in l4:
    if i not in new_list:
        new_list.append(i)
    else:
        dup_list.append(i)
print(set(dup_list))


