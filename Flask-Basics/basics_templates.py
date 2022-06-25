from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    my_variable = "Ashish"
    letters = list(my_variable.upper())
    pup_dict = {
        "pup_name": "Sammy",
        "age": 10
    }
    return render_template(
        "basics.html", my_variable= my_variable.upper(), letters = letters,
        pup_dict = pup_dict
    )


if __name__ == "__main__":
    app.run(debug=True)