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

sales = SHEET.worksheet('sales') #access the sales data in the worksheet

data = sales.get_all_values() #pulls the values from the sales worksheet

print(data)