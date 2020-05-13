# Game of hangman
# Can use a hint system to get a synonym for the given word, but it takes away a life


import string, wordlist, random, os

word = random.choice(wordlist.words).upper()

def list_duplicates_of(seq,item):
    start_at = -1
    locs = []
    while True:
        try:
            loc = seq.index(item,start_at+1)
        except ValueError:
            break
        else:
            locs.append(loc)
            start_at = loc
    return locs

def clear():
    os.system("cls")

hangmanPic = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
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
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

wordIndex = list(word)
wordChosen = []

for x in range(len(wordIndex)): # This loop generates the list with the hashes based on the length of the random string
    wordChosen.append("#")

blocking = "\n\n\n\n\n\n\n\n"
livesLeft = 7
i = 0
availableLetters = list(string.ascii_uppercase) # Letters still to use

# print(word)

# print("The word is:")
# print(*wordChosen)

# print("\nYou have the following letters available:")
# print(*availableLetters)

while livesLeft > 0 or wordChosen != wordIndex:
    
    # if lettersChosen == word:
    #     print("")
    # print("\n")
    print(*wordChosen)
    print("")
    print(*availableLetters)
    # print("")
    # # print("You have "+str(livesLeft)+" lives left. ")

    letterChoice = input("\nPick a letter. ").upper()

    
    if len(letterChoice) > 1:
        print("Too many characters. Please select just one. ")
        input("PRESS ENTER TO CONTINUE. ")
        clear()
        continue

    # while len(letterChoice) > 1:
    #     letterChoice = input("Too many characters. Please select one. ").upper()

    if letterChoice in wordIndex: # If the letter is in the word...
        
        if letterChoice not in availableLetters: # Checks to see if a letter has already been used. If it has, it loops back to the top
            print("You have already tried "+letterChoice+". Please try again. ")
            input("PRESS ENTER TO CONTINUE. ")
            clear()
            continue
        
        letterIndex = availableLetters.index(letterChoice) # Checks the index the letter is at and replaces the value at that index with a #
        availableLetters[letterIndex] = "#"
        
        if letterChoice in wordIndex:
            x_LetterIndex = list_duplicates_of(wordIndex, letterChoice)    
            for x in x_LetterIndex:
                wordChosen[x] = letterChoice

        print("Success. The letter "+letterChoice+" is in the word.\n")
        print(*wordChosen)
        if wordChosen == wordIndex:
                print("\nYou won.\n")
                input("Press enter to exit. ")
                break
        print("")
        input("PRESS ENTER TO CONTINUE. ")
        clear()

    
    elif letterChoice not in wordIndex: # If the letter isn't in the word...
        
        if letterChoice not in availableLetters:
            print("'"+letterChoice+"'"+" is not on your list of available characters. Please try again. ")
            input("PRESS ENTER TO CONTINUE. ")
            clear()
            continue

        letterIndex = availableLetters.index(letterChoice) # Checks the index the letter is at and replaces the value at that index with a #
        availableLetters[letterIndex] = "#"
        
        
        livesLeft-=1
        if livesLeft > 1:
            print("Failure. The letter "+letterChoice+" is not in the word. You have "+str(livesLeft)+" lives left. ")
        elif livesLeft == 1:
            print("Failure. The letter "+letterChoice+" is not in the word. You have "+str(livesLeft)+" life left. ")
        else:
            print("Failure. The letter "+letterChoice+" is not in the word. You have "+str(livesLeft)+" lives left. ")
        print(hangmanPic[i])
        i+=1
        if livesLeft == 0:
            print("")
            print("You have lost. The word was "+word.lower()+".\n")
            input("Press enter to exit. ")
            break
        else:
            # print("You have the following letters left:")
            # print(*availableLetters)
            # print(*wordChosen.values())
            input("PRESS ENTER TO CONTINUE. ")
            clear()




# if letterChoice in word:
#     print("Success\n"+letterChoice+" is a correct letter")
#     letterIndex = availableLetters.index(letterChoice)
#     availableLetters[letterIndex] = "#"
# print(*availableLetters)