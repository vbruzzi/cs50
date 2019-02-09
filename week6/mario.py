from cs50 import get_int

def main():
    while True:
        height = get_int("Height: ")
        if height <= 8 and height >= 1:
            break
    
    spaces = height - 1
    hashes = 1
    gap = 2
    for i in range(height):
        print(" " * spaces, end="")
        spaces -= 1
        print("#" * hashes, end="")
        print(" " * gap, end="")
        print("#" * hashes, end="")
        hashes += 1
        print("")
        
main()