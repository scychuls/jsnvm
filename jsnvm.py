import tkinter as tk
import random
import time

# --- Friend Data ---
friends = {
    "Soko": {
        "question": "If you are Soko, can you tell me your favorite color?",
        "choices": ["Blue", "Red", "Pink 💗", "Green"],
        "answer": "Pink 💗",
        "animation": "soko_animation"
    },
    "Paca": {
        "question": "If you are Paca, what flower do you love?",
        "choices": ["Rose", "Tulip", "Sunflower 🌻", "Lily"],
        "answer": "Sunflower 🌻",
        "animation": "paca_animation"
    },
    "Euki": {
        "question": "If you are Euki, which describes you best?",
        "choices": ["Calm 😌", "MEEEEEEEEEEEN 😎", "Sleepy 💤", "Shy 😳"],
        "answer": "MEEEEEEEEEEEN 😎",
        "animation": "euki_animation"
    },
    "Mazen": {
        "question": "If you are Mazen, what’s your vibe?",
        "choices": ["Coconut 🥥", "Noob NOOB NOOOOB 😜", "Chill", "Sweaty"],
        "answer": "Noob NOOB NOOOOB 😜",
        "animation": "mazen_animation"
    },
}

# --- Tkinter Setup ---
root = tk.Tk()
root.title("jsnvm")
root.geometry("600x400")
root.config(bg="black")

label = tk.Label(root, text="Hellloooo 👋\nMay I know who you are?", 
                 font=("Comic Sans MS", 18, "bold"), bg="black", fg="white")
label.pack(pady=40)

button_frame = tk.Frame(root, bg="black")
button_frame.pack()

# --- Functions ---
def reset_to_start():
    for widget in root.winfo_children():
        widget.destroy()
    label = tk.Label(root, text="Hellloooo 👋\nMay I know who you are?", 
                     font=("Comic Sans MS", 18, "bold"), bg="black", fg="white")
    label.pack(pady=40)
    frame = tk.Frame(root, bg="black")
    frame.pack()
    for name in friends.keys():
        tk.Button(frame, text=name, font=("Comic Sans MS", 14, "bold"),
                  bg="purple", fg="white", width=12, 
                  command=lambda n=name: ask_question(n)).pack(pady=5)

def ask_question(name):
    for widget in root.winfo_children():
        widget.destroy()
    f = friends[name]
    q_label = tk.Label(root, text=f["question"], font=("Comic Sans MS", 14), bg="black", fg="white")
    q_label.pack(pady=40)
    frame = tk.Frame(root, bg="black")
    frame.pack()
    for choice in f["choices"]:
        tk.Button(frame, text=choice, font=("Comic Sans MS", 12),
                  bg="gray20", fg="white", width=25,
                  command=lambda c=choice, n=name: check_answer(n, c)).pack(pady=5)

def check_answer(name, choice):
    f = friends[name]
    if choice == f["answer"]:
        # Correct → Show animation
        globals()[f["animation"]]()
    else:
        for widget in root.winfo_children():
            widget.destroy()
        wrong = tk.Label(root, text=f"U R NOT {name} 😤", font=("Comic Sans MS", 20, "bold"),
                         bg="black", fg="red")
        wrong.pack(pady=50)
        root.after(2000, reset_to_start)

# --- Animations ---

def soko_animation():
    clear_screen("hot pink")
    msg = tk.Label(root, text="❤️🔥 HI SOKO 🔥❤️", font=("Comic Sans MS", 30, "bold"),
                   bg="hot pink", fg="white")
    msg.pack(pady=120)
    animate_hearts(["❤️", "🔥", "💗", "💖", "🔥"])

def paca_animation():
    clear_screen("purple")
    msg = tk.Label(root, text="💜🌻 Hi Riaaa Mama 🌻💜", font=("Comic Sans MS", 28, "bold"),
                   bg="purple", fg="yellow")
    msg.pack(pady=120)
    animate_falling(["🌻", "💜", "🌼"])

def euki_animation():
    clear_screen("black")
    msg = tk.Label(root, text="😎 MEEEEEEEEEEEN 😎", font=("Comic Sans MS", 30, "bold"),
                   bg="black", fg="white")
    msg.pack(pady=120)
    animate_falling(["😈", "💀", "👾", "⚡", "🖤"])

def mazen_animation():
    clear_screen("chocolate")
    msg = tk.Label(root, text="🥥 NOOOOOOBBBB 🥥", font=("Comic Sans MS", 30, "bold"),
                   bg="chocolate", fg="white")
    msg.pack(pady=120)
    animate_hearts(["🥥", "😜", "💥", "🍹"])

def clear_screen(color):
    for widget in root.winfo_children():
        widget.destroy()
    root.config(bg=color)

def animate_hearts(symbols):
    lbl = tk.Label(root, text="", font=("Comic Sans MS", 50), bg=root["bg"])
    lbl.pack()
    def update():
        lbl["text"] = random.choice(symbols)
        lbl.place(x=random.randint(50, 550), y=random.randint(50, 350))
        root.after(200, update)
    update()

def animate_falling(symbols):
    lbl = tk.Label(root, text="", font=("Comic Sans MS", 40), bg=root["bg"])
    lbl.pack()
    def fall():
        lbl["text"] = random.choice(symbols)
        lbl.place(x=random.randint(0, 550), y=random.randint(0, 350))
        root.after(300, fall)
    fall()

# --- Start Program ---
reset_to_start()
root.mainloop()
