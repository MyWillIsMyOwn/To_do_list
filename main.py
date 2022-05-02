import mysql.connector

try:
    db = mysql.connector.connect(host='localhost', database='to_do', user='root', password='niema123')
    cursor = db.cursor()
    if db.is_connected():
        print("Connected to {} database".format(db.database))
except:
    print("Error while connecting to database")

def print_tasks():
    cursor.execute("SELECT * FROM tasks")
    result = cursor.fetchall()
    for row in result:
        print("Id: {}, Title: {}, Description: {}".format(row[0],row[1],row[2]))
    print("")



def add_task():
    pass

def remove_task():
    print_tasks()




while True:
    operation = input("'Add', 'Print', 'Delete', 'Exit' ")

    match operation:
        case 'Add':
            pass
        case 'Print':
            print_tasks()
        case 'Delete':
            remove_task()
        case 'Exit':
            db.close()
            break