device_status = "active"
temperature = int(input("Enter the temparature: "))

if device_status == "active":
    if temperature > 35:
        print("High temparature alert!!")
    else:
        print("Temparature is normal")
else:
    print("Device is offline")