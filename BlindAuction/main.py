# TODO-1: Ask the user for input
names, prices = [], []

bidding_finished = False

while not bidding_finished:
    name = input("What is your name?: ")
    price = int(input("What is your bid?: $"))

    names.append(name)
    prices.append(price)
    # TODO-3: Whether if new bids need to be added
    more_bidders = input("Are there any other bidders? Type 'yes or 'no': ").lower()
    if more_bidders == 'no':
        bidding_finished = True

 # TODO-2: Save data into dictionary {name: price}
user_dict = {name: price for name, price in zip(names, prices)}

# TODO-4: Compare bids in dictionary
highest_bidder = max(user_dict, key=user_dict.get)
highest_bid = user_dict[highest_bidder]

print(f"The winner is {highest_bidder} with a bid of ${highest_bid}")

