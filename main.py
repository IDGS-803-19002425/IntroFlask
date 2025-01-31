from flask import Flask, render_template, request
 

app = Flask(__name__)

@app.route('/')
def index():
    grupo = "IDGS803"
    lista = ["Aaron","Hernan","Rocha"]
    return render_template('index.html',grupo=grupo,lista=lista)

@app.route("/operasBas")
def operas():
        return render_template('OperasBas.html')
    


@app.route("/operasBas",methods=['POST',"GET"])
def resultado():
      resultado = 0
      if request.method == 'POST':
        opcion = request.form.get('opcion')
        numero1 = int(request.form.get('numero1'))
        numero2 = int(request.form.get('numero2'))
        if opcion == "suma":
            resultado = numero1 + numero2
        if opcion == "resta":
            resultado = numero1 - numero2
        if opcion == "multiplicacion":
            resultado = numero1 * numero2
        if opcion == "division":
            resultado = numero1 / numero2        
        return render_template('OperasBas.html',resultado=resultado)
      
@app.route("/ejemplo1")
def ejemplo1():
    return render_template('ejemplo1.html')

@app.route("/ejemplo2")
def ejemplo2():
    return render_template('ejemplo2.html')


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

@app.route("/foem1")
def form1():
       return  '''
        <form>
        <label>Nombre:</label>
        <input type="text" name="nombre" placeholder="Nombre">
        </br>
        <label>Nombre:</label>
        <input type="text" name="nombre" placeholder="Nombre">
        </br>
        </form>
        '''


if __name__ == '__main__':
    app.run(debug=True,port=3000)

