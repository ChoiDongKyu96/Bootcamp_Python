# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    HowManyMedals.py                                   :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: dochoi <dochoi@student.42seoul.kr>         +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/04/28 02:10:59 by dochoi            #+#    #+#              #
#    Updated: 2020/04/28 17:04:04 by dochoi           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import pandas as pd
from FileLoader import FileLoader

def howManyMedals(df, name):
    di = {}
    temp = df.loc[(df['Name']==name)][['Year', 'Medal']].dropna(axis=0)
    medals = temp.groupby(['Year','Medal']).size().reset_index(name='Count')
    for i in range(medals.shape[0]):
        if medals['Year'][i] not in di.keys():
            di[medals['Year'][i]] = {
            "G": 0,
            "S": 0,
            "B": 0
            }
        di[medals['Year'][i]][medals['Medal'][i][0]] += medals['Count'][i]
    return di


loader =FileLoader()
data = loader.load("../resources/athlete_events.csv")
print(howManyMedals(data, "Kjetil Andr Aamodt"))
