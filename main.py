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
    title = input("Enter title...")
    description = input("Enter description...")
    sql = "INSERT INTO tasks (id, name, description) VALUES (Null,%s,%s)"
    val = (title,description)
    cursor.execute(sql,val)
    db.commit()


def remove_task():
    print_tasks()


while True:
    operation = input("'Add', 'Print', 'Delete', 'Exit' ")

    match operation:
        case 'Add':
            add_task()
        case 'Print':
            print_tasks()
        case 'Delete':
            remove_task()
        case 'Exit':
            db.close()
            break