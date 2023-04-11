
def translator_hack(text):
    leet = {
        "A":"4", "B":"I3", "C":"[", "D":")", "E":"3", "F":"|=", "G":"&", "H":"#", "I":"1",
        "J":",_|", "K":">|", "L":"1", "M":"/\/\\", "N":"^/", "O":"0", "P":"|*", "Q":"(_,)", "R":"I2", 
        "S":"5", "T":"7", "U":"(_)", "V":"\/", "W":"\/\/", "X":"><", "Y":"j", "Z":"2", 
    }

    leet_text = ''
    for word in text:
        if(word.upper() in leet.keys()):
            leet_text += leet[word.upper()]
        else:
            leet_text += word
        
    return leet_text
print(translator_hack("Hola"))