from flask import Flask  # import Flask

app: Flask = Flask(__name__)  # application load


@app.route("/")
def saludar():
    return "¡Hola Mundo!"


# when the main is run the line 'app.run()' will be run
if __name__ == "__main__":
    app.run()  # app.run() runs Flaks to know that it is in constant execution

# no method is being run but 'app = Flask(__name__)' that was already instanced (Flask), the application 'app' that we
# have, the Flask object 'app' will be left running and the app will be waiting for someone to ask him for a page.
# In this case there is only one page which is the root: '@app.route("/")'

# when someone asks for this root "/" the root '@app.route("/")' will be routed to the code 'def saludar():' and the
# string "¡Hola Mundo!" will be returned
