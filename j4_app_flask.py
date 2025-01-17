# app.py https://realpython.com/primer-on-jinja-templating/

from flask import Flask, render_template

app = Flask(__name__)
max_score = 100
test_name = "Python Challenge"
students = [
    {"name": "Sandrine",  "score": 100},
    {"name": "Gergeley", "score": 87},
    {"name": "Frieda", "score": 92},
    {"name": "Fritz", "score": 40},
    {"name": "Sirius", "score": 75},
]


@app.route("/")
def home():
    return render_template("base.html", title="Jinja and Flask")

@app.route("/a")
def a():
    return "Hello a, World!"
    # return render_template("base.html", title="Jinja and Flask")

@app.route("/results")
def results():
        context = {
            "title": "Results",
            "students": students,
            "test_name": test_name,
            "max_score": max_score,
        }
        return render_template("results.html", **context)
    
if __name__ == "__main__":
    app.run(debug=True)
    
