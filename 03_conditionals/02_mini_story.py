snack_input = input("What is your prrferred snack: ").lower()

print(f"User want: {snack_input}")
if snack_input == "samosa" or snack_input == "cookies":
    print("Your order is confirmed...")
else:
    print("The item is not currently available...")