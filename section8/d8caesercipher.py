#importing libraries
import math
import section8.d8art as d8art

#function declarations
def greet():
    print('hello, how are you')
    print('i am riyaz kaleem')
    print('we are inside greet function')

def greetPerson(personName):
    print('hello, we are inside function with arguments')
    print(f'person name is = {personName}')

def greetPersonFullname(firstName, lastName):
    print('hello, we are inside function with arguments')
    print(f'person full name is = {firstName} {lastName}')

def paint_calc(height, width, cover):
  noOfCans = (height * width) / cover
  noOfCansInt = int(math.ceil(noOfCans))
  print(f"You'll need {noOfCansInt} cans of paint.")

def prime_checker(number):
  primeList = []
  for n in range(1, number+1):
    if number%n == 0:
      primeList.append(n)

  if len(primeList)>2:
    print("It's not a prime number.")
  else:
    print("It's a prime number.")

def caeserCipher(text, shift, alphabet, direction):
    print(d8art.logo)
    originalList = list(text)
    # print(f"original text = {text}")
    # print(f"original list: {originalList}")
    # originalListLen = len(originalList)

    modifiedAlphabet = []
    for i in alphabet:
        modifiedAlphabet.append(i)
    for i in alphabet:
        modifiedAlphabet.append(i)
    # print(f"modified list: {modifiedAlphabet}")
   
    updatedList = []
    for item in originalList:
        if item == ' ':
            updatedList.append(item)
        else:
            itemIndex = alphabet.index(item)
            if direction == 'encode':
                newItemIndex = itemIndex+shift
            else:
                newItemIndex = itemIndex-shift
            newItem = modifiedAlphabet[newItemIndex]
            updatedList.append(newItem)
    updatedText = ''.join(updatedList)
    print(f"updated text = {updatedText}")


# def encrypt(text, shift, alphabet):
#     originalList = list(text)
#     print(f"original text = {text}")
#     # print(f"original list: {originalList}")
#     # originalListLen = len(originalList)

#     modifiedAlphabet = []
#     for i in alphabet:
#         modifiedAlphabet.append(i)
#     for i in alphabet:
#         modifiedAlphabet.append(i)
#     # print(f"modified list: {modifiedAlphabet}")
   
#     updatedList = []
#     for item in originalList:
#         if item == ' ':
#             updatedList.append(item)
#         else:
#             itemIndex = alphabet.index(item)
#             newItemIndex = itemIndex+shift
#             newItem = modifiedAlphabet[newItemIndex]
#             updatedList.append(newItem)
#     updatedText = ''.join(updatedList)
#     print(f"updated text = {updatedText}")

# def decrypt(text, shift, alphabet):
#     originalList = list(text)
#     print(f"original text = {text}")
#     # print(f"original list: {originalList}")
#     # originalListLen = len(originalList)

#     modifiedAlphabet = []
#     for i in alphabet:
#         modifiedAlphabet.append(i)
#     for i in alphabet:
#         modifiedAlphabet.append(i)
#     # print(f"modified list: {modifiedAlphabet}")
   
#     updatedList = []
#     for item in originalList:
#         if item == ' ':
#             updatedList.append(item)
#         else:
#             itemIndex = alphabet.index(item)
#             newItemIndex = itemIndex-shift
#             newItem = modifiedAlphabet[newItemIndex]
#             updatedList.append(newItem)
#     updatedText = ''.join(updatedList)
#     print(f"updated text = {updatedText}")
        
#implementation
print('implementation of greet function')
greet()
print('\n')

print('implementation of greet function with single argument')
personName = 'riyaz'
greetPerson(personName)
print('\n')

print('implementation of greet function with multiple positional arguments')
firstName = 'riyaz'
lastName = 'kaleem'
greetPersonFullname(firstName, lastName)
print('\n')

print('implementation of greet function with multiple keyword arguments')
firstName = 'riyaz'
lastName = 'kaleem'
greetPersonFullname(lastName = 'riyaz', firstName = 'kaleem')
print('\n')

print('implementation of paint cans count function in auditorium')
test_h = int(input('enter height of wall')) # Height of wall (m)
test_w = int(input('enter width of wall')) # Width of wall (m)
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)
print('\n')

print('implementation of prime number checker')
n = int(input('enter number to check for primeness')) # Check this number
prime_checker(number=n)
print('\n')

print('implementation of caeser cipher')
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))
caeserCipher(text, shift, alphabet, direction)