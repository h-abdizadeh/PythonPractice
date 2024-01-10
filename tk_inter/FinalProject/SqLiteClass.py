import sqlite3

class SqliteDB():
    database='data/MyDB.db'
    connection=sqlite3.Connection(database)

    def CreateProductTable(self):
        commandText='''CREATE TABLE IF NOT EXISTS 
        Products(Id INTEGER PRIMARY KEY,
        Name TEXT NOT NULL,
        Inventory INT NOT NULL,
        Brand TEXT,
        Category TEXT NOT NULL)'''

        self.connection.execute(commandText)

    def InsertProduct(self,product):
        commandText='''INSERT INTO 
        Products(Name,Inventory,Brand,Category)
        Values (?,?,?,?)'''

        self.connection.execute(commandText,product)
        self.connection.commit()

    def GetProducts(self):
        commandText='SELECT * FROM Products'
        rows=self.connection.execute(commandText)

        return rows

    def DeleteProduct(self,productId):
        commandText='DELETE FROM Products WHERE Id=?'
        self.connection.execute(commandText,productId)
        self.connection.commit()

    def UpdateProduct(self,product):
        commandText='''UPDATE Products SET 
        Name=?,Inventory=?,Brand=?,Category=? 
        WHERE Id=?'''

        self.connection.execute(commandText,product)
        self.connection.commit()


    def GetProduct(self,productId):
        commandText='''SELECT * FROM Products 
        WHERE Id=?'''
        product=self.connection.execute(commandText,productId)
    
        return product