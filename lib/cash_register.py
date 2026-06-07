#!/usr/bin/env python3

class CashRegister:
    def __init__(self, discount=0):
        self.discount = discount
        self.total = 0
        self.items = []
        self.last_transaction_amount = 0
        self.last_transaction_items = []

    def add_item(self, title, price, quantity=1):
        transaction_total = price * quantity
        self.total += transaction_total
        self.last_transaction_amount = transaction_total
        self.last_transaction_items = [title] * quantity
        self.items.extend(self.last_transaction_items)

    def apply_discount(self):
        if self.discount <= 0:
            print("There is no discount to apply.")
            return

        discount_amount = self.total * (self.discount / 100)
        self.total -= discount_amount
        if self.total.is_integer():
            total_display = int(self.total)
        else:
            total_display = self.total
        print(f"After the discount, the total comes to ${total_display}.")

    def void_last_transaction(self):
        self.total -= self.last_transaction_amount
        if self.total < 0:
            self.total = 0.0

        for item in self.last_transaction_items:
            if item in self.items:
                self.items.remove(item)

        self.last_transaction_amount = 0
        self.last_transaction_items = []
