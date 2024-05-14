#libraries
import random

#functions
#function to split word into characters
def splitFunction(inputword):
    splitList=[]
    for character in inputword:
        splitList.append(character)
    return splitList

#function to check if the letter is in the word
def letterCheckFunction(inputLetter, selectedWord):
    if inputLetter in selectedWord:
        return True
    else:
        return False
    
#function to prepare list of appearence of checked character
def updatingCorrectList(inputLetter, selectedWord, updatedList):
    for index in range(len(selectedWord)):
        if inputLetter == selectedWord[index]:
            updatedList[index] = inputLetter
        else:
            continue
    return updatedList

#function to check if all the characters are filled
def checkForUnderscores(finalPrintList):
    if '_' in finalPrintList:
        return False
    else:
        return True

#implementation
#from a group of words selecting a word
listOfWords = ['my', 'name', 'is', 'riyaz', 'kaleem']
selectedWord = random.choice(listOfWords)
#print(f'selectedWord: {selectedWord}')

#converting the selected word into a list
selectedWordList = splitFunction(selectedWord)
#print(f'selected word list: {selectedWordList}')

#creating a blank string with same characters as selected word
selectedWordLength = len(selectedWord)
updatedList=[]
for i in range(selectedWordLength):
    updatedList.append('_')
finalPrintList=updatedList
#print(f'updated list: {updatedList}')

#game of replacing correct underscores
for counter in range(selectedWordLength):
    #check if all characters are filled
        underscoreCheckFlag = checkForUnderscores(finalPrintList)
        
    if underscoreCheckFlag == True:
        #take letter inputs from the user 
        inputLetter = input('guess a letter u think is in the word:\n').lower()
        
        #assigning the correct word length to the correct length counter
        correctLengthCounter = selectedWordLength

        #checking the letter is in the word
        letterInWordFlag = letterCheckFunction(inputLetter, selectedWord)

        #printing the checked letter
        finalPrintList = updatingCorrectList(inputLetter, selectedWord, updatedList)

    
        

#final test print statement
print(f'updated list: {finalPrintList}')