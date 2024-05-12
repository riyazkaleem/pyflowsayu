#importing the libraries
import random

#defining user defined functions
#split function
def splitFunction(inputword):
    splitList=[]
    for character in inputword:
        splitList.append(character)
    return splitList

#implementation
#from a group of words selecting a word
listOfWords = ['my', 'name', 'is', 'riyaz', 'kaleem']
selectedWord = random.choice(listOfWords)
print(f'selectedWord: {selectedWord}')

#take letter inputs from the user and check if the letter is in the chosen word
inputLetter = input('guess a letter u think is in the word:\n').lower()

#checking for letter in word and updating the list with each letter position compared
selectedWordList = splitFunction(selectedWord)
print(f'selected word list: {selectedWordList}')
for letter in selectedWordList:
    if (inputLetter == letter):
        print(f'match')
    else:
        print(f'no match')
