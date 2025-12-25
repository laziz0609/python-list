def is_palindrome(royxat: list) -> list:
    copy_royxat = royxat.copy()
    
    ret_toyxat = []
    
    for element in copy_royxat:
        
        pal_text = ""
        for i in element:
            if not i in " ,.!?:;":
                pal_text += i
            
        if pal_text == pal_text[::-1]:
            ret_toyxat.append(element)
        
        
    return ret_toyxat