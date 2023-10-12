import os
import random 
from colors import bcolors



while True:
    os.system('cls')
    print(bcolors.CYAN + """ 
      =============================
      G I S S A  T A L E T  1 - 100
      ====== Du har 7 försök ======
      """)
    print(bcolors.DEFAULT)

    




    while True: 
        secret_numer = random.randint(1,100)
        guesses = 0

        while guesses <=7:
            try:
                guess =int(input("gissa det hemliga talet "))
            except ValueError: 
                print (bcolors.RED + "du måste skriva ett riktigt tal - kör igen \n")
                print(bcolors.DEFAULT)
                continue

            guesses += 1

            if guess > secret_numer:
                print(bcolors.RED + "för högt ")
                print(bcolors.DEFAULT)
            elif guess < secret_numer:
                print(bcolors.YELLOW + "för lågt")
                print(bcolors.DEFAULT)
            elif guess == secret_numer:
                print(bcolors.GREEN + "du hittade rätt nummer!")
                print(bcolors.DEFAULT)
                break


            if guesses == 7:
                print(bcolors.RED + "Du hittade tyvärr inte nummret \n pröva igen") 
                print("det korrekta svaret var: ")
                print(bcolors.DEFAULT)
                print(bcolors.GREEN, secret_numer)
                print(bcolors.DEFAULT)
                break

        play_again = input ("vill du spela igen? ")
        if play_again== 'nej' or play_again== 'N':
            print(bcolors.CYAN + 'tack för att du spelade :)')
            print(bcolors.DEFAULT)
            exit()
        else:
            continue

    