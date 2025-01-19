This is a Python application that implements a Silent Auction system. It allows users to participate in an auction by anonymously placing bids for an item. The program determines the highest bidder and displays the winning bid and bidder's name.

Features-
   

    Allows multiple users to place bids.

    Ensures anonymity during the bidding process.

    Automatically determines the highest bid and the corresponding bidder.

    User-friendly interface for entering names and bid amounts.

    Option to add more bidders until the auction ends


Example Code Snippet-


    def collect_bids():
    bids = {}
    while True:
        name = input("Enter your name: ")
        bid = int(input("Enter your bid amount: "))
        bids[name] = bid
        should_continue = input("Are there any other bidders? (yes/no): ").lower()
        if should_continue == "no":
            break
    return bids

def find_highest_bidder(bids):
    highest_bid = 0
    winner = ""
    for bidder, amount in bids.items():
        if amount > highest_bid:
            highest_bid = amount
            winner = bidder
    return winner, highest_bid
