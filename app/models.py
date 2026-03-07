from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class Order(BaseModel):
    order_id: int
    student_name: str
    document_name: str
    pages: int
    print_type: str
    total_cost: Optional[float] = None
    created_at: datetime = datetime.now()

    def calculate_cost(self):
        # Prices per page
        cost_per_page = {
            "Black & White": 2.00,
            "Colored": 5.00,
            "Photo Paper": 20.00
        }
        self.total_cost = self.pages * cost_per_page.get(self.print_type, 0)
        return self.total_cost