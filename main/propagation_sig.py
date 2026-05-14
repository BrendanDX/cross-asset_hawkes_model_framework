import pandas as pd

def find_laggards(asset_rets, betas, leader_rets):
    # concept: after strong leader movement, weaker contracts tend to catch up
    # assumes propagation happens relatively quickly though, probably breaks in slower/choppier regimes

    aligned_mkt = leader_rets.loc[betas.index]
    aligned_asset = asset_rets.loc[betas.index]

    expected = betas * aligned_mkt

    residual = aligned_asset - expected

    # zscoring residuals probs will have too sparse signals
    return residual < 0
