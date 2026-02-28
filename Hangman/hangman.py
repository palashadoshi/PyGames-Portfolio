import random
from collections import Counter
from words import someWords

someWords = someWords.split()  # split() handles all whitespace including newlines

EndGame = False
while EndGame == False:
    word = random.choice(someWords)


    print("Welcome to HANGMAN, by Palash Doshi!")
    for _ in word:
        print('_', end=' ')
    print()  # ← moved outside the for loop (was inside, printing newline after each underscore)
    print(f"The word has {len(word)} letters.")
    if len(word) >= 10:
        print("You've got a tricky one! Good luck.")

    letterGuessed = ''
    if len(word) < 10:
        chances = len(word) + 2
    elif len(word) >= 10:
        chances = len(word) + 4
    DidYouWin = False

    try:
        while chances > 0 and DidYouWin == False:
            print()

            try:
                guess = input('Enter a letter to guess: ').lower()
            except:
                print('Enter only a letter!')
                continue

            if not guess.isalpha():
                print('Enter only a letter!')
                continue
            elif len(guess) > 1:
                print('Enter only a single letter!')
                continue
            elif guess in letterGuessed:
                print('You already guessed that letter!')
                continue

            if guess in word:
                letterGuessed += guess * word.count(guess)
            else:
                print(f"'{guess}' is not in the word. You have {chances} chances left.")
                chances -= 1

            for char in word:
                if char in letterGuessed:
                    print(char, end=' ')
                else:
                    print('_', end=' ')
            print()  # ← added newline after displaying the word progress

            if Counter(letterGuessed) == Counter(word):
                print("\nCongratulations! You guessed the word:", word)
                DidYouWin = True
                break

        if chances <= 0 and Counter(letterGuessed) != Counter(word):  # ← moved outside while, inside try
            print('\nYou lost! The word was:', word)

    except KeyboardInterrupt:
        print('\nGame interrupted. Bye!')
        exit()

    Exit = input("Do you want to leave? Y/N ").strip().upper()
    if Exit == "Y":
        print("Bye!")
        break