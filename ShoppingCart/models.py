import unittest


class Item:

    def __init__(self, product, p_type, price):
        self.name = product
        self.type = p_type
        self.price = price


class Cart:

    def __init__(self, items):
        # items is a dictionary {product:quantity}
        self.items = items

    def item_total(self, item):
        # get total for item
        item_total = item.price * self.items[item]
        if item.type == "confectionery":
            item_total *= 1.2
        return item_total

    def cart_total(self):
        # work out total cart total by getting the sum of the product price*quantity for all items in the dict.
        total_amount = sum(self.item_total(p) for p in self.items)
        return total_amount

    def remove_item(self, item, quantity):
        # remove an item from the cart
        if item in self.items:
            if self.items[item] > quantity:
                self.items[item] -= quantity
            else:
                del self.items[item]
        else:
            print("This item is not in the cart.")

        return self.items


# item1 = Item("Dairy Milk", "confectionery", 0.50)
# item2 = Item("Walkers", "Necessary", 1)
#
# cart = Cart({item1: 2, item2: 3})
# print("The cart total is £{:.2f}".format(cart.cart_total()))
#
# cart.remove_item(item1, 1)
# print("The cart total is now £{:.2f}".format(cart.cart_total()))
