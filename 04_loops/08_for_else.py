staff = [("akash", 24), ("shaibal", 23), ("sandeep", 23)]

for name, age in staff:
    if age >= 25:
        print(f"{name} is eligible to manage the staff")
        break
else:
    print(f"No one is eligible to manage the staff")