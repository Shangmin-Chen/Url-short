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
root_color = "#224870"
input_color = "#2a4494"
output_color = "#4ea5d9"
root.config(bg=root_color)


# define functions
def callback(event):
    webbrowser.open_new_tab(event)


def submit_url():
    api = "7b5faea0c51b9cb1aa4d8329d93cd689a7acc"
    url = shorturl.get()
    api_url = f"https://cutt.ly/api/api.php?key={api}&short={url}"
    data = requests.get(api_url).json()

    url_label = tkinter.Label(output_frame, text="Short Link: " + data["url"]["shortLink"] + "\n-----",
                              font=('Helveticabold'), fg="#0000FF", bg=output_color)

    # \/ is from stack overflow
    url_label.pack()
    url_label.bind("<Button-1>", lambda e:
    callback(data["url"]["shortLink"]))
    shorturl.delete(0, END)


# define frame
input_frame = tkinter.LabelFrame(root, bg=input_color)
output_frame = tkinter.LabelFrame(root, bg=output_color)
input_frame.pack(pady=10)
output_frame.pack(padx=10, pady=(0, 10), fill=BOTH, expand=True)

# create widgets
ask = tkinter.Label(input_frame, text="Enter Url", bg=input_color)
shorturl = tkinter.Entry(input_frame, text="Enter Url", width=40)
submit_button = tkinter.Button(input_frame, text="submit", command=submit_url)
ask.grid(row=0, column=0)
shorturl.grid(row=1, column=0, padx=10, pady=10)
submit_button.grid(row=1, column=1, padx=10, pady=10, ipadx=20)

# run root window main loop
root.mainloop()
