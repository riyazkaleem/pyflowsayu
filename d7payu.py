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
# def letterCheckFunction(inputLetter, selectedWord):
#     if inputLetter in selectedWord:
#         return True
#     else:
#         return False
    
#function to prepare list of appearence of checked character
# def updatingCorrectList(inputLetter, selectedWord, updatedList):
#     for index in range(len(selectedWord)):
#         if inputLetter == selectedWord[index]:
#             updatedList[index] = inputLetter
#         else:
#             continue
#     return updatedList

#function to check if all the characters are filled
# def checkForUnderscores(finalPrintList):
#     if '_' in finalPrintList:
#         return True
#     else:
#         return False
    
#function to replace all instances of matching letter
def replaceAllLetterMatch(inputLetter, updatedList):
    #game of replacing correct underscores
    counter = 0

    # for letter in updatedList:
    #     #check if all characters are filled
    #     # underscoreCheckFlag = checkForUnderscores(finalPrintList)
    #     # if underscoreCheckFlag == True:
    #     #     #assigning the correct word length to the correct length counter
    #     #     correctLengthCounter = selectedWordLength
    #     #     #checking the letter is in the word
    #     #     letterInWordFlag = letterCheckFunction(inputLetter, selectedWord)
    #     #     #printing the checked letter
    #     #     finalPrintList = updatingCorrectList(inputLetter, selectedWord, updatedList) 

    #     #logic function implementation for replacing matched letter with word and others with an underscore
    #     if counter < len(updatedList):
    #         if letter == inputLetter:
    #             counter += 1 
    #             # print(updatedList)
    #             continue 
    #         else:
    #             updatedList[counter] = '_'
    #             counter += 1
    #             # print(updatedList)

    #check if the letter in the list
    if inputLetter in updatedList:
        return True
    else:
        return False

    #returning final updated list
    return updatedList       

#function to implement the actual game logic
def actualGameLogic(updatedList):
    #declaring the no of chances
    chances = 6
    lettersMatching = []

    #loop to play
    while chances > 0:
        #take letter inputs from the user 
        inputLetter = input('guess a letter u think is in the word:\n').lower()

        print(f'updated list before implementing letter replace function {updatedList}')
        #implementation of the letter replace function
        if replaceAllLetterMatch(inputLetter, updatedList):
            lettersMatching.append(inputLetter)

        #update no of chances
        chances -= 1

    #returning the final updated list after all the chances
    return lettersMatching

#function to match the letters
def matchingLetter(lettersMatching, updatedList):
    print(f'updated list inside matching letter function: {updatedList}')
    print(f'letters matching inside matching letter function: {lettersMatching}')
    updatedCombinedList = []
    for letter in updatedList:
        print(f'letter: {letter}')
        if letter in lettersMatching:
            continue
        else:
            updatedtempstring = letterReplace(letter, updatedList) 
            updatedList = splitFunction(updatedtempstring)
            print(f'updatedtempstring: {updatedtempstring}')
            print(f'updatedlist: {updatedList}')

    print(f'updated list inside matching letter function: {updatedList}')
    return updatedList

#function to replace letter in the matching letter function
def letterReplace(letter, updatedList):
    updatedString = ''.join(updatedList)
    updatedCombinedString = updatedString.replace(letter, '_')
    return updatedCombinedString

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
for letter in selectedWordList:
    updatedList.append(letter)
# finalPrintList=updatedList
print(f'updated list: {updatedList}')

#implementation of actual game logic
lettersMatching = []
lettersMatching = actualGameLogic(updatedList)
print(f'letters matching: {lettersMatching}')

#implementing creating final list of matched letter
updatedCombinedList = matchingLetter(lettersMatching, updatedList)
print(f'updated list: {updatedCombinedList}')

#check if the person lost or won
# if "_" in updatedCombinedList:
#     print("You Lose")
# else:
#     print("You Win")

# #final test print statement
# print(f'updated list: {updatedList}')