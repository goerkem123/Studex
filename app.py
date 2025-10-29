from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "DU KLEINER FURZ"

# --- NEUER TEIL START ---
if __name__ == "__main__":
    app.run(debug=True)
# --- NEUER TEIL ENDE ---