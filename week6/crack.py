#direct port of crack.c to python
#NOT THE BEST SOLUTION FOR THIS PROBLEM SET IN PYTHON
#CHECK crack2.py

import crypt
import sys

alphabet = list("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVXWYZ")
maxKeyLength = 5
salt = "50"
alphabetLen = len(alphabet)


def main():
    key = []
    hash = sys.argv[1]
    for keyLength in range(maxKeyLength):
        
        #sets the list to 'a' 
        key = []
        for j in range(keyLength):
            key.append(alphabet[0])
            
        print(key)
        
        for count in range (pow(alphabetLen, keyLength)):
            if crypt.crypt(''.join(key)) == hash:
                print("The password is: ", hash)
                return True
                
            if keyLength > 0:
                cur = 0
                while key[keyLength-1] != alphabet[cur]:
                    cur += 1
                if cur == 51:
                    cur = 0
                key[keyLength-1] = alphabet[cur+1]
                
                
                n = keyLength-1
                while n > -1:
                    if key[n] == alphabet[keyLength-1]:
                        key[n] == alphabet[0]
                        cur = 0
                        while key[n-1] != alphabet[cur]:
                            cur += 1
                        key[n-1] = alphabet[cur+1]
                    n -= 1
                    
                
                
                
                print(key, keyLength)
                
                
                
                
main()