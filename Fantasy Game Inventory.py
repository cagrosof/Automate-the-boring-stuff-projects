
inven = {"arrow": 12, "gold coin": 42, "rope": 1, "torch": 6, "dagger": 1}


def displayInventory(inventory):
    print("Inventory:")
    item_total = 0
    for k, v in inventory.items():
        print(v," ",k)
        item_total += v
    print("Total number of items: " + str(item_total))   

displayInventory(inven)

    
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']


