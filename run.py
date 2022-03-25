import gspread #imports the entire gspread library so we can access any data and / or classes inside our worksheets
from google.oauth2.service_account import Credentials #imports the Credentials classs from service_acount() from google auth library


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
    |Get sales figures input from user
    """
    while True:
        print('Please enter your sales data from the last sales day')
        print('Data should be six numbers, seperated by commas(CSV).')
        print('Example: 10, 20, 30, 40, 50, 60\n')

        data_str = input('Enter your data here: ') #User inputs data here

        sales_data = data_str.split(',') #will remove commas from the string, the split() method returns the broken up values as a list
        validate_data(sales_data)

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
       [int(value) for value in values]
       if len(values) != 6:
           raise ValueError(
               f'Exactly 6 values required, you provided {len(values)}'
           )
    except ValueError as e:
        print(f'Invalid data: {e}, please try again.\n')
        return False

    return True
data = get_sales_data()