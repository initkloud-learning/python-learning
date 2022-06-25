from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    user_logged_in = True
    user_name = ["Anshu", "Ashish", "Aman"]
    return render_template(
        "ul_template.html", user_name = user_name, user_logged_in=user_logged_in
        )

if __name__ == "__main__":
    app.run(debug=True)