import tkinter as tk
from tkinter import filedialog

class notepad(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)

        #setting title
        self.title("NOTE PAD")

        #text widget
        self.text=tk.Text(self,wrap="word")
        self.text.pack(side="top",fill="both",expand=True)

        #creating menu bar
        self.menu=tk.Menu(self)
        self.config(menu=self.menu)

        #create a file menu
        file_menu=tk.Menu(self.menu)
        self.menu.add_cascade(label="File",menu=file_menu)
        file_menu.add_command(label="New",command=self.new_file_maker)
        file_menu.add_command(label="open",command=self.file_opener)
        file_menu.add_command(label="save",command=self.file_saver)

        #creating a edit menu
        edit_menu=tk.Menu(self.menu)
        self.menu.add_cascade(label="edit",menu=edit_menu)
        edit_menu.add_command(label="Cut",command=self.cut)
        edit_menu.add_command(label="Paste",command=self.paste)
        edit_menu.add_command(label="Copy",command=self.copy)

    def new_file_maker(self):
        self.text.delete("1.0","end")
        self.title("NOTE PAD")
    
    def file_opener(self):
        file = filedialog.askopenfile(parent=self,mode="rb",title="open a file")
        if file:
            contents=file.read()
            self.text.delete("1.0","end")
            self.text.insert("1.0",contents)
            file.close()
            self.title(file.name+"-NOTEPAD")
    
    def file_saver(self):
        file=filedialog.asksaveasfile(mode="w",defaultextension=".txt",filetypes=[("Text Documents","*.txt"),("All Files","*.*")])
        if file:
            contents=self.text.get("1.0","end")
            file.write(contents)
            file.close()
            self.title(file.name+"-NOTEPAD")
    def cut(self):
        self.text.event_generate("<<Cut>>")

    def paste(self):
        self.text.event_generate("<<Paste>>")

    def copy(self):
        self.text.event_generate("<<Copy>>")

    

if __name__=="__main__":
    np = notepad()
    np.mainloop()
