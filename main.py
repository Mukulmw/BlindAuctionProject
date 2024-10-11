import art
print(art.logo)
# TODO-1: Ask the user for input
more_people = True
bids = {}
while more_people:
    name = input("Enter You name\n")
    price = int(input("What is your bid?\n"))
    bids[name] = price
    proceed = input("Are there more people? Yes or No").lower()
    if proceed == "no":
        more_people = False
    else:
        print("\n" * 100)
print(bids)
# TODO-2: Save data into dictionary {name: price}
# TODO-3: Whether if new bids need to be added
# TODO-4: Compare bids in dictionary
highest = 0
for key in bids:
    if bids[key] > highest:
        highest = bids[key]
        bidder = key
print(f"The highest bid is {highest} by {bidder}")
