import math


def filterfunc(variable):

    if ((variable<='z'and variable>='a')or(variable<='Z'and variable>='A')):
        return False
    else:
        return True
text=input()
sequence = [char for char in text]
filteredLength = len(list(filter(filterfunc, sequence)))
nOfLetters=len(text)-filteredLength
nOfWords=len(text.split())
nOfSentences=text.count('.')+text.count('!')+text.count('?')
L=nOfLetters/nOfWords*100
S=nOfSentences/nOfWords*100
grade=round(0.0588 * L - 0.296 * S - 15.8)
if(grade>16):
    print("Grade 16+")
elif(grade<1):
    print("Before Grade 1")
else:
    print("Grade",grade)

