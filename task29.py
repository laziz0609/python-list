sonlar  = [1, 2, 2, 3, 4, 1, 5, 6, 3, 7]

sonlar2 = []

for i in sonlar:
    if sonlar.count(i) == 1:
        sonlar2.append(i)
        
print(sonlar2)
    