with open("contact.txt", "w") as f1:

    f1.write(
        """ name : Harsh\n
            carOwned: BMW
            \n
            name : Mukul\n
            carOwned: Merc
            \n
            name : Juhu\n
            carOwned: Audi
            """
    )

print(f1.name)  # contact.txt
print(f1.mode)  # w
print(f1.closed)  # True
