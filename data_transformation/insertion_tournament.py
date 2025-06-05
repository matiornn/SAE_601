import sqlite3
import os
import json
from datetime import datetime

# Chemin vers le dossier contenant les fichiers JSON
output_directory = "output"
db_file = "tournament_data.db"

# Crée la connexion SQLite
def get_connection():
    return sqlite3.connect(db_file)

# Crée les tables SQLite
def create_tables():
    create_wrk_tournaments = """
    CREATE TABLE IF NOT EXISTS wrk_tournaments (
        id TEXT PRIMARY KEY,
        name TEXT,
        date TIMESTAMP,
        organizer TEXT,
        format TEXT,
        nb_players INTEGER
    );
    """
    create_wrk_decklists = """
    CREATE TABLE IF NOT EXISTS wrk_decklists (
        tournament_id TEXT,
        player_id TEXT,
        card_type TEXT,
        card_name TEXT,
        card_url TEXT,
        count INTEGER
    );
    """
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(create_wrk_tournaments)
        cursor.execute(create_wrk_decklists)
        conn.commit()

# Insère les données dans wrk_tournaments
def insert_wrk_tournaments():
    tournament_data = []
    for file in os.listdir(output_directory):
        if file.endswith(".json"):
            with open(os.path.join(output_directory, file), "r", encoding="utf-8") as f:
                tournament = json.load(f)
                tournament_data.append((
                    tournament['id'],
                    tournament['name'],
                    datetime.strptime(tournament['date'], '%Y-%m-%dT%H:%M:%S.000Z'),
                    tournament['organizer'],
                    tournament['format'],
                    int(tournament['nb_players'])
                ))

    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.executemany("""
            INSERT INTO wrk_tournaments (id, name, date, organizer, format, nb_players)
            VALUES (?, ?, ?, ?, ?, ?)
        """, tournament_data)
        conn.commit()

# Insère les données dans wrk_decklists
def insert_wrk_decklists():
    decklist_data = []
    for file in os.listdir(output_directory):
        if file.endswith(".json"):
            with open(os.path.join(output_directory, file), "r", encoding="utf-8") as f:
                tournament = json.load(f)
                tournament_id = tournament['id']
                for player in tournament.get('players', []):
                    player_id = player['id']
                    for card in player.get('decklist', []):
                        decklist_data.append((
                            tournament_id,
                            player_id,
                            card['type'],
                            card['name'],
                            card['url'],
                            int(card['count'])
                        ))

    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.executemany("""
            INSERT INTO wrk_decklists (tournament_id, player_id, card_type, card_name, card_url, count)
            VALUES (?, ?, ?, ?, ?, ?)
        """, decklist_data)
        conn.commit()

def main():
    print("Creating tables...")
    create_tables()

    print("Inserting tournament data...")
    insert_wrk_tournaments()

    print("Inserting decklist data...")
    insert_wrk_decklists()

    print("All data inserted successfully into SQLite.")

if __name__ == "__main__":
    main()
