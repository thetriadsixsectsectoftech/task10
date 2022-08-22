

class Shoe:

    def __init__(self, country,code,product,cost,quantity):
        self.country = country 
        self.code = code
        self.product = product 
        self.cost = cost
        self.quantity = quantity 
    
    def get_cost(self):
        return self.cost
    
    def get_quantity(self):
        return self.quantity
    
    def get_code(self):
        return self.code

    def restock(self, quantity):
        self.quantity = quantity
    
    def __str__(self):
        return f"Country: {self.country}\n"\
        f"Code:{self.code}\n"\
        f"product{self.product}\n"\
        f"cost{self.cost}\n"\
        f"quantity{self.quantity}\n"
######################class code block###########################

#The code starts with the class definition.
#It takes four parameters: self, country, code, and product.
#The get_cost method returns the cost for the item
#The get_quantity method returns how many items 




def read_shoes_data():
    try:
        with open("inventory.txt", "r+", encoding="utf-8") as log_file:
        #    # log_file.seek(0)
            log_file.readline()
            for line in log_file:
                data = line.replace("\n", "").split(",")
                shoe = Shoe(data[0],data[1],data[2],int(data[3]),int(data[4]))
                shoe_details.append(shoe)     
    except FileNotFoundError:
        print("oops maybe this file doent exist")
        pass
###########################read_Shoes_data function###########################
#The code opens the file "inventory.txt" and reads in one line at a time using the with open function.
#The code then splits up each line into an individual string of data, which is then stored in a list called shoe_details.




def capture_shoes():
    shoe_country = input("which country is this shoe from?: ")
    shoe_code = input("please enter the shoe product code: ")
    shoe_name = input("what is the name of the shoe?: ")
    shoe_cost = int(input("how much does this hsoe cost?: "))
    shoe_quant = int(input("how many of these shoes do you have in stock?: "))

    shoe_obj = Shoe(shoe_country, shoe_code, shoe_name, shoe_cost, shoe_quant)

    shoe_details.append(shoe_obj)


def view_all():
    for onbect in shoe_details:
        print(onbect)
        



def update_file():
    with open("inventory.txt", "w") as write_file:
        for shoe in shoe_details:
            output = f"Country: {shoe.country}, "\
                f"Code:{shoe.code}, "\
                f"product{shoe.product}, "\
                f"cost{shoe.cost}, s"\
                f"quantity{shoe.quantity}\n"

            write_file.write(output)

            

def re_stock():
    


    minimum_quantity = shoe_details[0]


    for object in shoe_details:

        if int(object.get_quantity()) < int(minimum_quantity.get_quantity()):
            minimum_quantity = object

    
    user_input = input("would you like to update the quantitiy of this object yes or no: ")
    
    if user_input == "yes":

        shoe_restock = int(input("how many new pairs of shoes do you want to add?: "))

        updated_quantity = int(minimum_quantity.quantity) + shoe_restock
        minimum_quantity.restock(updated_quantity)
        

        update_file()
        
    else:
        pass

def search_shoe():
    user_input = input("please enter the shoes code to return it:")

    for object in shoe_details:
        if object.get_code() == user_input:
            print(object)


     

    ##### code block to loop through all shoe list to have minimum_quantity have the lowerst###############

def value_per_item():
    total_cost = 0 


    for object in shoe_details:
        value = object.get_cost() * object.get_quantity()
        total_cost += value

    print(f"the total number cost of all shoes in stock are R{total_cost}")

def highest_qty():
    maximum_quantity = shoe_details[0]


    for object in shoe_details:

        if int(object.get_quantity()) > int(maximum_quantity.get_quantity()):
            maximum_quantity = object
    print(f"""{maximum_quantity} 
                is on special!!!!!!!!!!!!!!!""")

shoe_details = []
read_shoes_data()

while True:
    # presenting the menu to the user and
    # making sure that the user input is coneverted to lower case.

    menu = input('''Select one of the following Options below:

    cs - capture shoe entry
    va - View all shoes
    rs - restock shoes
    ss - search shoes
    vpi - value for shoes
    hq - highest quality
    e - Exit
    : ''').lower()

        

    if menu == 'cs':
        capture_shoes()

    elif menu == 'va':
        view_all()

    elif menu == 'rs':
        re_stock()

    elif menu == 'ss':
        search_shoe()

    elif menu == 'vpi':
        value_per_item()
    
    elif menu == 'hq':
        highest_qty()
    
    elif menu == 'psl':
        print(shoe_details)
        
        
    elif menu == "e":
        break
