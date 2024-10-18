from nba_api.stats.endpoints import LeagueDashPlayerStats
import pandas as pd

# Fetch league-wide player statistics for the 2023-24 season
league_stats = LeagueDashPlayerStats(season='2023-24').get_data_frames()[0]

# Check available columns
print("Available columns in the DataFrame:")
print(league_stats.columns)

# Display the first few rows of player statistics
print("\nFirst few rows of player statistics:")
print(league_stats.head())

# Filter players who have made more than 50 three-pointers
df_filtered_players = league_stats[league_stats['FG3M'] > 50].copy()  # Make a copy to avoid SettingWithCopyWarning

# Calculate a new column safely using .loc
df_filtered_players.loc[:, '3PT_RATING'] = (df_filtered_players['FG3M'] + df_filtered_players['FG3A'] + df_filtered_players['FG3_PCT']) / 3

# Sort the players by three-point makes and get the top 5
the_best_shooters = df_filtered_players.sort_values(by='FG3M', ascending=False).head(200)

# Display the results
print("\nPlayers with more than 50 3-POINTERS:")
print(the_best_shooters[['PLAYER_NAME', 'FG3M', 'FG3A', 'FG3_PCT', '3PT_RATING']])

# Save the filtered data to a CSV file
the_best_shooters.to_csv('best3ptplayers.csv', index=False)
print("\nLeague player stats saved to 'best3ptplayers.csv'")
