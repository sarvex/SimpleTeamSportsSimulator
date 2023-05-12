# Copyright (C) 2020 Electronic Arts Inc.  All rights reserved.

import random
from sts2.environment import STS2Environment


def naive_action(obs):
    return {
        v: {
            'action': 'NONE',
            'input': [random.uniform(-1, 1), random.uniform(-1, 1)],
        }
        for k, v in obs.items()
        if isinstance(v, str) and "_ai_" in v
    }


if __name__ == "__main__":
    env = STS2Environment(num_home_players=3,
                          num_away_players=3,
                          num_home_agents=2,
                          num_away_agents=2,
                          with_pygame=True)
    obs, info = env.reset()
    while True:
        action = naive_action(obs)
        obs, r, done, info = env.step(action)
        env.render()

        if done: break
