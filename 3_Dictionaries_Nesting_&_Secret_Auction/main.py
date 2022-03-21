from logo import logo
from os import system, name

def clear():
    # for windows
    # if name == 'nt':
    #     _ = system('cls')
    # # for mac or linux
    # else:
    _= system('clear')

print(logo)

bids = {}
def add_bidder():
    name = input("Ваше имя:")
    bid = int(input("Ваша ставка:"))
    bids[name] = bid

def get_winner(bids):
    max_bid = 0
    for bidder in bids:
        bid_amount = bids[bidder]
        if bids[bidder] > max_bid:
            max_bid = bids[bidder]
            winner = bidder
    print(f"Победитель {winner}  со ставкой {max_bid}")

new_bid = True
while new_bid:
    add_bidder()
    answer = input("Есть ли кроме Вас еще покупатель?, 'Да' или 'Нет'")
    if answer == 'Нет':
        new_bid = False
        get_winner(bids)
    if answer == 'Да':
        # clear()
        # add_bidder()

print(bids)