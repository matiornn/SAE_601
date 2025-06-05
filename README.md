![Pokemon TCG Pocket logo](https://upload.wikimedia.org/wikipedia/commons/c/c2/Pokemon_TCG_Pocket_logo.png)

# Pokemon TCG Pocket Metagame Analysis

[Pokémon Trading Card Game Pocket](https://en.wikipedia.org/wiki/Pok%C3%A9mon_Trading_Card_Game_Pocket) (often abbreviated as **Pokémon TCG Pocket**) is a free-to-play mobile adaptation of the [Pokémon Trading Card Game](https://en.wikipedia.org/wiki/Pok%C3%A9mon_Trading_Card_Game) (TCG), developed by [Creatures Inc.](https://en.wikipedia.org/wiki/Creatures_Inc.) and [DeNA](https://en.wikipedia.org/wiki/DeNA), and published by [The Pokémon Company](https://en.wikipedia.org/wiki/The_Pok%C3%A9mon_Company).

In this game, players build decks containing sets of cards and battle each other online.

## Goal

The goal of this project is to perform a metagame analysis of Pokémon TCG Pocket. This involves determining which cards have the highest win rates, identifying which cards work well together in the same deck, and finding effective strategies against popular decks. Additionally, we aim to track how these trends have evolved since the game's launch and uncover other useful patterns from the data.

## Data Collection

We scraped data from tournaments and player decklists available on [Limitless TCG](https://play.limitlesstcg.com). This data includes match results and deck compositions, which are essential for computing win rates and performing metagame analysis.

We have also scraped data from the cards themselves to enrich our analysis.

## Program for Win-Rate Retrieval

A program has been developed to calculate the win rates by deck. This program processes the collected data to provide insights into the performance of various decks in the current metagame.

## Database

We have created a SQLite database to store the collected and processed data. This database is designed to be easily integrated with Power BI for advanced data visualization and analysis.

## Data Visualization

For data visualization, we use Power BI to create insightful graphs and tables. These visualizations help showcase the findings from our data analysis, such as the most used cards per season, the cards with the highest win rates, and the usage and win rates of interesting cards over time.

## Deliverables

All data collection, transformation, and visualization code is published in a public Git repository. The repository includes detailed instructions on how to run each step of the process.

- The repository layout mirrors the structure of this project, with each step clearly separated.
- A README.md file explains how to run each step.
- Commit messages are clear and relevant.
- No secrets or sensitive information are shared publicly.
- The code is portable and can be easily run by the client.
