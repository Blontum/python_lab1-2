''''Write a code using functions that will add items in your grocery cart and return total in a receipt text.
Order = I 'tomato': 30, 'thyme': 4.50, 'garlic': 7.5, 'rice': 10, 'onions': 4, 'fish': 9.99 l
Add it to your GitHub and send us screenshot of working'''''

def add_to_cart(order):
    total = 0
# Open or create the receipt file
    with open('receipt.txt', 'w') as receipt:
        receipt.write("Receipt\n")
        receipt.write("-------\n")
        for item, price in order.items():
# Write each item and its price to the receipt
            receipt.write(f"{item}: ${price}\n")
            total += price
 # Write the total to the receipt
        receipt.write("-------\n")
        receipt.write(f"Total: ${total:.2f}\n")
    return total
# Order with items and prices
order = {
    'tomato': 30,
    'thyme': 4.50,
    'garlic': 7.5,
    'rice': 10,
    'onions': 4,
    'fish': 9.99
}

# Call the function and generate the receipt
total = add_to_cart(order)
print(f"Total cost: ${total:.2f}")

# Let's also verify the receipt contents
with open('receipt.txt', 'r') as file:
    print("\nHere's your receipt:")
    print(file.read())