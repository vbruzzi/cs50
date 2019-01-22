#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>
#include <cs50.h>


int main(int argc, string argv[])
{ 
    if(argc < 2 || argc > 2) {
       printf("Usage: ./vigenere keyword\n");
       return 1;
    }
    
    string key = argv[1];
    
    
    //keeps track of the position in the key
    int keyIndex = 0;
    int keySize = strlen(key);
    
    for(int i = 0; i < keySize; i++) {
        if(isdigit(key[i])) {
           printf("Usage: ./vigenere keyword\n");
           return 1;
        }
    }
    
    string plainText = get_string("plaintext: ");
    
    //how many characters in the string
    int iterations = strlen(plainText);
    
    //creates a copy of the plaintext inside cyphertext
    char cypherText[iterations];
    strcpy(cypherText, plainText);   

    //makes the keyword all lowercase
    for(int i = 0; i < keySize; i++) {
        key[i] = tolower(key[i]) - 97;
    }
    for (int i = 0; i < iterations; i++) {
        //goes back to the beginning of the keyword
        if(keyIndex == keySize) {
            keyIndex = 0;
        }
        if(strncmp(&cypherText[i], " ", 1) == 0 || cypherText[i] < 65){
            continue;
        }
        
        int valid = cypherText[i] + key[keyIndex];
        
        if((isupper(cypherText[i]) && valid > 90) || (islower(cypherText[i]) && valid > 122)) {
            cypherText[i] -= 26;
        }
        
        char cypherChar = cypherText[i] + key[keyIndex];
        
        cypherText[i] = cypherChar;
        keyIndex++;
    }
    
    printf("ciphertext: %s\n", cypherText);
}
