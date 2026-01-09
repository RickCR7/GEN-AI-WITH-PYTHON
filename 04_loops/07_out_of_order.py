flavours = ["Ginger", "Out of Stock", "Lemon", "Discontinued", "Tulsi"]

for flavour in flavours:
    if flavour == "Out of Stock":
        continue
    elif flavour == "Discontinued":
        break

    print(f"You ordered for {flavour} tea")