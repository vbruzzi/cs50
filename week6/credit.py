from cs50 import get_string


#Luhn's algorithm
def luhn(cardNum, company):
    cardLength = len(cardNum) - 2
    tempVal = 0
    tempCardNum = list(cardNum)
    while cardLength >= 0:
        tempCardNum[cardLength] = ''
        product = int(cardNum[cardLength]) * 2
        if product >= 10:
            tempVal += product % 10 + 1
        else:
            tempVal += product
        cardLength -= 2
        
    tempCardNum = ''.join(tempCardNum)
    for j in range(len(tempCardNum)):
        tempVal += int(tempCardNum[j])

    if tempVal % 10 == 0:
        print(company)
        return True
    
    print("INVALID")
    return False
        
        
#Checks size/card type and applies luhn's algorithm to it
def validation(cardNum):
    #VISA CASE
    if int(cardNum[0]) == 4 and (len(cardNum) == 13 or len(cardNum) == 16):
        luhn(cardNum, "VISA")
    
    #MASTERCARD CASE
    elif cardNum[0:2] in {"51", "52", "53", "54", "55"} and len(cardNum) == 16:
        luhn(cardNum,"MASTERCARD")
        
    #AMEX CASE
    elif cardNum[0:2] in {"34", "37"} and len(cardNum) == 15:
        luhn(cardNum, "AMEX")
    
    else:
        print("INVALID")
        return False
        

def main():
    while True:
        cardNum = get_string("Number: ")
        if cardNum.isdigit():
            break
    validation(cardNum)
    
    
    
main()