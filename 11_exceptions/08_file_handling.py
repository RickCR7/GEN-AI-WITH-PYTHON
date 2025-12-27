# file = open("order.txt", "w")
# try:
#     file.write("Masala chai - 2 cups")
# finally:
#     file.close()

# modern way
with open("order.txt", "w") as file:
    file.write("Ginger tea - 2 cups")