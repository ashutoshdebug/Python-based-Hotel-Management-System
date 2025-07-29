import mysql.connector as sql
from mysql.connector import Error
from tabulate import tabulate
import os
import subprocess

try:
    user_name = input("Enter your account:")
    password= input("Enter your password:")
    con = sql.connect(host = 'localhost', user = user_name, passwd = password, database = "ROOM_MANAGEMENT_SYSTEM")
    
    if con.is_connected():
        print("Connection successful!")
        cursor_var = con.cursor()

except Error as e:
    print(f"Connection failed to MySQL: {e}")


class GuestManagement:
    """Managing guest data in Check In and Check Out tables"""
    def __init__(self, connection):
        self.connection = connection
        self.cursor = self.connection.cursor()

    def collect_checkin_info(self):
        print("\n--- Guest Check-In ---")
        type_of_room = input("Enter type of room chosen: ")
        days = int(input("Enter number of day(s): "))
        name = input("Enter name(s) of guest(s): ")
        aadhaar = input("Enter Aadhaar card number(s): ")
        mobile = input("Enter mobile number: ")
        checkin_date = input("Enter date of check-in (YYYY-MM-DD): ")
        room_no = input("Enter allotted room number: ")
        return (type_of_room, days, name, aadhaar, mobile, checkin_date, room_no)

    def insert_checkin(self, data):
        sql = '''
        INSERT INTO CHECK_IN 
        (ROOM_TYPE, NO_OF_DAYS, NAME, AADHAAR_CARD_NO, MOBILE_NO, DATE, ROOM_NO)
        VALUES (%s, %s, %s, %s, %s, %s, %s)
        '''
        self.cursor.execute(sql, data)

    def check_in_guests(self):
        try:
            count = int(input("Enter number of guest(s) for check-in: "))
            for _ in range(count):
                guest_info = self.collect_checkin_info()
                self.insert_checkin(guest_info)
            self.connection.commit()
            print("\nCheck-in data entered successfully!")
        except Exception as e:
            self.connection.rollback()
            print(f"\nCheck-in error: {e}")

    def collect_checkout_info(self):
        print("\n--- Guest Check-Out ---")

        head = ['Credentials', 'Room Type']
        options = [
            ['1', 'EXECUTIVE ROOM'],
            ['2', 'DELUXE ROOM'],
            ['3', 'SIMPLE_ROOM (WITH AC)'],
            ['4', 'SIMPLE_ROOM (NON AC)']
        ]
        print(tabulate(options, headers=head, tablefmt='fancy_grid'))
        print(" ")

        room_type_no = int(input("Enter room type number from the above table: "))
        room_no = input("Enter Room number: ")
        guest_count = int(input("Enter number of guest(s): "))

        room_rates = {
            1: 5000,
            2: 2500,
            3: 1500,
            4: 1000
        }

        all_checkout_data = []
        total_fare = 0

        for _ in range(guest_count):
            type_of_room = input("Enter room type (by name): ")
            name = input("Enter name of the guest: ")
            mobile = input("Enter mobile number: ")
            aadhaar = input("Enter Aadhaar card number: ")
            days = int(input("Enter number of stay days: "))
            billing_date = input("Enter billing date (YYYY-MM-DD): ")

            rate_per_day = room_rates.get(room_type_no, 0)
            fare = rate_per_day * days
            total_fare += fare

            data = (type_of_room, room_no, name, mobile, aadhaar, days, fare, billing_date)
            all_checkout_data.append(data)

        return all_checkout_data, total_fare

    def insert_checkout(self, data_list):
        sql = '''
        INSERT INTO CHECK_OUT 
        (ROOM_TYPE, ROOM_NO, NAME, MOBILE_NO, AADHAAR_CARD_NO, NO_OF_DAYS, TOTAL_BILL, DATE_OF_BILLING)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
        '''
        for data in data_list:
            self.cursor.execute(sql, data)

    def check_out_guests(self):
        try:
            all_checkout_data, total_fare = self.collect_checkout_info()
            self.insert_checkout(all_checkout_data)
            self.connection.commit()
            print(f"\nTotal bill for guest(s): ₹{total_fare}")
            print("Check-out data entered successfully!")
        except Exception as e:
            self.connection.rollback()
            print(f"\nCheck-out error: {e}")


class details:
    """Fetching Guest(s) data from Check In and Check Out tables"""
    def __init__(self, connection):
        self.connection = connection
        self.cursor = self.connection.cursor()
        self.columns = {
            'CHECK_IN': {
                1: 'ROOM_TYPE',
                2: 'NO_OF_DAYS',
                3: 'NAME',
                4: 'AADHAAR_CARD_NO',
                5: 'MOBILE_NO',
                6: 'DATE',
                7: 'ROOM_NO'
            },
            'CHECK_OUT': {
                1: 'ROOM_TYPE',
                2: 'ROOM_NO',
                3: 'NAME',
                4: 'MOBILE_NO',
                5: 'AADHAAR_CARD_NO',
                6: 'NO_OF_DAYS',
                7: 'TOTAL_BILL',
                8: 'DATE_OF_BILLING'
            }
        }
        self.table_map = {1: 'CHECK_IN', 2: 'CHECK_OUT'}

    def collect_guest_info(self):
        print("Select table to fetch data from:")
        for num, name in self.table_map.items():
            print(f"{num}. {name}")
        
        try:
            table_choice = int(input("Enter table number (1 or 2): "))
            table_name = self.table_map[table_choice]
        except (ValueError, KeyError):
            raise ValueError("Invalid table number. Please choose 1 for CHECK_IN or 2 for CHECK_OUT.")

        column_dict = self.columns[table_name]

        print("\nAvailable Columns:")
        for num, col_name in column_dict.items():
            print(f"{num}. {col_name}")

        try:
            col_choice = int(input("\nEnter the number corresponding to the column: "))
            column_name = column_dict[col_choice]
        except (ValueError, KeyError):
            raise ValueError("Invalid column number selected.")

        value = input(f"Enter your value for '{column_name}': ").strip()

        return table_name, column_name, value

    def insert_guest_info(self, table_name, column_name, value):
        try:
            column_dict = self.columns[table_name]
            head = [column_dict[i] for i in sorted(column_dict.keys())]
            sql = f"SELECT * FROM {table_name} WHERE {column_name} = %s"
            self.cursor.execute(sql, (value,))
            result = self.cursor.fetchall()

            if result:
                print("\nFetched Data:")
                print(tabulate(result, headers=head, tablefmt='fancy_grid'))
                
            else:
                print("\nNo matching data found.")

        except Exception as e:
            print(f"\nQuery failed! Error: {e}")

    def fetchdata(self):
        try:
            table_name, column_name, value = self.collect_guest_info()
            self.insert_guest_info(table_name, column_name, value)
            self.connection.commit()
        except Exception as e:
            self.connection.rollback()
            print(f"\nError occurred: {e}")


class Updater:
    """Updating Guest(s) data in Check In and Check Out table"""
    def __init__(self, connection):
        self.connection = connection
        self.cursor = self.connection.cursor()
        self.column_map = {
            'CHECK_IN': {
                1: 'ROOM_TYPE',
                2: 'NO_OF_DAYS',
                3: 'NAME',
                4: 'AADHAAR_CARD_NO',
                5: 'MOBILE_NO',
                6: 'DATE',
                7: 'ROOM_NO'
            },
            'CHECK_OUT': {
                1: 'ROOM_TYPE',
                2: 'ROOM_NO',
                3: 'NAME',
                4: 'MOBILE_NO',
                5: 'AADHAAR_CARD_NO',
                6: 'NO_OF_DAYS',
                7: 'TOTAL_BILL',
                8: 'DATE_OF_BILLING'
            }
        }

    def update_field(self):
        table_name = input("Enter table name (CHECK_IN or CHECK_OUT): ").strip().upper()
        if table_name not in self.column_map:
            print("Invalid table name.")
            return

        columns = self.column_map[table_name]

        print("\nSelect the column number you want to update:")
        for key, value in columns.items():
            print(f"{key}. {value}")
        try:
            col_choice = int(input("Enter your choice: ").strip())
            column_to_update = columns.get(col_choice)
            if not column_to_update:
                print("Invalid column selection.")
                return
        except ValueError:
            print("Invalid input.")
            return

        new_value = input(f"Enter the new value for {column_to_update}: ").strip()

        print("\nSelect the reference column number (to locate the guest):")
        for key, value in columns.items():
            print(f"{key}. {value}")
        try:
            ref_choice = int(input("Enter your choice: ").strip())
            reference_column = columns.get(ref_choice)
            if not reference_column:
                print("Invalid reference column selection.")
                return
        except ValueError:
            print("Invalid input.")
            return

        reference_value = input(f"Enter the current value for {reference_column} to identify the record: ").strip()

        try:
            sql = f"UPDATE {table_name} SET {column_to_update} = %s WHERE {reference_column} = %s"
            self.cursor.execute(sql, (new_value, reference_value))
            if self.cursor.rowcount == 0:
                print("No record found to update.")
            else:
                self.connection.commit()
                print("\nRecord updated successfully!")
        except Exception as e:
            self.connection.rollback()
            print(f"\nFailed to update record: {e}")



class DeleteData:
    """Deleting Guest(s) data from Check In and Check Out table"""
    def __init__(self, connection):
        self.connection = connection
        self.cursor = self.connection.cursor()
        self.columns_by_table = {
            'CHECK_IN': {
                1: 'ROOM_TYPE',
                2: 'NO_OF_DAYS',
                3: 'NAME',
                4: 'AADHAAR_CARD_NO',
                5: 'MOBILE_NO',
                6: 'DATE',
                7: 'ROOM_NO'
            },
            'CHECK_OUT': {
                1: 'ROOM_TYPE',
                2: 'ROOM_NO',
                3: 'NAME',
                4: 'MOBILE_NO',
                5: 'AADHAAR_CARD_NO',
                6: 'NO_OF_DAYS',
                7: 'TOTAL_BILL',
                8: 'DATE_OF_BILLING'
            }
        }

    def select_table(self):
        print("\nPress 1 for CHECK_IN table\nPress 2 for CHECK_OUT table\n")
        table_choice = input("Enter your choice: ").strip()
        if table_choice == '1':
            return "CHECK_IN"
        elif table_choice == '2':
            return "CHECK_OUT"
        else:
            print("Invalid input!")
            return None

    def display_options(self, table_name):
        columns = self.columns_by_table.get(table_name, {})
        head = ['Press', 'Column Name']
        table_data = [[key, value] for key, value in columns.items()]
        print(tabulate(table_data, headers=head, tablefmt='fancy_grid'))
        print(" ")
        return columns

    def delete_data(self):
        table_name = self.select_table()
        if not table_name:
            return

        columns = self.display_options(table_name)

        try:
            user_choice = int(input("Enter your choice for the column to match for deletion: "))
            column_name = columns.get(user_choice)

            if not column_name:
                print("Invalid column choice!")
                return

            delete_value = input(f"Enter the value for {column_name}: ").strip()

            if not column_name.isidentifier():
                print("Invalid column name!")
                return

            sql = f"DELETE FROM {table_name} WHERE {column_name} = %s"
            self.cursor.execute(sql, (delete_value,))
            if self.cursor.rowcount == 0:
                print("No matching record found.")
            else:
                self.connection.commit()
                print("Data deleted successfully!")

        except Exception as e:
            self.connection.rollback()
            print(f"Error: {e}")

class DiscountInitializer:
    """Inserting and updating the discount in Check Out table"""
    def __init__(self, connection):
        self.connection = connection
        self.cursor = self.connection.cursor()
        self.columns = {
            1: 'ROOM_TYPE',
                2: 'ROOM_NO',
                3: 'NAME',
                4: 'MOBILE_NO',
                5: 'AADHAAR_CARD_NO',
                6: 'NO_OF_DAYS',
                7: 'TOTAL_BILL',
                8: 'DATE_OF_BILLING'
        }
    
    def column_options(self):
        print("\nChoose the column for reference:")
        for key, col in self.columns.items():
            print(f"{key}.{col}")

    def discount_amount(self):
        inbill_dis = input("Enter the amount which needs to be deducted from the total bill:")

        self.column_options()
        col_key = int(input("Enter the number of the reference column:").strip())
        reference_column = self.columns.get(col_key)
        if not reference_column:
            raise ValueError("Invalid column key selected.")

        reference_value = input(f"Enter the value for {reference_column}: ").strip()
        return inbill_dis, reference_column, reference_value
    
    def updatingdiscount(self):
        try:
            discount, column, value = self.discount_amount()
            sql = f"UPDATE CHECK_OUT SET TOTAL_BILL = TOTAL_BILL - %s WHERE {column} = %s"
            self.cursor.execute(sql, (discount, value))
            self.connection.commit()
            print("Discount applied successfully!")
        except Exception as e:
            self.connection.rollback()
            print(f"Error applying discount: {e}")

class calculator:
    """Just opening calculator...."""
    def __init__(self, connection):
        self.connection = connection
        self.cursor = self.connection.cursor()

    def OpenCalc(self):
        subprocess.Popen(['calc.exe'])
        print("Opening calculator...")


class RoomDetails:
    """Showcasing different types of room and its details"""
    def __init__(self, connection):
        self.connection = connection
        self.cursor =  self.connection.cursor()

    def justprint(self):
        head = ["Type of Room", "Facilities", "Cost(per day/guest)"]
        roomdata = [
                ['Executive Room','Wi-Fi, TV, Air Conditioner, Bathroom with Geyser, Tub and Jacuzzi, Breakfast,Lunch, Dinner','Rs.5000'],
                ['Deluxe Room','Wi-Fi, TV, Air Conditioner, Bathroom with Tub and Geyser, Lunch, Dinner','Rs.2500'],
                ['Normal Room(with AC)','Wi-Fi, TV, Air Conditioner, Bathroom with Geyser','Rs.1500'],
                ['Normal Room(Non-AC)','Wi-Fi, TV, Bathroom with Geyser','Rs.1000']
        ]

        print(tabulate(roomdata, headers=head, tablefmt='fancy_grid'))

class Services:
    """Showcasing all services available for Guests"""
    def __init__(self, connection):
        self.connection = connection
        self.cursor = self.connection.cursor()

    def services(self):
        head=['Service','Phone_No.']
        myd=[
                ['Room_Service','900'],
                ['Cleaner','901'],
                ['Kitchen','902'],
                ['Reception','903']
        ]
        print(tabulate(myd, headers=head, tablefmt='fancy_grid'))
        print(" ")

def main():
        """
        Main function for calling other functions of the programs
        """
        print(" ")
        while True:
            head=['Credential','Assigned_Task']

            myd=[
                ['Press 1','Check In'],
                ['Press 2','Check Out'],
                ['Press 3','Show Room Details'],
                ['Press 4','Show Services'],
                ['Press 5','Update Guest Info'],
                ['Press 6','Search Guest'],
                ['Press 7','Delete Guest Info'],
                ['Press 8','Open Calculator'],
                ['Press 9','Apply Discount'],
                ['Press 10','Exit'],
            ]
            print(tabulate(myd, headers=head, tablefmt='fancy_grid'))
            print(" ")
            try:
                choice = int(input("Enter your choice (1-10): "))
            except ValueError:
                print("Invalid input, please enter a number")
                continue

            if choice == 1:
                gm = GuestManagement(con)
                gm.check_in_guests()
            elif choice == 2:
                gm = GuestManagement(con)
                gm.check_out_guests()
            elif choice == 3:
                rd = RoomDetails(con)
                rd.justprint()
            elif choice == 4:
                svc = Services(con)
                svc.services()
            elif choice == 5:
                updater = Updater(con)
                updater.update_field()
            elif choice == 6:
                detail = details(con)
                detail.fetchdata()
            elif choice == 7:
                deleter = DeleteData(con)
                deleter.delete_data()
            elif choice == 8:
                calc = calculator(con)
                calc.OpenCalc()
            elif choice == 9:
                discount = DiscountInitializer(con)
                discount.updatingdiscount()
            elif choice == 10:
                print("Thank you for using the Room Management System.")
                con.close()
                break

            else:
                print("Invalid choice. Please try again.")
            
            input("\nPress Enter to continue...")
            os.system('cls' if os.name == 'nt' else 'clear')
main()