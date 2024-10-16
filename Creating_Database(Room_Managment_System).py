import mysql.connector as sql
con=sql.connect(host='localhost', user=input("Enter your account name:"), passwd=input('Enter your password:'), auth_plugin='mysql_native_password')
cursor_var=con.cursor()

def database_creation():
        """
        Creating database using and tables (CHECK_IN and CHECK_OUT).
        """
        create='CREATE DATABASE ROOM_MANAGEMENT_SYSTEM'
        cursor_var.execute(create)
        print("DATABASE CREATED SUCCESSFULLY!!!")
        
        use='USE ROOM_MANAGEMENT_SYSTEM'
        cursor_var.execute(use)
        create_checkin='CREATE TABLE CHECK_IN(ROOM_TYPE VARCHAR(20), NO_OF_DAYS INT, NAME VARCHAR(20), AADHAAR_CARD_NO VARCHAR(12), MOBILE_NO VARCHAR(13), DATE VARCHAR(20), ROOM_NO INT)'
        cursor_var.execute(create_checkin)
        print("CHECK_IN TABLE CREATED SUCCESSFULLY!!!")
        
        create_checkout='CREATE TABLE CHECK_OUT(ROOM_TYPE VARCHAR(30), ROOM_NO INT, NAME VARCHAR(20), MOBILE_NO VARCHAR(13), AADHAAR_CARD_NO VARCHAR(12), NO_OF_DAYS INT, TOTAL_BILL FLOAT, DATE_OF_BILLING VARCHAR(20))'
        cursor_var.execute(create_checkout)
        print("CHECK_OUT TABLE CREATED SUCCESSFULLY!!!")
        
        con.commit()
        main()

def database_deletion():
        
        """
        Deleting database.
        """
        print(" ")
        print("Press 1 for to delete entire database.")
        print("Press 2 to delete tables in database.")
        print(" ")

        user_choice=int(input("Enter your choice:"))
        if user_choice==1:
            drop_database='DROP DATABASE ROOM_MANAGEMENT_SYSTEM'
            cursor_var.execute(drop_database)
            print("DATABASE deleted successfully!!!")
            
        elif user_choice == 2:
            print(" ")
            print("Press 1 to delete both tables.")
            print("Press 2 to delete CHECK_IN table only.")
            print("Press 3 to delete CHECK_OUT table only.")
            print(" ")
            user_choice_table = int(input("Enter your choice:"))

            if user_choice_table == 1:
                cursor_var.execute("DROP TABLE IF EXISTS CHECK_IN")
                cursor_var.execute("DROP TABLE IF EXISTS CHECK_OUT")
                print("Both tables deleted successfully")
            elif user_choice_table == 2:
                cursor_var.execute("DROP TABLE IF EXISTS CHECK_IN")
                print("CHECK_IN table deleted successfully")
            elif user_choice_table == 3:
                cursor_var.execute("DROP TABLE IF EXISTS CHECK_OUT")
                print("CHECK_OUT table deleted successfully")
                
        con.commit()
        main()

def main():
        print("Enter 1 to create database 'ROOM_MANAGEMENT_SYSTEM'")
        print("Enter 2 to drop database/table from 'ROOM_MANAGEMENT_SYSTEM'")
        user_choice=int(input("Enter your choice:"))
        if user_choice==1:
                database_creation()
        elif user_choice==2:
                database_deletion()
        else:
                print("Wrong input...")
        main()
main()
