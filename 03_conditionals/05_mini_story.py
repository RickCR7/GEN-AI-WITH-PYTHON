order_amount =  int(input("Enter the order amount: "))

print(f"Order Amount: {order_amount}")

delivery_fees = 0 if order_amount > 300 else 0

print(f"Delivery fees : {delivery_fees}")