import configparser
import psycopg2
import pandas as pd
import datetime
import hashlib
import sys

# is_duplicate function computes the SHA-256 hash of the contents of the file and 
# compares it to the hashes of previously processed files, 
# stored in a text file called hashes.txt (need to be externalised to DB)
def is_duplicate(filename):
    with open(filename, 'rb') as file:
        file_contents = file.read()
        file_hash = hashlib.sha256(file_contents).hexdigest()

    with open('hashes.txt', 'r') as hashes:
        for line in hashes:
            if file_hash == line.strip():
                return True

    with open('hashes.txt', 'a') as hashes:
        hashes.write(file_hash + '\n')

    return False


filename = 'input_sheet.xlsx'
if is_duplicate(filename):
    print('The file is a duplicate.')
    sys.exit()
else:
    print('The file is not a duplicate.')
    
    
# Read data from the spreadsheet into a pandas DataFrame
df = pd.read_excel(filename)

config = configparser.ConfigParser()
config.read('config.ini')

conn = psycopg2.connect(
    host=config['postgresql']['host'],
    database=config['postgresql']['database'],
    user=config['postgresql']['user'],
    password=config['postgresql']['password'],
    port=config['postgresql']['port']
)

# rest of the code to execute queries, fetch data, etc.
cur = conn.cursor()

number_inserted = 0
# Insert data from the DataFrame into the table
for index, row in df.iterrows():
    try:
        cur.execute (f"INSERT INTO public.accounts (user_id, username, password, email, created_on, last_login) \
                    VALUES (DEFAULT, '{row['username']}', '{row['password']}', '{row['email']}', '{datetime.datetime.now()}', '{datetime.datetime.now()}')")
        conn.commit()
        number_inserted +=1
    
    except (Exception, psycopg2.DatabaseError) as error:
        print(f"Error inserting record: {error}")
        conn.rollback()
print(f"Total number of data inserted {number_inserted}")
conn.close()



