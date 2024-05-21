import requests
import csv

url = "https://tennisapi1.p.rapidapi.com/api/tennis/rankings/atp/live"
headers = {
    "X-RapidAPI-Key": "450b34affcmsh6f8896825ede163p10b618jsn51953d493a05",
    "X-RapidAPI-Host": "tennisapi1.p.rapidapi.com"
}
params = {
    'formatType': 'odi'
}

response = requests.get(url, headers=headers)

if response.status_code == 200:
    print("Connection made")
    data = response.json().get('rankings', [])  # Extracting the 'rankings' data
    csv_filename = 'tennis_player_rankings.csv'

    if data:
        field_names = ['player_name', 'rank', 'country_name', 'points']  # Specify required field names

        # Write data to CSV file with only specified field names
        with open(csv_filename, 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=field_names)
            writer.writeheader()
            for entry in data:
                # Extracting required fields
                team = entry.get('team', {})
                country = team.get('country', {})
                
                
                row = {
                    'player_name': entry.get('rowName', 'N/A'),  # Player name
                    'rank': team.get('ranking', 'N/A'),  # Player rank
                    'country_name': country.get('name', 'N/A'),  # Country name
                    'points': entry.get('points', 'N/A')  # Points
                }
                writer.writerow(row)

        print(f"Data fetched successfully and written to '{csv_filename}'")
    else:
        print("No data available from the API.")
else:
    print("Failed to fetch data:", response.status_code)

