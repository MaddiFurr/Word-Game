import requests
import os
import time

play = True
while play:
    # Word URL
    URL = 'https://random-word-api.herokuapp.com/word?number=1'
    
    # Setup game variables
    guesses = ""
    wrong = 0
    failed = 0
    fill = ""
    
    def get_word(api):
        # Get our word request
        r = requests.get(url = api)
        data = r.json()
        return data

    word = str(get_word(URL))

    os.system('cls' if os.name == 'nt' else 'clear')
    print("Welcome to Word Game!\n*************\nTry to find the word on letter at a time\nYou have as many guesses as there are letters in the word\nGood Luck!")
    time.sleep(5)
    os.system('cls' if os.name == 'nt' else 'clear')

    for char in "'[]":
        word = word.replace(char, "")

    print("The word has ", len(word), " letters\n")
    while wrong < len(word):
        fill = ""
        failed = 0
        for char in word:
            if char in word:
                
                if char in guesses:
                    fill += (char + " ")
                else:
                    fill += "_ "
                failed += 1
        
        
        if fill.replace(" ","") == str(word):
            answer = input("You found the word!: " + word + "\n\nThanks For Playing!\n\n Continue? (y/n)")
            if answer not in ('y', 'n'):
                print("Not a valid answer")
            if answer == 'y':
                os.system('cls' if os.name == 'nt' else 'clear')
                break
            else:
                play = False
                break
                   
        
        
        
        print("\n" + fill)

        guess = input(str("\nWRONG GUESSES: " + str(wrong) + "/" + str(len(word)) + " | guess a letter: ")).lower()
        os.system('cls' if os.name == 'nt' else 'clear')
        if guess not in word:
            wrong += 1
            print("That letter is not in the word\n")
        if len(guess) > 1:
            print("You can only guess one letter at a time\n")
        else:
            guesses += guess

        if wrong == len(word):
            answer = input("You didn't find the word. It was: " + word + "\n\nThanks For Playing!\n\n Continue? (y/n)")
            if answer not in ('y', 'n'):
                print("Not a valid answer")
            if answer == 'y':
                os.system('cls' if os.name == 'nt' else 'clear')
                break
            else:
                play = False
                break
