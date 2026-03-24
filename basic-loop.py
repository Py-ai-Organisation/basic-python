value=1
while value<5 :
    print ('Value viz '+str(value))
    value=value+1
    if value==3:
        print('Value loop broken at : '+str(value))
        break


for num in range(3,5):
    print ('Nums current value is : '+str(num))

import random
for i in range (1,10):
    print( random.randint(i,18))

#Secret number guess between 1 to 20
secret_number = random.randint(1,20)

for i in range(1,7):
    guess=input("Please guess the secret number : ")
    if int(guess) < secret_number:
        print('Your guess is less than secret number')
    elif int(guess)>secret_number :
        print('Your guess is more than secret number')
    else :
        print('Bingo! You guessed the number viz    : '+str(secret_number)+' in '+str(i)+' guesses')
        break