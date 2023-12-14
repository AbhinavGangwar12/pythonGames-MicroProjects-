import os

logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''
print(f"{logo}\n\t\t\tSecret Auction\n")
bids = {}

name = input("Enter your name : ")
bid = int(input("Your bid : $"))
bids[name] = bid
loop = True
choice = input("Enter 'yes' if there is any other person otherwise no 'no'\n")
# if choice == "yes":
#     os.system('cls')
if choice == "yes":
    while loop:
        os.system('cls')
        name = input("Enter your name : ")
        bid = int(input("Your bid : $"))
        bids[name] = bid
        choice = input("Enter 'yes' if there is any other person otherwise 'no'\n").lower()
        if choice == "no":
            loop = False
max = 0
winner = ""
for nominee in bids:
    if bids[nominee] > max:
        max = bids[nominee]
        name = nominee
print(f"The item is sold to {nominee} with a bid of ${max}")
