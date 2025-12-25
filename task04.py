ismlar = []

while len(ismlar) < 3:
    ism = input(f"{len(ismlar) + 1} - ism: ")
    
    if ism.isalpha():
        ismlar.append(ism)
        
    else:
        print("Bu ism emas")