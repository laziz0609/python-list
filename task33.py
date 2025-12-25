list1 = [1, 2, 3, 4, 5] 
list2 = [4, 5, 6, 7]

list4 = []

for i in list1:
    if i in list2 and not i in list4:
        list4.append(i)