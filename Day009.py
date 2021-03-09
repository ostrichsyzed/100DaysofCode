# https://repl.it/@ostrichsyzed/blind-auction-start

from replit import clear
from art import logo
print(logo)

print("Welcome to the Silent Auction! I hope you win something. If you didn't, then it's because you are cheap. So... Welcome!")

auctioneers = {}
completed = False

def highest_bidder(high_bid):
  highest_bid = 0
  winner = ""
  for bidder in high_bid:
    bid_amount = high_bid[bidder]
    if bid_amount > highest_bid:
      highest_bid = bid_amount 
      winner = bidder
  print(f"The winner is {winner} with a bid of ${highest_bid}.")
    


while not completed:
  name = input("What is your name? ")
  bid = int(input("How much are you bidding? $"))
  auctioneers[name] = bid
  anyone_else = input("Is there another bidder? ").lower()
  
  if anyone_else == "no":
    completed = True
    highest_bidder(auctioneers)
  elif anyone_else == "yes":
    clear()
  

    

  
  


 


