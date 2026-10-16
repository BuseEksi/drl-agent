"""Ortak değerlendirme: tüm ajanlar aynı sabit seed'li test setinde ölçülür.

Örnek:
    python scripts/evaluate.py --agent random --env CartPole-v1 --episodes 20
"""
import argparse
import os
import sys

import numpy as np
import yaml

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from agents import make_agent  # noqa: E402
from envs import make_env  # noqa: E402


def evaluate(agent, env, seeds):
    returns = []
    for s in seeds:
        obs, _ = env.reset(seed=int(s))   # sabit seed -> sabit harita
        done, ret = False, 0.0
        while not done:
            obs, r, term, trunc, _ = env.step(agent.act(obs, explore=False))
            ret += r
            done = term or trunc
        returns.append(ret)
    return np.array(returns)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--config", default="configs/default.yaml")
    ap.add_argument("--agent", required=True)
    ap.add_argument("--env", default=None)
    ap.add_argument("--model", default=None, help="Yüklenecek model dosyası")
    ap.add_argument("--episodes", type=int, default=None)
    args = ap.parse_args()

    with open(args.config) as f:
        cfg = yaml.safe_load(f)
    env_name = args.env or cfg["env"]["name"]
    n = args.episodes or cfg["eval"]["episodes"]
    start = cfg["eval"]["map_seeds_start"]
    seeds = range(start, start + n)

    env = make_env(env_name)
    agent = make_agent(args.agent, env.observation_space, env.action_space, cfg["agents"].get(args.agent, {}))
    if args.model:
        agent.load(args.model)
    rets = evaluate(agent, env, seeds)
    print(f"{args.agent} @ {env_name}: {rets.mean():.2f} ± {rets.std():.2f} ({len(rets)} bölüm, seed {start}..{start+n-1})")


if __name__ == "__main__":
    main()
