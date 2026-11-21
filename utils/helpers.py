"""
Helper functions for inventory operations.
"""

def highest_stock_value_item(inventory):
    """Return the inventory item with the highest total stock value."""
    if not inventory:
        return None

    return max(
        inventory,
        key=lambda item: item["quantity"] * item["price"]
    )