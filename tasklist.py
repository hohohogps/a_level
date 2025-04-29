import sqlite3, os
from pprint import pprint
from datetime import date, timedelta

db_path = os.path.join(os.getcwd(), 'tasklist.db')
connection = sqlite3.connect(db_path)
cur = connection.cursor()

cur.execute("PRAGMA foreign_keys = ON")
cur.execute("""CREATE TABLE IF NOT EXISTS User (
                userid INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                name TEXT NOT NULL,
                avg_grade REAL
)""")
cur.execute("""CREATE TABLE IF NOT EXISTS Task (
                taskid INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                description TEXT NOT NULL,
                category TEXT NOT NULL,
                date_created TEXT NOT NULL
)""")
cur.execute("""CREATE TABLE IF NOT EXISTS User_task (
                userid INTEGER NOT NULL,
                taskid INTEGER NOT NULL,
                due_date TEXT NOT NULL,
                date_assigned TEXT,
                grade INTEGER,
                PRIMARY KEY (userid, taskid),
                FOREIGN KEY (userid) REFERENCES User(userid),
                FOREIGN KEY (taskid) REFERENCES Task(taskid)
)""")

connection.commit()

def add_task():
    cat_dict = {'s': 'science', 'm': 'math', 'e': 'english', 'l': 'language', 'a': 'arts'}
    des = ''
    cat = ''
    while (not des) or (not cat):
        des = str(input('Enter description. Must not be null.'))
        pprint(list(cat_dict.values()))
        cat = (input('Enter first character of subject.')).lower()
        if cat not in cat_dict.keys():
            cat = ''
        else:
            cat = cat_dict[cat]    
    dat = date.today().strftime('%Y-%m-%d')
            
    cur.execute("""INSERT INTO Task (description, category, date_created) VALUES (?, ?, ?)""", [des, cat, dat])
    connection.commit()

def add_user():
    name = ''
    while not name:
        name = str(input('Enter name. Must not be null.'))
    
    cur.execute("""INSERT INTO User (name, avg_grade) VALUES (?, ?)""", [name, 0])
    connection.commit()

def show_all_tasks():
    category_filter = input("Filter tasks by category (leave blank for no filter): ").lower()
    query = "SELECT taskid, description, category, date_created FROM Task"
    params = []

    if category_filter:
        query += " WHERE category = ?"
        params.append(category_filter)

    query += " ORDER BY date_created"
    
    cur.execute(query, params)
    tasks = cur.fetchall()

    if not tasks:
        print("No tasks found.\n")
        return False
    
    print("\nAll Tasks:")
    for taskid, description, category, date_created in tasks:
        print(f"Task ID: {taskid}\nDescription: {description}\nCategory: {category}\nCreated on: {date_created}\n")
    return True

def mark_task():
    cur.execute("SELECT userid, name FROM User")
    users = cur.fetchall()
    pprint([(r[0], r[1]) for r in users])
    user_id_list = [r[0] for r in users]

    user_id = None
    while user_id not in user_id_list:
        try:
            user_id = int(input('Enter user_id of student to assign task to: '))
            if user_id not in user_id_list:
                print("Invalid user ID.")
        except ValueError:
            print("Please enter a valid number.")

    cur.execute("""SELECT Task.taskid, Task.description FROM Task JOIN User_task ON Task.taskid = User_task.taskid WHERE User_task.userid = ?""", [user_id])
    tasks = cur.fetchall()
    pprint([(r[0], r[1]) for r in tasks]) 
    task_id_list = [r[0] for r in tasks] 

    task_id = None  
    while task_id not in task_id_list:
        try:
            task_id = int(input('Enter taskid of task to mark: '))
            if task_id not in task_id_list:
                print("Invalid task ID.")
        except ValueError:
            print("Please enter a valid number.")
    
    while True:
        try:
            marks = int(input('Enter an integer mark from 1–10: '))
            if marks not in range(1, 11):
                print("Not in range.")
                continue
            break
        except ValueError:
            print("Not an integer.")
    
    cur.execute("""UPDATE User_task SET grade = ? WHERE userid = ? AND taskid = ?""", [marks, user_id, task_id])
    connection.commit()

def assign_task():
    if show_all_tasks():
        print('No tasks to assign.')
        return

    cur.execute("SELECT taskid FROM Task")
    task_id_list = [r[0] for r in cur.fetchall()]
    pprint(task_id_list)

    task_id = None
    while task_id not in task_id_list:
        try:
            task_id = int(input('Enter task id to assign: '))
            if task_id not in task_id_list:
                print("Invalid task ID.")
        except ValueError:
            print("Please enter a valid number.")

    cur.execute("SELECT userid, name FROM User")
    users = cur.fetchall()
    pprint([(r[0], r[1]) for r in users])
    user_id_list = [r[0] for r in users]

    user_id = None
    while user_id not in user_id_list:
        try:
            user_id = int(input('Enter user_id of student to assign task to: '))
            if user_id not in user_id_list:
                print("Invalid user ID.")
        except ValueError:
            print("Please enter a valid number.")

    while True:
        try:
            days = int(input('In how many days is the task due? '))
            if days < 0:
                print("Please enter a non-negative number.")
                continue
            break
        except ValueError:
            print("Please enter a valid number.")

    due_date = (date.today() + timedelta(days=days)).strftime('%Y-%m-%d')
    date_assigned = date.today().strftime('%Y-%m-%d')

    cur.execute("""INSERT INTO User_task (userid, taskid, due_date, date_assigned, grade) VALUES (?, ?, ?, ?, ?)""", [user_id, task_id, due_date, date_assigned, 0])
    connection.commit()

while True:
    options = {
        1: ("Add a task", add_task),
        2: ("Add a user", add_user),
        3: ("Show all tasks", show_all_tasks),
        4: ("Mark a task", mark_task),
        5: ("Assign a task", assign_task)
    }

    print("Options")
    for k, (desc, _) in options.items():
        print(f"{k}: {desc}")
    print("6: Quit")

    try:
        choice = int(input("Enter your choice: "))
        if choice == 6:
            break
        elif choice in options:
            options[choice][1]()
        else:
            print("Invalid option. Please select a number from the menu.")
    except ValueError:
        print("Please enter a valid number.")

connection.close()
