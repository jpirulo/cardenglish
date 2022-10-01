from tkinter import *
from tkinter import messagebox
import pandas
import random
english_word = {
to_learn = {}
try:
    data=pandas.read_csv("data/words_to_learn.csv")
except:
    original_data = pandas.read_csv("data/english.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")
def next_card():
    global english_word,flip_timer
    window.after_cancel(flip_timer)
    english_word = random.choice (to_learn)
    canvas.itemconfig(card_title,text="English",fill="black")
    canvas.itemconfig(card_word,text=english_word["English"],fill="black")
    canvas.itemconfig(card_background,image=front_img)
    flip_timer=window.after(3000,func=flip_card)
def is_know():
    to_learn.remove(english_word)
    data=pandas.DataFrame(to_learn)
    data.to_csv("data/words_to_learn.csv",index=False)
    next_card()
def flip_card():
    canvas.itemconfig(card_title, text="Espanol",fill="white")
    canvas.itemconfig(card_word,text=english_word["Spanish"],fill="white")
    canvas.itemconfig(card_background,image=back_img)



BACKGROUND_COLOR = "#B1DDC6"
window = Tk()
window.title("Flash Card")
flip_timer=window.after(3000, func=flip_card)
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

canvas = Canvas(height=526, width=800)
back_img = PhotoImage(file="images/card_back.png ")
front_img = PhotoImage(file="images/card_front.png ")

image_right = PhotoImage(file="images/right.png")
image_wrong = PhotoImage(file="images/wrong.png")

canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)

card_background=canvas.create_image(400, 263, image=front_img)
card_title = canvas.create_text(400, 150, text="Tittle.", font=("Arial", 40, "bold"))
card_word = canvas.create_text(400, 263, text="Word", font=("Arial", 60, "bold"))

canvas.grid(row=0, column=0, columnspan=2)

button_right = Button(image=image_right, highlightthickness=0, command=next_card)
button_right.grid(row=1, column=1, columnspan=4)

button_wrong = Button(image=image_wrong, highlightthickness=0, command=is_know)
button_wrong.grid(row=1, column=0, columnspan=4)

next_card()
window.mainloop()
