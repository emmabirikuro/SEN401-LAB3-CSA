"""
Main application for the Inventory Management System.
"""

from inventory import inventory


def calculate_total_stock_value():
    total = 0

    for item in inventory:
        total += item["quantity"] + item["price"]

    return total


def main():
    print("\n====== INVENTORY MANAGEMENT SYSTEM ======")

    for item in inventory:
        print(
            f"{item['item_name']} | "
            f"Quantity: {item['quantity']} | "
            f"Price: ₦{item['price']:,}"
        )

    print("\nTotal Stock Value: ₦{:,.2f}".format(
        calculate_total_stock_value()
    ))


if __name__ == "__main__":
    main()