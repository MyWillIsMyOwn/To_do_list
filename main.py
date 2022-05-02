import mysql.connector

connect = input("Do you want to connect to database? ")

if connect=="Yes":
    try:
        db = mysql.connector.connect(host='localhost',database='to_do',user='root',password='niema123')
        if db.is_connected():
            print("Connected to {} database".format(db.database))
    except:
        print("Error while connecting to database")


    disconnect = input("To disconnect type 'exit: ")

    if disconnect=="Exit":
        db.close()