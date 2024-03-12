from tkinter import *

class Todo:
    def __init__(self, root):
        self.root = root
        root.resizable(False,False)
        self.root.title('To-do-list')
        self.root.geometry('650x410+300+150')

        self.label = Label(self.root, text='To-Do-List-App', font='Arial 25 bold', width=10, bd=5, bg='brown', fg='lightgray')
        self.label.pack(side='top', fill=BOTH)

        self.label2 = Label(self.root, text='Add Task', font='Arial 18 bold', width=10, bd=5, bg='brown', fg='black')
        self.label2.place(x=40, y=54)

        self.label3 = Label(self.root, text='Tasks', font='Arial 18 bold', width=10, bd=5, bg='brown', fg='black')
        self.label3.place(x=320, y=54)

        self.main_text = Listbox(self.root, height=9, bd=5, width=23, font="Arial 20 italic bold")
        self.main_text.place(x=280, y=100)

        self.text = Text(self.root, bd=5, height=2, width=30, font='Arial 10 bold')
        self.text.place(x=20, y=120)

        self.load_tasks()

        # Buttons
        self.add_button = Button(self.root, text="Add", width=10, command=self.add_task, bg='brown', fg='black',font="serif 10 bold")
        self.add_button.place(x=30, y=180)

        self.delete_button = Button(self.root, text="Delete", width=10, command=self.delete_task, bg='brown', fg='lightgrey',font="serif 10 bold")
        self.delete_button.place(x=130, y=180)

    def add_task(self):
        content = self.text.get(1.0, END)
        if content.strip():  # check if content is not empty
            self.main_text.insert(END, content)
            with open('data.txt', 'a') as file:
                file.write(content.strip() + '\n')
            self.text.delete(1.0, END)

    def delete_task(self):
        delete_ = self.main_text.curselection()
        if delete_:
            index = delete_[0]
            self.main_text.delete(index)
            with open('data.txt', 'r+') as f:
                lines = f.readlines()
                f.seek(0)
                for line in lines:
                    if line.strip() != self.main_text.get(index):
                        f.write(line)
                f.truncate()

    def load_tasks(self):
        try:
            with open('data.txt', 'r') as file:
                tasks = file.readlines()
                for task in tasks:
                    self.main_text.insert(END, task.strip())
        except FileNotFoundError:
            pass


def main():
    root = Tk()
    ui = Todo(root)
    root.mainloop()


if __name__ == "__main__":
    main()
