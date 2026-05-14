import numpy as np
from tick.hawkes import HawkesExpKern

def check_hawkes(events, leader='ES'):
    # decay still needs proper calibration
    # but ES/NQ reacted differently enough that fixed decay felt wrong

    decay = 0.8 if leader == 'ES' else 1.1

    learner = HawkesExpKern(decay=decay, verbose=False)
    learner.fit(events.reshape(-1, 1))

    base = learner.baseline[0]
    curr = learner.intensity(events[-1:])[0]

    thr = base * 1.8

    return curr, base, curr > thr