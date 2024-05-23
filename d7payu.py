#libraries
import random

#functions
#function to split word into characters
def splitFunction(inputword):
    splitList=[]
    for character in inputword:
        splitList.append(character)
    return splitList
    
#function to replace all instances of matching letter
def replaceAllLetterMatch(inputLetter, updatedList):
    #check if the letter in the list
    if inputLetter in updatedList:
        return True
    else:
        return False      

#function to implement the actual game logic
def actualGameLogic(updatedList):
    #declaring the no of chances
    chances = 6
    lettersMatching = []

    #loop to playe
    while chances > 0:
        #take letter inputs from the user 
        inputLetter = input('guess a letter u think is in the word:\n').lower()

        #print(f'updated list before implementing letter replace function {updatedList}')
        #implementation of the letter replace function
        if replaceAllLetterMatch(inputLetter, updatedList):
            lettersMatching.append(inputLetter)

        if inputLetter not in updatedList:
            print(stages[chances])

        #update no of chances
        chances -= 1

    #returning the final updated list after all the chances
    return lettersMatching

#function to match the letters
def matchingLetter(lettersMatching, updatedList):
    print(f'updated list inside matching letter function: {updatedList}')
    print(f'letters matching inside matching letter function: {lettersMatching}')
    # updatedCombinedList = []
    deathCounter = 6
    for letter in updatedList:
        print(f'letter: {letter}')
        if letter in lettersMatching:
            continue
        else:
            updatedtempstring = letterReplace(letter, updatedList) 
            updatedList = splitFunction(updatedtempstring)
            #print(f'updatedtempstring: {updatedtempstring}')
            print(f'lose one attempt and the updated list is: {updatedList}')
            print(stages[deathCounter])
            deathCounter -= 1

    print(f'updated list inside matching letter function: {updatedList}')
    return updatedList

#function to replace letter in the matching letter function
def letterReplace(letter, updatedList):
    updatedString = ''.join(updatedList)
    updatedCombinedString = updatedString.replace(letter, '_')
    return updatedCombinedString

#function to check if the person won the game
def gameWonCheck(updatedCombinedList):
    if '_' in updatedCombinedList:
        return False
    else:
        return True

#implementation
#declaring ascii art for hangman
stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

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
print(f'list we are working on: {updatedList}')

#implementation of actual game logic
lettersMatching = []
lettersMatching = actualGameLogic(updatedList)
print(f'letters matching: {lettersMatching}')

#implementing creating final list of matched letter
updatedCombinedList = matchingLetter(lettersMatching, updatedList)

#checking if the person won the game
gameWonFLag = gameWonCheck(updatedCombinedList)
if gameWonFLag == True:
    print('You won')
else:
    print('You lose')