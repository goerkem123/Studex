from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "Görkem ist der Beste!"

# --- NEUER TEIL START ---
if __name__ == "__main__":
    app.run(debug=True)
# --- NEUER TEIL ENDE ---