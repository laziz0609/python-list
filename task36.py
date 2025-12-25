def uzun(royxat: list) -> str:
    eng_uzun = 0
    
    for soz in royxat:
        if len(soz) > eng_uzun:
            eng_uzun = soz
            
    return eng_uzun