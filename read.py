# read.py
def reading_products(filename = 'products.txt'):
    """
    Reads product details from a text file and stores them in a dictionary.

    Each line in the file represents a single product with attributes
    separated by commas. The function assigns a unique product ID to each product.

    Parameters:
        filename (str): The name of the file containing product data.
                        Here the file is 'products.txt'.

    Returns:
        products: A dictionary where each key is a product ID (int) and each value
              is a list containing the product's details.

    Raises:
        FileNotFoundError: If the specified file does not exist.
              
    Example
        {
            1: ['Vitamin C Serum', 'Garnier', '200', '1000', France],
            2: ['Skin Cleanser', 'Cetaphil', '100', '280', 'Switzerland']
        }
    """
    #empty dictionary to store product details
    products = {}
    try:
        #opening the file containig products detail in reading mode
        with open(filename, "r") as file:
            info = file.readlines()#read each lines from the files
            product_id = 1 #initializing the product id
            #storing the details from files in a dictionary
            for line in info:
                line = line.replace("\n","").split(",") # removing new line characters and splitting data by 
                products[product_id] = line  #using product id as key to store details of products
                product_id = product_id + 1 #increment product_id by 1

    # handles case where file doesnt exist
    except FileNotFoundError:
        print("File not found. Please check the path of file.")

    return products







