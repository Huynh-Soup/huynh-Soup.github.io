




print("This is an adventure! Would you like to play?")
response=input()

if response=='yes' or response=='y':
    print ("Great! let's start!")
    
else:
    print('That is not a choice.')

    
if response=='yes':
    print('Your Adventure starts out in your rundown apartment you barely pay rent for')
    print('As a young adult you try to make a living by searching for a job.')
    print("What do you do now?")


print("a. Decide to go ot and look for a business that's hiring")
print("b. Stay home and look online")
print("c. Realise that you have no part in this world and decide to end it all by hanging yourself")

response=input()
response=response.lower()

if response =='a':
   
    print("You decide to go out and look for a job.")
    print('After driving in time for about 30 minutes, you noticed that 3 places that were hiring.')
    print

if response =='b':
 
    print("You decide to go on your laptop to look online.")
    print("The three jobs you see are")
    print("a. Programmer")
    print('b. Website designer')
    print('c. Tech support')

    response=input()
    response=response.lower()

    if response =='a' or response =='b':
        print('You chose a job that the future needs, and made money that would support your apartment')

    if response=='b':
        print('You chose a job that scams others of their money.')
    

if response =='c':
    print('You realize that your life is just sad and miserable, you then proceed to commit suicide')
