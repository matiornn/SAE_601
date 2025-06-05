import sqlite3
import json
import os

# Chemin vers le dossier contenant les fichiers JSON
json_folder_path = "data_collection/tournament_win"

# Fonction pour créer une connexion à la base de données SQLite
def create_connection(db_file):
    """Crée et retourne une connexion à la base de données SQLite."""
    conn = sqlite3.connect(db_file)
    return conn

# Fonction pour créer une table dans la base de données
def create_table(conn):
    """Crée une table pour stocker les données des joueurs."""
    create_table_sql = """
    CREATE TABLE IF NOT EXISTS players (
        tournament_id TEXT,
        tournament_name TEXT,
        name TEXT,
        placing INTEGER,
        points INTEGER,
        victories INTEGER,
        losses INTEGER,
        draws INTEGER,
        winrates REAL,
        deck TEXT
    );
    """
    cursor = conn.cursor()
    cursor.execute(create_table_sql)

# Fonction pour insérer des données dans la table
def insert_player_data(conn, player_data):
    """Insère les données d'un joueur dans la table."""
    insert_sql = """
    INSERT INTO players (tournament_id, tournament_name, name, placing, points, victories, losses, draws, winrates, deck)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """
    cursor = conn.cursor()
    cursor.execute(insert_sql, (
        player_data.get("tournament_id"),
        player_data.get("tournament_name"),
        player_data.get("name"),
        player_data.get("placing"),
        player_data.get("points"),
        player_data.get("victories"),
        player_data.get("losses"),
        player_data.get("draws"),
        player_data.get("winrates"),
        player_data.get("deck", "")
    ))
    conn.commit()

# Fonction principale pour lire les fichiers JSON et insérer les données dans la base de données
def main():
    db_file = "tournament_data.db"
    conn = create_connection(db_file)
    create_table(conn)

    for file_name in os.listdir(json_folder_path):
        if file_name.endswith('.json'):
            file_path = os.path.join(json_folder_path, file_name)
            try:
                with open(file_path, 'r', encoding='utf-8') as file:
                    player_data = json.load(file)
                    insert_player_data(conn, player_data)
            except Exception as e:
                print(f"Erreur lors de la lecture du fichier {file_path}: {e}")

    conn.close()

if __name__ == "__main__":
    main()
