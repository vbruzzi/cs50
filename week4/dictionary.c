// Implements a dictionary's functionality
#define _GNU_SOURCE 1
#include <ctype.h>
#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>

#include "dictionary.h"

// Represents number of buckets in a hash table
#define N 26

// Represents a node in a hash table
typedef struct node
{
    char word[LENGTH + 1];
    struct node *next;
}
node;

// Represents a hash table
node *hashtable[N];

// Hashes word to a number between 0 and 25, inclusive, based on its first letter
unsigned int hash(const char *word)
{
    return tolower(word[0]) - 'a';
}

// Loads dictionary into memory, returning true if successful else false
bool load(const char *dictionary)
{
    // Initialize hash table
    for (int i = 0; i < N; i++)
    {
        hashtable[i] = NULL;
    }

    // Open dictionary
    FILE *file = fopen(dictionary, "r");
    if (file == NULL)
    {
        unload();
        return false;
    }

    // Buffer for a word
    char word[LENGTH + 1];


    // Insert words into hash table
    while (fscanf(file, "%s", word) != EOF)
    {
        int index = hash(word);
        node *tempWord = malloc(sizeof(node));
        if(!tempWord) {
            unload();
            return false;
        }
        strcpy(tempWord->word, word);
        tempWord->next = hashtable[index];
        hashtable[index] = tempWord;

    }

    // Close dictionary
    fclose(file);

    // Indicate success
    return true;
}

// Returns number of words in dictionary if loaded else 0 if not yet loaded
unsigned int size(void)
{
    int count = 0;
    for (int i = 0; i < N; i++) {
        node *currentVal = hashtable[i];
        while(currentVal != NULL) {
            currentVal = currentVal->next;
            count++;
        }
    }
    return count;
}

// Returns true if word is in dictionary else false
bool check(const char *word)
{
    char tempStr[strlen(word)];
    strcpy(tempStr, word);
    for (int i = 0; i < strlen(word); i++) {
        tempStr[i] = tolower(tempStr[i]);
    }
    int index = hash(word);
    node *temp = hashtable[index];
    if(strcmp(temp->word, tempStr) == 0) {
            return true;
    }
    while(temp->next != NULL) {
        temp = temp->next;
        if(strcmp(temp->word, tempStr) == 0) {
            return true;
        }
    }
    return false;

}

// Unloads dictionary from memory, returning true if successful else false
bool unload(void)
{
    for (int i = 0; i < N; i++)
    {
        node *cursor = hashtable[i];
        while(cursor != NULL) {
            node *temp = cursor;
            cursor = cursor->next;
            free(temp);
        }
    }
    return true;

}
