from nltk.tokenize import sent_tokenize

def lines(a, b):
    """Return lines in both a and b"""
    
    repeat = []
    
    for line in a:
        if line in b:
            if line in repeat:
                continue
            repeat.append(line.rstrip())
        
    print(repeat)
    
    return repeat


def sentences(a, b):
    """Return sentences in both a and b"""
    
    textA = sent_tokenize(a)
    textB = sent_tokenize(b)
    repeat = []
    
    for sentence in textA:
        if sentence in textB:
            if sentence in repeat:
                continue
            repeat.append(sentence)
            
    return repeat


def substringify(string, n):
    substrings = []
    for x in string:
        y = x + n
        temp = string[x:y]
        x += n
    print(substrings)
    return substrings

def substrings(a, b, n):
    """Return substrings of length n in both a and b"""

    for x in 
    for substring in 
    return []

fileA = open('inputs/LittlePrince_WoodsTranslation.txt')
fileB = open('inputs/LittlePrince_HowardTranslation.txt')

sentences(fileA.read(), fileB.read())

fileA.close()
fileB.close()