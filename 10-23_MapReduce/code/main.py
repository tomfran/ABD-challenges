from dataset import load_dataset
from revisited_map_reduce import *
import matplotlib.pyplot as plt
import pandas as pd
from pprint import pprint

if __name__ == "__main__":
    # load dataset
    user_range = 30

    ll = load_dataset(user_range = user_range, track_range = 10, count_range = 10)

    mean_ll = [compute_mean(l) for l in ll]


    pprint(mean_ll)

    # Visualization
    df = pd.DataFrame(mean_ll)
    df.columns=['User','Average']

    if(user_range <= 30):
        ax = plt.subplot(1, 2, 1)
        df.hist(ax = ax, figsize=(14,7))
        plt.title("Average histogram")
        # Use only in case of small number of users
        ax = plt.subplot(1, 2, 2)
        df.plot.bar(x = 'User', y = 'Average', ax = ax, figsize=(14,7), legend = False)
        plt.title("Average per users")
    else:
        df.hist(figsize=(14,7))
        plt.title("Average histogram")

    plt.show()
