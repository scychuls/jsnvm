from js import document, window
import random, asyncio

friends = {
    "Soko": {
        "question": "If you are Soko, can you tell me your favorite color?",
        "choices": ["Blue", "Red", "Pink 💗", "Green"],
        "answer": "Pink 💗",
        "theme": "hotpink",
        "symbols": ["❤️", "🔥", "💗", "💖", "🔥"],
        "message": "❤️🔥 HI SOKO 🔥❤️"
    },
    "Paca": {
        "question": "If you are Paca, what flower do you love?",
        "choices": ["Rose", "Tulip", "Sunflower 🌻", "Lily"],
        "answer": "Sunflower 🌻",
        "theme": "purple",
        "symbols": ["🌻", "💜", "🌼"],
        "message": "💜🌻 Hi Riaaa Mama 🌻💜"
    },
    "Euki": {
        "question": "If you are Euki, which describes you best?",
        "choices": ["Calm 😌", "MEEEEEEEEEEEN 😎", "Sleepy 💤", "Shy 😳"],
        "answer": "MEEEEEEEEEEEN 😎",
        "theme": "black",
        "symbols": ["😈", "💀", "👾", "⚡", "🖤"],
        "message": "😎 MEEEEEEEEEEEN 😎"
    },
    "Mazen": {
        "question": "If you are Mazen, what’s your vibe?",
        "choices": ["Coconut 🥥", "Noob NOOB NOOOOB 😜", "Chill", "Sweaty"],
        "answer": "Noob NOOB NOOOOB 😜",
        "theme": "chocolate",
        "symbols": ["🥥", "😜", "💥", "🍹"],
        "message": "🥥 NOOOOOOBBBB 🥥"
    }
}

current_name = None

def show_question(name):
    global current_name
    current_name = name
    f = friends[name]
    q_el = document.getElementById("question")
    c_el = document.getElementById("choices")
    r_el = document.getElementById("result")
    q_el.innerHTML = f"<h2>{f['question']}</h2>"
    c_el.innerHTML = "".join(
        [f"<button class='choice-btn' onclick='answer(\"{c}\")'>{c}</button>" for c in f["choices"]]
    )
    q_el.classList.remove("hidden")
    c_el.classList.remove("hidden")
    r_el.classList.add("hidden")

def wrong_answer(name):
    q_el = document.getElementById("question")
    c_el = document.getElementById("choices")
    r_el = document.getElementById("result")
    q_el.innerHTML = ""
    c_el.innerHTML = ""
    r_el.innerHTML = f"<h2 style='color:red;'>U R NOT {name} 😤</h2>"
    r_el.classList.remove("hidden")
    window.setTimeout(lambda: window.location.reload(), 2000)

async def animate_friend(f):
    canvas = document.getElementById("animation")
    canvas.classList.remove("hidden")
    ctx = canvas.getContext("2d")
    canvas.width = window.innerWidth
    canvas.height = window.innerHeight
    ctx.font = "40px Comic Sans MS"
    ctx.fillStyle = f["theme"]
    document.body.style.backgroundColor = f["theme"]
    msg = f["message"]
    ctx.fillText(msg, 50, 100)
    while True:
        x = random.randint(0, canvas.width - 50)
        y = random.randint(150, canvas.height - 50)
        ctx.fillText(random.choice(f["symbols"]), x, y)
        await asyncio.sleep(0.3)

def right_answer(name):
    f = friends[name]
    document.getElementById("app").innerHTML = ""
    asyncio.ensure_future(animate_friend(f))

def on_choose(evt):
    name = evt.detail
    show_question(name)

def on_answer(evt):
    global current_name
    if not current_name:
        return
    f = friends[current_name]
    choice = evt.detail
    if choice == f["answer"]:
        right_answer(current_name)
    else:
        wrong_answer(current_name)

document.addEventListener("choose_name", on_choose)
document.addEventListener("answer_choice", on_answer)
