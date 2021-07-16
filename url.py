import tkinter
from tkinter import BOTH, END
import requests
import webbrowser

# Notes: Tkinter was from my APCOMSCI class, the api was from a website, the hyperlink click was from stack overflow
# Finished: (July 14th 2021)
# -----------------------------
# define window
root = tkinter.Tk()
root.title("Url Shortener")
root.geometry("600x400")
root.resizable(0, 0)

# define fonts and colors
root_color = "#b6da67"
input_color = "#a0c05b"
output_color = "#d3eb9e"
root.config(bg=root_color)


# define functions
def callback(event):
    webbrowser.open_new_tab(event)


def submit_url():
    api = "7b5faea0c51b9cb1aa4d8329d93cd689a7acc"
    url = shorturl.get()
    api_url = f"https://cutt.ly/api/api.php?key={api}&short={url}"
    data = requests.get(api_url).json()
    if int(data["url"]["status"]) != 7:
        error_label = tkinter.Label(output_frame, text="Error, enter valid link", bg=output_color)
        error_label.pack()
    else:
        url_label = tkinter.Label(output_frame, text="Short Link: " + data["url"]["shortLink"],
                                  font='Helveticabold', fg="#0000FF", bg=output_color)
        text_frame.insert(1.0, data["url"]["shortLink"] + "\n")
        url_label.pack()
        url_label.bind("<Button-1>", lambda e:
        callback(data["url"]["shortLink"]))

    shorturl.delete(0, END)


# define frame
input_frame = tkinter.LabelFrame(root, bg=input_color)
output_frame = tkinter.LabelFrame(root, bg=output_color)
link_desc = tkinter.LabelFrame(root, bg=root_color)
text_desc = tkinter.LabelFrame(root, bg=root_color)
text_frame = tkinter.Text(root, height=5, pady=10, bg=output_color)
clear_frame = tkinter.LabelFrame(root, bg=root_color)
# pack all frames
input_frame.pack()
link_desc.pack()
output_frame.pack(padx=10, fill=BOTH, expand=True)
text_desc.pack()
text_frame.pack()
clear_frame.pack()

# create widgets
click_label = tkinter.Label(link_desc, text="Click on blue link to open!", bg=root_color)
click_label.pack()
text_desc_label = tkinter.Label(text_desc, text="Use textbox below to copy and paste!", bg=root_color)
text_desc_label.pack()
ask = tkinter.Label(input_frame, text="Enter Url:", bg=input_color)
shorturl = tkinter.Entry(input_frame, text="Enter Url", width=40)
submit_button = tkinter.Button(input_frame, text="Submit", command=submit_url)
ask.grid(row=0, column=0)
shorturl.grid(row=0, column=1, padx=10, pady=10)
submit_button.grid(row=0, column=2, padx=10, pady=10, ipadx=20)

# run root window main loop
root.mainloop()
