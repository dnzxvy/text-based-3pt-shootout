from nba_api.stats.endpoints import LeagueDashPlayerStats

import time
import random
import sys

# Fetch league-wide player statistics for the 2023-24 season
league_stats = LeagueDashPlayerStats(season='2023-24').get_data_frames()[0]


print("Available columns in the DataFrame:")
print(league_stats.columns)


print("\nFirst few rows of player statistics:")
print(league_stats.head())

# Filter players who have made more than 50 three-pointers
df_filtered_players = league_stats[league_stats['FG3M'] > 50].copy()  # Make a copy to avoid SettingWithCopyWarning


df_filtered_players.loc[:, '3PT_RATING'] = (df_filtered_players['FG3M'] + df_filtered_players['FG3A'] + df_filtered_players['FG3_PCT']) / 3


the_best_shooters = df_filtered_players.sort_values(by='FG3M', ascending=False).head(200)

# Display the results
print("\nPlayers with more than 50 3-POINTERS:")
print(the_best_shooters[['PLAYER_NAME', 'FG3M', 'FG3A', 'FG3_PCT', '3PT_RATING']])

# Save the filtered data to a CSV file
the_best_shooters.to_csv('best3ptplayers.csv', index=False)
print("\nLeague player stats saved to 'best3ptplayers.csv'")


def delay_print(s):
    # print one character at a time
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.20)


def simulate_contest(player_name, fg3_rating, num_shots=5):
    print(f"\n{player_name} is taking {num_shots} shots...")

    score = 0
    streak_modifier = 0
    for rack in range(num_shots):

        print(f"\n{player_name} is shooting on rack {rack + 1} now")


        made_this_rack = sum(1 for _ in range(5) if random.randint(75, 450) < fg3_rating)
        score += made_this_rack
        totalshots = num_shots * 5
        delay_print(f"Made {made_this_rack} shots this rack \n")
    print(f"{player_name} finished with a score of {score}/{totalshots}")
    return score

scores ={}
entered_players = []

for i in range(5):
    while True:
        player_name_input = input(f"Enter a player name for player {i+1}: ").strip().lower()

        matched_player = None
        for _, player in the_best_shooters.iterrows():
            if player['PLAYER_NAME'].strip().lower() == player_name_input:
                matched_player = player
                break

        if matched_player is not None:
            print(f"{matched_player['PLAYER_NAME']} is entered into the 3 Point Shootout")
            entered_players.append(matched_player) #adds the player
            break
        else:
            print("player not found. please enter a valid player name.")


for player in entered_players:
    player_name = player['PLAYER_NAME']
    fg3_rating = player['3PT_RATING']

    scores[player_name] = simulate_contest(player_name, fg3_rating)


winner = max(scores, key=scores.get)
print(f"\nThe winner of the 3-point contest is {winner} with {scores[winner]} points!")