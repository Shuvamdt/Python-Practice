import art
print(art.logo)
print("Welcome to the secret auction program.")
auction_bids={}
# TODO-1: Ask the user for input
choice = "yes"
while choice == "yes":
    name = input("What is your name?:")
    bid = int(input("What's your bid?: $"))
    auction_bids[name] = bid
    choice = input("Are there any other bidders? Type 'yes' or 'no' \n").lower()
    print("\n" * 100)
# TODO-2: Save data into dictionary {name: price}
# TODO-3: Whether if new bids need to be added
# TODO-4: Compare bids in dictionary
maxBid = 0
maxBidder =""
for key in auction_bids:
    if maxBid < auction_bids[key]:
        maxBid = auction_bids[key]
        maxBidder = key

print(f"The winner is {maxBidder} with a bid of ${maxBid}")