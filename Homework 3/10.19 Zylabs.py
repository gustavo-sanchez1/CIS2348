#  Gustavo Sanchez PSID:1861118
class ItemToPurchase:  # class name
    def __init__(self):
        self.item_name = "none"  # attributes
        self.item_price = 0
        self.item_quantity = 0
        self.item_description = "none"

    def print_item_cost(self):  # get percentage of wins
        print(self.item_name + ' ' + str(self.item_quantity) + " @ $" + str(self.item_price) + " = $" +
              str(self.item_price * self.item_quantity))

    def print_item_description(self):  # item description
        string = '{}: {}'.format(self.item_name, self.item_description)
        print(string)
        return string


print('Item 1')  # input item 1
item1 = ItemToPurchase()
item2 = ItemToPurchase()
print("Enter the item name:")
item1.item_name = input()
print('Enter the item price:')
item1.item_price = int(input())
print('Enter the item quantity:')
item1.item_quantity = int(input())

print('\nItem 2')  # input item 2
print('Enter the item name:')
item2.item_name = input()
print('Enter the item price:')
item2.item_price = int(input())
print('Enter the item quantity:')
item2.item_quantity = int(input())

print('\nTOTAL COST')  # print total cost
item1.print_item_cost()
item2.print_item_cost()

total_cost = (item1.item_price * item1.item_quantity) + (item2.item_price * item2.item_quantity)
print('\nTotal: $' + str(total_cost))
