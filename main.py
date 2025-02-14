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
      if request.method == 'GET':
            return render_template('OperasBas.html')
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
      

@app.route("/Cinepolis", methods=['POST',"GET"])
def cinepolis():
        costoBoleto = 12.00        
        descuentoTarjeta = 0.10
        descuento2 = 0.10
        descuento3 = 0.15                
        if request.method == 'GET':
                return render_template('Cinepolis.html')
        if request.method == 'POST':
                nombre = request.form.get('nombre')
                compradores = int(request.form.get('Compradores'))
                tarjeta = request.form.get('tarjeta')
                boletos = int(request.form.get('boletos'))   
                limiteBoletos = compradores * 7

                if boletos > limiteBoletos:
                      mensaje = "Solo se pueden comprar 7 boletos por comprador."
                      return render_template('Cinepolis.html',mensaje=mensaje)
                if boletos == 2 or boletos == 1:                      
                      if tarjeta == "si":
                            costoBoletos = boletos * costoBoleto
                            precioDescuento = costoBoletos * descuentoTarjeta
                            precioFinal = costoBoletos - precioDescuento  
                            valor = precioFinal
                            valor = round(valor,2)
                            return render_template('Cinepolis.html',valor=valor)
                      if tarjeta == "no":
                            costoBoletos = boletos * costoBoleto
                            valor = costoBoletos
                            valor = round(valor,2)
                            return render_template('Cinepolis.html',valor=precioFinal)
                if boletos == 3 or boletos == 4 or boletos ==5:
                      precioTotalBoletos = boletos * costoBoleto
                      precioDescuento = precioTotalBoletos * descuento2
                      precioFinal = precioTotalBoletos - precioDescuento  
                      precioFinal = round(precioFinal,2)
                      if tarjeta == "si":             
                        descuentoCineco = precioFinal * descuentoTarjeta
                        valor = precioFinal - descuentoCineco          
                        valor = round(valor,2)
                        return render_template('Cinepolis.html',valor=valor)
                      if tarjeta == "no":                        
                        return render_template('Cinepolis.html',valor=precioFinal)
                if boletos > 5:
                      precioTotalBoletos = boletos * costoBoleto
                      precioDescuento = precioTotalBoletos * descuento3
                      precioFinal = precioTotalBoletos - precioDescuento
                      precioFinal = round(precioFinal,2)
                      if tarjeta == "si":
                            descuentoCineco = precioFinal * descuentoTarjeta
                            valor = precioFinal - descuentoCineco       
                            valor = round(valor,2)
                            return render_template('Cinepolis.html',valor=valor)
                      if tarjeta == "no":                           
                            return render_template('Cinepolis.html',valor=precioFinal)
                                                      
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

