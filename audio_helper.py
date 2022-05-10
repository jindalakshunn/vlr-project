import torch
import numpy as np

def track_id_to_audio_embedding(track_id,embedding_loader):
    feats = embedding_loader.feats
    song_list = embedding_loader.song_list
    search = [i for i,song_name in enumerate(song_list) if track_id in song_name]
    
    if (len(search)==0):
        print('song not found')
        assert(False)
    elif len(search)>1:
        print(track_id)
        for i in range(len(search)):
            print(song_list[search[i]])
        print('too many songs found')
        
    idx = search[0]
    return feats[idx]

def track_id_to_filename(track_id,embedding_loader):
    song_list = embedding_loader.song_list

    search = [song_name for i,song_name in enumerate(song_list) if track_id in song_name]
    if (len(search)==0):
        print('song not found')
        assert(False)
    elif len(search)>1:
        print(track_id)
        print(search)
        print('too many songs found')
    return search[0]

def song_to_track_id(path):
    #'aa'.split('b') == ['aa']
    return path.split('/')[-1].split('_')[-1].replace('.mp3', '')
    
    
import glob
def get_all_track_id_audio():
    song_paths = glob.glob('vlr-dataset/song_previews/*.mp3')
    song_paths.sort()
    return [song_to_track_id(x) for x in song_paths]

def get_intersection_track_id(tl1,tl2):
    return list(set(tl1).intersection(set(tl2)))