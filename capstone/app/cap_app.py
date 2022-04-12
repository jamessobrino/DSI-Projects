import streamlit as st
import pandas as pd
import numpy as np

from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.metrics import accuracy_score

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout, GRU, LSTM
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.preprocessing.sequence import TimeseriesGenerator
from tensorflow.keras.wrappers.scikit_learn import KerasRegressor
from tensorflow.keras.callbacks import EarlyStopping

df = pd.read_csv('./data/player_game_data.csv')
df['GAME_DATE_EST'] = pd.to_datetime(df['GAME_DATE_EST'])
df = df.set_index('GAME_DATE_EST')
df.dropna(inplace= True)
df.sort_index(inplace= True)

df= df[['PLAYER_NAME', 'PLAYER_ID','GAME_ID', 'SEASON','FGM','FGA','FG_PCT','FG3M',
'FG3A','FG3_PCT','FTM','FTA','FT_PCT','OREB','DREB','REB','AST','STL','BLK','TNO','PF','PTS',
'PLUS_MINUS','SECONDS','FTSY_PTS']]

st.title('NBA Fantasy Predictor')

start = st.text_input("What is the first day of the week?")
end = st.text_input("What is the last day of the week?")
date_range= pd.date_range(start= start, end = end)

player_lst = []
count = 0
roster_size = int(st.text_input("How many players are on your roster?"))
for i in range(roster_size):
    player_lst.append(st.text_input("Type a player's name here.", key= count))
    count += 1
player_df= pd.DataFrame()


for player in player_lst:
        data_df = df.loc[df['PLAYER_NAME'] == player]
        data_df = data_df.iloc[:,4:-1].rolling(window=5).mean()
        data_df['FTSY_PTS'] = df.loc[df['PLAYER_NAME']== player]['FTSY_PTS']
        data_df.dropna(inplace= True)

        output_lst = []

        for day in date_range:
            if day in data_df.index:
                X_train = data_df.loc['2015-10-02': day].drop(columns= 'FTSY_PTS')
                X_train = X_train[:-1]
                y_train = data_df.loc['2015-10-02': day]['FTSY_PTS']
                y_train = y_train[:-1]

                day_ind = data_df.index.get_loc(day)
                X_test = data_df.iloc[[day_ind,day_ind+1]].drop(columns = 'FTSY_PTS')
                y_test = data_df.iloc[[day_ind,day_ind+1]]['FTSY_PTS']

                ss = StandardScaler()
                X_train_sc = ss.fit_transform(X_train)
                X_test_sc = ss.transform(X_test)

                train_seq = TimeseriesGenerator(X_train_sc, y_train, length=1, batch_size=64)
                test_seq = TimeseriesGenerator(X_test_sc, y_test, length = 1, batch_size=64)

                model = Sequential()

                model.add(LSTM(64, input_shape=(1,20), return_sequences=True))
                model.add(LSTM(32, return_sequences=False))

                model.add(Dense(32, activation= 'relu'))
                model.add(Dropout(.1))

                model.add(Dense(8, activation= 'relu'))
                model.add(Dropout(.1))

                model.add(Dense(2))
                model.compile(optimizer='adam', loss= 'mse', metrics= ['mae'])

                early_stop = EarlyStopping(patience = 5, restore_best_weights=True)

                history=model.fit(train_seq, epochs=100, validation_data=test_seq,
                                  verbose=1, callbacks = [early_stop])

                output = model.predict(train_seq)
                output_lst.append(output[0][0])
        row = pd.Series(output_lst)
        player_df = player_df.append(row, ignore_index= True)
player_df.index = player_lst

st.write(player_df)
