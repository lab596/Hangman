import random
n = open("nouns.txt","r")
a = open("adj.txt","r")

strn = n.readlines()
r1= random.randint(0,len(strn)-1)
word = strn[r1]
word = word[0 : len(word)-1]
#print(word)

###########################################
#stra = a.readlines()
#r2= random.randint(0,len(stra)-1)
#print(stra[r2])
###########################################

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
