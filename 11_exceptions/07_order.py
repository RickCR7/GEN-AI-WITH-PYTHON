class InvalidChaiError(Exception):
    pass

def bill(flavor, cups):
    menu = {"masala": 20, "ginger": 40, "elaichi": 50}
    try:
        if flavor not in menu:
            raise InvalidChaiError("This item is not available in our menu!!!")
        if not isinstance(cups, int):
            raise TypeError("Sorry! We can't understand what you are saying...")
        total = menu[flavor] * cups
        print(f"Your bill for {cups} cups of {flavor} chai is {total}Rs.")
    except Exception as e:
        print("Error: ", e)
    finally:
        print("Thank you for visiting our shop...")

bill("mint", 2)
bill("masala", "three")
bill("ginger", 3)