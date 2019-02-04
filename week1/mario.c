//prints out a pyramid made with #

#include <cs50.h>
#include <stdio.h>

int main(void)
{
    //prompt user for pyramid height
    printf("What is the height of the pyramid? ");
    int height = get_int();
    while(height > 23 || height < 0)
    {
        if(height > 23)
        {
            printf("Height cannot be more than 23.");
        }
        if(height < 0)
        {
            printf("Height cannot be less than 0.");
        }
        height = get_int();
    }
    //amount of blocks per level
    int blocks = 1;
    //iterates levels
    for(int i = height; i > 0; i--)
    {
        //spaces
        for(int x = height; x > 1; x--)
        {
            printf(" ");
        }
        //blocks
        for(int z = blocks*2; z > 0; z--)
        {
            //first line right side
            if(z == 1 && z == blocks)
                printf("  #\n");
            //middle block with the space dividing it
            else if(z == blocks)
                printf("  #");
            //last block with new line
            else if(z == 1)
                printf("#\n");
            //normal block
            else
                printf("#");
        }
        //adds a block/level and removes a space
        blocks++;
        height--;
    }
}
