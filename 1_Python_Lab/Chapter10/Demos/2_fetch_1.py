import pyodbc

conn_str = ('DRIVER={SQL Server Native Client 11.0};'
    'SERVER=DATA\SQLEXPRESS;'
    'DATABASE=AdventureWorksLT2016;'
    'TRUSTED_CONNECTION=yes;')
conn = pyodbc.connect(conn_str)
query = '''
        select top(5) CustomerID,FirstName,MiddleName,LastName,CompanyName,EmailAddress,Phone 
from SalesLT.Customer
where CustomerID=1
        '''
cursor = conn.cursor()
cursor.execute(query)
results = cursor.fetchone()
if results:
    cust_full_name = results.FirstName + ' ' + results.MiddleName + ' ' + results.LastName
    Email = results.EmailAddress
    phone = results.Phone

    print(f'{cust_full_name} {Email} {phone}')
else:
    print('No results found.')
    cursor.close()
    conn.close()

# rows = cursor.fetchall()
# print(rows[0])
    


