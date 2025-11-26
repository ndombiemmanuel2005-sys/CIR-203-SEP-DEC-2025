from itertools import product

inventory = {
    'Laptops': 15,
    'Mouse': 8,
    'Keyboard': 5,
    'Speakers': 13
}
print("1. Initial inventory:", inventory)

inventory['Webcam'] = 10
inventory['Mouse'] = 25
print("2. Updated inventory:", inventory)

def low_stock_product(inv):
    return {product: quantity for product, quantity in inv.items() if quantity<10}

low_stock = low_stock_product(inventory)
print('\n3. Low stock product (<10):', low_stock)

del inventory['Keyboard']
print("\n4. After deleting the keyboard:", inventory)

print("\n5. Current inventory")
for product, quantity in inventory.items():
    print(f"{product}: {quantity} units")