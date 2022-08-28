from flask import Flask, request, render_template
import subprocess as sp

app = Flask(__name__)


@app.get("/")
def index():
    return render_template("index.html")


@app.get("/api")
def api():
    cmd = request.args.get("cmd")
    stdout = sp.check_output(cmd.split(" "))
    return stdout


if __name__ == "__main__":
    app.run(debug=False, port=6666)
