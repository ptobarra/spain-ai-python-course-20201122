import datetime
from flask import Flask

app = Flask(__name__)


@app.route("/")
def saludar():
    return "¡Hola Mundo!"


@app.route("/adios")
def despedir():
    return "Hasta pronto, nos vemos!"


@app.route("/hora")
def dar_hora():
    return str(datetime.datetime.now())


@app.route("/ejemplo_html")
def mostrar_html():
    return """
<!DOCTYPE html>
<html>
<body>

<p id="demo">>This example calls a function which outputs "Hello World" in a p element with id="demo".</p>

<p></p>

<script>
function myFunction() {
  document.getElementById("demo").innerHTML = "Hola AHORA!";
}

myFunction();
</script>

</body>
</html>    
    """


if __name__ == "__main__":
    app.run()
