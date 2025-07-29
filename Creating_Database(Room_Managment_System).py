import mysql.connector as sql
from mysql.connector import Error

try:
    username = input("Enter your username:")
    password = input("Enter your password:")
    con = sql.connect(host = "localhost", user = username, passwd = password, auth_plugin = "mysql_native_password")

    if con.is_connected():
        print("Connection successful!")
        cursor_var = con.cursor()
except Error as e:
    print(f'Connection failed to MySQL, error:{e}') 


class DataBaseCreation:
    '''Creating the database, Room Management System'''
    def __init__(self, connection):
        self.connection = connection
        self.cursor = self.connection.cursor()

    def database_create(self):
        try:
            create = "CREATE DATABASE IF NOT EXISTS ROOM_MANAGEMENT_SYSTEM"
            self.cursor.execute(create)
            self.connection.commit()
            print("Database created or already exists.")
        except Error as e:
            print(f"Unable to create Database, error: {e}")

    def UseDatabase(self):
        try:
            database = "USE ROOM_MANAGEMENT_SYSTEM"
            self.cursor.execute(database)
            self.connection.commit()
        except Error as e:
            print(f"Error: {e}")

    def CreateTable(self):
        try:
            create_checkin = '''
                CREATE TABLE IF NOT EXISTS CHECK_IN (
                    ROOM_TYPE VARCHAR(20), 
                    NO_OF_DAYS INT, 
                    NAME VARCHAR(20), 
                    AADHAAR_CARD_NO VARCHAR(12), 
                    MOBILE_NO VARCHAR(13), 
                    DATE VARCHAR(20), 
                    ROOM_NO INT
                )
            '''
            self.cursor.execute(create_checkin)

            create_checkout = '''
                CREATE TABLE IF NOT EXISTS CHECK_OUT (
                    ROOM_TYPE VARCHAR(30), 
                    ROOM_NO INT, 
                    NAME VARCHAR(20), 
                    MOBILE_NO VARCHAR(13), 
                    AADHAAR_CARD_NO VARCHAR(12), 
                    NO_OF_DAYS INT, 
                    TOTAL_BILL FLOAT, 
                    DATE_OF_BILLING VARCHAR(20)
                )
            '''
            self.cursor.execute(create_checkout)

            self.connection.commit()
            print("Both tables created (if not already existing).")
        except Error as e:
            print(f"Error: {e}")


class DataBaseDeletion:
    '''Deleting database, Room Management System'''
    def __init__(self, connection):
        self.connection = connection
        self.cursor = self.connection.cursor()

    def perform_deletion(self):
        print("\nPress 1 to delete entire database.")
        print("Press 2 to delete tables in database.\n")
        user_choice = int(input("Enter your choice: "))

        if user_choice == 1:
            try:
                self.cursor.execute("DROP DATABASE IF EXISTS ROOM_MANAGEMENT_SYSTEM")
                print("DATABASE deleted successfully!")
            except Error as e:
                print(f"Error: {e}")
        elif user_choice == 2:
            self.cursor.execute("USE ROOM_MANAGEMENT_SYSTEM")
            print("\nPress 1 to delete both tables.")
            print("Press 2 to delete CHECK_IN table only.")
            print("Press 3 to delete CHECK_OUT table only.\n")
            user_choice_table = int(input("Enter your choice: "))
            try:
                if user_choice_table == 1:
                    self.cursor.execute("DROP TABLE IF EXISTS CHECK_IN")
                    self.cursor.execute("DROP TABLE IF EXISTS CHECK_OUT")
                    print("Both tables deleted successfully.")
                elif user_choice_table == 2:
                    self.cursor.execute("DROP TABLE IF EXISTS CHECK_IN")
                    print("CHECK_IN table deleted successfully.")
                elif user_choice_table == 3:
                    self.cursor.execute("DROP TABLE IF EXISTS CHECK_OUT")
                    print("CHECK_OUT table deleted successfully.")
                else:
                    print("Invalid choice.")
                self.connection.commit()
            except Error as e:
                print(f"Error: {e}")


class ColumnModification:
    '''Help to modify the columns'''
    def __init__(self, connection):
        self.connection = connection
        self.cursor = self.connection.cursor()

    def modify_column(self):
        self.cursor.execute("USE ROOM_MANAGEMENT_SYSTEM")
        print("\nPress 1 to ADD column.")
        print("Press 2 to DELETE column.\n")
        try:
            choice = int(input("Enter your choice: "))
            table = input("Enter table name (CHECK_IN/CHECK_OUT): ").upper()
            column_name = input("Enter column name: ")

            if choice == 1:
                column_type = input("Enter column type (e.g. VARCHAR(20), INT): ")
                query = f"ALTER TABLE {table} ADD COLUMN {column_name} {column_type}"
                self.cursor.execute(query)
                print("Column added successfully.")
            elif choice == 2:
                query = f"ALTER TABLE {table} DROP COLUMN {column_name}"
                self.cursor.execute(query)
                print("Column deleted successfully.")
            else:
                print("Invalid option.")
            self.connection.commit()
        except Error as e:
            print(f"Error: {e}")
        except Exception as ex:
            print(f"Invalid input: {ex}")


class IndividualTableCreation:
    '''Can create individual tables also'''
    def __init__(self, connection):
        self.connection = connection
        self.cursor = self.connection.cursor()

    def create_checkin_table(self):
        try:
            self.cursor.execute('''
                CREATE TABLE IF NOT EXISTS CHECK_IN (
                    ROOM_TYPE VARCHAR(20), 
                    NO_OF_DAYS INT, 
                    NAME VARCHAR(20), 
                    AADHAAR_CARD_NO VARCHAR(12), 
                    MOBILE_NO VARCHAR(13), 
                    DATE VARCHAR(20), 
                    ROOM_NO INT
                )
            ''')
            self.connection.commit()
            print("CHECK_IN table created successfully.")
        except Error as e:
            print(f"Error creating CHECK_IN table: {e}")

    def create_checkout_table(self):
        try:
            self.cursor.execute('''
                CREATE TABLE IF NOT EXISTS CHECK_OUT (
                    ROOM_TYPE VARCHAR(30), 
                    ROOM_NO INT, 
                    NAME VARCHAR(20), 
                    MOBILE_NO VARCHAR(13), 
                    AADHAAR_CARD_NO VARCHAR(12), 
                    NO_OF_DAYS INT, 
                    TOTAL_BILL FLOAT, 
                    DATE_OF_BILLING VARCHAR(20)
                )
            ''')
            self.connection.commit()
            print("CHECK_OUT table created successfully.")
        except Error as e:
            print(f"Error creating CHECK_OUT table: {e}")

    def perform_table_creation(self):
        self.cursor.execute("USE ROOM_MANAGEMENT_SYSTEM")
        print("\nPress 1 to create CHECK_IN table.")
        print("Press 2 to create CHECK_OUT table.")
        print("Press 3 to create both tables.\n")
        try:
            user_choice = int(input("Enter your choice: "))
            if user_choice == 1:
                self.create_checkin_table()
            elif user_choice == 2:
                self.create_checkout_table()
            elif user_choice == 3:
                self.create_checkin_table()
                self.create_checkout_table()
            else:
                print("Invalid choice.")
        except Exception as e:
            print(f"Error: {e}")


def main():
    print("\n==== ROOM MANAGEMENT SYSTEM ====")
    print("1. Create database and both tables")
    print("2. Drop database or specific tables")
    print("3. Add/Delete column from table")
    print("4. Create individual tables (if not exist)")
    print("0. Exit")

    try:
        user_choice = int(input("Enter your choice: "))
        if user_choice == 1:
            db = DataBaseCreation(con)
            db.database_create()
            db.UseDatabase()
            db.CreateTable()
        elif user_choice == 2:
            deleter = DataBaseDeletion(con)
            deleter.perform_deletion()
        elif user_choice == 3:
            modifier = ColumnModification(con)
            modifier.modify_column()
        elif user_choice == 4:
            creator = IndividualTableCreation(con)
            creator.perform_table_creation()
        elif user_choice == 0:
            print("Exiting program.")
            return
        else:
            print("Invalid input.")
    except Exception as e:
        print(f"Error in main menu: {e}")

    main()  # Recursive loop

if __name__ == "__main__":
    main()
