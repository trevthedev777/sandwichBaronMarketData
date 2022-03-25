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
    print('Please enter your sales data from the last sales day')
    print('Data should be six numbers, seperated by commas(CSV).')
    print('Example: 10, 20, 30, 40, 50, 60\n')

    data_str = input('Enter your data here: ')
    print(f'The data provided is {data_str}')

get_sales_data()