import random

name = "Heather"
question = "Will I win the lottery"
answer = ""

if name == "":
  name = "question"


one = "Yes-definately"
two = "It is decidedly so"
three = "Without a doubt"
four = "Reply hazy, try again"
five = "Ask again later"
six = "Better not tell you now"
seven = "My sources say no"
eight = "Outlook not so good"
nine = "Very doubtful"
ten = "maybe, maybe not"
eleven = "Hmm that could be a possibility"

random_number = random.randint(1,11)

if random_number == 1:
  answer = one
elif random_number == 2:
  answer = two
elif random_number == 3:
  answer = three
elif random_number == 4:
  answer = four
elif random_number == 5:
  answer = five
elif random_number == 6:
  answer = six
elif random_number == 7:
  answer = seven
elif random_number == 8:
  answer = eight
elif random_number == 9:
  answer = nine
elif random_number == 10:
  answer = ten
elif random_number == 11:
  answer = eleven
else:
  print("Error")


if name == "":
  name = "question"
else:
  print(name, "asks:", question)

if len(question) == 0:
  print("Error please enter a question")
else: 
  print("Magic 8-ball's:", answer)


