#operations.py
from write import invoice_generation, writing_products

#function to handle product sale
def sell_product(products):
    """
    Control the process of selling products.
   

    Parameters:
        products (dict): Dictionary of product details with product IDs as keys.

    Returns:
        None

    Raises:
        Exception: If an unexpected error occurs during the selling process.
    """
    try:
        while True:
            customer_name = input("Enter the customer's name: ")
            if customer_name.replace(" ", "").isalpha() and len(customer_name) > 2:
                break
            else:
                print("Please enter a valid name.")
        while True:
            phone_number = input("Enter customer's phone number: ")
            if phone_number.isdigit() and len(phone_number) == 10:
                break
            else:
                print("Please enter a valid phone number.")

            
        cart = [] #list to store the sold items
        grand_total = 0
        

        while True:
            print("We have the following products available \n")
            #printing the headers to display products
            print("ID  \t\tProduct Name   \t\t Brand  \t\tQuantity  \t Price  \t Country of Origin \n")

            #opening the file again in reading mode to display the product details
            file = open("products.txt", "r") #opening file to display products

            #initializing the no of items
            items = 1

            #reading each line from file and then displaying it
            for line in file:
                line = line.replace("\n", "")
                info = line.split(",")
                print(str(items) + "\t\t" + info[0] + "\t\t" + info[1] + "\t\t" + info[2] + "\t\t" + info[3] + "\t\t" + info[4] + "\n") #displaying the product details
                items = items + 1

            while True:
                enter_product_id = input("Enter product ID of the product you want to sell: ")
                if enter_product_id.isdigit():
                    product_id = int(enter_product_id)
                    if product_id in products:
                        break
                    else:
                        print("The ID you entered does not exist. Please enter a valid product ID.")
                else:
                    print("Invalid input. Please enter the product ID in positive number format.")

            while True:
                enter_qty = input("Enter quantity of product you want to sell: ")
                if enter_qty.isdigit() and int(enter_qty) > 0:
                    quantity = int(enter_qty)
                    break
                else:
                    print("Invalid input. Please enter a positive number for quantity.")
                    
            stock = int(products[product_id][2]) #current stock
            free_items = quantity // 3 #buy three get one free offer
            total_required = quantity + free_items # total items to be deducted from stock

            print("Dear", customer_name, "we are having buy 3 get one free offer, you have received", free_items, "free on this purchase.")

            if total_required > stock:
                print("Sorry, the stock for this product is not sufficient.\n")
                continue
            
            #update stock
            products[product_id][2] = str(stock - total_required)
            price_per_piece = int(products[product_id][3]) * 2 #selling price = cost price * 2
            item_total_price = price_per_piece * quantity #total price for the products
            grand_total += item_total_price

            #add to card
            cart.append({
                "product_name": products[product_id][0],
                "brand": products[product_id][1],
                "quantity": quantity,
                "unit_price": price_per_piece,
                "total": item_total_price
            })

            writing_products(products) # save the updated stock to file

            while True:
                more_items_to_sell = input("Do you want to sell more items? (yes/no): ").lower()
                if more_items_to_sell in ['yes', 'no']:
                    break
                else:
                    print("Invalid input. Please enter 'yes' or 'no'.")

            if more_items_to_sell == 'no':
                break

            
        #generate invoice
        invoice_generation("sale", customer_name, phone_number, cart, grand_total, free_items)
        display_updated_products()

    
    except Exception as e:
        print("An error occurred during selling: " + str(e))

#handles restocking of products
def restock_product(products):
    """
    Controls the process of restocking products from a manufacturer.

    
    Parameters:
        products (dict): Dictionary of product details with product IDs as keys.

    Returns: None

    Raises:
        Exception: If an unexpected error occurs during the restocking process.
    """
    try:
        while True:
            seller_name = input("Enter the seller's name: ")
            if seller_name.replace(" ", "").isalpha() and len(seller_name) > 2:
                break
            else:
                print("Please enter a valid name.")
        while True:
            phone_number = input("Enter customer's phone number: ")
            if phone_number.isdigit() and len(phone_number) == 10:
                break
            else: 
                print("Please enter a valid phone number.")
                
        cart = []
        total_cost = 0

        while True:
            print("We have the following products available\n")
            #printing the headers to display products
            print("ID  \t\tProduct Name   \t\t Brand  \t\tQuantity  \t Price  \t Country of Origin \n")

            #opening the file again in reading mode to display the product details
            file = open("products.txt", "r")

            #initializing the no of items
            items = 1

            #reading each line from file and then displaying it
            for line in file:
                line = line.replace("\n", "")
             
                info = line.split(",")
                print(str(items) + "\t\t" + info[0] + "\t\t" + info[1] + "\t\t" + info[2] + "\t\t" + info[3] + "\t\t" + info[4]+ "\n") #displaying the product details
                items = items + 1

            while True:
                enter_product_id = input("Enter product ID of the product you want to restock: ")
                if enter_product_id.isdigit():
                    product_id = int(enter_product_id)
                    if product_id in products:
                        break
                    else:
                        print("The ID you entered does not exist. Please enter a valid product ID.")
                else:
                    print("Invalid input. Please enter the product ID in positive number format.")

            while True:
                enter_qty = input("Enter quantity of product you want to restock: ")
                if enter_qty.isdigit() and int(enter_qty) > 0:
                    quantity = int(enter_qty)
                    break
                else:
                    print("Invalid input. Please enter a positive number for quantity.")
            cost_per_piece = int(products[product_id][3]) #cost price
            total = cost_per_piece * quantity #total price
            total_cost += total

            # Update stock
            products[product_id][2] = str(int(products[product_id][2]) + quantity)

            cart.append({
                "product_name": products[product_id][0],
                "brand": products[product_id][1],
                "quantity": quantity,
                "unit_price": cost_per_piece,
                "total": total
            })

            writing_products(products) #save updated stock to file
    
            while True:
                more_items_to_stock = input("Do you want to stock more items? (yes/no): ").lower()
                if more_items_to_stock in ['yes', 'no']:
                    break
                else:
                    print("Invalid input. Please enter 'yes' or 'no'.")

            if more_items_to_stock == 'no':
                break

        invoice_generation("restock", seller_name, phone_number, cart, total_cost)
        display_updated_products()

    except Exception as e:
        print("Error during restocking:", e)

def display_updated_products():
    """
    Reads and displays the updated products list from 'products.txt' file.

    Parameters: none

    Returns: none

    Raises:
        Exception: if the file is not found or there is an issue while displaying products.
    """
    
    try:
        print("\nUpdated Product List:\n")
        print("ID  \t\tProduct Name   \t\t Brand  \t\tQuantity  \t Price  \t Country of Origin \n")
        with open("products.txt", "r") as file:
            items = 1
            for line in file:
                line = line.replace("\n", "")
             
                info = line.split(",")
                print(str(items) + "\t\t" + info[0] + "\t\t" + info[1] + "\t\t" + info[2] + "\t\t" + info[3] + "\t\t" + info[4]+ "\n") #displaying the product details
                items = items + 1

    except Exception as e:
        print("Error displaying products:", e)
