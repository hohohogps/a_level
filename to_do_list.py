from tkinter import *

td_list = {}

root = Tk()
root.title("To do list")
root.geometry('350x200')
add_task_var = StringVar()
comp_task_var = StringVar()


def add_task():
    addtask = add_task_var.get()
    td_list[addtask] = False
    add_task_var.set('')

def show_tasks():
    global td_list
    show_label.configure(text = list(td_list.keys()))

def complete_task():
    comptask = comp_task_var.get()
    td_list[comptask] = True
    comp_task_var.set('')

add_label = Label(root, text = 'Add a task')
add_entry = Entry(root,textvariable = add_task_var)
add_btn = Button(root,text = 'Submit', command = add_task)

show_label = Label(root,text='')
show_btn = Button(root,text = 'Show all tasks', command = show_tasks)

comp_label = Label(root,text='Enter task to be set completed')
comp_entry = Entry(root,textvariable = comp_task_var)
comp_btn = Button(root,text = 'Submit', command = complete_task)

quit_btn = Button(root, text="Quit", command=root.destroy)

add_label.grid(row=0,column=0)
add_entry.grid(row=0,column=1)
add_btn.grid(row=1,column=1)

show_label.grid(row=2,column=0)
show_btn.grid(row=2,column=1)

comp_label.grid(row=3,column=0)
comp_entry.grid(row=3,column=1)
comp_btn.grid(row=4,column=1)

quit_btn.grid(row=5,column=1)


root.mainloop()
