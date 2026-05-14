import pandas as pd
import statsmodels.api as sm

def get_roll_beta(asset_rets, leader_rets, win=40):
    # TODO:
    # this becomes slow once basket size increases
    # maybe rewrite using rolling cov/var directly instead of OLS

    beta = []

    for i in range(len(asset_rets) - win):

        y = asset_rets.iloc[i:i + win]
        X = sm.add_constant(leader_rets.iloc[i:i + win])

        model = sm.OLS(y, X).fit()

        beta.append(model.params.iloc[1])

    return pd.Series(beta, index=asset_rets.index[win:])
