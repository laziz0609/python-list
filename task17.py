ismlar = []

while True:
    print("chiqish uchun enter tugmasini bosing\t")
    ism = input("Ism: ")
    
    if ism != "":
        if ism.isalpha():
            ismlar.append(ism)
            
        else:
            print("bu ism emas")
        
    else:
        break
    
print(ismlar)