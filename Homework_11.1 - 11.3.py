import random
import json
import datetime
from operator import itemgetter


secret = random.randint(1,30)
attempts = 0
wrong_guesses = []

with open("score_list.txt", "r") as score_file:
    score_list = json.loads(score_file.read())
    score_list.sort(key=itemgetter("attempts"))

for score_dict in score_list[0:3]:
    print(f'NAME: {str(score_dict["name"])}, ATTEMPTS: {str(score_dict["attempts"])},'
          f' SECRET NUMBER: {str(score_dict["secret"])}, WRONG GUESSES: {str(score_dict["wrong_guesses"])},'
          f' DATE: {score_dict["date"]}')

name = input("Name: ")

while True:
    attempts += 1
    guess = int(input("Guess: "))

    if secret == guess:
        score_list.append({"attempts": attempts, "date": str(datetime.datetime.now()),
                           "name": name, "wrong_guesses": wrong_guesses, "secret": secret})

        with open("score_list.txt", "w") as score_file:
            score_file.write(json.dumps(score_list))

        print("You've guessed it - congratulations! It's number " + str(secret))
        print("Attempts needed: " + str(attempts))
        break

    elif guess > secret:
        print("Your guess is not correct... try something smaller")

    elif guess < secret:
        print("Your guess is not correct... try something bigger")

    wrong_guesses.append(guess)

