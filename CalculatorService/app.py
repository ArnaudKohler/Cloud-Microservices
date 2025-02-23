from flask import Flask, request, jsonify
import requests
import logging
import sys

app = Flask(__name__)

# 🔥 Configuration du logger pour voir les logs dans Minikube
logging.basicConfig(
    level=logging.INFO,  # Niveau d'affichage
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[logging.StreamHandler(sys.stdout)],  # Envoi les logs vers la sortie standard (stdout)
)

logger = logging.getLogger(__name__)  # Récupérer un logger

def log_result(result):
    logger_url = "http://logger-service/update"
    data = {"result": result}
    try:
        response = requests.post(logger_url, json=data, timeout=5)
        if response.status_code != 200:
            logger.error(f"❌ Erreur lors de l'envoi du log: {response.status_code}, {response.text}")
        else:
            logger.info(f"✅ Log envoyé : {data}")
    except requests.exceptions.RequestException as e:
        logger.exception("❌ Impossible de se connecter au logger-service")

def validate_values(request):
    try:
        val1 = float(request.args.get("val1"))
        val2 = float(request.args.get("val2"))
        return val1, val2
    except (ValueError, TypeError):
        logger.error("❌ Valeurs invalides reçues")
        return None

def calculate(operation):
    values = validate_values(request)
    if values is None:
        return jsonify({"error": "Both values must be numbers"}), 400

    val1, val2 = values

    if operation == "add":
        result = val1 + val2
        symbol = "+"
    elif operation == "subtract":
        result = val1 - val2
        symbol = "-"
    elif operation == "multiply":
        result = val1 * val2
        symbol = "*"
    elif operation == "divide":
        if val2 == 0:
            logger.warning("❌ Division par zéro tentée")
            return jsonify({"error": "Cannot divide by 0!"}), 400
        result = val1 / val2
        symbol = "/"
    else:
        return jsonify({"error": "Invalid operation"}), 400

    result_str = "{:.2f} {} {:.2f} = {:.2f}".format(val1, symbol, val2, result)
    
    # Log et envoyer le résultat au logger-service
    logger.info(f"📝 Calcul effectué : {result_str}")
    log_result(result_str)

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
    logger.info("🚀 Démarrage du service Flask...")
    app.run(host="0.0.0.0", port=8085, debug=True, use_reloader=False)  # Désactiver le reloader Flask
