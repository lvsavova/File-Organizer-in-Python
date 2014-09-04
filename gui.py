from tkinter import *
from tkinter.messagebox import showinfo, showerror, showwarning
from tkinter.filedialog import askdirectory
import configparser
import organizefiles

root = Tk()
root.wm_title("File Organizer")
target_entry = Entry(root, state='disabled')
source_entry = Entry(root, state='disabled')
content_entry = Entry(root, state='disabled')
selected_type = ""


def callback_dir(entry):
    """
    Callback method for browse buttons that open
    a directory chooser dialog. After directory is chosen
    writes its full path to the respected text entry.
    """
    entry.configure(state='normal')
    entry.delete(0, END)
    directory_name = askdirectory()
    entry.insert(0, directory_name)
    entry.configure(state='disabled')


def callback_rb(type, content_entry_state):
    """
    Callback method for the radio buttons that hold
    information on type of reorganization. Writes
    the type in a global variable selected_type.
    """
    content_entry.configure(state=content_entry_state)
    global selected_type
    selected_type = type


def organize():
    """
    Callback method for the Organize button. Edits the
    config.ini file according to the values from the gui elements.
    Raises exceptions upon empty entries or unselected reorganization
    type. At last calls the main method in organizefiles.py, notifies
    the user if something went wrong and when the job has successfully
    finished
    """
    if selected_type == "":
        showwarning('Ok', 'Please choose organization type!')
        raise Exception('Organization type not set')
    if source_entry.get() == "" or target_entry.get() == "":
        showwarning('Ok', 'Please choose target and source folders!')
        raise Exception('Target or Source directory not set')
    if selected_type == "content" and content_entry.get() == "":
        showwarning('Ok', 'Choose strings by which docx files are organized!')
        raise Exception('No strings by which to perform content organization ')

    config = configparser.ConfigParser()
    config.read(r'config.ini')
    config.set('Directory', 'SourceDirectoryPath', source_entry.get())
    config.set('Directory', 'TargetDirectoryPath', target_entry.get())
    config.set('Content', 'SearchedText', content_entry.get())
    config.set('Orgtype', 'ReorganizationType', selected_type)

    with open('config.ini', 'w') as configfile:
        config.write(configfile)
    configfile.close()
    try:
        organizefiles.main()
        showinfo('Ok', 'Directory re-organized!')
    except Exception as e:
        showerror('НЕ', 'Something went wrong!')

w = Label(root, text="Choose type of re-organization:")
w.pack()
v = IntVar()
Radiobutton(root, text="By Type", variable=v, value="type",
            command=lambda: callback_rb("type", "disabled")).pack(anchor=W)
Radiobutton(root, text="By Extension", variable=v, value="extension",
            command=lambda: callback_rb("extension",
                                        "disabled")).pack(anchor=W)
Radiobutton(root, text="By Content", variable=v, value="content",
            command=lambda: callback_rb("content", "normal")).pack(anchor=W)


w = Label(root, text="Choose directory to be re-organized:")
w.pack()
source_entry.pack()
source_browse_button = Button(root, text="Browse",
                              command=lambda: callback_dir(source_entry))
source_browse_button.pack()

w = Label(root, text="Choose target directory:")
w.pack()
target_entry.pack()
target_browse_button = Button(root, text="Browse",
                              command=lambda: callback_dir(target_entry))
target_browse_button.pack()

w = Label(root,
          text="Type strings(semicolon separated) for content organization:")
w.pack()
content_entry.pack()

organize_button = Button(root, text="Organize Now", command=organize)
organize_button.pack()

root.mainloop()
