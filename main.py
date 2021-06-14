'''
                                  CODE CHEF
PLEASE READ THE INSTRUCTIONS GIVEN BELOW!:

Instructions to follow prior to running the program:
Depending on the IDE you are using:
  1.Repl.it online IDE:
        If you are using repl.it, then you can go ahead and run the program. Everytime you open the program on your browser and run the program for the FIRST TIME, the console will show that it's installing & updating the modules required for this program to run. The modules will NOT be installed onto your computer locally.
  2.PyCharm/IDLE/SublimeText/VSCode:
        If you are running the program on a local IDE, then please follow these steps:
        On Windows:
          i.Open command prompt
         ii.Type "pip install Pyenchant" without the quotation marks.
        iii.You're DONE! You can now run the code on your IDE.


Modules used:
1.itertools
2.enchant
3.string
4.random
5.time

User-defined methods:
1. instructions():    lines 46-56
2. list_of_letters(): lines 59-113
3. user():            lines 117-172
4. playagain():       lines 177-191

 
Programmed by:
  1.Anagha Upadyaya,
  2.Sneha Prem Pratap, 
  3.Veeraja Veeraesh,
students of grade 11'A' studying in Delhi Public School, Electronic City, Bengaluru.



'''

#importing necessary modules for the program
from itertools import permutations
import enchant
import string
import random
'''
The function instructions() displays the rules and main page
'''


def instructions():

    print("\t\t\t\t\t\t\t\t\tWORD CHEF\n\n")
    print("Instructions:")
    print(
        "   1.You are supposed to make sensible words from a group of jumbled letters."
    )
    print()
    print(
        "   2.To get those letters, you will need to enter the number of letters you want.(Note that you might need to enter it multiple times.) "
    )
    print()
    print(
        "   3.The short forms of words like United Nations Organizations or UNO is considered as a word. "
    )
    print()
    print("You're ready to go!!!")


print()
'''
The function list_of_letters:
  1.retrieves a random set of letters
  2.finds all possible "meaningful" words by permuting the letters
'''


def list_of_letters():
    string.ascii_letters  #Importing alphabets
    lofl = []
    n = 0
    letters = 0
    while True:
        n = int(input("No. of letters: "))
        if n < 3:
            print("Please enter a number more than 3")
            continue
        elif n >= 9:
            print("Please enter a number less than 9")
            continue
        else:
            #code to get a random set of letters based on the length entered by User
            while letters < n - 1:
                a = random.choice(string.ascii_letters)
                a = a.upper()
                if a in lofl:
                    continue
                else:
                    lofl.append(a)  #Adds the random letters to a list.
                    letters += 1
            lofl.append(random.choice(['A', 'E', 'I', 'O','U']))  #Adds vowels to the same list.
        break
    prmtns = []
    letters = lofl
    ###########################################################################

    #code to find all possible permutations of a set of letters
    for size in range(3, n + 1):  #min letter size should be 3
        x = permutations(letters, size)
        y = [''.join(i) for i in x]
        prmtns.append(y)

    lstofsolutions = []
    dictionary1 = enchant.Dict("en_GB")

    #code to check if a word from prmtns is present in the english dictionary
    for lst in prmtns:
        for word in lst:
            if dictionary1.check(word) == True:
                lstofsolutions.append(word)

#code to make sure no. of solns. is more than 4
    if len(lstofsolutions) <= 4:
        print("Enter no. of letters again.")
        return list_of_letters()
    else:
        return (letters, lstofsolutions)
'''
The function user():
  1.Displays information related to the game(lives etc.)
'''


def user():

    tup = list_of_letters()
    listofQstn = tup[0]
    listofSoln = tup[1]

    #initializing the game parameters
    lives = 5
    userinputs = []
    wordsguessed = 0
    maxwordstoguess = 0

    if len(listofSoln) <= 10:
        maxwordstoguess = int(0.6 * len(listofSoln))
    else:
        maxwordstoguess = 6

    while lives > 0:
        print("Lives: ", lives)
        print("Words Guessed= ", wordsguessed)
        print("You need to guess:", maxwordstoguess - wordsguessed,
              " more word(s)")
        print("Your letters:   ", '   '.join(listofQstn))
        print()

        if len(set(userinputs)) == maxwordstoguess:
            break

        inp = str(input("Enter your combination of these letters: "))
        inp = inp.upper()
        if ' ' in inp:
            print("Enter a single word!!!")
            print()
            continue

        if inp not in listofSoln:
            lives -= 1
            print("Wrong word!")
            continue
        else:
            if inp not in userinputs:
                userinputs.append(inp)
                wordsguessed += 1
                continue
            else:
                print("You guessed the same word!")
                continue

    if lives == 0:
        print("You have lost! Better luck next time.")
        print("Solution: ", listofSoln)

    else:
        print("You have WON!!! :)")
        print("Solution: ",listofSoln)
    playagain()


'''
The function playagain() is called so that the user can play again if he/she wants to
'''


def playagain():
    instructions()
    while True:
        play = input("If you want to play, press Y else press N: ")
        play = play.upper()

        if play == 'Y':
            return user()

        elif play == 'N':
            break

        else:
            print("Invalid input!")
            continue


#calling the function to run
playagain()
print("Thank You")
