#!/usr/bin/env python3

class CashRegister:
    def __init__(self, discount=0):
        """Initialize a CashRegister object with a discount percentage."""
        self.total = 0
        self.discount = discount
        self.items = []
        self.last_transaction_amount = 0

    def add_item(self, title, price, quantity=1):
        """
        Add an item to the cash register.
        
        Args:
            title (str): The item's name
            price (float): The item's price
            quantity (int): How many of the item (default: 1)
        """
        transaction_amount = price * quantity
        self.total += transaction_amount
        self.last_transaction_amount = transaction_amount
        
        # Add each item individually to the items list
        for _ in range(quantity):
            self.items.append(title)

    def apply_discount(self):
        """
        Apply the discount to the total price.
        Prints a message and returns the discounted total.
        """
        if self.discount == 0:
            print("There is no discount to apply.")
            return "There is no discount to apply."
        
        # Calculate discount amount and apply it
        discount_amount = (self.discount / 100) * self.total
        self.total = self.total - discount_amount
        
        # Print success message with updated total
        print(f"After the discount, the total comes to ${int(self.total)}.")
        return self.total

    def void_last_transaction(self):
        """
        Remove the last transaction from the total.
        """
        self.total -= self.last_transaction_amount