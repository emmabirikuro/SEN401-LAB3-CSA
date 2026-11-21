"""
Main application for the Inventory Management System.
"""

from inventory import inventory

from utils.helpers import highest_stock_value_item 

def calculate_total_stock_value():
    """Calculate the total value of all inventory items."""
    total = 0

    for item in inventory:
        total += item["quantity"] * item["price"]

    return total


def main():
    """Display inventory records and summary information."""
    print("\n====== INVENTORY MANAGEMENT SYSTEM ======")

    for item in inventory:
        item_value = item["quantity"] * item["price"]

        print(
            f"{item['item_name']} | "
            f"Quantity: {item['quantity']} | "
            f"Price: ₦{item['price']:,} | "
            f"Stock Value: ₦{item_value:,}"
        )

    print("\nTotal Stock Value: ₦{:,.2f}".format(
        calculate_total_stock_value()
    ))

    highest_item = highest_stock_value_item(inventory)

    if highest_item:
        print(
            f"\nMost Valuable Item: {highest_item['item_name']} "
            f"(₦{highest_item['quantity'] * highest_item['price']:,})"
        )


if __name__ == "__main__":
    main()