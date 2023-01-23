import random
import linecache
import time


def hide(word):
    word2 = list()
    for i in range(len(word)):
        if word[i] == " ":
            word2.append(" ")
        else:
            word2.append("-")
    return word2


latin = "qwertyuiopasdfghjklzxcvbnm"
menu_0 = 'Type "play" to play the game, "results" to show the scoreboard, and "exit" to quit:'
msg_0 = "Input a letter:"
msg_1 = "That letter doesn't appear in the word."
msg_2 = "Thanks for playing!"
msg_3 = "Attempts left: "
msg_4 = "You guessed the word "
msg_5 = "You survived!"
msg_6 = "You lost!"
err_0 = "Please, input a single letter."
err_1 = "Please, enter a lowercase letter from the English alphabet."
err_2 = "You've already guessed this letter."

won_games = 0
lost_games = 0
attempts = 8
print("Welcome to ...")
time.sleep(0.9)
print("H A N G M A N - animal edition")
time.sleep(0.7)
while True:
    print(menu_0)
    choose = input()
    if choose == "play":
        attempts = 8
        true_attempts = attempts
        line = random.randint(1, 1648)
        word = linecache.getline('animals.txt', 1648, module_globals=None)
        word = word.replace('\n', '')
        word = word.lower()
        hidden = hide(word)
        word2 = list(word)
        guessed = list()
        while True:
            time.sleep(0.5)
            print("".join(hidden))
            time.sleep(0.5)
            print(msg_0)
            guess = input()
            if len(guess) != 1:
                time.sleep(0.5)
                print(err_0)
                continue
            if guess not in latin:
                time.sleep(0.5)
                print(err_1)
                continue
            if guess in guessed:
                time.sleep(0.5)
                print(err_2)
                continue
            elif guess in word2:
                x = word2.count(guess)
                while x > 0:
                    ind = word2.index(guess)
                    hidden[ind] = guess
                    word2[ind] = "!"
                    x -= 1
            else:
                print(msg_1)
                time.sleep(0.5)
                attempts -= 1
                print(msg_3 + str(attempts))
            if attempts == 0:
                win = False
                break
            if "".join(hidden) == word:
                win = True
                break
            guessed.append(guess)
        if win:
            print(msg_4 + "".join(hidden) + "!")
            print(msg_5)
            won_games += 1
        else:
            print(msg_6)
            lost_games += 1
        continue
    elif choose == "results":
        print("You won: " + str(won_games) + " times")
        print("You lost: " + str(lost_games) + " times")
        continue
    elif choose == "exit":
        break
    else:
        continue
