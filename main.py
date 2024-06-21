from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

# Replace with your actual TBA API key
TBA_API_KEY = '9AMhff0rvpZKV8DrjVepfs7FckKftiVy7odokTeT8SeAaIpjPAwwrWDUE2e8XkAj'
TBA_BASE_URL = 'https://www.thebluealliance.com/api/v3'

headers = {
    'X-TBA-Auth-Key': TBA_API_KEY
}

def get_team_events(team):
    url = f"{TBA_BASE_URL}/team/{team}/events"
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.HTTPError as http_err:
        if response.status_code == 404:
            print(f"Team {team} not found at {url}")
            return []
        else:
            print(f"HTTP error occurred: {http_err}")
            return []
    except Exception as err:
        print(f"An error occurred: {err}")
        return []

def get_event_matches(event_key):
    url = f"{TBA_BASE_URL}/event/{event_key}/matches"
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    return response.json()

def find_matches_with_teams(team1, team2):
    events1 = get_team_events(team1)
    events2 = get_team_events(team2)
    
    if not events1 or not events2:
        return []
    
    # Find common events
    common_events = {event['key'] for event in events1}.intersection(
        {event['key'] for event in events2}
    )
    
    matches_with_both_teams = []
    
    for event in common_events:
        matches = get_event_matches(event)
        for match in matches:
            if team1 in match['alliances']['red']['team_keys'] and team2 in match['alliances']['red']['team_keys']:
                matches_with_both_teams.append(match)
            elif team1 in match['alliances']['blue']['team_keys'] and team2 in match['alliances']['blue']['team_keys']:
                matches_with_both_teams.append(match)
            elif (team1 in match['alliances']['red']['team_keys'] and team2 in match['alliances']['blue']['team_keys']) or (team1 in match['alliances']['blue']['team_keys'] and team2 in match['alliances']['red']['team_keys']):
                matches_with_both_teams.append(match)
    
    return matches_with_both_teams

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/find_matches', methods=['POST'])
def find_matches():
    team1 = request.form.get('team1')
    team2 = request.form.get('team2')
    # append frc to both team names
    team1 = f"frc{team1}"
    team2 = f"frc{team2}"
    matches = find_matches_with_teams(team1, team2)
    return jsonify(matches)

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=8080)