from fastapi import FastAPI
from .models import Order
from .database import load_orders, save_order
from pydantic import BaseModel
from typing import List
from datetime import datetime

app = FastAPI(title="EazyPrint Printing Management System")

class OrderCreate(BaseModel):
    student_name: str
    document_name: str
    pages: int
    print_type: str  # must be "Black & White", "Colored", or "Photo Paper"

@app.post("/orders/", response_model=Order)
def create_order(order: OrderCreate):
    # Create new Order object
    new_order = Order(
        order_id=len(load_orders()) + 1,
        student_name=order.student_name,
        document_name=order.document_name,
        pages=order.pages,
        print_type=order.print_type,
        created_at=datetime.now()
    )

    # Calculate total cost based on print type
    new_order.calculate_cost()

    # Save order
    save_order(new_order)

    return new_order

@app.get("/orders/", response_model=List[Order])
def get_order_summary():
    return load_orders()