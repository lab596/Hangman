print("Welcome to Hangman!")
print ("There is two game modes: single word or sentance")
inp = int(input ("Type '1' for single word or '2' for sentance"))
if inp == 1:
  print("Welcome to word mode")
  print("Your goal is to guess the word within 6 guesses")
  import random
  n = open("nouns.txt","r")

  strn = n.readlines()
  r1= random.randint(0,len(strn)-1)
  word = strn[r1]
  word = word[0 : len(word)-1]

  guesses = 6
  gword = ""
  for i in word:
    gword+="*"
  print(gword)
  gword=""
  letters = []
  print("Guesses " + str(guesses))
  while guesses>0:
    letter = input("Guess a letter: ")

    if len(letter)>1:
      print("Guess only one letter.")
      continue
    if letter.isdigit():
      print("Bro what are you doing? I said put a letter")
      continue
    if word.count(letter) > 0:
      num = word.count(letter)
      print("There are "+ str(num)+" " + letter.capitalize() +"(s)")
      letters.append(letter)
      for i in word:
        if i in letters:
          gword+=i
        else:
          gword+="*"
      print(gword)
      if gword == word:
        print("You guessed the word!")
        break
      gword=""   
    else:
      print("Sorry the word does not have a "+ letter.capitalize())
      guesses-=1
      print("Guesses " + str(guesses))
  if guesses == 0:
    print("You ran out of guessses.")
    print("The word was " + word)

elif inp == 2:
  print("Welcome to sentance mode.")
  print("Your goal is to guess the scentance within 6 guesses")
  s = open("sentences.txt","r")
  strs = s.readlines()
  r2= random.randint(0,len(strs)-1)
  sentence = strs[r2]
  print(sentence)
  sentence = sentence[0 : len(sentence)-1]
  guesses = 6
  gsen = ""
  for i in sentence:
    if i == " ":
      gsen += " "
    else:
      gsen+="*"
  print(gsen)
  gsen=""
  letterss = []
  print("Guesses " + str(guesses))
  while guesses>0:
    letter = input("Guess a letter: ")

    if len(letter)>1:
      print("Guess only one letter.")
      continue
    if letter.isdigit():
      print("Bro what are you doing? I said put a letter")
      continue
    if sentence.count(letter) > 0:
      num = sentence.count(letter)
      print("There are "+ str(num)+" " + letter.capitalize() +"(s)")
      letterss.append(letter)

      
      for i in sentence:
        if i in letterss:
          gsen+=i
        else:
          gsen+="*"
      print(gsen)
      if gsen == sentence:
        print("You guessed the word!")
        break
      gword=""   
    else:
      print("Sorry the word does not have a "+ letter.capitalize())
      guesses-=1
      print("Guesses " + str(guesses))
  if guesses == 0:
    print("You ran out of guessses.")
    print("The word was " + word)
  
else:
  print("Please type 1 or 2.")
