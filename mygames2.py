import random
total_money = 100



def cho_han(bet, choice):
  print(f"Here we go! you bet ${bet} that it will be {choice}")
  d1 = random.randint(1,6)
  print(f"The first dice is a {d1}!")
  d2 = random.randint(1,6)
  print(f"The second dice is a {d2}!")
  together = d1 + d2
  print(f"Thats a {together}!!")
  if together % 2 == 0:
    answer = "even"
  else:
    answer = "odd"
  if choice == answer:
    print(f"Wow! you did it! it was {answer}! You won ${bet}!")
    return total_money + bet
  else:
    print(f"Awwww man, it was {answer}, maybe next time you wont lose ${bet}...")
    return total_money - bet
    



def heads_or_tails(bet, choice):
  print("Here comes the flip!\nyou bet ${0} that it will be {1}..".format(bet, choice))
  num = random.randint(1,10)
  if num > 5:
    num = "heads"
  else:
    num = "tails"
  if choice == num:
    print("Congratulations! it was {0}! you have won ${1}!".format(choice,bet))
    return total_money + bet
  elif choice != num:
    
    print("Awwww man, it was {0}, maybe next time you won't lose ${1}..".format(num, bet))
    return total_money - bet

def cards(bet,name):
  print(f"Let's go {name}!! pick a good one!")
  cardlist = [11, 11, 11, 11, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 9, 9, 9, 9, 8, 8, 8, 8, 7, 7, 7, 7, 6, 6, 6, 6, 5, 5, 5, 5, 4, 4, 4, 4, 3, 3, 3, 3, 2, 2, 2, 2]
  num1, num2 = random.randint(1,len(cardlist) - 1), random.randint(1,len (cardlist) - 1)
  card1 = cardlist[num1]
  cardlist.remove(card1)
  print(f"{name} has a {card1}.")
  card2 = cardlist[num2]
  print(f"House has a {card2}.")
  if card1 > card2:
    
    print(f"Congratulations! You won ${bet}!")
    return total_money + bet
  elif card2 > card1:
    
    print(f"Awwww man, you lost.. maybe next time you wont lose ${bet}..")
    return total_money - bet
  else:
    return total_money
    print(f"It's a tie! replace your bets!")

def roulette(number, numbet, color, colbet, pick, pickbet):
  print(f"Let's go! you bet ${numbet} it will be {number}, ${colbet} it will be {color}, and ${pickbet} it will be {pick}! good luck!")
  num = random.randint(0,37)
  numwin = 0
  colwin = 0
  pickwin = 0
  if num == 37:
    col = "green"
    num == "00"
    print("It's a 00!")
  else:
    print(f"It's a {num}!")
  if num == 37 and number == 00:
    print(f"WOW! you got it! you just won ${numbet * 35}! on your 00 pick!")
    numwin += numbet * 35
  elif num == number:
    print(f"Wow! thats a hit! you won ${numbet *35} on your {number}!")
    numwin += numbet * 35
  elif num != number: 
    print(f"Aww man, missed out on that {number}, it was a {num}, maybe next time! You lose ${numbet} on that one")
    numwin -= numbet
  if num % 2 == 0 and num != 37:
    col, odev = "red", "even"
    print(f"It's {col}, thats {odev}!")
  elif num % 2 != 0 and num != 37:
    col, odev = "black", "odd"
    print(f"It's {col}, that's {odev}!")
  if col == color:
    print(f"You hit your color pick of {color}! You won ${colbet} on that one!")
    colwin += colbet
  elif col == color and col == "green":
    print(f"Holy moly it was green! you won ${colbet} for that crazy pick!")
    colwin += colbet
  else: 
    print(f"Aww man, you guess wrong on the color! it was {col}, you lost ${colbet} on that one!")
    colwin -= colbet
  if pick == odev:
    print(f"You did it! it was {odev}! You won ${pickbet} on your {pick} choice!")
    pickwin += pickbet
  else: 
    print(f"Aww man, it was {odev}, you picked {pick}. You lost ${pickbet} on that one!")
    pickwin -= pickbet
  total = pickwin + numwin + colwin
  if total > 0:
    print(f"You did it! your total winnings are ${total}!")
  else:
    print(f"Better luck next time, you lost ${total} on all your bets")
  return total

print("Let's play Roulette!")
total_money = roulette(11, 20, "black", 25, "odd", 15)
print(f"You now have ${total_money} after Roulette!")
print("Let's play Cho Han!")
total_money = cho_han(50, "even")
print(f"You now have ${total_money} after Roulette and one game of Cho Han!")
print("Let's play Heads or Tails!")
total_money = heads_or_tails(50, "heads")
print(f"You now have ${total_money} after Roulette, Cho Han and Heads or Tails!")
print("Now, lets play cards!")
total_money = cards(50, "Jeff")
print(f"You now have ${total_money} after all four games!")
