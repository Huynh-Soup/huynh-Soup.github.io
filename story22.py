import time
import sys
from colorama import*
from colorama import init, Fore, Back, Style
init(convert=True)



def print_s(str):
  for letter in str:
    sys.stdout.write(letter)
    sys.stdout.flush()
    time.sleep(0.04)

def print_f(str):
  for letter in str:
    sys.stdout.write(letter)
    sys.stdout.flush()
    time.sleep(0.1)

Bad = ("Bad Ending")
Good = ("Good Ending")
print (Fore.RED + Back.WHITE)
print_f ('Welcome to\nCHOOSE\nYOUR\nOWN\nADVENTURE!')
print (Fore.RESET + Back.RESET)
print (Fore.BLUE + Back.YELLOW)
print_f ('Press enter to begin!')
print (Fore.RESET + Back.RESET)
input()
age = int(input('Before we start this story, How old are you?: '))
print_s ('You recieve a text from your friend asking, "Do you wanna get a new game from GameStop?"')
p1 = input ("\nYes or No: ")
''' Part 1 '''
if p1.lower() == ('yes'):
    print_s("You decide to go but realize that you lost your car keys a while ago")
    pa2 = input("\nWalk or Uber: ")
    ''' Part 2 '''
    if pa2.lower() == ('uber'):
        print_s("You uber'd to GameStop but get there with no money. (" + Bad + ')')
    elif pa2.lower() == ('walk'):
        print_s("You decide to walk, but a stranger jumps you!")
        pa3 = input("\nFight or Run?: ")
        if pa3.lower() == ('fight'):
            print_s('You fight but soon realize that you are out of shape and get knocked out')
            print_s('\nYou wake up in the Hospital with your money gone. (' + Bad + ')')
        elif pa3.lower() == ('run'):
            ''' Part 3 '''
            print_s('You flee the scene and')
            print_s('\nmake it safely to GameStop to find two games of choice. ')
            pa4 = input('\nWould you like to buy Detroit Become Human(DBH) or Spider-Man(SM): ')
            if pa4.lower() == ('dbh') and (age < 18):
                print_s('sorry you are ' + str(age) + ' years old, you have to be 17 or older to play this game ' + "(" + Bad + ')')
            elif pa4.lower() == ('dbh') and (age >= 18):
                print_s('You buy a great game and go home happy (' + Good + ')' )
            elif pa4.lower() == ('SM') or ('Spider-man'):
                print_s('You buy a great game and go home happy (' + Good + ')' )
elif p1.lower() == ('no'):
    print_s("You stay at home and do nothing, do you want to watch Netflix or TV?")
    sh1 = input("\nNetflix or TV?: ")
    ''' Part 2 (no) '''       
    if  sh1.lower() == ('netflix'):
        print_s("You forgot to pay your Netflix bill! You now are sad and cry. (" + Bad + ')')
    elif sh1.lower() == ('tv'):
        ''' Part 3 (no) '''       
        print_s ("There is nothing interesting on TV you no longer want to be inside (You go on a walk)")
        print_s ("\nYou are still walking and get near Gamestop , you decide to walk there anyways")
        print_s ("\nYou walk near Gamestop, but a stranger jumps you!")
        pa3 = input("\nFight or Run?: ")
        if pa3.lower() == ('fight'):
            ''' Part 4 (no) '''       
            print_s ('You fight but soon realize that you are out of shape and get knocked out')
            print_s ('\nYou wake up in the Hospital with your money gone. (' + Bad + ')')
        elif pa3.lower() == ('run'):
            ''' Part 5 (no) '''       
            print_s ('You flee the scene and')
            print_s ('\nmake it to GameStop to find two games of choice. ')
            pa4 = input('\nWould you like to buy Detroit Become Human(DBH) or Spider-Man(SM): ')
            ''' Part 6 (no) '''       
            if pa4.lower() == ('dbh') and (age < 18):
                print_s('sorry you are ' + str(age) + ' years old, you have to be 17 or older to play this game ' + "(" + Bad + ')')
            elif pa4.lower() == ('dbh') and (age >= 18):
                print_s('You buy a great game and go home happy (' + Good + ')' )
            elif pa4.lower() == ('SM') or ('Spider-man'):
                print_s('You buy a great game and go home happy (' + Good + ')' )

else:
  print_s ('Pick one of the listed options next time. Play again! ')

input()
        
