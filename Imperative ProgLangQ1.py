inventory = {
    "laptop": {"price": 899.99, "quantity": 5},
    "mouse": {"price": 19.99, "quantity": 42},
    "keyboard": {"price": 49.50, "quantity": 8},
    "monitor": {"price": 229.00, "quantity": 3},
    "webcam": {"price": 59.95, "quantity": 15}
}

def check_low_stock(threshold):
    print("Items with stock below", threshold, ":")
    for item, info in inventory.items():
        if info["quantity"] < threshold:
            print("•", item, "- quantity:", info["quantity"], "- price: $", info["price"])

# Main program
check_low_stock(10)