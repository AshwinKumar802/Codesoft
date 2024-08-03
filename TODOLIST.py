
from tkinter import *
from tkinter import messagebox
import sqlite3 as sql

def add_task():  
    task_string = task_field.get()  
    if not task_string:  
        messagebox.showinfo('Error', 'Field is Empty.')  
        return
    tasks.append(task_string)   
    the_cursor.execute('insert into tasks values (?)', (task_string ,))    
    list_update()    
    task_field.delete(0, 'end')  

def list_update():    
    task_listbox.delete(0, 'end')    
    for task in tasks:    
        task_listbox.insert('end', task)  

def delete_task():  
    try:  
        selected_index = task_listbox.curselection()[0]
        the_value = task_listbox.get(selected_index)    
        tasks.remove(the_value)    
        the_cursor.execute('delete from tasks where title = ?', (the_value,))
        list_update()   
    except IndexError:   
        messagebox.showinfo('Error', 'No Task Selected. Cannot Delete.')        

def delete_all_tasks():  
    if messagebox.askyesno('Delete All', 'Are you sure?'):    
        tasks.clear()    
        the_cursor.execute('delete from tasks')   
        list_update()  

def close():    
    the_connection.commit()  
    the_cursor.close()      
    the_connection.close()  
    guiWindow.destroy()  

def retrieve_database():    
    tasks.clear()  
    tasks.extend(row[0] for row in the_cursor.execute('select title from tasks'))  

if __name__ == "__main__":   
    guiWindow = Tk()   
    guiWindow.title("To-Do List")  
    guiWindow.geometry("665x400+550+250")   
    guiWindow.configure(bg = "#B5E5CF")  

    the_connection = sql.connect('listOfTasks.db')   
    the_cursor = the_connection.cursor()   
    the_cursor.execute('create table if not exists tasks (title text)')  

    tasks = []  

    functions_frame = Frame(guiWindow, bg = "#8EE5EE") 
    functions_frame.pack(side = "top", expand = True, fill = "both")  

    Label(functions_frame, text = "TO-DO-LIST \n Enter the Task Title:", font = ("arial", "14", "bold"), background = "#8EE5EE", foreground="#FF6103").place(x = 20, y = 30)  
    task_field = Entry(functions_frame, font = ("Arial", "14"), width = 42, foreground="black", background = "white")    
    task_field.place(x = 180, y = 30)  

    Button(functions_frame, text = "Add", width = 15, bg='#D4AC0D', font=("arial", "14", "bold"), command = add_task).place(x = 18, y = 80)  
    Button(functions_frame, text = "Remove", width = 15, bg='#D4AC0D', font=("arial", "14", "bold"), command = delete_task).place(x = 240, y = 80)  
    Button(functions_frame, text = "Delete All", width = 15, bg='#D4AC0D', font=("arial", "14", "bold"), command = delete_all_tasks).place(x = 460, y = 80)  
    Button(functions_frame, text = "Exit / Close", width = 52, bg='#D4AC0D', font=("arial", "14", "bold"), command = close).place(x = 17, y = 330)  

    task_listbox = Listbox(functions_frame, width = 70, height = 9, font="bold", selectmode = 'SINGLE', background = "WHITE", foreground="BLACK", selectbackground = "#FF8C00", selectforeground="BLACK")    
    task_listbox.place(x = 17, y = 140)  

    retrieve_database()  
    list_update()    
    guiWindow.mainloop()  
