from tabulate import tabulate 
import mysql.connector as sql
con=sql.connect(host='localhost', user=input("Enter your account:"), passwd=input("Enter your password:"), database='ROOM_MANAGEMENT_SYSTEM', auth_plugin="mysql_native_password")
print("                                                                     #___WELCOME_TO_QUADCORE_HOTELS___#                                      ")

def checkin():
        """
        Use to fill the data of a guest in the CHECK_IN table of the database.
        """
        guest=int(input("Enter number of guest(s):"))
        cursor_var=con.cursor()

        for i in range(guest):
                type_of_room=input("Enter type of Room choosen:")
                days=input("Enter number of day(s):")
                name_of_guest=input("Enter Name(s) of guest(s):")
                adhaar_card=input("Enter Aadhaar Card Number(s) of guest(s):")
                mobile_no=input("Enter Mobile_No. of guest:")
                date_of_checkin=input("Enter date of Check_In:")
                alloted_room=input("Enter alloted Room_No:")
                data=(type_of_room,days,name_of_guest,adhaar_card,mobile_no,date_of_checkin,alloted_room)
                sql1='INSERT INTO CHECK_IN VALUES(%s,%s,%s,%s,%s,%s,%s)'
                cursor_var.execute(sql1,data)
        
        con.commit()
        print(" ")
        print("Data entered successfully!!!")
        
        main()

def detailsroom():
        """
        Showcase details of a guests using his/her alloted room number in CHECK_IN/CHECK_OUT table of database.
        """
        print(" ")
        
        had=['Credentials','Assigned_Task']
        myd=[
                ['Press 1','DETAILS FROM CHECK_IN'],
                ['Press 2','DETAILS FROM CHECK_OUT']
        ]
        print(tabulate(myd, headers=had, tablefmt='fancy_grid'))
        print(" ")
        print("*If you get empty table, then it means no matches found...")
        
        user_choice=int(input("Enter your choice:"))
        cursor_var=con.cursor()

        if user_choice==1:
                alloted_room_no=input("Enter Room_No:")
                cursor_var.execute("SELECT * FROM CHECK_IN WHERE ROOM_NO=%s",(alloted_room_no,))
                data=cursor_var.fetchall()
                head=['Room_Type','Day(s)','Name(s)','Aadhaar_Card_No.','Mobile_NO.','Date','Room_No.']
                print(tabulate(data, headers=head, tablefmt='grid'))
        
        elif user_choice==2:
                alloted_room_no=input("Enter Room_No:")
                cursor_var.execute("SELECT * FROM CHECK_OUT WHERE ROOM_NO=%s",(alloted_room_no,))
                data1=cursor_var.fetchall()
                heads=['Room_Type','Room_No.','Name(s)','Mobile_No.','Aadhaar_Card_No.','No._of_day(s)','Total_bill','Date_of_billing']
                print(tabulate(data1, headers=heads, tablefmt='grid' ))
        
        else: 
                print("Wrong input...")
        
        main()

def updatein():
        """
        This function updates the guest detail in the CHECK_IN table of database.
        """
        head=['Credentials','Column Name']
        myd=[
                ['Press 1','ROOM_TYPE'],
                ['Press 2','NO_OF_DAYS'],
                ['Press 3','NAME'],
                ['Press 4','AADHAAR_CARD_NO'],
                ['Press 5','MOBILE_NO'],
                ['Press 6','DATE'],
                ['Press 7','ROOM_NO']
        ]
        print(tabulate(myd, headers=head, tablefmt='fancy_grid'))
        print(" ")
        
        user_choice=int(input("Enter your choice:"))
        cursor_var=con.cursor()
        
        if user_choice==1:
                room_type=input("Enter details after changing:")
                mobile_no=input("Enter mobile number as a reference detail of guest:")
                data1=(room_type,mobile_no)
                sql1='UPDATE CHECK_IN SET ROOM_TYPE=%s WHERE MOBILE_NO=%s'
                cursor_var.execute(sql1,data1)
                print("Details update successfully!!!")
        
        elif user_choice==2:
                no_of_days=input("Enter details after changing:")
                mobile_no=input("Enter mobile number as a reference detail of guest:")
                data2=(no_of_days,mobile_no)
                sql2='UPDATE CHECK_IN SET NO_OF_DAYS=%s WHERE MOBILE_NO=%s'
                cursor_var.execute(sql2,data2)
                print("Details update successfully!!!")
        
        elif user_choice==3:
                name_of_guest=input("Enter details after changing:")
                mobile_no=input("Enter mobile number as a reference detail of guest:")
                data3=(name_of_guest,mobile_no)
                sql3='UPDATE CHECK_IN SET NAME=%s WHERE MOBILE_NO=%s'
                cursor_var.execute(sql3,data3)
                print("Details update successfully!!!")
        
        elif user_choice==4:
                aadhaar_card=input("Enter details after changing:")
                mobile_no=input("Enter mobile number as a reference detail of guest:")
                data4=(aadhaar_card,mobile_no)
                sql4='UPDATE CHECK_IN SET AADHAAR_CARD_NO=%s WHERE MOBILE_NO=%s'
                cursor_var.execute(sql4,data4)
                print("Details update successfully!!!")
        
        elif user_choice==5:
                mobile_no=input("Enter details after changing:")
                aadhaar_card=input("Enter aadhaar card number as a reference detail of guest:")
                data5=(mobile_no,aadhaar_card)
                sql5='UPDATE CHECK_IN SET MOBILE_NO=%s WHERE AADHAAR_CARD_NO=%s'
                cursor_var.execute(sql5,data5)
                print("Details update successfully!!!")
        
        elif user_choice==6:
                date=input("Enter details after changing:")
                mobile_no=input("Enter mobile number as a reference detail of guest:")
                data6=(date,mobile_no)
                sql6='UPDATE CHECK_IN SET DATE=%s WHERE MOBILE_NO=%s'
                cursor_var.execute(sql6,data6)
                print("Details update successfully!!!")
        
        elif user_choice==7:
                room_no=input("Enter details after changing:")
                mobile_no=input("Enter mobile number as a reference detail of guest:")
                data7=(room_no,mobile_no)
                sql7='UPDATE CHECK_IN SET ROOM_NO=%s WHERE MOBILE_NO=%s'
                cursor_var.execute(sql7,data7)
                print("Details update successfully!!!")
        
        else:
                print("Wrong input")
        
        con.commit()
        main()


def detailsname():
        """
        This function finds the detail of the person from CHECK_IN/CHECK_OUT table using name of the guest.
        """
        print(" ")
        
        had=['Credentials','Assigned_Task']
        myd=[
                ['Press 1','DETAILS FROM CHECK_IN'],
                ['Press 2','DETAILS FROM CHECK_OUT']
        ]
        
        print(tabulate(myd, headers=had, tablefmt='fancy_grid'))
        print(" ")
        print("*If you get empty table, then it means no matches found...")
        
        x=int(input("Enter your choice:"))
        cursor_var=con.cursor()
        
        if x==1:
                name_of_guest=input("Enter name of the guest:") 
                cursor_var.execute("SELECT * FROM CHECK_IN WHERE NAME=%s",(name_of_guest,))
                data=cursor_var.fetchall()
                head=['Room_Type','Day(s)','Name(s)','Aadhaar_Card_No.','Mobile_No.','Date','Room_No.']
                print(tabulate(data, headers=head, tablefmt='fancy_grid'))
        
        elif x==2:
                name_of_guest=input("Enter name of the guest:")
                cursor_var.execute("SELECT * FROM CHECK_OUT WHERE NAME=%s",(name_of_guest,))
                data=cursor_var.fetchall()
                heads=['Room_Type','Room_No.','Name(s)','Mobile_No.','Aadhaar_Card_No.','No._of_day(s)','Total_bill','Date_of_billing']
                print(tabulate(data, headers=heads, tablefmt='grid'))
        
        else:
                print("Wrong input...")
                
        main()

def calculator():
        """
        Opens the calculator in the program.
        """
        
        import subprocess
        subprocess.Popen('C:\\Windows\\System32\\calc.exe')
        print("Opening calculator...")
        main()

def checkout():
        """
        Helps to fill out the details of a guest in CHECK_OUT table of database.
        """
        
        room_no=int(input("Enter Room number:"))
        print(" ")
        
        head=['Credentials','Assigned_Task']
        myd=[
                ['Press 1','EXECUTIVE ROOM'],
                ['Press 2','DELUXE ROOM'],
                ['Press 3','SIMPLE_ROOM(WITH AC)'],
                ['Press 4','SIMPLE_ROOM(NON AC)']
        ]
        
        print(tabulate(myd, headers=head, tablefmt='fancy_grid'))
        print(" ")
        
        room_type_no=int(input("Enter type of Room from above table(in number):"))
        guest=int(input("Enter number(s) of guest:"))
        cursor_var=con.cursor()
        
        for i in range(guest):
                type_of_room=input("Enter type of Room(in name):")
                name_of_guest=input("Enter name of the guest:")
                mob=int(input("Enter Mobile_no:"))
                aadhaar_card=input("Enter Aadhar_Card_Number:")
                days=int(input("Enter number of days:"))
                billing_date=input("Enter date of billing:")
                room1=5000
                room2=2500
                room3=1500
                room4=1000
                tyroom=0
                if room_type_no==1:
                        tyroom=room1
                        fare=(guest*days*tyroom)
                elif room_type_no==2:
                        tyroom=room2
                        fare=(guest*days*tyroom)
                elif room_type_no==3:
                        tyroom=room3
                        fare=(guest*days*tyroom)
                elif room_type_no==4:
                        tyroom=room4
                        fare=(guest*days*tyroom)
                data=(type_of_room,room_no,name_of_guest,mob,aadhaar_card,days,fare,billing_date)
                sql1='INSERT INTO CHECK_OUT VALUES(%s,%s,%s,%s,%s,%s,%s,%s)'
                cursor_var.execute(sql1,data)
        print(" ")
        print("Total bill:Rs.",fare)
        con.commit()
        print(" ")
        print("Data entered successfully!!!")
        main()

def discount():
        """
        Helps to generate discount over the total bill of the guest
        """
        
        bill_discount=int(input("Enter number of guest(s):"))
        cursor_var=con.cursor()

        for i in range(bill_discount):
                aadhaar_card=input("Enter Aadhaar card number:")
                total_bill=input("Enter amount:")
                data=(total_bill,aadhaar_card)
                sql1='UPDATE CHECK_OUT SET TOTAL_BILL=TOTAL_BILL-%s WHERE AADHAAR_CARD_NO=%s'
                cursor_var.execute(sql1,data)
                print("Bill updated successfully!!!")
        
        con.commit()
        main()

def updateout():
        """
        Updates the details of a guest in CHECK_OUT table of database.
        """
        head=['Credentials','Column Name']
        myd=[
                ['Press 1','ROOM_TYPE'],
                ['Press 2','ROOM_NO'],
                ['Press 3','NAME'],
                ['Press 4','MOBILE_NO'],
                ['Press 5','AADHAAR_CARD_NO'],
                ['Press 6','NO_OF_DAYS'],
                ['Press 7','TOTAL_BILL'],
                ['Press 8','DATE_OF_BILLING']
        ]
        print(tabulate(myd,headers=head, tablefmt='fancy_grid'))
        print(" ")
        
        user_choice=int(input("Enter your choice:"))
        cursor_var=con.cursor()

        if user_choice==1:
                room_type=input("Enter room type you want to change:")
                mobile_no=input("Enter mobile number as a reference detail of guest:")
                data1=(room_type,mobile_no)
                sql1='UPDATE CHECK_OUT SET ROOM_TYPE=%s WHERE MOBILE_NO=%s'
                cursor_var.execute(sql1,data1)
                print("Room type updated successfully!!!")
        
        elif user_choice==2:
                room_no=input("Enter room no. you want to change:")
                mobile_no=input("Enter mobile number as a reference detail of guest:")
                data2=(room_no,mobile_no)
                sql2='UPDATE CHECK_OUT SET ROOM_NO=%s WHERE MOBILE_NO=%s'
                cursor_var.execute(sql2,data2)
                print("Room number updated successfully!!!")
        
        elif user_choice==3:
                name_of_guest=input("Enter name of guest you want to change:")
                mobile_no=input("Enter mobile number as a reference detail of guest:")
                data3=(name_of_guest,mobile_no)
                sql3='UPDATE CHECK_OUT SET NAME=%s WHERE MOBILE_NO=%s'
                cursor_var.execute(sql3,data3)
                print("Name of guest updated successfully!!!")
        
        elif user_choice==4:
                mobile_no=input("Enter mobile number you want to change:")
                aadhaar_card=input("Enter mobile Aadhaar Card number as a reference detail of guest:")
                sql4='UPDATE CHECK_OUT SET MOBILE_NO=%s WHERE AADHAAR_CARD_NO=%s'
                data4=(mobile_no,aadhaar_card)
                cursor_var.execute(sql4,data4)
                print("Mobile no. updated successfully!!!")
        
        elif user_choice==5:
                aadhaar_card=input("Enter aadhaar card number change:")
                mobile_no=input("Enter mobile number as a reference detail of guest:")
                data5=(aadhaar_card,mobile_no)
                sql5='UPDATE CHECK_OUT SET AADHAAR_CARD_NO=%s WHERE MOBILE_NO=%s'
                cursor_var.execute(sql5,data5)
                print("Aadhaar card number updated successfully!!!")
        
        elif user_choice==6:
                no_of_days=input("Enter number of days you want to change:")
                mobile_no=input("Enter mobile number as a reference detail of guest:")
                data6=(no_of_days,mobile_no)
                sql6='UPDATE CHECK_OUT SET NO_OF_DAYS=%s WHERE MOBILE_NO=%s'
                cursor_var.execute(sql6,data6)
                print("Number of days updated successfully!!!")
        
        elif user_choice==7:
                total_bill=input("Enter total bill you want to change:")
                mobile_no=input("Enter mobile number as a reference detail of guest:")
                data7=(total_bill,mobile_no)
                sql7='UPDATE CHECK_OUT SET TOTAL_BILL=%s WHERE MOBILE_NO=%s'
                cursor_var.execute(sql7,data7)
                print("Total bill updated successfully!!!")
        
        elif user_choice==8:
                date_of_bill=input("Enter date of billing you want to change:")
                mobile_no=input("Enter mobile number as a reference detail of guest:")
                data8=(date_of_bill,mobile_no)
                sql8='UPDATE CHECK_OUT SET DATE_OF_BILLING=%s WHERE MOBILE_NO=%s'
                cursor_var.execute(sql8,data8)
                print("Date of billing updated successfully!!!")
        
        else:
                print("Wrong input")
        
        con.commit()
        main()

def rooms():
        """
        Shows types of the rooms availble in our hotel.
        """
        head=["Room_Type","Facilities","Cost(per day/guest)"]
        mydata=[
                ['Executive Room','Wi-Fi, TV, Air Conditioner, Bathroom with Geyser, Tub and Jacuzzi, Breakfast,Lunch, Dinner','Rs.5000'],
                ['Deluxe Room','Wi-Fi, TV, Air Conditioner, Bathroom with Tub and Geyser, Lunch, Dinner','Rs.2500'],
                ['Normal Room(with AC)','Wi-Fi, TV, Air Conditioner, Bathroom with Geyser','Rs.1500'],
                ['Normal Room(Non-AC)','Wi-Fi, TV, Bathroom with Geyser','Rs.1000']
        ]
        print(tabulate(mydata, headers=head, tablefmt='fancy_grid'))
        main()

def deletionum():
        """
        Delets data of guests using his/her mobile number.
        """        
        print(" ")
        head=['Credentials','Assigned_Task']
        myd=[
                ['Press 1','FROM CHECK_IN'],
                ['Press 2','FROM CHECK_OUT']
        ]
        print(tabulate(myd, headers=head, tablefmt='grid'))
        print(" ")
        
        user_choice=int(input("Enter your choice:"))
        cursor_var=con.cursor()

        if user_choice==1:
                mobile_no=input("Enter Mobile Number:")
                sql1='DELETE FROM CHECK_IN WHERE MOBILE_NO=%s'
                cursor_var.execute(sql1,(mobile_no,))
                print("Data deleted successfully!!!")
        
        elif user_choice==2:
                mobile_no=input("Enter Mobile Number:")
                sql1='DELETE FROM CHECK_OUT WHERE MOBILE_NO=%s'
                cursor_var.execute(sql1,(mobile_no,))
                print("Data deleted successfully!!!")
        
        else:
                print("Wrong input...")
        con.commit()
        main()

def deletioncard():
        """
        Delets data of a guest using his/her aadhaar card number.
        """
        print(" ")
        head=['Credentials','Assigned_Task']
        myd=[
                ['Press 1','FROM CHECK_IN'],
                ['Press 2','FROM CHECK_OUT']
        ]
        print(tabulate(myd, headers=head, tablefmt='fancy_grid'))
        print(" ")
        
        user_choice=int(input("Enter your choice:"))
        cursor_var=con.cursor()
        if user_choice==1:
                aadhaar_card=input("Enter Card Number:")
                sql1='DELETE FROM CHECK_IN WHERE AADHAAR_CARD_NO=%s'
                cursor_var.execute(sql1,(aadhaar_card,))
                print(" ")
                print("Data deleted successfully!!!")

        elif user_choice==2:
                aadhaar_card=input("Enter Card Number:")
                sql1='DELETE FROM CHECK_OUT WHERE AADHAAR_CARD_NO=%s'
                cursor_var.execute(sql1,(aadhaar_card,))
                print(" ")
                print("Data deleted successfully!!!")
        
        else:
                print("Wrong input...")

        con.commit()
        main()

def services():
        """
        To showcase what services we offers to the guests.
        """
        print(" ")
        head=['Service','Phone_No.']
        myd=[
                ['Room_Service','900'],
                ['Cleaner','901'],
                ['Kitchen','902'],
                ['Reception','903']
        ]
        print(tabulate(myd, headers=head, tablefmt='fancy_grid'))
        print(" ")
        main()

def main():
        """
        Main function for calling other functions of the programs
        """
        print(" ")
        
        head=['Credential','Assigned_Task']

        myd=[
                ['Press 1','FARE AND FACILITIES'],
                ['Press 2','CHECK_IN PROMPT'],
                ['Press 3','UPDATE_IN_CHECK_IN PROMPT'],
                ['Press 4','DETAILS(VIA ROOM NUMBER) PROMPT'],
                ['Press 5','DETAILS(VIA NAME) PROMPT'],
                ['Press 6','OPEN CALCULATOR'],
                ['Press 7','CHECK_OUT PROMPT'],
                ['Press 8','UPDATEOUT PROMPT'],
                ['Press 9','SERVICE CONTACT'],
                ['Press 10','DISCOUNT'],
                ['Press 11','DELETION_OF_DETAILS(MOBILE NUMBER)'],
                ['Press 12','DELETION_OF_DETAILS(AADHAAR CARD)']
        ]
        print(tabulate(myd, headers=head, tablefmt='fancy_grid'))
        print(" ")
        user_choice=int(input("Enter PROMPT choice:"))
        if user_choice==1:
                rooms()
        elif user_choice==2:
                checkin()
        elif user_choice==3:
                updatein()
        elif user_choice==4:
                detailsroom()
        elif user_choice==5:
                detailsname()
        elif user_choice==6:
                calculator()
        elif user_choice==7:
                checkout()
        elif user_choice==8:
                updateout()
        elif user_choice==9:
                services()
        elif user_choice==10:
                discount()
        elif user_choice==11:
                deletionum()
        elif user_choice==12:
                deletioncard()
        else:
                print("WRONG INPUT... ENTER VALID CHOICE")
        main()
main()  
