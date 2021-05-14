import random

def hungman():

	words=random.choice(["earth","planet","Avenger","thor","spiderman","superman","savewater","war","indian","movie","cricket","player","soccer","captials","engineer","doctor"])

	guessmade=""

	turns=3

	validletters="abcdefghijklmnopqrstuvwxyz"

	while(len(words)>0):

		main=""

		for letter in words:

			if(letter in guessmade):

				main=main+letter

			else:

				main=main+"_"+" "

				

		if(main==words):

			print("\n")

			print(main,"is crct word")

			print("Yaahooo u guessd the crct word")

			print("You Won")

			print("congratulations Mr/Ms.",name)

			break

		print("Guess the word:",main)

		guess=input()

		

		if(guess in validletters):

			guessmade+=guess

		else:

			print("Enter valid character-")

			guess=input()

		if(guess not in words):

			turns=turns-1

			if(turns==2):

				print("Two more chances")

				print("Play carefull Mr/Ms.",name)

			if(turns==1):

				print("Last chance")

				print("Take a Breath")

			if(turns==0):

				print("Oh No! ")

				print("You Lost")

				print("Better luck next time")

				break

name=input("Enter your name-")

print("---------------------------")

print("Welcome 	Mr/Ms.",name)

hungman()

print()

		
