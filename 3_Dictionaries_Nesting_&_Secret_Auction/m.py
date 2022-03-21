from logo import logo
from os import system, name
print(logo)
def clear():
     # for windows
    if name == 'nt':
        _ = system('cls')
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')
  

bids = {}

def add_bidder():
    name = input("What is your name?: ")
    bid = int(input("What is your bid?: "))
    bids[name] = bid

def get_winner(bidding_record):
    max_bid = 0 
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > max_bid:
            max_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of ${max_bid}")

new_bid = True # is there any new bid, cheking
while new_bid: #while there new bid, repeat taking new bid
    add_bidder()  # saving to the disctionarry new bidder details 
    answer = input("Are there any other bidders? Type 'yes' or 'no'.")
    if answer == "no":
        new_bid = False
        get_winner(bids)
    elif answer == "yes":
        clear()







# print(bids)

