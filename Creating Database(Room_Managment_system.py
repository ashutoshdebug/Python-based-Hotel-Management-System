import mysql.connector as sql
con=sql.connect(host='localhost', user='root', passwd='Your Password')
b=con.cursor()

def creation():
        c='CREATE DATABASE ROOM_MANAGEMENT_SYSTEM'
        b.execute(c)
        print("DATABASE CREATED SUCCESSFULLY!!!")
        d='USE ROOM_MANAGEMENT_SYSTEM'
        b.execute(d)
        e='CREATE TABLE CHECK_IN(ROOM_TYPE VARCHAR(20), NO_OF_DAYS INT, NAME VARCHAR(20), AADHAAR_CARD_NO VARCHAR(12), MOBILE_NO VARCHAR(13), DATE VARCHAR(20), ROOM_NO INT)'
        b.execute(e)
        print("CHECK_IN TABLE CREATED SUCCESSFULLY!!!")
        f='CREATE TABLE CHECK_OUT(ROOM_TYPE VARCHAR(30), ROOM_NO INT, NAME VARCHAR(20), MOBILE_NO VARCHAR(13), AADHAAR_CARD_NO VARCHAR(12), NO_OF_DAYS INT, TOTAL_BILL FLOAT, DATE_OF_BILLING VARCHAR(20))'
        b.execute(f)
        print("CHECK_OUT TABLE CREATED SUCCESSFULLY!!!")
        con.commit()
        main()

def deletion():
        k='DROP DATABASE ROOM_MANAGEMENT_SYSTEM'
        b.execute(k)
        print("DATABASE deleted successfully!!!")
        con.commit()
        main()

def main():
        print("Enter 1 to create database 'ROOM_MANAGEMENT_SYSTEM'")
        print("Enter 2 to drop database 'ROOM_MANAGEMENT_SYSTEM'")
        a=int(input("Enter your choice:"))
        if a==1:
                creation()
        elif a==2:
                deletion()
        else:
                print("Wrong input...")
        main()
main()
