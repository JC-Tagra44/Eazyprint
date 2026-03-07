import json
import os
from .models import Order

# Ensure the storage folder exists
storage_folder = os.path.join(os.path.dirname(__file__), "storage")
if not os.path.exists(storage_folder):
    os.makedirs(storage_folder)

orders_file_path = os.path.join(storage_folder, "orders.json")

def load_orders():
    if os.path.exists(orders_file_path):
        with open(orders_file_path, "r") as f:
            data = json.load(f)
            return [Order(**order) for order in data]
    return []

def save_order(order: Order):
    orders = load_orders()
    orders.append(order)
    with open(orders_file_path, "w") as f:
        json.dump([order.dict() for order in orders], f, default=str)