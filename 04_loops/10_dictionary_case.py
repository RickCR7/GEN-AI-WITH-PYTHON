users = [
    {"id": 1, "total": 100, "coupon": "A20"},
    {"id": 2, "total": 200, "coupon": "F10"},
    {"id": 3, "total": 50, "coupon": "P50"},
]

discounts = {
    "A20": (0.2, 0),
    "F10": (0.5, 0),
    "P50": (0, 10),
}

for user in users:
    percent, fixed = discounts.get(user["coupon"], (0, 0))
    discount = user["total"] * percent + fixed
    print(f"{user["id"]} paid {user["total"]} and got discount for next visit of rupees {discount}")