from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"

my_data = pandas.read_csv("data/french_words.csv")
data_dict = {row.French: row.English for (index, row) in my_data.iterrows()}
words_to_learn = {}
word = None
random_word = None



def next_card():
    global random_word, flip_timer
    random_word = random.choice(list(data_dict.keys()))
    window.after_cancel(flip_timer)
    canvas.itemconfig(background_img, image=front_img)
    canvas.itemconfig(title_text, text="French", fill="black")
    canvas.itemconfig(word, text=random_word, fill="black")

    flip_timer = window.after(3000, flip_card)


def unknown_card():
    words_to_learn[random_word] = data_dict[random_word]
    words_dict = pandas.Series(words_to_learn)
    words_dict.to_csv("data/words_to_learn.csv")
    next_card()


def flip_card():
    global random_word
    canvas.itemconfig(background_img, image=back_img)
    canvas.itemconfig(title_text, text="English", fill="white")
    canvas.itemconfig(word, text=data_dict[random_word], fill="white")

"""
def crossed():
    # when the crossed button is clicked it should delete all the elements
    # that were displayed on the front image
    canvas.delete('all')
    # then create canvas with back image displaying the english word. At this point,
    # to display the english word, simply access that variable using data_dict[random_word]
    canvas.create_image(400, 263, image=back_img)
    canvas.create_text(400, 150, text="English", font=("Ariel", 40, "italic"))
    canvas.create_text(400, 263, text=data_dict[random_word], font=("Ariel", 60, "bold"))

def checked():
    # Use random_word and french_word as global variables
    global random_word, french_word
    # First thing when checked button is click is to delete all the
    # elements of canvas
    canvas.delete("all")
    # then create canvas with front image and set another random_word
    canvas.create_image(400, 263, image=front_img)
    random_word = random.choice(list(data_dict.keys()))
    # Display title "French" and the random word
    canvas.create_text(400, 150, text="French", font=("Ariel", 40, "italic"))
    french_word = canvas.create_text(400, 263, text=random_word, font=("Ariel", 60, "bold"))
    #print(type(french_word))
    #print(data_dict[french_word])
    #canvas.grid(row=0, column=0, columnspan=2)
"""

# Create window and set title, bg, padding
window = Tk()
window.title("Flash Card")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=flip_card)
# Create canvas
canvas = Canvas(width=800, height=526, highlightthickness=0)
print("RUnning")
# create images
front_img = PhotoImage(file="images/card_front.png")
back_img = PhotoImage(file="images/card_back.png")

# create images and a French word for canvas. As default, it should display front image of
# flash card app and a random French word.
background_img = canvas.create_image(400, 263, image=front_img)
title_text = canvas.create_text(400, 150, text="French", font=("Ariel", 40, "italic"))
random_word = random.choice(list(data_dict.keys()))
word = canvas.create_text(400, 263, text=random_word, font=("Ariel", 60, "bold"))

canvas.config(bg=BACKGROUND_COLOR)
canvas.grid(row=0, column=0, columnspan=2)

# Buttons
cross_img = PhotoImage(file="images/wrong.png")
check_img = PhotoImage(file="images/right.png")
right = Button(image=check_img, highlightthickness=0, bg=BACKGROUND_COLOR, command=next_card)
wrong = Button(image=cross_img, highlightthickness=0, bg=BACKGROUND_COLOR, command=unknown_card)

right.grid(row=1, column=1)
wrong.grid(row=1, column=0)



window.mainloop()


