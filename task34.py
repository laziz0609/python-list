sonlar = [1, 2, 3, 7, 8, 9]

sonlar2 = []

for i in range(len(sonlar)-1):
    print(i)
    for m in range(i+1, len(sonlar)):
        print(m)
        if sonlar[i] + sonlar[m] == 10:
            sonlar2.append([sonlar[i], sonlar[m]])
            
print(sonlar2)
print(range(len(sonlar)-1))