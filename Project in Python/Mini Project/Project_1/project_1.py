from collections import defaultdict
from datetime import datetime

def get_order_data(permission):
    
    if permission == 1:
        # Default order data set
        orders = [
            {"customer_id": 1, "order_date": "2024-08-01", "order_amount": 150},
            {"customer_id": 5, "order_date": "2024-08-03", "order_amount": 500},
            {"customer_id": 1, "order_date": "2024-08-05", "order_amount": 350},
            {"customer_id": 3, "order_date": "2024-08-07", "order_amount": 120},
            {"customer_id": 4, "order_date": "2024-08-09", "order_amount": 300},
            {"customer_id": 2, "order_date": "2024-08-11", "order_amount": 300},
            {"customer_id": 3, "order_date": "2024-08-13", "order_amount": 400},
            {"customer_id": 2, "order_date": "2024-08-15", "order_amount": 250},
            {"customer_id": 1, "order_date": "2024-08-17", "order_amount": 200},
            {"customer_id": 4, "order_date": "2024-08-01", "order_amount": 550},
            {"customer_id": 2, "order_date": "2024-08-03", "order_amount": 200},
            {"customer_id": 1, "order_date": "2024-08-05", "order_amount": 350},
            {"customer_id": 3, "order_date": "2024-08-07", "order_amount": 120},
            {"customer_id": 1, "order_date": "2024-08-09", "order_amount": 100},
            {"customer_id": 4, "order_date": "2024-08-11", "order_amount": 360},
            {"customer_id": 2, "order_date": "2024-08-13", "order_amount": 400},
            {"customer_id": 2, "order_date": "2024-08-15", "order_amount": 250},
            {"customer_id": 5, "order_date": "2024-08-17", "order_amount": 200},
        ]
        start_date = "2024-08-01"
        end_date = "2024-08-15"
        
    elif permission == 2:
        # Custom data input
        orders = []
        num_orders = int(input("Enter the number of orders: "))
        
        for _ in range(num_orders):
            customer_id = int(input("Enter customer ID: "))
            order_date = input("Enter order date (YYYY-MM-DD): ")
            order_amount = float(input("Enter order amount: "))
            orders.append({"customer_id": customer_id, "order_date": order_date, "order_amount": order_amount})
        
        start_date = input("Enter start date (YYYY-MM-DD): ")
        end_date = input("Enter end date (YYYY-MM-DD): ")

    else:
        print("Please select 1 or 2.\nThank you.")
        return None, None, None
    
    return orders, start_date, end_date

def analyze_orders(orders, start_date, end_date):
    """
    Analyze orders to find the customer(s) with the most orders and their total spending.
    
    Args:
    orders (list): List of orders.
    start_date (str): Start date for filtering orders.
    end_date (str): End date for filtering orders.
    
    Returns:
    list: List of top customers with the most orders.
    dict: Dictionary of customer order counts.
    dict: Dictionary of customer spending totals.
    """
    customer_order_count = defaultdict(int)
    customer_spending = defaultdict(int)

    for order in orders:
        order_date = order["order_date"]
        if start_date <= order_date <= end_date:
            customer_order_count[order["customer_id"]] += 1
            customer_spending[order["customer_id"]] += order["order_amount"]

    max_orders = max(customer_order_count.values(), default=0)
    top_customers = [customer for customer, count in customer_order_count.items() if count == max_orders]

    return top_customers, customer_order_count, customer_spending

def print_customer_summary( top_customers, customer_order_count, customer_spending, start_date, end_date):
    """
    Print the summary of top customers.
    
    Args:
    top_customers (list): List of top customers.
    customer_order_count (dict): Dictionary of customer order counts.
    customer_spending (dict): Dictionary of customer spending totals.
    start_date (str): Start date for filtering orders.
    end_date (str): End date for filtering orders.
    """
    for customer in top_customers:
        print(f"Customer {customer} placed the most orders ({customer_order_count[customer]}) "
              f"with total spending of {customer_spending[customer]} during the period {start_date} to {end_date}.")

def main():
    permission = int(input("Can you use the default data set?\n1. Yes\n2. No\n~ "))
    orders, start_date, end_date = get_order_data(permission)
    
    if orders:
        top_customers, customer_order_count, customer_spending = analyze_orders(orders, start_date, end_date)
        print_customer_summary(top_customers, customer_order_count, customer_spending, start_date, end_date)

if __name__ == "__main__":
    main()

