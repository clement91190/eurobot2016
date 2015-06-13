from flask import Flask, request
import utils

app = Flask(__name__)


@app.route("/table")
def table():
    return utils.memory.to_json()


@app.route("/set_big_robot", methods=['GET', 'POST'])
def set_big_robot():
    x = request.args.get('x', 0)
    y = request.args.get('y', 1000)
    cap = request.args.get('cap', 0)
    utils.memory.big_robot = dict(x=float(x), y=float(y), cap=float(cap))
    return "{} {} {}".format(x, y, cap)

if __name__ == "__main__":
    app.run(debug=True)
