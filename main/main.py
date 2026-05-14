from correlation_struc import get_adj_matrix, get_leader
from hawkes import check_hawkes
from beta_est import get_roll_beta
from propagation_sig import find_laggards

def run_model(df, events):

    adj = get_adj_matrix(df)

    leader = get_leader(adj)

    curr, base, active = check_hawkes(
        events,
        leader=leader
    )

    if not active:
        return None

    # remove extremes slightly
    leader_rets =df[leader].clip(-0.03, 0.03)

    betas = get_roll_beta(
        df['asset'],
        leader_rets
    )

    laggards =find_laggards(
        df['asset'],
        betas,
        leader_rets
    )

    latest_beta =betas.iloc[-1]

    # avoid bad low-beta setups
    if abs(latest_beta) < 0.2:
        return None

    # simple catch-up logic for now
    if laggards.iloc[-1]:
        return "BUY"

    return None