import os
import json

# Folder where the JSON files are located
json_folder = "C:/Users/paper/Desktop/public_html/player_profiles"

# Template JSON structure
template = {
    "stats": {
        "gamesPlayed": "0",
        "wins": "0",
        "losses": "0",
        "winRate": "0%"
    },
    "lastGame": {
        "score": "NA",
        "opponent": "NA",
        "date": "NA"
    },
    "achievements": [
        {"title": "Top Rank", "description": "Challenger"},
        {"title": "Favorite Champion", "description": "Olaf"},
        {"title": "Jungle Main", "description": "1v9"},
        {"title": " ", "description": " "},
        {"title": "# of Bans", "description": "14"},
        {"title": " ", "description": " "},
        {"title": " ", "description": " "},
        {"title": " ", "description": " "}
    ],
    "schedule": [
        {"date": "03/12/2025", "opponent": "Team X", "result": "Win", "score": "30-22"},
        {"date": "03/15/2025", "opponent": "Team Y", "result": "Loss", "score": "28-30"}
    ]
}

# Ensure the folder exists
if not os.path.exists(json_folder):
    print(f"Error: The folder '{json_folder}' does not exist.")
    exit()

# Loop through all JSON files
for filename in os.listdir(json_folder):
    if filename.endswith(".json"):  # Process only JSON files
        file_path = os.path.join(json_folder, filename)

        # Extract name from filename and capitalize it properly
        name = filename.replace(".json", "").capitalize()

        # Create new JSON content
        new_data = {"name": name, **template}

        # Write updated content to the file
        with open(file_path, "w") as file:
            json.dump(new_data, file, indent=4)

print(f"✅ Updated all JSON files in '{json_folder}' successfully!")
