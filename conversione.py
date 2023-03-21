from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/', methods = ['GET'])
def conversione():
  return render_template("conversione.html", methods = ['GET']) 

@app.route('/conversione', methods = ['GET'] )
def conversione1():
    temperatura = float(request.args.get('temp'))
    tipo = int(request.args.get('primo'))
    def trasmutazione(a):
        if tipo == 0:
            risultato = (a*1.8) + 32
        elif tipo == 1:
            risultato = (a - 32) * (5/9)
        elif tipo == 2:
          risultato = a + 273.15 
        return risultato
    return render_template("convertito.html", risut = trasmutazione(temperatura)) 


if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)

  # moltiplicare il numero di gradi centigradi per 1,8 e sommare 32 al risultato.