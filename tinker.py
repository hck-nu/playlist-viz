import json

song_ids = []
with open('songs.json') as json_data:
    d = json.load(json_data)
    for item in d['items']:
        song_ids.append(item['track']['id'])

#print(song_ids)

feature_ids = {}
with open('features.json') as json_data:
    f = json.load(json_data)
    for feature in f['audio_features']:
        feature_ids['danceability'] = feature_ids.get('danceability',[])
        feature_ids['danceability'].append(feature['danceability']*100)

        feature_ids['energy'] = feature_ids.get('energy',[])
        feature_ids['energy'].append(feature['energy']*100)

        feature_ids['speechiness'] = feature_ids.get('speechiness',[])
        feature_ids['speechiness'].append(feature['speechiness']*100)

        feature_ids['liveness'] = feature_ids.get('liveness',[])
        feature_ids['liveness'].append(feature['liveness']*100)

        feature_ids['valence'] = feature_ids.get('valence',[])
        feature_ids['valence'].append(feature['valence']*100)

    avgs = {}

    for k,v in feature_ids.items():
        sum = 0
        for val in v:
            sum += val
        avgs[k] = sum/len(v)

    print (avgs)






# danceability, energy, speechiness, acousticness, instrumentalness, liveness, valence
