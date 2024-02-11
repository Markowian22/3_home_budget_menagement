class Repository:



    
    """
    Class for interacting with the database.

    Methods
    -------
    add_item(name: str, category: str, date: str, value: float):
        Adds an item to the database.
    delete_item(item_id: int):
        Deletes an item from the database.
    get_item():
        Retrieves items from the database.
    get_stats():
        Retrieves statistics from the database.
    """

    def __init__(self, connection):
        """
        Initializes the repository.

        Parameters
        ----------
        connection : sqlite3.Connection
            Connection to the SQLite3 database.
        """
        self.connection = connection

    def add_item(self, name: str, category: str, date: str, value: float):
        """
        Adds an item to the database.

        Parameters
        ----------
        name : str
            Name of the item.
        category : str
            Category of the item.
        date : str
            Date of the item.
        value : float
            Value of the item.
        """
        category_id = self.get_or_create_cateogry(category)
        sql = "INSERT INTO items VALUES(null, ?, ?, ?, ?)"
        cursor = self.connection.cursor()
        cursor.execute(sql, (name, category_id, value, date))

    def get_or_create_cateogry(self, name):
        """
        Retrieves a category from the
        database or creates it if it doesn't exist.

        Parameters
        ----------
        name : str
            Name of the category.

        Returns
        -------
        int
            ID of the category.
        """
        cursor = self.connection.cursor()
        cursor.execute("SELECT ID FROM categories WHERE name=?", (name,))
        result = cursor.fetchone()
        if result is None:
            cursor.execute("INSERT INTO categories VALUES(null, ?)", (name,))
            self.connection.commit()
            category_id = cursor.lastrowid
        else:
            category_id = result[0]

        return category_id

    def delete_item(self, item_id: int):
        """
        Deletes an item from the database.

        Parameters
        ----------
        item_id : int
            ID of the item to delete.
        """
        cursor = self.connection.cursor()
        cursor.execute("DELETE FROM items WHERE id=?", (item_id,))
        self.connection.commit()

    def get_item(self):
        """
        Retrieves all items from the database.

        Returns
        -------
        sqlite3.Cursor
            Cursor pointing to the result set of the query.
        """
        cursor = self.connection.cursor()
        return cursor.execute("SELECT * FROM items")

    def get_stats(self):
        """
        Retrieves statistics from the database.

        Returns
        -------
        sqlite3.Cursor
            Cursor pointing to the result set of the query.
        """
        cursor = self.connection.cursor()
        return cursor.execute(
            """SELECT
                        strftime('%m', date) as month,
                        strftime('%Y', date) as year,
                        SUM(amount) as total
                    FROM items
                    GROUP BY month, year"""
        )
