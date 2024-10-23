from flask import Flask, render_template, request, redirect, url_for, flash
import pandas as pd
import random

app = Flask(__name__)
app.secret_key = '#lifecrazy'  # Required for flash messages

# Load player data from CSV
player_data = pd.read_csv('best3ptplayers.csv')  # Adjust the path to your CSV file
player_names = player_data['PLAYER_NAME'].str.strip().str.lower().tolist()  # Normalize player names
fg3_rating = player_data['3PT_RATING']

# Home route to render the form page
@app.route('/')
def index():
    return render_template('index.html')


#
@app.route('/simulate', methods=['POST'])
def simulate():

    player_inputs = [
        request.form.get('player1'),
        request.form.get('player2'),
        request.form.get('player3'),
        request.form.get('player4'),
        request.form.get('player5'),
        request.form.get('player6')
    ]


    normalized_inputs = [name.strip().lower() for name in player_inputs]


    invalid_players = [name for name in normalized_inputs if name not in player_names]

    if invalid_players:
        # Flash error message for invalid players
        flash(f"Invalid player names: {', '.join(invalid_players)}. Please enter valid player names from the list.")
        return redirect(url_for('index'))

    results = {}  # Dictionary to store rack-by-rack results for each player
    scores = {}  # Dictionary to store the total score for each player

    #Simulate the 3-point contest for each player
    for player_name in normalized_inputs:
        racks = []
        total_score = 0
        player_row = player_data[player_data['PLAYER_NAME'].str.strip().str.lower() == player_name]

        # Make sure we get a scalar value for the 3PT_RATING
        fg3_rating = player_row['3PT_RATING'].item()
        for rack in range(5):  # Assume 5 racks of shots
            print(f"\n{player_name} is shooting on rack {rack + 1} now")
            made_this_rack = sum(1 for _ in range(5) if random.randint(75, 450) < fg3_rating)
            total_score += made_this_rack  # Add the rack score to total
            racks.append(f"{player_name} made {made_this_rack} shots in rack {rack + 1}")
        results[player_name] = racks
        scores[player_name] = total_score


    winner = max(scores, key=scores.get)
    winner_score = scores[winner]


    return render_template('results.html', results=results, winner=winner, winner_score=winner_score)


if __name__ == '__main__':
    app.run(debug=True)
