import time

inventory=["sword","armor","shield","healing potion"]
time.sleep(1)
print(inventory)
print(len(inventory))
print("trade the sword with an axe")
inventory[0]="axe"
print(inventory)
for item in inventory:
    print(item)

chest=["coins","gold"]
print("Picked items from chest")
inventory+=chest
print(inventory)

if "healing potion" in inventory:
    print("you can still fight")


print("used your coins and gold to buy fire orb")
inventory[4:6]=["fire orb"]
print(inventory)
print("your shield is destroyed")
print(inventory.index("shield"))
del inventory[2]
print(inventory)


#delete a slice
print("healing potion and your fire orb was stolen")
del inventory[2:4]
print(inventory)

