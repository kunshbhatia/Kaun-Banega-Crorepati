Python 3.13.1 (tags/v3.13.1:0671451, Dec  3 2024, 19:06:28) [MSC v.1942 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> # My KBC
... 
... print("Welcome to Kaun Banega Crorepati " . center(50) . upper())
... print("Made By Kunsh".center(50).upper())
... print()
... print("To start the game , press Y and to exit press N")
... print()
... a = str(input("Enter your choice : "))
... 
... def exit():
...   print()
...   print("Thanks for playing the game" . center(50) . upper())
...   return()
... 
... def CorE():
...   print("Type C to Continue or Type E to Exit")
...   z = input("Enter your choice: ")
...   
...   if z == "E":
...     exit()
...     quit()
... 
...   elif z == "C":
...     print()
...     print("Here is the next question" . center(50) . upper())
... 
...   else:
...     print("Invalid Input")
...     quit()
...     
... def Q1():
...   print()
...   print("Here is your Q1:-\n \nWho is Prime Miniser Of India in 2025?")
...   print()
...   print("1. Narendra Modi\n2. Rahul Gandhi\n3. Amit Shah\n4. Arvind Kejriwal")
...   print()
...   b = int(input("Enter your answer:- "))
  print()
  if b == 1:
    print ("Correct Answer" . center(50))
    print("You have won 500Rs" . center(50))

  elif b == 2:
    print("Wrong Answer")
    print()
    exit()
    quit()

  elif b == 3:
    print("Wrong Answer")
    print()
    exit()
    quit()

  elif b == 4:
    print("Wrong Answer")
    print()
    exit()
    quit()

def Q2():
  print()
  print("Here is your Q2:-\n \nIn which year Python was introduced ?")
  print()
  print("1. 1996\n2. 1995\n3. 1991\n4. 1992")
  print()
  b = int(input("Enter your answer:- "))
  print()

  if b == 1:
    print ("Wrong Answer")
    print()
    exit()
    print("You have won 500Rs" . center(50))
    quit()

  elif b == 2:
    print("Wrong Answer")
    print()
    exit()
    print("You have won 500Rs" . center(50))
    quit()

  elif b == 3:
    print ("Correct Answer" . center(50))
    print("You have won 1000Rs" . center(50))

  elif b == 4:
    print("Wrong Answer")
    print()
    exit()
    print("You have won 500Rs" . center(50))
    quit()

def Q3():
  print()
  print("Here is your Q3:-\n \nWhich player Indian Cricket Team is known as 'Mr Cool' ?")
  print()
  print("1. Rohit Sharma\n2. Virat Kohli \n3. Rishabh Pant \n4. MS Dhoni")
  print()
  b = int(input("Enter your answer:- "))
  print()

  if b == 1:
    print ("Wrong Answer")
    print()
    exit()
    print("You have won 1000Rs" . center(50))
    quit()

  elif b == 2:
    print("Wrong Answer")
    print()
    exit()
    print("You have won 1000Rs" . center(50))
    quit()

  elif b == 4:
    print ("Correct Answer" . center(50))
    print("You have won 1500Rs" . center(50))

  elif b == 3:
    print("Wrong Answer")
    print()
    exit()
    print("You have won 1000Rs" . center(50))
    quit()

def Q4():
  print()
  print("Here is your Q4:-\n \nWhich of the following is software?")
  print()
  print("1. Monitor\n2. Operating System \n3. Printer \n4. Keyboard")
  print()
  b = int(input("Enter your answer:- "))
  print()

  if b == 1:
    print ("Wrong Answer")
    print()
    exit()
    print("You have won 1500Rs" . center(50))
    quit()

  elif b == 4:
    print("Wrong Answer")
    print()
    exit()
    print("You have won 1500Rs" . center(50))
    quit()

  elif b == 2:
    print ("Correct Answer" . center(50))
    print("You have won 2000Rs" . center(50))

  elif b == 3:
    print("Wrong Answer")
    print()
    exit()
    print("You have won 1500Rs" . center(50))
    quit()

def Q5():
  print()
  print("Here is your Q5:-\n \nHow many keys are there in Keyboard ?")
  print()
  print("1. 104\n2. 100 \n3. 102 \n4. None of the above")
  print()
  b = int(input("Enter your answer:- "))
  print()

  if b == 4:
    print ("Wrong Answer")
    print()
    exit()
    print("You have won 2000Rs" . center(50))
    quit()

  elif b == 2:
    print("Wrong Answer")
    print()
    exit()
    print("You have won 2000Rs" . center(50))
    quit()

  elif b == 1:
    print ("Correct Answer" . center(50))
    print("You have won 2500Rs" . center(50))

  elif b == 3:
    print("Wrong Answer")
    print()
    exit()
    print("You have won 2000Rs" . center(50))
    quit()


if a == "Y":
  print()
  Q1()
  print()
  CorE()
  print()
  Q2()
  print()
  CorE()
  print()
  Q3()
  print()
  CorE()
  print()
  Q4()
  print()
  CorE()
  print()
  Q5()
  print()
  print("Thanks For Playing the Game\n(Made By Kunsh Bhatia)" . center(50) . upper())

elif a == "N":
  print()
  print("Why N ? 👀 , come on let's play the game" . center(50) )

else:
  print()
  print("Invalid Input")
