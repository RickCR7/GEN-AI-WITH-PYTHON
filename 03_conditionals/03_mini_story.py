cup_size = input("Choose your cup size (small/medium/large): ").lower()

if cup_size == "small":
    print("Price is 10 rupees")
elif cup_size == "medium":
    print("Price is 15 rupees")
elif cup_size == "large":
    print("Price is 20 rupees")
else:
    print("Unknown cup size")