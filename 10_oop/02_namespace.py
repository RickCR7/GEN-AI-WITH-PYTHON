class Chai:
    origin = "India" # properties

print(Chai.origin)

# adding a property/attributes
Chai.is_hot = True
print(Chai.is_hot)

# creating objects from class Chai

masala = Chai()
print(masala.origin)
print(masala.is_hot)

masala.is_hot = False
print(f"Class : {Chai.is_hot}")
print(f"Object : {masala.is_hot}")

masala.flavor = "Masala"
print(masala.flavor)