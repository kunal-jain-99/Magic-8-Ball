import random
import time
#https://en.wikipedia.org/wiki/Magic_8-Ball#Possible_answers

answers = ["It is certain", "It is decidedly so", "Without a doubt", "Yes, definitely",
           "You may rely on it", "As I see it, yes", "Most Likely", "Outlook Good",
           "Yes", "Signs point to yes", "Reply hazy, try again", "Ask again later",
           "Better not tell you now", "Cannot predict now", "Concentrate and ask again",
           "Don't count on it", "My reply is no", "My sources say no", "Outlook not so good", 
           "Very Doubtful!"]

print('  __  __          _____ _____ _____    ___  ')
print(' |  \/  |   /\   / ____|_   _/ ____|  / _ \ ')
print(' | \  / |  /  \ | |  __  | || |      | (_) |')
print(' | |\/| | / /\ \| | |_ | | || |       > _ < ')
print(' | |  | |/ ____ \ |__| |_| || |____  | (_) |')
print(' |_|  |_/_/    \_\_____|_____\_____|  \___/ ')
print('')
print('')
print('')

print("I'm Magic 8 Ball, What is you Name?: ")
name = input()
print("\n")
print(f"Welcome, {name}")

def magic8ball():
	print("Ask me a Question: ")
	quest = input()
	print("\n")
	print("Thinking...")
	time.sleep(4)
	print("\n")
	print(random.choice(answers))
	replay()

def replay():
	print("Do you want to Try Again?[y/n]: ")
	ch = input()
	if ch == "y":
		magic8ball()
	elif ch == "n":
		exit()
	else:
		print("Sorry, I didn't catch that!")
		replay()

magic8ball()