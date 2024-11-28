from flask import Flask, render_template, request, jsonify
import random

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/calculate", methods=["POST"])
def calculate_love():
    name1 = request.form["name1"]
    name2 = request.form["name2"]
    
    # Love calculation logic (random for now)
    love_percentage = random.randint(50, 100)
    
    return render_template("result.html", name1=name1, name2=name2, love_percentage=love_percentage)

@app.route("/health")
def health():
    return jsonify({"status": "server is up and running"}), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)

