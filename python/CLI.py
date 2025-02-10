import re
from datetime import datetime

def validate_date(date_str):
    try:
        datetime.strptime(date_str, '%Y-%m-%d')
        return True
    except ValueError:
        return False

def input_product():
    print("\nEnter Product Details:")
    product_id = int(input("Product ID: "))
    product_name = input("Product Name: ")
    category = input("Category: ")
    cost_price = float(input("Cost Price (₹): "))
    selling_price = float(input("Selling Price (₹): "))
    
    return f"""
    INSERT INTO Products (ProductID, ProductName, Category, CostPrice, SellingPrice)
    VALUES ({product_id}, '{product_name}', '{category}', {cost_price}, {selling_price});
    """

def input_sale():
    print("\nEnter Sale Details:")
    sale_id = int(input("Sale ID: "))
    product_id = int(input("Product ID: "))
    sale_date = input("Sale Date (YYYY-MM-DD): ")
    while not validate_date(sale_date):
        print("Invalid date format! Use YYYY-MM-DD.")
        sale_date = input("Sale Date (YYYY-MM-DD): ")
    quantity = int(input("Quantity Sold: "))
    city = input("City: ")
    state = input("State: ")
    customer_id = int(input("Customer ID: "))
    
    return f"""
    INSERT INTO Sales (SaleID, ProductID, SaleDate, Quantity, City, State, CustomerID)
    VALUES ({sale_id}, {product_id}, '{sale_date}', {quantity}, '{city}', '{state}', {customer_id});
    """

def input_inventory():
    print("\nEnter Inventory Details:")
    inventory_id = int(input("Inventory ID: "))
    product_id = int(input("Product ID: "))
    stock_quantity = int(input("Stock Quantity: "))
    last_restock = input("Last Restock Date (YYYY-MM-DD): ")
    while not validate_date(last_restock):
        print("Invalid date format! Use YYYY-MM-DD.")
        last_restock = input("Last Restock Date (YYYY-MM-DD): ")
    
    return f"""
    INSERT INTO Inventory (InventoryID, ProductID, StockQuantity, LastRestockDate)
    VALUES ({inventory_id}, {product_id}, {stock_quantity}, '{last_restock}');
    """

def main():
    sql_scripts = []
    while True:
        print("\nChoose a table to add data:")
        print("1. Products")
        print("2. Sales")
        print("3. Inventory")
        print("4. Exit")
        choice = input("Enter your choice (1-4): ")
        
        if choice == '1':
            sql = input_product()
            sql_scripts.append(sql)
        elif choice == '2':
            sql = input_sale()
            sql_scripts.append(sql)
        elif choice == '3':
            sql = input_inventory()
            sql_scripts.append(sql)
        elif choice == '4':
            break
        else:
            print("Invalid choice!")
    
    # Save SQL scripts to a file
    with open("insert_queries.sql", "w") as f:
        for sql in sql_scripts:
            f.write(sql + "\n")
    print("\nSQL insert statements saved to insert_queries.sql")

if __name__ == "__main__":
    main()
