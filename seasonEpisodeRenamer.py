from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox

from episodeClass import EpisodeFormatter
from seasonClass import SeasonFormatter

root = Tk()
root.title("Episode Renamer")

#Sets up the look
mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

#Select type of thing to be organized (Season/Episode)
ttk.Label(mainframe, text = "Type: ", width = 10).grid(row = 0, column = 0, sticky = (N, W), ipadx = 10)
renameType = StringVar(None,"Season")

ttk.Radiobutton(mainframe, 
              text="Season",
              variable=renameType, 
              value="Season").grid(row = 0, column = 1)
ttk.Radiobutton(mainframe, 
              text="Episode",
              variable=renameType, 
              value="Episode").grid(row = 0, column = 2,sticky = (N, E))

ttk.Label(mainframe, text = "Location: ").grid(row = 1, column = 0, sticky = (N, W), ipadx = 10)

# This section is for selection your file
def browseButton():
    # Allow user to select a directory and store it in global var
    # called folder_path
    global folderPath
    filename = filedialog.askdirectory()
    folderPath.set(filename)
    print(filename)

folderPath = StringVar()
locationLabel = ttk.Label(mainframe, textvariable=folderPath)
locationLabel.grid(row=1, column=1, sticky = (W))
browseButton = ttk.Button(mainframe,text="Browse", command=browseButton)
browseButton.grid(row=1, column=2)

# Closes the window and performs the renaming with the options selected
# This section is for selection your file
def close(event = None):
    optionType = renameType.get()
    path = folderPath.get()
    if not (optionType and path):
        messagebox.showerror("Incomplete", "Please fill out all the options")
        return
    if optionType =="Season":
        seasonFormatter = SeasonFormatter(path)
        seasonFormatter.renameSeasons()
    elif optionType == "Episode":
        episodeFormatter = EpisodeFormatter(path)
        episodeFormatter.renameEpisodes()
    root.destroy()

ttk.Button(mainframe,text="Rename", command=close).grid(row=4, column=0, columnspan = 3)

root.bind('<Return>', close)

root.mainloop()