import random
num = random.randint(01, 99)
guess = ""
guess_count = 0

while guess != num:
      guess=int(input("Guess a two digit number:"))
guess_count+=1
if guess==num:
     print("Your guess is right. You guessed it as:"+str(guess_count)+"guesses.")
     break
elif guess>num:
    print("Your Guess is high")
else:
    print("Your Guess is low")
