import pandas as pd

def get_adj_matrix(rets, win=120):
    # shorter windows were too noisy intraday
    # especially during open / post-news bursts
    return rets.rolling(win).corr()


def get_leader(adj):
    # crude proxy for now, whichever contract stays most connected to the basket
    # ES kept dominating during most macro sessions in testing
    avg_corr = adj.mean()

    if isinstance(avg_corr, pd.DataFrame):
        avg_corr = avg_corr.mean()

    return avg_corr.idxmax()