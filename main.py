# main.py
from read import reading_products
from write import writing_products
from operations import sell_product, restock_product

#function to run program
def main():
    """
        This function is the entry point for the WeCare Wholesalenmanagement system.
        It handles the main menu operations including sales, restocking, and exit
    """
    
    print("Welcome to WeCare Wholesale System \n")
    products = reading_products() #load the products
    

    while True:
        #display choice
        print("Enter 1 to sell the product to customer")
        print("Enter 2 to buy from manufacturer")
        print("Enter 3 to exit")
        try:
            choice = int(input("Enter your choice: "))
            if choice == 1:
                sell_product(products)
            elif choice == 2:
                restock_product(products)
            elif choice == 3:
                writing_products(products)
                print("Thank you for using the system.")
                break
            else:
                print("Invalid choice.")
        except ValueError:
            print("Invalid input. Please enter a number.")

if __name__ == "__main__":
    main()
