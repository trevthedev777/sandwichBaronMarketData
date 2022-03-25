import gspread #imports the entire gspread library so we can access any data and / or classes inside our worksheets
from google.oauth2.service_account import Credentials #imports the Credentials classs from service_acount() from google auth library
from pprint import pprint


#Constant Variables
SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('love_sandwiches_final')

def get_sales_data():
    """ 
    Get sales figures input from user.
    Run a while loop to collect a valid string of data from the user
    via the terminal, which must be a string of 6 numbers seperated
    by commas. The loop will repeatedly request data, until it is valid
    """
    while True:
        print('Please enter your sales data from the last sales day')
        print('Data should be six numbers, seperated by commas(CSV).')
        print('Example: 10, 20, 30, 40, 50, 60\n')

        data_str = input('Enter your data here: ') #User inputs data here

        sales_data = data_str.split(',') #will remove commas from the string, the split() method returns the broken up values as a list
        
        if validate_data(sales_data):
            print('Data is valid')
            break

    return sales_data


def validate_data(values):
    """
    Inside the try, converts all string values into integers.
    Raises ValueError if strings cannot be converted into int,
    or if there aren't exactly 6 values
    """
    try:
       [int(value) for value in values]# for each value in values, convert to integers
       if len(values) != 6:
           raise ValueError(
               f'Exactly 6 values required, you provided {len(values)}'
           )
    except ValueError as e:
        print(f'Invalid data: {e}, please try again.\n')
        return False

    return True


# def  update_sales_worksheet(data):
#     """
#     Update sales worksheet, add new row with the list data provided
#     """
#     print('Updating sales worksheet....\n')
#     sales_worksheet = SHEET.worksheet('sales')
#     sales_worksheet.append_row(data)
#     print('Sales worksheet updated successfully.\n')

# def  update_surplus_worksheet(data):
#     """
#     Update surplus worksheet, add new row with the list data provided
#     """
#     print('Updating surplus worksheet....\n')
#     surplus_worksheet = SHEET.worksheet('surplus')
#     surplus_append_row(data)
#     print('Surplus worksheet updated successfully :).\n')



def calculate_surplus_data(sales_row):
    """
    Compare sales with stock and calculate the surplus for each item type.

    The surplus is defines as the sales figure subtracted from the stock:
    - Positive surplus indicates waste
    - Negative Surplus indicates extra made when stock was sold out
    """
    print('Calculating surplus data....\n')
    stock = SHEET.worksheet('stock').get_all_values()
    stock_row = stock.pop()
    
    surplus_data = []
    for stock, sales in zip(stock_row, sales_row):
        surplus = int(stock) - sales
        surplus_data.append(surplus)

    return surplus_data


def get_five_last_entries_sales():
    """
    Collects the columns of data from sales worksheet, collecting 
    the last 5 entries for each sandwich and returmns the data as a list of lists.
    """
    sales = SHEET.worksheet('sales')

    columns = []
    for ind in range(1, 7):
        column = sales.col_values(ind)
        columns.append(column[-5:])
    
    return columns

def update_worksheet(data, worksheet):
    """
    Receives a list of integers to be inserted into a worksheet
    Update the relevant worksheet with the data provided
    """
    print(f'Updating {worksheet} worksheet...\n')
    worksheet_to_update = SHEET.worksheet(worksheet)
    worksheet_to_update.append_row(data)
    print(f'{worksheet} worksheet updated successfully.\n')

def main():
    """
    Run all program functions
    """
    #Collects data from sheets document
    data = get_sales_data()
    #for each num in data, convert to integers
    sales_data = [int(num) for num in data] 
    #adds user input data to new row in worksheet
    update_worksheet(sales_data, 'sales') 
    #calculates the sales and the stock
    new_surplus_data = calculate_surplus_data(sales_data) 
    #returns the calulation of new_surplus_data and appends to surplus worksheet
    update_worksheet(new_surplus_data, 'surplus')
    print(new_surplus_data)


print('Welcome to Sandwich Baron Data Automation')
# main()
get_five_last_entries_sales()