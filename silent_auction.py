import os
print ("*****Welcome to the Silent Auction Program!*****")
def find_winner(bidder_details): #{Mukesh:10000 ,Ram:5000,Shyam:2000}
    highest_bid=0  #10000
    winner=" "
    for bidder in bidder_details:#Mukesh
        bidding_price=bidder_details[bidder]#10000
        if bidding_price>highest_bid:
            highest_bid=bidding_price
            winner=bidder
    print(f"Here is the list of all the bidders: {bidder_details}")
    print(f"The winner is {winner} with a bid of {highest_bid}")

bidder_data={}
end_of_bidding=False
while not end_of_bidding:
    name=input("What is your name?:")
    price=int(input("What is your bid?:"))
    bidder_data[name]=price

    more_bidders=input("Are there any other bidders? Type 'yes' or 'no':").lower()
    if more_bidders=="no":
        end_of_bidding=True
        find_winner(bidder_data)
    elif more_bidders=="yes":
        os.system("cls")

 

