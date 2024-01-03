import pyodbc

conn_str = ('DRIVER={SQL Server Native Client 11.0};'
    'SERVER=DATA\SQLEXPRESS;'
    'DATABASE=AdventureWorksLT2016;'
    'TRUSTED_CONNECTION=yes;')
conn = pyodbc.connect(conn_str)
query = '''
        select CustomerID,FirstName,MiddleName,LastName,CompanyName,EmailAddress,Phone 
        from SalesLT.Customer
        order by CustomerID
        '''
cursor = conn.cursor()
cursor.execute(query)
rows = cursor.fetchall()
for row in rows:
    print(row)
    
cursor.close()
conn.close()
