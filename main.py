from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "Hola mundo nuevo Flask"

@app.route("/Hola")
def hola():
        return "hola"

@app.route("/user/<string:user>")
def user(user):
        return f"hola {user}"

@app.route("/numero/<int:n>")
def numero(n):
        return "Numero es {}".format(n)

@app.route("/user/<string:user>/<int:id>")
def username(user,id):
        return f"Nombre: {user} y id: {id}"

@app.route("/suma/<float:n1>/<float:n2>")
def suma(n1,n2):
        return "La suma es {}".format(n1+n2)

@app.route("/default")
@app.route("/default/<string:nom>")
def func(nom="Aaron"):             
       return "El nombre es: {}".format(nom)

if __name__ == '__main__':
    app.run(debug=True,port=3000)


