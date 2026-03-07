# EazyPrint Application

EazyPrint is a FastAPI application designed to manage printing orders for students. It allows users to create and retrieve printing orders, with a focus on simplicity and efficiency.

## Project Structure

```
eazyprint
├── app
│   ├── main.py          # Entry point of the FastAPI application
│   ├── models.py        # Defines the data model for printing orders
│   ├── database.py      # Handles file-based database operations
│   └── routers
│       └── __init__.py  # Sets up the application routes
├── requirements.txt     # Lists project dependencies
└── README.md            # Documentation for the project
```

## Setup Instructions

1. **Clone the repository:**
   ```
   git clone <repository-url>
   cd eazyprint
   ```

2. **Install dependencies:**
   It is recommended to use a virtual environment. You can create one using:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```
   Then install the required packages:
   ```
   pip install -r requirements.txt
   ```

3. **Run the application:**
   Start the FastAPI application using Uvicorn:
   ```
   uvicorn app.main:app --reload
   ```

## Usage

- **Create a new printing order:**
  Send a POST request to `/orders` with the order details in JSON format.

- **Get order summary:**
  Send a GET request to `/orders/{order_id}` to retrieve the summary of a specific order.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.