from nltk.tokenize import sent_tokenize

def lines(a, b):
    """Return lines in both a and b"""
    textA = a.split('\n')
    textB = b.split('\n')
    repeat = []
    
    for line in textA:
        if line in textB:
            if line in repeat:
                continue
            repeat.append(line.rstrip())
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


#helper that transforms a string into a substring
def substringify(text, n):
    subs = []
    for x in range(len(text)):
        y = x + n
        temp = text[x:y]
        if temp in subs:
            continue
        subs.append(temp)
        x += n
        
    return subs

def substrings(a, b, n):
    """Return substrings of length n in both a and b"""

    textA = substringify(a, n)
    textB = substringify(b, n)
    repeat = []
    
    for i in textA:
        if len(i) < n or ' ' in i:
            continue
        if i in textB:
            if i in repeat:
                continue
            repeat.append(i)
    print(repeat)
    print(len(repeat))
    return repeat