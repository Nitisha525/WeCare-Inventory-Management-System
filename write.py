#write.py
from datetime import datetime

#function to write products data to the file after it is updated
def writing_products(products, filename="products.txt"):
     """
    Writes product data to the text file.

    Each product's details in a list are joined by commas
    and written to the specified file.

    Parameters:
        products (dict): Dictionary where each value is a list and represents a product's details.
        filename (str): Name of the file to write the product data. here the file is 'products.txt'.

    Returns:
        None

    Raises:
        Exception: If an unexpected error occurs while writing to the file.
    """
     try:
        with open(filename, 'w') as file:  #opening file in writing mode
            for item in products.values(): #iterationg through the products
                #converts the list to string
                line = ",".join(item)
                file.write(line + "\n")
     except Exception as e:
        print("Error while writing to file:", e)

#function to generate invoice after each transaction
def invoice_generation(transaction_type, customer_name, phone_number, items, total, free_items = None):
    """
    Generates a transaction invoice and saves it to a text file.

    The invoice includes customer info, transaction time, item details, and total amount.

    Parameters:
        transaction_type (str): Type of transaction (e.g., 'sales' or 'purchase').
        customer_name (str): Name of the customer.
        phone_number (str): Customer's phone number.
        items (list of dict): List of item dictionaries with keys: 
        total (float): The total amount of the transaction.

    Returns:
        None

    Raises:
        Exception: If an error occurs while writing to file writing.
    """
    
    try:
        now = datetime.now() #get current date and time
        #create timestamp
        timestamp = (str(now.year) + str(now.month) + str(now.day) + "_" + str(now.hour) + str(now.minute) + str(now.second))
        filename = transaction_type + "_invoice_" + timestamp + ".txt"   #defining filename
        invoice_details = []
       
        invoice_details.append("WeCare Wholesale\n")
        invoice_details.append("Kamalpokhari, Kathmandu | Phone No: 9875643256\n")
        invoice_details.append(transaction_type.upper() + " INVOICE\n")
        invoice_details.append("Transaction Date: " + str(now.year) + "-" + str(now.month) + "-" + str(now.day) + " \tTransaction Time: " + str(now.hour) + ":" + str(now.minute) + ":" + str(now.second) + "\n")
        invoice_details.append("Customer Name: " + customer_name + "\nPhone Number: " + phone_number + "\n")
        invoice_details.append("-" * 80 + "\n")

        for item in items:
             invoice_details.append("Product Name: " + item['product_name'])
             invoice_details.append("Brand: " + item['brand'])
             invoice_details.append("Quantity: " + str(item['quantity']))
             
             if transaction_type == "sale":
                   invoice_details.append("Free items (Buy 3 Get 1 Free offer): " + str(free_items))
                   
             invoice_details.append("Unit Price: Rs. " + str(item['unit_price']))
             invoice_details.append("Total Price: Rs. " + str(item['total']))
             invoice_details.append("-" * 40)
            
        
        invoice_details.append("Grand Total: Rs. " + str(total) + "\n")

        # save invoice to file
        with open(filename, "w") as file: #opening file in writing mode to write invoice
             for line in invoice_details:
                  file.write(line + "\n")

        # Print on screen
        print("\n" + "\n".join(invoice_details))  # Display invoice
          
        print("Your " + transaction_type + " invoice has been saved \n")

    except Exception as e:
        print("Error generating invoice:", e)
