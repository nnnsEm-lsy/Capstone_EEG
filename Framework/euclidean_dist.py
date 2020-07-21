import pandas as pd
import numpy as np
import csv

import scipy
from scipy import spatial

mood = pd.read_csv("C:/Users/asus/Desktop/Mood_Coordinates.csv")
song_value = pd.read_csv("C:/Users/asus/Desktop/Harmonic_AV_test.csv")
'''
df_temp = mood.loc[:, ['Arousal','Valence']]
#print (song_value)
df_temp1 = song_value.loc[:, ['Arousal','Valence']]
#print (df_temp1)
df_n1 = mood.loc[:, ['Arousal','Valence']].to_numpy()
df_n2 = song_value.loc[:, ['Arousal','Valence']].to_numpy()


for x,y in df_n2:
    for a,b in df_n1:
        np.linalg.norm(df_n2[x][y] - df_n1[a][b])


import scipy
from scipy import spatial
ary = scipy.spatial.distance.cdist(mood.loc[:, ['Arousal','Valence']], song_value.loc[:, ['Arousal','Valence']], metric='euclidean')
#print (ary)
euclid = pd.DataFrame(ary)
#print (euclid)
'''

pairs_1 = list(tuple(zip(mood.Arousal, mood.Valence)))
pairs_2 = list(tuple(zip(song_value.Arousal, song_value.Valence)))

min_distances = []
closest_pairs = []
names = []
for i in pairs_2:
    min_dist = scipy.spatial.distance.cdist([i], pairs_1, metric='euclidean').min()
    index_min = scipy.spatial.distance.cdist([i], pairs_1, metric='euclidean').argmin()
    min_distances.append(min_dist)
    closest_pairs.append(mood.loc[index_min, ['Arousal', 'Valence']])
    names.append(mood.loc[index_min, 'Name'])
song_value['min_distance'] = min_distances
song_value['closest_pairs'] = [tuple(i.values) for i in closest_pairs]
song_value['name'] = names

print(song_value)