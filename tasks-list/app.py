from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Lista de Tarefas"

if __name__ == "__main__":
    app.run()