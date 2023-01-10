def he_has_jokes():
  print("Welcome to the knock knock joke library")
  joke = input("Do you want to hear a joke? (Yes or No) \n")
  question = input("Do you want to hear a joke about robbers, tanks , or pencils? " )
  punchlines = ["Calder police- I've been robbed! ", "You are welcome! " , "Nevermind, it's pointless! "  ]
  if joke == "no":
   print("Okay suit yourself")
  while (joke == "yes"):
    print("Great, Lets Play")
    he_actually_has_the_jokes(question, punchlines)
    joke = input("Do you want to hear another joke or are you finished? ")
  if joke == "finished":
     rate = int(input("Please rate our game 1-10! "))
     final_score = int((rate * 10))
     print(str(final_score)  +  " percent satisfaction rate")
     friend = input("Would you recommend this game to a friend? ")
     print (friend)
     if friend == "yes" or friend == "maybe" :
       print("Thanks, we appreciate it. ")
     else:
       print("Sorry you did not enjoy it. ")
  else:
    he_actually_has_the_jokes()

def he_actually_has_the_jokes(question,punchlines):
  punchlines = ["Calder police- I've been robbed! ", "You are welcome! " , "Nevermind, it's pointless! "]
  input("Knock Knock ")
  if question == "robbers":
     input("Calder")
     print(punchlines[0])
  elif question == "tanks":
     input("Tank ")
     input(punchlines[1])
  elif question == "pencils":
     input("Broken pencil ")
     input(punchlines[2])
  