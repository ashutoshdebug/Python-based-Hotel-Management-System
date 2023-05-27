from tabulate import tabulate 
import mysql.connector as sql
con=sql.connect(host='localhost', user='root', passwd='Ashutosh@3005', database='ROOM_MANAGEMENT_SYSTEM')
print("                                                                     #___WELCOME_TO_QUADCORE_MOTELS___#                                      ")
def checkin():
        guest=int(input("Enter number of guest(s):"))
        for i in range(guest):
                tyroom=input("Enter type of Room choosen:")
                days=input("Enter number of day(s):")
                n=input("Enter Name(s) of guest(s):")
                card=input("Enter Aadhaar Card Number(s) of guest(s):")
                mob=input("Enter Mobile_No. of guest:")
                date=input("Enter date of Check_In:")
                room=input("Enter alloted Room_No:")
                data=(tyroom,days,n,card,mob,date,room)
                sql1='INSERT INTO CHECK_IN VALUES(%s,%s,%s,%s,%s,%s,%s)'
                c=con.cursor(sql1,data)
                c.execute(sql1,data)
        con.commit()
        print(" ")
        print("Data entered successfully!!!")
        main()

def detailsroom():
        print(" ")
        had=['Credentials','Assigned_Task']
        myd=[
                ['Press 1','DETAILS FROM CHECK_IN'],
                ['Press 2','DETAILS FROM CHECK_OUT']
        ]
        print(tabulate(myd, headers=had, tablefmt='fancy_grid'))
        print(" ")
        print("*If you get empty table, then it means no matches found...")
        b=int(input("Enter your choice:"))
        if b==1:
                a=input("Enter Room_No:")
                c=con.cursor()
                c.execute("SELECT * FROM CHECK_IN WHERE ROOM_NO=%s",(a,))
                data=c.fetchall()
                head=['Room_Type','Day(s)','Name(s)','Aadhaar_Card_No.','Mobile_NO.','Date','Room_No.']
                print(tabulate(data, headers=head, tablefmt='grid'))
        elif b==2:
                l=input("Enter Room_No:")
                c=con.cursor()
                c.execute("SELECT * FROM CHECK_OUT WHERE ROOM_NO=%s",(l,))
                data1=c.fetchall()
                heads=['Room_Type','Room_No.','Name(s)','Mobile_No.','Aadhaar_Card_No.','No._of_day(s)','Total_bill','Date_of_billing']
                print(tabulate(data1, headers=heads, tablefmt='grid' ))
        else: 
                print("Wrong input...")
        main()

def updatein():
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
        al=int(input("Enter your choice:"))
        if al==1:
                b=input("Enter details after changing:")
                d=input("Enter mobile number as a reference detail of guest:")
                data1=(b,d)
                sql1='UPDATE CHECK_IN SET ROOM_TYPE=%s WHERE MOBILE_NO=%s'
                r=con.cursor(sql1,data1)
                r.execute(sql1,data1)
                print("Details update successfully!!!")
                con.commit()
        elif al==2:
                f=input("Enter details after changing:")
                g=input("Enter mobile number as a reference detail of guest:")
                data2=(f,g)
                sql2='UPDATE CHECK_IN SET ROOM_TYPE=%s WHERE MOBILE_NO=%s'
                s=con.cursor(sql2,data2)
                s.execute(sql2,data2)
                print("Details update successfully!!!")
                con.commit()
        elif al==3:
                h=input("Enter details after changing:")
                i=input("Enter mobile number as a reference detail of guest:")
                data3=(h,i)
                sql3='UPDATE CHECK_IN SET ROOM_TYPE=%s WHERE MOBILE_NO=%s'
                t=con.cursor(sql3,data3)
                t.execute(sql3,data3)
                print("Details update successfully!!!")
                con.commit()
        elif al==4:
                j=input("Enter details after changing:")
                k=input("Enter mobile number as a reference detail of guest:")
                data4=(j,k)
                sql4='UPDATE CHECK_IN SET ROOM_TYPE=%s WHERE MOBILE_NO=%s'
                u=con.cursor(sql4,data4)
                u.execute(sql4,data4)
                print("Details update successfully!!!")
                con.commit()
        elif al==5:
                l=input("Enter details after changing:")
                m=input("Enter aadhaar card number as a reference detail of guest:")
                data5=(l,m)
                sql5='UPDATE CHECK_IN SET ROOM_TYPE=%s WHERE AADHAAR_CARD_NO=%s'
                v=con.cursor(sql5,data5)
                v.execute(sql5,data5)
                print("Details update successfully!!!")
                con.commit()
        elif al==6:
                n=input("Enter details after changing:")
                o=input("Enter mobile number as a reference detail of guest:")
                data6=(n,o)
                sql6='UPDATE CHECK_IN SET ROOM_TYPE=%s WHERE MOBILE_NO=%s'
                w=con.cursor(sql6,data6)
                w.execute(sql6,data6)
                print("Details update successfully!!!")
                con.commit()
        elif al==7:
                p=input("Enter details after changing:")
                q=input("Enter mobile number as a reference detail of guest:")
                data7=(p,q)
                sql7='UPDATE CHECK_IN SET ROOM_TYPE=%s WHERE MOBILE_NO=%s'
                x=con.cursor(sql7,data7)
                x.execute(sql7,data7)
                print("Details update successfully!!!")
                con.commit()
        else:
                print("Wrong input")
        main()

def detailsname():
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
        if x==1:
                a=input("Enter name of the guest:")
                c=con.cursor()
                c.execute("SELECT * FROM CHECK_IN WHERE NAME=%s",(a,))
                data=c.fetchall()
                head=['Room_Type','Day(s)','Name(s)','Aadhaar_Card_No.','Mobile_No.','Date','Room_No.']
                print(tabulate(data, headers=head, tablefmt='fancy_grid'))
        elif x==2:
                y=input("Enter name of the guest:")
                c=con.cursor()
                c.execute("SELECT * FROM CHECK_OUT WHERE NAME=%s",(y,))
                data=c.fetchall()
                heads=['Room_Type','Room_No.','Name(s)','Mobile_No.','Aadhaar_Card_No.','No._of_day(s)','Total_bill','Date_of_billing']
                print(tabulate(data, headers=heads, tablefmt='grid'))
        else:
                print("Wrong input...")
                
        main()

def calculator():
        import subprocess
        subprocess.Popen('C:\Windows\System32\calc.exe')
        print("Opening calculator...")
        main()

def checkout():
        room=int(input("Enter Room number:"))
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
        rooms=int(input("Enter type of Room from above table(in number):"))
        guest=int(input("Enter number(s) of guest:"))
        for i in range(guest):
                tyrm=input("Enter type of Room(in name):")
                Nm=input("Enter name of the guest:")
                mob=int(input("Enter Mobile_no:"))
                card=input("Enter Aadhar_Card_Number:")
                days=int(input("Enter number of days:"))
                billing=input("Enter date of billing:")
                room1=5000
                room2=2500
                room3=1500
                room4=1000
                tyroom=0
                if rooms==1:
                        tyroom=room1
                        fare=(guest*days*tyroom)
                elif rooms==2:
                        tyroom=room2
                        fare=(guest*days*tyroom)
                elif rooms==3:
                        tyroom=room3
                        fare=(guest*days*tyroom)
                elif rooms==4:
                        tyroom=room4
                        fare=(guest*days*tyroom)
                data=(tyrm,room,Nm,mob,card,days,fare,billing)
                sql1='INSERT INTO CHECK_OUT VALUES(%s,%s,%s,%s,%s,%s,%s,%s)'
                c=con.cursor(sql1,data)
                c.execute(sql1,data)
        print(" ")
        print("Total bill:Rs.",fare)
        con.commit()
        print(" ")
        print("Data entered successfully!!!")
        main()

def discount():
        d=int(input("Enter number of guest(s):"))
        for i in range(d):
                a=input("Enter Aadhaar card number:")
                b=input("Enter amount:")
                data=(b,a)
                sql1='UPDATE CHECK_OUT SET TOTAL_BILL=TOTAL_BILL-%s WHERE AADHAAR_CARD_NO=%s'
                c=con.cursor(sql1,data)
                c.execute(sql1,data)
                print("Bill updated successfully!!!")
        con.commit()
        main()

def updateout():
        head=['Credentials','Column Name']
        myd=[
                ['Press 1','ROOM_TYPE'],
                ['Press 2','ROOM_No'],
                ['Press 3','NAME'],
                ['Press 4','MOBILE_NO'],
                ['Press 5','AADHAAR_CARD_NO'],
                ['Press 6','NO_OF_DAYS'],
                ['Press 7','TOTAL_BILL'],
                ['Press 8','DATE_OF_BILLING']
        ]
        print(tabulate(myd,headers=head, tablefmt='fancy_grid'))
        print(" ")
        al=int(input("Enter your choice:"))
        if al==1:
                b=input("Enter details after changing:")
                d=input("Enter mobile number as a reference detail of guest:")
                data1=(b,d)
                sql1='UPDATE CHECK_OUT SET ROOM_TYPE=%s WHERE MOBILE_NO=%s'
                r=con.cursor(sql1,data1)
                r.execute(sql1,data1)
                print("Details update successfully!!!")
                con.commit()
        elif al==2:
                f=input("Enter details after changing:")
                g=input("Enter mobile number as a reference detail of guest:")
                data2=(f,g)
                sql2='UPDATE CHECK_OUT SET ROOM_TYPE=%s WHERE MOBILE_NO=%s'
                s=con.cursor(sql2,data2)
                s.execute(sql2,data2)
                print("Details update successfully!!!")
                con.commit()
        elif al==3:
                h=input("Enter details after changing:")
                i=input("Enter mobile number as a reference detail of guest:")
                data3=(h,i)
                sql3='UPDATE CHECK_OUT SET ROOM_TYPE=%s WHERE MOBILE_NO=%s'
                t=con.cursor(sql3,data3)
                t.execute(sql3,data3)
                print("Details update successfully!!!")
                con.commit()
        elif al==4:
                j=input("Enter details after changing:")
                k=input("Enter mobile number as a reference detail of guest:")
                data4=(j,k)
                sql4='UPDATE CHECK_OUT SET ROOM_TYPE=%s WHERE MOBILE_NO=%s'
                u=con.cursor(sql4,data4)
                u.execute(sql4,data4)
                print("Details update successfully!!!")
                con.commit()
        elif al==5:
                l=input("Enter details after changing:")
                m=input("Enter aadhaar card number as a reference detail of guest:")
                data5=(l,m)
                sql5='UPDATE CHECK_OUT SET ROOM_TYPE=%s WHERE AADHAAR_CARD_NO=%s'
                v=con.cursor(sql5,data5)
                v.execute(sql5,data5)
                print("Details update successfully!!!")
                con.commit()
        elif al==6:
                n=input("Enter details after changing:")
                o=input("Enter mobile number as a reference detail of guest:")
                data6=(n,o)
                sql6='UPDATE CHECK_OUT SET ROOM_TYPE=%s WHERE MOBILE_NO=%s'
                w=con.cursor(sql6,data6)
                w.execute(sql6,data6)
                print("Details update successfully!!!")
                con.commit()
        elif al==7:
                p=input("Enter details after changing:")
                q=input("Enter mobile number as a reference detail of guest:")
                data7=(p,q)
                sql7='UPDATE CHECK_OUT SET ROOM_TYPE=%s WHERE MOBILE_NO=%s'
                x=con.cursor(sql7,data7)
                x.execute(sql7,data7)
                print("Details update successfully!!!")
                con.commit()
        elif al==8:
                y=input("Enter details after changing:")
                z=input("Enter mobile number as a reference detail of guest:")
                data8=(y,z)
                sql8='UPDATE CHECK_OUT SET ROOM_TYPE=%s WHERE MOBILE_NO=%s'
                x=con.cursor(sql8,data8)
                x.execute(sql8,data8)
                print("Details update successfully!!!")
                con.commit()
        else:
                print("Wrong input")
        main()

def rooms():
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
        print(" ")
        head=['Credentials','Assigned_Task']
        myd=[
                ['Press 1','FROM CHECK_IN'],
                ['Press 2','FROM CHECK_OUT']
        ]
        print(tabulate(myd, headers=head, tablefmt='grid'))
        print(" ")
        a=int(input("Enter your choice:"))
        if a==1:
                k=input("Enter Mobile Number:")
                sql1='DELETE FROM CHECK_IN WHERE MOBILE_NO=%s'
                c=con.cursor(sql1,(k,))
                c.execute(sql1,(k,))
                con.commit()
                print("Data deleted successfully!!!")
        elif a==2:
                h=input("Enter Mobile Number:")
                sql1='DELETE FROM CHECK_OUT WHERE MOBILE_NO=%s'
                c=con.cursor(sql1,(h,))
                c.execute(sql1,(h,))
                con.commit()
                print("Data deleted successfully!!!")
        else:
                print("Wrong input...")
        main()

def deletioncard():
        print(" ")
        head=['Credentials','Assigned_Task']
        myd=[
                ['Press 1','FROM CHECK_IN'],
                ['Press 2','FROM CHECK_OUT']
        ]
        print(tabulate(myd, headers=head, tablefmt='fancy_grid'))
        print(" ")
        a=int(input("Enter your choice:"))
        if a==1:
                k=input("Enter Card Number:")
                sql1='DELETE FROM CHECK_IN WHERE AADHAAR_CARD_NO=%s'
                c=con.cursor(sql1,(k,))
                c.execute(sql1,(k,))
                con.commit()
                print(" ")
                print("Data deleted successfully!!!")
        elif a==2:
                h=input("Enter Card Number:")
                sql1='DELETE FROM CHECK_OUT WHERE AADHAAR_CARD_NO=%s'
                c=con.cursor(sql1,(h,))
                c.execute(sql1,(h,))
                con.commit()
                print(" ")
                print("Data deleted successfully!!!")
        else:
                print("Wrong input...")
        main()

def services():
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
        print(" ")
        
        head=['Credential','Assigned_Task']

        myd=[
                ['Press 1','FARE AND FACILITIES'],
                ['Press 2','CHECK_IN PROMPT'],
                ['Press 3','UPDATE_IN PROMPT'],
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
        choice=int(input("Enter PROMPT choice:"))
        if choice==1:
                rooms()
        elif choice==2:
                checkin()
        elif choice==3:
                updatein()
        elif choice==4:
                detailsroom()
        elif choice==5:
                detailsname()
        elif choice==6:
                calculator()
        elif choice==7:
                checkout()
        elif choice==8:
                updateout()
        elif choice==9:
                discount()
        elif choice==10:
                services()
        elif choice==11:
                deletionum()
        elif choice==12:
                deletioncard()
        else:
                print("WRONG INPUT... ENTER VALID CHOICE")
        main()
main()  