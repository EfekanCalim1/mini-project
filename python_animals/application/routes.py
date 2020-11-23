from application import app
import requests, random


@app.route('/', mwthods="POST", "GET")
def index(): 
    return render_template("index.html")

@app.route('/animal')
def animal():
    random_animal = random.randint(0,4)
    if random_animal == 0: