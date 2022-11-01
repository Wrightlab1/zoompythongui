
from tkinter import *
from tkinter import ttk
import webbrowser
from utils.log import *
from utils.req import *
from utils.printJSON import *

# clear Text widget


def clearToTextInput():
    print("Text widget cleared")
    text.delete("1.0", "end")

# Get logs and write them to text widget


def display_logs():
    print("displaying logs")
    with open("logs/log.log", "r") as f:
        text.insert(INSERT, f.read())


def clear_logs():
    print("logs cleared")
    open('logs/log.log', 'w').close()


def read_inputs():
    url = URL.get()
    data = DATA.get()
    action = ACTION.get()
    return [action, url, data]


# write data to the text widget


def show_msg(message):
    try:
        parsed = json.loads(message)
        formatted = json.dumps(parsed, indent=4)
        text.insert("2.0", formatted)
    except ValueError as e:
        text.insert("2.0", message)


        # SETUP LOGGING
create_log()


def new_request():
    clearToTextInput()
    inputs = read_inputs()
    print("Sending Request: Action: %s, URL: %s, Body: %s" %
          (inputs[0], inputs[1], inputs[2]))
    response = send_request(inputs[0], inputs[1], inputs[2])
    show_msg("Response status code: %s \n" % response[1])
    show_msg(response[0])


def open_docs():
    print("opening Zoom API docs")
    webbrowser.open_new(
        "https://marketplace.zoom.us/docs/api-reference/zoom-api/methods/#overview")


# Code Goes Here
# setup tkinter
window = Tk()
window.title("POSTguy")

# Setup syntac highlighting


# Create input fields
URL = Entry(
    window, text="url", width=60)
DATA = Entry(
    window, text="data", width=60)
ACTION = Entry(
    window, text="action", width=60)


# Create a button
# Create a Button to fetch Token
btn = ttk.Button(window, text="Send Request",
                 command=new_request)
# Create a button to clear text
clear_btn = ttk.Button(window, text="Clear Window", command=clearToTextInput)

# create a button to display the log
log_btn = ttk.Button(window, text="Show Logs", command=display_logs)

# create a button to clear the log
clear_log_btn = ttk.Button(window, text="Clear Logs", command=clear_logs)
# create a button to open Zoom API docs
open_docs_btn = ttk.Button(window, text="Zoom API Docs", command=open_docs)

# create a text Box to show the response and dispaly logs
text = Text(window, height=60, width=200, relief=RIDGE, borderwidth=2)
text.insert("1.0", "")

# draw Window
Label(window, text="URL: https://api.zoom.us/v2").grid(row=1, column=0, columnspan=2)
Label(window, text="Data: must be valid JSON").grid(
    row=2, column=0, columnspan=2)
Label(window, text="Action: get,post,patch,delete").grid(
    row=3, column=0, columnspan=2)
URL.grid(row=1, padx=4, column=2, columnspan=4)
DATA.grid(row=2, padx=4, column=2, columnspan=4)
ACTION.grid(row=3, padx=4, column=2, columnspan=4)
btn.grid(row=4, column=3)
text.grid(row=5, columnspan=8)
log_btn.grid(row=6, column=0)
clear_log_btn.grid(row=6, column=1)
open_docs_btn.grid(row=6, column=6)
clear_btn.grid(row=6, column=7)


# run the app
window.mainloop()
