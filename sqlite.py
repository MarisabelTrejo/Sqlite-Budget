import sqlite3


# File path
connection = sqlite3.connect('budgeting.db')

# Cursor obect calls execute() method
cursor = connection.cursor()

# Create table for purchase
CREATE_PURCHASE_TABLE = "CREATE TABLE IF NOT EXISTS purchase (id INTEGER PRIMARY KEY, purchase_type CHAR, amount REAL, purchase_date CHAR );"

# Insert purchase
INSERT_PURCHASE = "INSERT INTO purchase (purchase_type, amount, purchase_date) VALUES(?, ?, ?);"

# Get all purchases
GET_ALL_PURCHASE = "SELECT * FROM purchase;"

# Get a purchase by name
GET_PURCHASE_BY_NAME = "SELECT * FROM purchase WHERE purchase_type = ?;"

# Get a purchase by date
GET_PURCHASE_DATE = "SELECT DATE(purchase_date), purchase_type, PRINTF('$%.2F', amount) FROM purchase WHERE purchase_date = ?;"

# Update a purchase
UPDATE_PURCHASE = "UPDATE purchase SET amount = ? WHERE id = ?;"

#Delete a purchase
DELETE_PURCHASE = "DELETE FROM purchase WHERE id = ?;"

# Biggest and smallest purchase
MAX_PURCHASE ="SELECT MAX(amount), purchase_type FROM purchase;"
MIN_PURCHASE = "SELECT MIN(amount), purchase_type FROM purchase;"


# Create table for deposits
CREATE_DEPOSIT_TABLE =  "CREATE TABLE IF NOT EXISTS deposits (id INTEGER PRIMARY KEY, amount REAL, deposit_date CHAR);"

INSERT_DEPOSIT = "INSERT INTO deposits (amount, deposit_date) VALUES(?, ?);"

GET_ALL_DEPOSITS = "SELECT * FROM deposits"

def connect():
    return sqlite3.connect('budgeting.db')

def create_tables(cursor):
    with cursor:
        cursor.execute(CREATE_PURCHASE_TABLE)
        cursor.execute(CREATE_DEPOSIT_TABLE)

def add_purchase(cursor, purchase_type, amount, purchase_date):
    with cursor:
        cursor.execute(INSERT_PURCHASE, (purchase_type, amount, purchase_date))

def get_all_purchase(cursor):
    with cursor:
        return cursor.execute(GET_ALL_PURCHASE).fetchall()

def get_purchase_by_name(cursor, purchase_type):
    with cursor:
        return cursor.execute(GET_PURCHASE_BY_NAME, (purchase_type,)).fetchall()

def get_purchase_date(cursor, purchase_date):
    with cursor:
        return cursor.execute(GET_PURCHASE_DATE, (purchase_date,)).fetchall()

def update_purchase(cursor, amount, id):
    with cursor:
        cursor.execute(UPDATE_PURCHASE, (amount, id))
    
def add_deposit(cursor, amount, deposit_date):
    with cursor:
        cursor.execute(INSERT_DEPOSIT, (amount, deposit_date))

def get_all_deposits(cursor):
    with cursor:
        return cursor.execute(GET_ALL_DEPOSITS).fetchall()

def delete_purchase(cursor, id):
    with cursor:
        cursor.execute(DELETE_PURCHASE, (id,))

def max_purchase(cursor):
    with cursor:
        return cursor.execute(MAX_PURCHASE)

def min_purchase(cursor):
    with cursor:
        return cursor.execute(MIN_PURCHASE)




