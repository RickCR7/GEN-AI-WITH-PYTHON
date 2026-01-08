seat_type = input("Enter your seat type (sleeper/AC/general/luxury): ").lower()

match seat_type:
    case "sleeper":
        print("Sleeper Class")
    case "ac":
        print("AC Class")
    case "general":
        print("General Class")
    case "luxury":
        print("Luxury class")
    case _:
        print('Invalid seat type')
