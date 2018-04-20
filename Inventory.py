
inventory = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}

def display_inventory(anyInventory):
    print('Inventory:')
    itemTotal = 0
    for k, v in inventory.items():
        
        print (v, k)
        itemTotal += v

    print("Total number of items: " + str(itemTotal))

print (display_inventory(inventory))
