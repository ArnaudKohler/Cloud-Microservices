from flask import Flask, request, jsonify
import mysql.connector
import datetime
import os

# Configuration de Flask et de la base de données
app = Flask(__name__)

# Connexion à MariaDB avec hôte dynamique via une variable d'environnement
def get_db_connection():
    db_host = os.getenv('DB_HOST', 'localhost')  # Récupère l'hôte de la DB, 'localhost' par défaut
    connection = mysql.connector.connect(
        host=db_host,        # Utilise l'hôte récupéré à partir de l'environnement
        user="admin",         # Remplace par ton utilisateur MariaDB
        password="password", # Remplace par ton mot de passe MariaDB
        database="Logs"  # Nom de la base de données
    )
    return connection

# Route GET pour récupérer tous les logs
@app.route('/data', methods=['GET'])
def get_logs():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM LogTable")
    logs = cursor.fetchall()
    cursor.close()
    conn.close()
    return jsonify(logs), 200

# Route POST pour ajouter un log
@app.route('/update', methods=['POST'])
def add_log():
    try:
        # Récupérer les données envoyées dans le body
        data = request.get_json()

        # Vérifier que le JSON contient un "result"
        if 'result' not in data:
            return jsonify({"error": "Missing 'result' in the request"}), 400

        result = data['result']

        # Récupérer la date actuelle au format souhaité
        current_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        # Enregistrer dans la base de données avec le calcul et l'heure actuelle
        conn = get_db_connection()
        cursor = conn.cursor()

        cursor.execute(
            "INSERT INTO LogTable (time, calculus) VALUES (%s, %s)",
            (current_time, result)  # On enregistre le calcul tel quel
        )
        conn.commit()

        cursor.close()
        conn.close()

        return jsonify({"message": "Log successfully added", "time": current_time, "calculus": result}), 201

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
