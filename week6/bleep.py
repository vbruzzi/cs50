from cs50 import get_string
import sys


def main():
    #checks if there is more than 2 arguments
    if len(sys.argv) != 2:
        print("Usage: python bleep.py dictionary")
        sys.exit(1)
    
    dictionary = sys.argv[1]
    
    #Gets the string and splits it into a list
    getter = get_string("What message would you like to censor? ")
    check = getter.split(" ")
    
    i = 1
    for word in check: 
        if word in open(dictionary).read():
            print("*" * len(word), end="")
        else:
            print(word, end="")
        
        #prints a space if the last word isn't the last
        if i == len(check):
            print()
            break
        else:
            print(" ", end="")
        i += 1


if __name__ == "__main__":
    main()
