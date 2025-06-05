import sqlite3
import json
import os

# Chemin vers le dossier contenant les fichiers JSON
json_folder_path = "data_collection/cartes_pokemon"

# Fonction pour créer une connexion à la base de données SQLite
def create_connection(db_file):
    """Crée et retourne une connexion à la base de données SQLite."""
    conn = sqlite3.connect(db_file)
    return conn

# Fonction pour créer les tables dans la base de données
def create_tables(conn):
    """Crée les tables pour stocker les données des cartes."""
    create_trainer_table_sql = """
    CREATE TABLE IF NOT EXISTS trainer_cards (
        url_source TEXT,
        categorie_carte TEXT,
        name TEXT,
        image_url TEXT,
        set_number_id TEXT,
        card_number INTEGER,
        artist TEXT
    );
    """

    create_pokemon_table_sql = """
    CREATE TABLE IF NOT EXISTS pokemon_cards (
        url_source TEXT,
        categorie_carte TEXT,
        name TEXT,
        image_url TEXT,
        set_number_id TEXT,
        card_number INTEGER,
        artist TEXT,
        Stage_devolution TEXT,
        Pre_evolution TEXT,
        type TEXT,
        hp INTEGER,
        faiblesse TEXT,
        retrait INTEGER,
        Nom_attaque_1 TEXT,
        Cout_attaque_1 TEXT,
        Degat_attaque_1 INTEGER,
        Nom_attaque_2 TEXT,
        Cout_attaque_2 TEXT,
        Degat_attaque_2 TEXT
    );
    """

    cursor = conn.cursor()
    cursor.execute(create_trainer_table_sql)
    cursor.execute(create_pokemon_table_sql)

# Fonction pour insérer les données dans les tables
def insert_card_data(conn, card_data):
    """Insère les données d'une carte dans la table appropriée."""
    if card_data["categorie_carte"] == "Trainer":
        insert_sql = """
        INSERT INTO trainer_cards (url_source, categorie_carte, name, image_url, set_number_id, card_number, artist)
        VALUES (?, ?, ?, ?, ?, ?, ?)
        """
        cursor = conn.cursor()
        cursor.execute(insert_sql, (
            card_data.get("url_source"),
            card_data.get("categorie_carte"),
            card_data.get("name"),
            card_data.get("image_url"),
            card_data.get("set_number_id"),
            card_data.get("card_number"),
            card_data.get("artist")
        ))
    elif card_data["categorie_carte"] == "Pokémon":
        insert_sql = """
        INSERT INTO pokemon_cards (url_source, categorie_carte, name, image_url, set_number_id, card_number, artist, Stage_devolution, Pre_evolution, type, hp, faiblesse, retrait, Nom_attaque_1, Cout_attaque_1, Degat_attaque_1, Nom_attaque_2, Cout_attaque_2, Degat_attaque_2)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """
        cursor = conn.cursor()
        cursor.execute(insert_sql, (
            card_data.get("url_source"),
            card_data.get("categorie_carte"),
            card_data.get("name"),
            card_data.get("image_url"),
            card_data.get("set_number_id"),
            card_data.get("card_number"),
            card_data.get("artist"),
            card_data.get("Stage_devolution", "Inconnu"),
            card_data.get("Pre_evolution", "Inconnu"),
            card_data.get("type", "Inconnu"),
            card_data.get("hp", 0),
            card_data.get("faiblesse", "Inconnu"),
            card_data.get("retrait", 0),
            card_data.get("Nom_attaque_1", "Inconnu"),
            card_data.get("Cout_attaque_1", "Inconnu"),
            card_data.get("Degat_attaque_1", 0),
            card_data.get("Nom_attaque_2", "Inconnu"),
            card_data.get("Cout_attaque_2", "Inconnu"),
            card_data.get("Degat_attaque_2", "Inconnu")
        ))
    conn.commit()

# Fonction principale pour lire les fichiers JSON et insérer les données dans la base de données
def main():
    db_file = "tournament_data.db"
    conn = create_connection(db_file)
    create_tables(conn)

    for file_name in os.listdir(json_folder_path):
        if file_name.endswith('.json'):
            file_path = os.path.join(json_folder_path, file_name)
            try:
                with open(file_path, 'r', encoding='utf-8') as file:
                    card_data = json.load(file)
                    print(f"Processing file: {file_name}")  # Debugging line
                    print(card_data)  # Debugging line
                    insert_card_data(conn, card_data)
            except Exception as e:
                print(f"Erreur lors de la lecture du fichier {file_path}: {e}")

    conn.close()

if __name__ == "__main__":
    main()
