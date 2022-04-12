# Fantasy Basketball Predictor

### Problem Statement
---------------------
I dont have the time nor energy to study up on fantasy basketball and change lineups daily. This project aims to produce a model that can accurately predict an NBA player's fantasy output in a given date range.

### Motivation
--------------
I enjoy watching sports, specifically basketball. My friends like to play fantasy sports and spend significantly more time researching which players will be a better for their team compared to a similar player. While I enjoy reading up on players and projections for the season, my friends have a much deeper understanding of how to pick their players for their team. Normally I could care less about who wins the league each year, but my "friends" Are now using fantasy basketball to siphon money from me in a "winner take all" prize pool. Knowing that I dont have the deeper knowledge nor time necessary to continuously update my fantasy team, I've turned to machine learning to lead me to a first place fantasy basketball finish.

### Methods
-------------
This project has had many ups and downs, I found a kaggle data set <https://www.kaggle.com/nathanlauga/nba-games> with NBA player data for seasons 2004-2020. I thought I could create a model that took in the rolling average of player outputs for the past couple of games and return a fantasy projection for the next game. I used two different models, a recurrent nueral network with GRU activation layer and another recurrent nerual network with a LSTM activation layer. The LSTM model performed slightly better so I uesd that model for the next step of my project.

Once I had my model I used the  [Streamlit](https://docs.streamlit.io/library/get-started) library to make an small app. This app took 2 dates as inputs for a date range, an interger specifying how many players you would like to run through the model, and the names of players to run through the model. I was suprised how Streamlit was so simple and easy to use and was able to make the app a quite quickly. The app output a dataframe with the players as the index and the fantasy predictions for the games in the date range.

<img src = './Images/Screen Shot 2021-11-21 at 10.53.30 PM.png' width = '550'>
<img src = './Images/Screen Shot 2021-11-22 at 12.24.08 AM.png' width = '550'>

### Results
-------------
In the end my model was not very good. My model only recieved the player outputs from previous games and lacked a lot of indepth insight that I wish I could have added. The next iteration of this project will be scraping more indepth data to feed the model. Data would include: player specific plays (such as pick and roll), team defensive stats (pick and roll defense, opponets 3pt field goal percentage), usage rates, ect. For instance, while playing on the Houston Rockets, James Harden ran a lot of pick and roll plays. If a team defended that specific play very well, I predict Harden would score less from pick and rolls that game. 