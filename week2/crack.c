#include <stdio.h>
#include <string.h>
#include <crypt.h>
#include <math.h>
#include <cs50.h>
 
#define MAX_KEY_LENGTH 5
 
int main(int argc, string argv[])
{
    if(argc != 2) {
        printf("Usage: ./crack hash");
        return 0;
    }
    char alphabet[] = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVXWYZ\0";
    char *hash1 = argv[1];
    int len = strlen(alphabet);
 
    for (int key_length = 1; key_length <= MAX_KEY_LENGTH; key_length++) {
 
        char key[key_length + 1];
        key[key_length] = '\0';
        for (int i = 0; i < key_length; i++) key[i] = alphabet[0];
 
        for (int count = 0; count < pow(len, key_length); count++) {
 
            if (strcmp(hash1, crypt(key, "50")) == 0) {
                printf("%s\n", key);
                goto fim;
            }
 
            int cur;
            for (cur = 0; alphabet[cur] != key[key_length-1]; cur++);
            key[key_length-1] = alphabet[cur + 1];
            
            for (int i = key_length - 1; i > 0; i--) {
                if (key[i] == alphabet[len-1]) {
                    key[i] = alphabet[0];
                    for (cur = 0; alphabet[cur] != key[i-1]; cur++);
                    key[i-1] = alphabet[cur + 1];
                }
            }        
        }
    }
    fim:
    return 0;
}
