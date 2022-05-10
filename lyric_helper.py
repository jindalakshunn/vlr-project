import numpy as np
import pickle

def track_id_to_lyric_embedding(track_id,embedding_loader):
    track_id_embedding_dict = embedding_loader.track_id_embedding_dict

    if track_id in track_id_embedding_dict:
        return track_id_embedding_dict[track_id]
    
    assert(False)


def get_all_track_id_lyrics(embedding_loader):
    
    return embedding_loader.get_all_track_id_lyrics

