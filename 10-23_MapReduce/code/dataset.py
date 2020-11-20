from random import randint
from pprint import pprint

def dataset_generation(user_range = 50, track_range = 100, count_range = 10):
    '''
    Dataset generation for the challenge.
    Can specify how many users, tracks, and the max value for the count.

    Note: generation made with the simple rand list comprehension lead to 
    duplicates of userid-trackid
    '''
    ll = []
    for i in range(user_range):
        dd = {}
        dd['User_id'] = f"User{i}"
        for k in range(track_range):
            dd[f"Track{k}"] = randint(0,count_range)
        ll.append(dd)

    with open("../data/dataset.txt", "w+") as f:
        f.write(str(ll))
    return ll
    
def load_dataset(user_range = 50, track_range = 100, count_range = 10):
    '''
    Load the dataset or generate it if not found.
    '''
    try:
        with open('../data/dataset.txt') as f:
            return eval(f.read())
    except FileNotFoundError:
        return dataset_generation(user_range, track_range, count_range)