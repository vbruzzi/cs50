#import <stdio.h>
#import <cs50.h>
#import <math.h>

long cardNum;
int numLength;

int firstDigits(difference) {
    int x = cardNum/pow(10, numLength-difference);
    return x;
}

//Checks the validity of the card
int cardVal(int length, long num) {
    //makes the int into an array
    int arr[length];
    for(int i = 0; i < length; i++) {
        arr[i] = num % 10;
        num /= 10;
    }
    //Luhns Algorithm
    int total = 0;
    for(int i = 1; i < length; i += 2) {
        int numProduct = arr[i]*2;
        if(numProduct > 9) {
            total += numProduct % 10;
            numProduct /= 10;
        }
        total += numProduct;
    }
    for(int i = 0; i < length; i += 2) {
        total += arr[i];
    }
    for(int i = 0; i < length; i++){
    }
   return total % 10;
}



int main(void) {
    while(numLength != 13 && numLength != 15 && numLength != 16){
        numLength = 0;
        cardNum = get_long("What's your card number? ");
        long tempNum = cardNum;
        while(tempNum > 0) {
            tempNum /= 10;
            numLength++;
        }
    }
    
    int cardModulo = cardVal(numLength, cardNum);    
    switch(numLength) {
        case 13: //VISA
            if(firstDigits(1) != 4 || cardModulo != 0){
                printf("INVALID\n");
                break;
            }
            printf("VISA\n");
            break;
        case 15://AMEX
            if((firstDigits(2) != 34 && firstDigits(2) != 37) || cardModulo != 0) {
                printf("INVALID\n");
                break;
            }
            printf("AMEX\n");
            break;
        case 16://MASTERCARD AND VISA
           if(cardModulo == 0) {
               if(firstDigits(1) == 4) {                   
                   printf("VISA\n");
                   break;
               }
               else if(firstDigits(2) > 50 && firstDigits(2) < 56) {
                   printf("MASTERCARD\n");
                   break;
               }
           }
            printf("INVALID\n");
            break;
    }
}
