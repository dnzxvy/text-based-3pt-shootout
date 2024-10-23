# text-based-3pt-shootout

This is a project made to simulate an NBA 3-Point contest.
I achieved this using the nba_api by swar https://github.com/swar/nba_api. Also, i used the language Python to manage the backend of the project via Flask to actually simulate the game logic so that it can be printed onto the frontend (the html website)
with the nba_api, I fetched the league player stats for the 2023-24 season but this can be changed on the code to have stats from previous nba seasons
I then saved this information into a csv file where I then coded logic to find out the 3pt rating of these players by dividing their 3-pointer made, their 3-pointers attempted then dividing it by 3 which therfore gave me a new metric to measure the 3 point rating of the NBA players which I then added to a new row.

To run this you should download the best3ptplayers.csv file, the main.py file and the 3pointsim.py file
