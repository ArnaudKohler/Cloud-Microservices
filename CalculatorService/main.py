from flask import Flask, request, jsonify

app = Flask(__name__)

def validate_values(request):
    try:
        val1 = float(request.args.get("val1"))
        val2 = float(request.args.get("val2"))
        return val1, val2
    except (ValueError, TypeError):
        return None

def calculate(operation):
    values = validate_values(request)
    if values is None:
        return jsonify({"error": "Both values must be numbers"}), 400
    
    val1, val2 = values
    
    if operation == "add":
        result = val1 + val2
        operation = "+"
    elif operation == "subtract":
        result = val1 - val2
        operation = "-"
    elif operation == "multiply":
        result = val1 * val2
        operation = "*"
    elif operation == "divide":
        if val2 == 0:
            return jsonify({"error": "Cannot divide by 0!"}), 400
        result = val1 / val2
        operation = "/"
    else:
        return jsonify({"error": "Invalid operation"}), 400
    
    result_str = "{:.2f} {} {:.2f} = {:.2f}".format(val1, operation, val2, result)
    return jsonify({"result": result_str}), 200

@app.route("/add", methods=["GET"])
def add():
    return calculate("add")

@app.route("/subtract", methods=["GET"])
def subtract():
    return calculate("subtract")

@app.route("/multiply", methods=["GET"])
def multiply():
    return calculate("multiply")

@app.route("/divide", methods=["GET"])
def divide():
    return calculate("divide")

if __name__ == '__main__':
    app.run(debug=True)
