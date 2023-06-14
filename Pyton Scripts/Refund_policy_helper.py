purchase_age = int(input("How many days ago have you purchased the item? "))
item_used = input("Have you used the item at all [y/n]? ")
item_broken = input("Has the item broken down on its own [y/n]? ")

if purchase_age <= 10:
    if item_used == "n":
        print("You can get a refund.")
    elif item_broken == "y":
        print("You can get a refund.")
    else:
        print("You cannot get a refund.")
elif item_broken == "y":
    print("You can get a refund.")
else:
    print("You cannot get a refund.")