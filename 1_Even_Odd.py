GivenList = [10, 501, 22, 37, 100, 999, 87, 351]

even_list = []
odd_list = []
# Create Even number list and Odd number list from the given list
for i in range(len(GivenList)):
    if(GivenList[i] % 2) == 0 and GivenList[i] != 0:
        even_list.append(GivenList[i])
    elif GivenList[i] == 0:
        print('Zero')
    else:
        odd_list.append(GivenList[i])
print('Given list is:', GivenList)
print('Even numbers  list :', even_list)
print('Odd numbers list:', odd_list)
