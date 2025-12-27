favourite_chais = [
    "Masala chai",
    "Green Tea",
    "Masala chai",
    "Lemon Tea",
    "Green Tea",
    "Elaichi chai"
]

unique_chai = {chai for chai in favourite_chais}
print(unique_chai)

recipes = {
    "Masala Chai": ["ginger", "cardamom", "clove"],
    "Elaichi Chai": ["cardamom", "milk"],
    "Spicy Chai": ["ginger", "black pepper", "clove"],
}


unique_spices = {spice for ingredients in recipes.values() for spice in ingredients}
print(unique_spices)
