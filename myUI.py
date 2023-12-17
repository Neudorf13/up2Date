import subprocess
import tkinter as tk

from myScraper import *

myItems = {}

options = [
    "java",
    "python",
    "git",
    "ruby"
]


def testSetItem(text):
    try:
        result = subprocess.run([text, "--version"], capture_output=True, text=True)
        output = result.stdout
        print(output)
        return_code = result.returncode
        if return_code == 0:
            tempString = result.stdout
            lines = tempString.splitlines()
            if len(lines) > 1:
                tempString = lines[0]
            tempString = tempString.replace('\n', '')

            if text == 'python':
                versionString = scrapePython()
                formatted = formatPython(versionString)
                myItems[text] = (tempString, formatted)
            elif text == 'ruby':
                versionString = scrapeRuby()
                myItems[text] = (tempString, versionString)
            else:
                myItems[text] = (tempString, "Haven't Implemented Yet.")

            print("Command executed successfully.")

        else:

            print("Command failed with return code", return_code)
    except Exception as e:
        print(e)


def displayItems():
    for widget in frame.winfo_children():
        widget.destroy()

    frame.columnconfigure(0, weight=1)
    frame.columnconfigure(1, weight=1)
    frame.columnconfigure(2, weight=1)

    label1 = tk.Label(frame, text='Item')
    label1.grid(row=0, column=0, sticky=tk.W + tk.E)
    label2 = tk.Label(frame, text='Current version')
    label2.grid(row=0, column=1, sticky=tk.W + tk.E)
    label3 = tk.Label(frame, text='Newest Version')
    label3.grid(row=0, column=2, sticky=tk.W + tk.E)

    count = 1
    for key, (value1, value2) in myItems.items():
        print("Inside Loop!")
        tempLabel1 = tk.Label(frame, text=f'{key}')
        tempLabel2 = tk.Label(frame, text=f'{value1}')
        tempLabel3 = tk.Label(frame, text=f'{value2}')
        tempLabel1.grid(row=count, column=0, sticky=tk.W + tk.E)
        tempLabel2.grid(row=count, column=1, sticky=tk.W + tk.E)
        tempLabel3.grid(row=count, column=2, sticky=tk.W + tk.E)
        count += 1

    frame.pack(fill='x')


def update_display():
    # Update the displayed items
    displayItems()
    # Schedule the next update after a certain time (in milliseconds)
    root.after(5000, update_display)  # Update every 5 seconds (5000 milliseconds)


def show():
    selected_items = selected_listbox.get(0, tk.END)
    print(selected_items)
    for item in selected_items:
        testSetItem(item)
    displayItems()



def move_to_selected():
    selected_item = options_listbox.get(options_listbox.curselection())
    selected_listbox.insert(tk.END, selected_item)
    options_listbox.delete(options_listbox.curselection())


def move_to_options():
    selected_item = selected_listbox.get(selected_listbox.curselection())
    options_listbox.insert(tk.END, selected_item)
    selected_listbox.delete(selected_listbox.curselection())

root = tk.Tk()

root.geometry("1000x500")  # window dimensions
root.title("Up-2-Date")  # title of window

label = tk.Label(root, text="Up-2-Date", font=('Times New Roman', 18))
label.pack(pady=20)

# Create Listbox for available options
options_listbox = tk.Listbox(root, selectmode=tk.SINGLE)
# options = ["Option 1", "Option 2", "Option 3", "Option 4", "Option 5"]

for option in options:
    options_listbox.insert(tk.END, option)
options_listbox.pack(side=tk.LEFT, padx=10)


move_right_button = tk.Button(root, text=">", command=move_to_selected)
move_right_button.pack(side=tk.LEFT)

move_left_button = tk.Button(root, text="<", command=move_to_options)
move_left_button.pack(side=tk.LEFT)


selected_listbox = tk.Listbox(root, selectmode=tk.SINGLE)
selected_listbox.pack(side=tk.LEFT, padx=10)



button1 = tk.Button(root, text="Load Items", command=show)
button1.pack()

frame = tk.Frame(root)

displayItems()
# root.after(5000, update_display)  # Update every 5 seconds (5000 milliseconds)
root.mainloop()
