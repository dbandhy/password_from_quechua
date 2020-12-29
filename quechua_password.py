# Return a lenght of characters from quechua alphabet

import random

def aleatory_password(lenght):
    pw = str()
    characters = "achiklmnñpqrstuwy" + "0123456789"
    for i in range(lenght):
        pw = pw + random.choice(characters)
    return pw
    
