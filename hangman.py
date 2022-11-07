import random


def hide(word):
    word2 = list()
    for i in range(len(word)):
        word2.append("-")
    return word2


latin = "qwertyuiopasdfghjklzxcvbnm"
menu_0 = 'Type "play" to play the game, "results" to show the scoreboard, and "exit" to quit:'
msg_0 = "Input a letter:"
msg_1 = "That letter doesn't appear in the word."
msg_2 = "Thanks for playing!"
msg_3 = "No improvements."
msg_4 = "You guessed the word "
msg_5 = "You survived!"
msg_6 = "You lost!"
err_0 = "Please, input a single letter."
err_1 = "Please, enter a lowercase letter from the English alphabet."
err_2 = "You've already guessed this letter."

example_list = ['python', 'java', 'swift', 'javascript']

won_games = 0
lost_games = 0

print("H A N G M A N")
while True:
    print(menu_0)
    choose = input()
    if choose == "play":
        attempts = 8
        word = example_list[random.randint(0, 3)]
        hidden = hide(word)
        word2 = list(word)
        guessed = list()
        while True:
            print("".join(hidden))
            print(msg_0)
            guess = input()
            if len(guess) != 1:
                print(err_0)
                continue
            if guess not in latin:
                print(err_1)
                continue
            if guess in guessed:
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
                attempts -= 1
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
