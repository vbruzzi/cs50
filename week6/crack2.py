#Crack implemented with itertools

import crypt
import sys
import itertools

alphabet = list("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVXWYZ")
maxKeyLength = 5
salt = "51"

def main():
    hash = sys.argv[1]
    for keyLength in range(maxKeyLength+1):
        
        for guess in itertools.product(alphabet, repeat=keyLength):
            tempGuess = ''.join(guess)
            if(crypt.crypt(tempGuess, salt) == hash):
                print(tempGuess)
                return True
                
            
main()