import random
rock="✊"
paper="🖐"
scissors="✌️"
g=[rock, paper, scissors]
games=random.choice(g)
uc=int(input("What do you choose. Type 0 for rock, 1 for paper and 2 for scissors.\n"))
if uc==0 and games==scissors:
  print(f"rock{rock}")
  print(f"Computer Choose {games}")
  print("You Win")
elif uc==1 and games==rock:
  print(f"paper{paper}")
  print(f"Computer Choose {games}")
  print("You Win")
elif uc==2 and games==paper:
  print(f"scissors{scissors}")
  print(f"Computer Choose {games}")
  print("You Win")
else:
  if uc==0:
    print(f"rock{rock}")
  elif uc==1:
    print(f"paper{paper}")
  elif uc==2:
    print(f"scissors{scissors}")
  print(f"Computer Choose {games}")
  print("You Loos. Try again")