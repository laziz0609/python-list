def taqsim(royxat: list) -> list:
    ret_list = [[], [], []]
    
    for text in royxat:
        
        if len(text) <= 3:
            ret_list[0].append(text) 
               
        elif 4 <= len(text) <= 6:
            ret_list[1].append(text)
                
        if len(text) > 6:
            ret_list[2].append(text) 
            
    return ret_list   