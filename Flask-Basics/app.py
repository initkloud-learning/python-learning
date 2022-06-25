from flask import Flask

app = Flask(__name__)


@app.route("/")  # 127.0.0.1:5000
def index():
    return "<h1>Hello Buddy!!</h1>"


@app.route("/information")
def info():
    return """<h1>Buddy! you are Awesome....</h1>
    <p>Hey! This is Ashish Panwar from Dehradun, Please call when available.</p>
    """


@app.route("/users/<name>")
def user_info(name):
    return "<h1>This page belongs to User: {}</h1>".format(name.upper())

@app.route("/puppy/<name>")
def puppy_name_validation(name):
    latin_name = name
    if latin_name[len(latin_name) - 1] != 'y':
        latin_name += 'y'
    elif latin_name[len(latin_name) - 1] == 'y':
        latin_name = latin_name[:len(latin_name) - 1] + "iful"
    
    return "<h1>Hi {} your Puppy Latin name is {}</h1>".format(name, latin_name)


if __name__ == "__main__":
    app.run(debug=True)
