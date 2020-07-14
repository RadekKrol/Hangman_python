###################################################
###                 Hangman                     ###
###################################################

print("H A N G M A N\n")
ask = input('Type "play" to play the game, "exit" to quit: ')

while ask not in ['play', 'exit']:
    ask = input('Type "play" to play the game, "exit" to quit: ')

if ask == 'play':
    import random

    list = ['python', 'java', 'kotlin', 'javascript']
    b = random.choice(list)

    word = set(b)

    string = len(b)*"-"
    guesses = []

    i=0
    while i <8:
        print("\n",string)
        a = input("Input a letter: ")
        if len(a) != 1:
            print("You should input a single letter")
            continue
        if not a.islower():
            print("It is not an ASCII lowercase letter")
            continue
        if a in guesses:
            print("You already typed this letter")
            continue
        if a in word:
            times = b.count(a)
            if times == 1:
                position = b.find(a)
                string = string[:position] + a + string[position+1:]
                guesses.append(a)
            elif times == 2:
                position1 = b.find(a)
                position2 = b.rfind(a)
                string = string[:position1] + a + string[position1+1:]
                string = string[:position2] + a + string[position2+1:]
                guesses.append(a)
        else:
            print("No such letter in the word")
            guesses.append(a)
            i += 1
        if string == b:
            print(string)
            print("You guessed the word!")
            print("You survived!")
            break

    if string == b:
        print(string)
        print("You guessed the word!")
        print("You survived!")
    else:
        print("You are hanged!")