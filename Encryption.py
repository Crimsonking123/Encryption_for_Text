from bindec import*
#This function converts characters to base 64 encoded binary
def charToBin(c):
    c = str(c)
#Conversion should be done to enable use of ASCII in built functions for base64 encoding
#Check if character is alphabetic to loop over the sequence and convert to base64 encoding
    if c.isalpha() == True:
        if c.isupper() == True:
            setform = ord(c) - 65
        else:
            setform = ord(c) - 71
#Check if character is numeric to loop over the sequence and convert to base64 encoding
    if c.isnumeric() == True:
        setform = ord(c) + 4
#Repeat the process with the special characters
    else:
        if c == "+":
            setform = 62
        if c == "/":
            setform = 63
    return decToBin(setform)
#This program converts base 64 encoded binary characters to their representative characters
def binToChar(b):
    b = binToDec(b)
#Using ASCII tools - chr to convert the converted numbers to their actual characters. 
    if b != 62 and b!= 63:
#Upper alphabetic,lower alphabetic and numbers
        if b <= 25:
            b += 65
        elif b <= 51:
            b += 71
        else:
            b -= 4
#Special characters
    else:
        if b == 62:
            b = 43
        if b == 63:
            b = 47
    return chr(b)
#Convert a string of characters to binary code using the charToBin method
def strToBin(s):
    lst = []
    lst1 = []
    for i in s:
        lst.append(charToBin(i))
    for i in range(0,len(lst)):
        for x in range(0,6):
            lst1.append(lst[i][x])
    return lst1
#Convert binary list to a string of characters
def binToStr(b_list):
    str1 = ""
    x,y = 0,6
#Iterate with a count of 6 so the slice of 6 bits is maintained
    for i in range(0,len(b_list),6):
        char = binToChar(b_list[x:y])
        str1 += char
        x,y = x+6,y+6
    return str1
#This function generates an LSFR from a seed [N,k]
def generatePad(seed,k,l):
    lst1, N = [], len(seed)
#Reverse the list so generating is easier
    seed.reverse()
#Add the leftmost number for each iteration to the LSFR
    for i in range(l):
        if seed[k-1] + seed[N-1] != 2:
            lst1.append(seed[k-1] + seed[N-1])
        else:
            lst1.append(0)
        seed = seed[0:len(seed)-1]
        seed.insert(0,lst1[i])
    return lst1
#This function encrypts a message as a cipher text
def encrypt(message,seed,k):
    cipher = []
    LSFR = generatePad(seed,k,len(message)*6)
    message = strToBin(message)
#Use XOR logic to encrypt the message with the LSFR generated from the seed
    for i in range(len(message)):
        if message[i] + LSFR[i] != 2:
            cipher.append(message[i] + LSFR[i])
        else:
            cipher.append(0)
    cipher = binToStr(cipher)
    return cipher

def main():   
    print(binToChar([0,0,0,1,1,0]))
    print("Converted Base 64 encoding: ",strToBin("sausage"))
    print("Converted string: ",binToStr([1, 0, 1, 0, 0, 1, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 1, 0, 1, 0, 1, 1, 1, 1, 0]))
    print("Generated LSFR: ",generatePad([1,0,0,0,1,1,0,0,1,0],8,20))
    Cipher = encrypt("WhenSeagullsFollowTheTrawlerItIsBecauseTheyThinkSardinesWillBeThrownIntoTheSea",[1,0,0,0,1,1,0,0,1,0],8)
    print("Ciphered Text: " + encrypt("WhenSeagullsFollowTheTrawlerItIsBecauseTheyThinkSardinesWillBeThrownIntoTheSea",[1,0,0,0,1,1,0,0,1,0],8))
    print("Deciphered Text: " + encrypt(Cipher,[1,0,0,0,1,1,0,0,1,0],8))

main()















