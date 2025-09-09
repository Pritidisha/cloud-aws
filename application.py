from flask import Flask, render_template_string, request, redirect

app = Flask(_name_)
tasks = []  # in-memory list

template = """
<!DOCTYPE html>
<html>
<head>
    <title>To-Do List</title>
    <style>
        body { font-family: Arial; background:#f0f8ff; text-align:center; }
        h1 { color: #2c3e50; }
        form { margin: 20px; }
        input[type=text] { padding: 8px; width: 200px; }
        button { padding: 8px 12px; }
        li { list-style:none; background:#dff9fb; margin:8px auto; padding:10px; width:250px; border-radius:8px; }
    </style>
</head>
<body>
    <h1>📝 To-Do List</h1>
    <form method="POST" action="/add">
        <input type="text" name="task" placeholder="Enter task" required>
        <button type="submit">Add</button>
    </form>
    <ul>
        {% for t in tasks %}
            <li>{{ loop.index }}. {{ t }}</li>
        {% endfor %}
    </ul>
</body>
</html>
"""

@app.route("/")
def home():
    return render_template_string(template, tasks=tasks)

@app.route("/add", methods=["POST"])
def add():
    task = request.form.get("task")
    if task:
        tasks.append(task)
    return redirect("/")

if _name_ == "_main_":
    app.run(host="0.0.0.0", port=8080, debug=True)


'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
#AS
from flask import Flask, render_template_string
import random

app = Flask(_name_)

jokes = [
    "Why don’t scientists trust atoms? Because they make up everything!",
    "Parallel lines have so much in common… it’s a shame they’ll never meet.",
    "Why did the computer go to therapy? It had too many bytes of anxiety.",
    "Why was the math book sad? Because it had too many problems.",
    "I told my computer I needed a break… now it won’t stop sending me Kit-Kats."
]

template = """
<!DOCTYPE html>
<html>
<head>
    <title>Random Joke Generator</title>
    <style>
        body { font-family: 'Comic Sans MS'; background:#ffeaa7; text-align:center; padding-top:50px; }
        h1 { color:#d63031; }
        p { font-size:20px; background:#fab1a0; display:inline-block; padding:20px; border-radius:10px; }
        a { display:block; margin-top:20px; color:#2d3436; text-decoration:none; font-weight:bold; }
    </style>
</head>
<body>
    <h1>😂 Random Joke Generator</h1>
    <p>{{ joke }}</p>
    <a href="/">Get another joke</a>
</body>
</html>
"""

@app.route("/")
def home():
    return render_template_string(template, joke=random.choice(jokes))

if _name_ == "_main_":
    app.run(host="0.0.0.0", port=9090, debug=True)
