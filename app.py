# To run, use: $ flask --app app run
# First cd /home/utilisateur/Projects/flask
# https://www.digitalocean.com/community/tutorials/processing-incoming-request-data-in-flask


from flask import Flask, request, render_template
from computation_module import compute_text

app = Flask(__name__)
# voir demarche dans stack overflow au lien : https://stackoverflow.com/questions/12277933/send-data-from-a-textbox-into-flask
@app.route('/') #by default, calls get
def my_form(): #renvoie le formulaire qui est dans 'my_form.html'
    return render_template('my-form.html')

@app.route('/', methods=['POST'])
def my_form_post():
    text = request.form['text']
    processed_text = text.upper()
    return processed_text
#@app.route("/")
#def hello_world():
#    return "<p>Hello, World!</p>"

@app.get("/who_is_the_cutest_dog")
def beauty():
    return "The cutest dog is of course Ice !"

@app.route("/add/<int:a>/<int:b>")
def addition(a, b):
    return f"The sum of {a} and {b} is {a+b}"

@app.route("/machine_learning/<name>")
def algorithm(name):
    # Do some machine learning stuff here
    return f"Based on some complex machine learning algorithm, your name is {name} !"

@app.post("/multiply")
def this_name_method_doesnt_matter_here():
    data = request.get_json()
    return f"The multiplication of {data['key1']} and {data['key2']} is {data['key1']*data['key2']}"

@app.post("/calculate")
def compute_this():
    data = request.get_json()
    return compute_text(data["question"])
    