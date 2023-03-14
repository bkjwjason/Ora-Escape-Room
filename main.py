import tkinter as tk
import pygame
import threading
import time

# Create the main window
root = tk.Tk()
root.geometry("1920x1080")
root.title("Pokemon Menu")



pygame.mixer.init()
pygame.mixer.music.load("pallet2.wav")
pygame.mixer.music.play(-1)

counter = 0

# Set the background image (you will need to have an image named "background.gif" saved on your computer)
background_image = tk.PhotoImage(file="dex.png")
background_label = tk.Label(root, image=background_image)
background_label.place(relwidth=1, relheight=1)

legendary_sound = pygame.mixer.Sound("groudon.wav")

def play_legendary():
    while True:
        time.sleep(120)
        legendary_sound.play()
legendary_sound_thread = threading.Thread(target = play_legendary)
legendary_sound_thread.daemon = True
legendary_sound_thread.start()

def submit_name():
    global counter
    correct_answer = "YUKINARI"
    answer = answer_entry.get().upper()
    if answer == correct_answer:
        next_menu()
    elif answer == "":
        answer_entry.delete(0, tk.END)
    else:
        if (counter + 1 == 3):
            game_over()
        else:
            counter += 1
            wrong_answer_label.config(text="Login Failed! \n" + " You used " + str(counter) + " / 3 attempts. \n \n Hint: My first name.")
            answer_entry.delete(0, tk.END)

def game_over():
    for child in root.winfo_children():
        if (not child == background_label):
            child.destroy()
    pygame.mixer.music.stop()
    pygame.mixer.music.load("explode.wav")
    pygame.mixer.music.play(1)
    pygame.time.delay(5000)
    pygame.mixer.music.load("gameover.wav")
    pygame.mixer.music.queue("verdanturf.wav")
    pygame.mixer.music.play(1)
    label = tk.Label(root, text="PokeComputer Exploded.. \n Thanks for Playing!", bg="red", fg="black", font = ("Arial", 30))
    label.place(relx=0.5, rely=0.5, anchor="center")

def task_1(self):
    for child in root.winfo_children():
        if (not child == background_label):
            child.destroy()
    label = tk.Label(root, text="Task 1", bg="#c9f1f9", fg="black", font = ("Arial", 18))
    label.place(relx=0.5, rely =0.3, anchor="center")
    text_widget = tk.Text(root, height = 30, width = 40, bg="#c9f1f9", fg="black", font = ("Arial", 14), wrap='word')
    text_widget.place(relx = 0.5, rely = 0.5, anchor="center")
    text = """Dear Diary,

Today was an exciting day as I embarked on a mission to catch a particularly elusive Pikachu. This little electric-type Pokémon has been giving me quite the run-around lately, and I'm determined to add it to my collection. I heard the reason why it's so special is because of a certain marking on it.

I've been studying its movements and behavior for weeks now, and I believe I may have finally found a clue that could lead me to it. Word on the street is that this Pikachu is more active at night, and I think I might have a better chance of spotting it in the dark.

So tonight, I plan on venturing out into the forest, armed with my trusty Pokéballs and flashlight, in hopes of finally catching this sneaky little Pokémon. I'm eager to put my skills to the test and see if I have what it takes to capture such an elusive creature.

I know it won't be easy, but I'm confident that with a little patience and perseverance, I'll be able to add this Pikachu to my collection in no time and find out why it's so special. Wish me luck!

Until tomorrow,
Professor Oak"""
    text_widget.insert(tk.END, text)
    backbutton = tk.Button(root, text="Back to Main Menu", command=next_menu, highlightbackground="#97d7e3", fg="black", font = ("Arial", 12))
    backbutton.place(relx=0.5, rely=0.85, anchor="s")


def task_2(self):
    for child in root.winfo_children():
        if (not child == background_label):
            child.destroy()
    label = tk.Label(root, text="Task 2", bg="#c9f1f9", fg="black", font = ("Arial", 18))
    label.place(relx=0.5, rely =0.3, anchor="center")
    text_widget = tk.Text(root, height = 25, width = 50, bg="#c9f1f9", fg="black", font = ("Arial", 14), wrap='word')
    text_widget.place(relx = 0.5, rely = 0.5, anchor="center")
    # q1:37, q2:3, q3:6, q4: 1341, q5:6713
    text = """ 
I have been busy trying to come up with a plan to keep Team Rocket from discovering the password to my computer. 
After much deliberation, I have come up with a plan that involves some math teasers. Hopefully, they will be too difficult for Team Rocket to solve.

Find the hidden rule based on the examples and solve for the answer!
The answer to this task is A + B + C + D + E


    Q1: 22 😂 7 = A (34 😂 4 = 64, 57 😂 3 = 111) 
    
    Q2: 4 😊 19 = B (51 😊 5 = 1, 1 😊 51 = 0)

    Q3: 11 😉 7 = C (1 😉 4 = 5, 10 😉 5 = 3)

    Q4: 11 🧐 14 = D (79 🧐 972 = 729221, 
                                  8976 🧐 8933 = 8292716132)
                                
    Q5: Monday = 617, Tuesday = 729, Wednesday = 9312, 
           Thursday = 8412, Friday = 6511, Saturday = 8614, 
           Sunday = E)

    If you're stuck, search the surroundings. I've hidden some hints for you.
    """
    text_widget.insert(tk.END, text)
    backbutton = tk.Button(root, text="Back to Main Menu", command=next_menu, highlightbackground="#97d7e3", fg="black", font = ("Arial", 12))
    backbutton.place(relx=0.5, rely=0.85, anchor="s")

def task_3(self):
    for child in root.winfo_children():
        if (not child == background_label):
            child.destroy()
    text_widget = tk.Text(root, height = 10, width = 50,bg = "#c9f1f9", fg="black", font = ("Arial", 14), wrap='word')
    text_widget.place(relx = 0.5, rely = 0.4, anchor="center")
    text = """
Dear Diary,

Today I spent my morning in my lab, organizing data on Hoenn region's Pokémon. Suddenly, I heard a peculiar cry that I have never heard before. It sounded like a Hoenn trio's cry but I couldn't quite place it.

I immediately put down my work and started to analyze the sound. It was unlike any Pokémon cry I have ever heard before. It was high-pitched and had a unique tone to it.

As I listened to the cry on repeat, I started to identify certain features in the sound that reminded me of the Hoenn trio. I am certain that this cry belongs to one of them."""
    text_widget.insert(tk.END, text)
    rayquaza_img = tk.PhotoImage(file = "rayquaza.png")
    groudon_img = tk.PhotoImage(file = "groudon.png")
    kyogre_img = tk.PhotoImage(file = "kyogre.png")
    r_top = tk.Label(root, bg= "#c4f0f8", fg = "black", text="Rayquaza")
    r_top.place(relx = 0.4, rely = 0.52, anchor='center')
    r_label = tk.Label(root, image=rayquaza_img)
    r_label.place(relx = 0.4, rely = 0.6, anchor='center')
    r_label.image = rayquaza_img
    r_button = tk.Button(root, text="Sound",highlightbackground="#c4f0f8", command = r_sound)
    r_button.place(relx=0.4, rely = 0.7, anchor = 'center')
    g_top = tk.Label(root, bg= "#c4f0f8", fg = "black", text="Groudon")
    g_top.place(relx = 0.5, rely = 0.52, anchor='center')
    g_label = tk.Label(root, image = groudon_img)
    g_label.image = groudon_img
    g_label.place(relx=0.5, rely = 0.6, anchor='center')
    g_button = tk.Button(root, text="Sound",highlightbackground="#c4f0f8", command = g_sound)
    g_button.place(relx=0.5, rely = 0.7, anchor = 'center')
    k_top = tk.Label(root, bg= "#c4f0f8", fg = "black", text="Kyogre")
    k_top.place(relx = 0.6, rely = 0.52, anchor='center')
    k_label = tk.Label(root, image=kyogre_img)
    k_label.place(relx=0.6, rely = 0.6, anchor='center')
    k_label.image = kyogre_img
    k_button = tk.Button(root, text="Sound",highlightbackground="#c4f0f8", command = k_sound)
    k_button.place(relx=0.6, rely = 0.7, anchor = 'center')
    backbutton = tk.Button(root, text="Back to Main Menu", command=next_menu, highlightbackground="#97d7e3", fg="black", font = ("Arial", 12))
    backbutton.place(relx=0.5, rely=0.85, anchor="s")

def g_sound():
    button_sound = pygame.mixer.Sound("groudon.wav")
    button_sound.play()

def r_sound():
    button_sound = pygame.mixer.Sound("rayquaza.wav")
    button_sound.play()

def k_sound():
    button_sound = pygame.mixer.Sound("kyogre.wav")
    button_sound.play()

def task_4(self):
    text_widget = tk.Text(root, height = 25, width = 50, bg="#c9f1f9", fg="black", font = ("Arial", 14), wrap='word')
    text_widget.place(relx = 0.5, rely = 0.5, anchor="center")
    text = """
Dear Diary,

Today was a challenging day in the lab. I was attacked by several types of Pokemon, and it was quite difficult to identify what type they were. However, I did notice some interesting characteristics that might help me narrow it down.

Firstly, the Pokemon that attacked me were all not very affected by Grass-type moves. Bug-type moves were not effective as well.

On the other hand, they were weak to Fire-type moves and took extra damage from Fighting-type moves. 

I am still not entirely sure what type of Pokemon I was attacked by, but with these clues, I am confident that we will be able to narrow it down. I will continue to analyze the data and hopefully, we can identify the type soon.

Best regards,
Professor Oak
    """
    text_widget.insert(tk.END, text)
    backbutton = tk.Button(root, text="Back to Main Menu", command=next_menu, highlightbackground="#97d7e3", fg="black", font = ("Arial", 12))
    backbutton.place(relx=0.5, rely=0.85, anchor="s")

def get_passcode(self):
    for child in root.winfo_children():
        if (not child == background_label):
            child.destroy()
    question_label = tk.Label(root, text="Enter the Passcode \n Hint: Answer for Task1 + \n Answer for Task 2 + \n First Letter of Answer for Task 3 + \n First Letter of Answer for Task 4", bg="#c4f0f8", fg = "black", font = ("Arial", 18))
    question_label.place(relx = 0.5, rely = 0.4, anchor="center")

    global answer_entry
    answer_entry = tk.Entry(root, width= 30, bg = "white", fg = "black")
    answer_entry.place(relx = 0.5, rely = 0.5, anchor="center")

    submit_button = tk.Button(root, text = "Play the flute!", command=passcode, bg = "white", fg = "Black", font = ("Arial", 16))
    submit_button.place(relx = 0.5, rely= 0.6, anchor = "center")
    global wrong_answer_label
    wrong_answer_label = tk.Label(root, text = "", bg = "#c4f0f8", fg = "Red", font = ("Arial", 16))
    wrong_answer_label.place(relx=0.5, rely=0.7, anchor="center")
    backbutton = tk.Button(root, text="Back to Main Menu", command=next_menu, highlightbackground="#97d7e3", fg="black", font = ("Arial", 12))
    backbutton.place(relx=0.5, rely=0.85, anchor="s")
        
def passcode():
    global answer_entry
    global counter
    correct_answer = "STAR8100GS"
    answer = answer_entry.get().upper()
    if answer == correct_answer:
        end_menu()
    elif answer == "":
        answer_entry.delete(0, tk.END)
    else:
        if (counter + 1 == 3):
            game_over()
        else:
            counter += 1
            global wrong_answer_label
            wrong_answer_label.config(text="Login Failed! \n" + " You used " + str(counter) + " / 3 attempts.")
            answer_entry.delete(0, tk.END)

def end_menu():
    for child in root.winfo_children():
        if (not child == background_label):
            child.destroy()
    pygame.mixer.music.load("flute.wav")
    pygame.mixer.music.queue("verdanturf.wav")
    pygame.mixer.music.play()
    pygame.time.delay(6500)
    end_time = time.time()
    global start_time
    elapsed = end_time - start_time
    time_str = format_time(elapsed)
    snorlax_img = tk.PhotoImage(file = "snorlax.png")
    s_label = tk.Label(root, image=snorlax_img)
    s_label.place(relx = 0.5, rely = 0.4, anchor='center')
    s_label.image = snorlax_img
    question_label = tk.Label(root, text="Snorlax Has Awakened! \n Thanks for playing! \n Your team took " + time_str, bg="#c4f0f8", fg = "black", font = ("Arial", 18))
    question_label.place(relx = 0.5, rely = 0.7, anchor="center")

def format_time(seconds):
    minutes = int(seconds // 60)
    seconds = int(seconds % 60)
    return f"{minutes:02d} minutes and {seconds:02d} seconds."

def next_menu():
    for child in root.winfo_children():
        if (not child == background_label):
            child.destroy()
    label = tk.Label(root, text="Tasks", bg="#c9f1f9", fg="black", font = ("Arial", 18))
    label.place(relx=0.5, rely =0.3, anchor="center")

    # Create four buttons
    button1 = tk.Button(root, text="Task 1", bg="#c4f0f8", fg="black", font = ("Arial", 16))
    button1.bind("<Button-1>", task_1)
    button1.place(relx=0.5, rely=0.4, anchor="center")

    button2 = tk.Button(root, text="Task 2", bg="#c4f0f8", fg="black", font = ("Arial", 16))
    button2.bind("<Button-1>", task_2)
    button2.place(relx=0.5, rely=0.45, anchor="center")

    button3 = tk.Button(root, text="Task 3", bg="#c4f0f8", fg="black", font = ("Arial", 16))
    button3.bind("<Button-1>", task_3)
    button3.place(relx=0.5, rely=0.5, anchor="center")

    button4 = tk.Button(root, text="Task 4", bg="#c4f0f8", fg="black", font = ("Arial", 16))
    button4.bind("<Button-1>", task_4)
    button4.place(relx=0.5, rely=0.55, anchor="center")

    button5 = tk.Button(root, text="Passcode for the FLUTE", bg="#c4f0f8", fg="black", font = ("Arial", 16))
    button5.bind("<Button-1>", get_passcode)
    button5.place(relx=0.5, rely=0.7, anchor="center")




question_label = tk.Label(root, text="Login", bg="#c4f0f8", fg = "black", font = ("Arial", 18))
question_label.place(relx = 0.5, rely = 0.4, anchor="center")


answer_entry = tk.Entry(root, width= 30, bg = "white", fg = "black")
answer_entry.place(relx = 0.5, rely = 0.5, anchor="center")

submit_button = tk.Button(root, text = "Submit", command=submit_name, bg = "white", fg = "Black", font = ("Arial", 16))
submit_button.place(relx = 0.5, rely= 0.6, anchor = "center")

wrong_answer_label = tk.Label(root, text = "", bg = "#c4f0f8", fg = "Red", font = ("Arial", 16))
wrong_answer_label.place(relx=0.5, rely=0.7, anchor="center")
start_time = time.time()
# Start the main loop
root.mainloop()
