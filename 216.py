# Problem: Given a number in Roman numeral format, convert it to decimal.


def romToDec(rom):
    
    table = {"I": 1,"V": 5,"X": 10,"L": 50,"C": 100,"D": 500,"M": 1000}
    dec = 0
    
    for i in range(len(rom)):
        if i < len(rom)-1 and table[rom[i]] < table[rom[i+1]]:
            dec -= table[rom[i]]
        else:
            dec+= table[rom[i]]
    
    return dec



print(romToDec("MMMCMXCIX")) #3999 in decimal. Max number possible for the algorithm
