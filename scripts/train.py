"""Ortak eğitim döngüsü. Tüm algoritmalar bunu kullanır (bütçe = ortam adımı).

Örnek:
    python scripts/train.py --agent random --env CartPole-v1 --steps 5000 --seed 0
"""
import argparse
import os
import sys

import yaml

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from agents import make_agent  # noqa: E402
from common.logger import CSVLogger  # noqa: E402
from common.seeding import set_global_seed  # noqa: E402
from envs import make_env  # noqa: E402


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--config", default="configs/default.yaml")
    ap.add_argument("--agent", required=True)
    ap.add_argument("--env", default=None)
    ap.add_argument("--steps", type=int, default=None)
    ap.add_argument("--seed", type=int, default=0)
    ap.add_argument("--out", default="results")
    args = ap.parse_args()

    with open(args.config) as f:
        cfg = yaml.safe_load(f)
    env_name = args.env or cfg["env"]["name"]
    total_steps = args.steps or cfg["train"]["total_steps"]

    set_global_seed(args.seed)
    env = make_env(env_name)
    agent = make_agent(args.agent, env.observation_space, env.action_space,
                       cfg["agents"].get(args.agent, {}), args.seed)
    run_dir = os.path.join(args.out, f"{env_name}_{args.agent}_s{args.seed}")
    logger = CSVLogger(run_dir)

    obs, _ = env.reset(seed=args.seed)
    ep, ep_ret, ep_len = 0, 0.0, 0
    for step in range(1, total_steps + 1):
        action = agent.act(obs, explore=True)
        next_obs, reward, terminated, truncated, _ = env.step(action)
        agent.observe(obs, action, reward, next_obs, terminated, truncated)
        agent.update()
        obs = next_obs
        ep_ret += reward
        ep_len += 1
        if terminated or truncated:
            ep += 1
            logger.log_episode(ep, step, ep_ret, ep_len)
            if ep % cfg["train"]["log_every_episodes"] == 0:
                print(f"[{args.agent} s{args.seed}] ep {ep} step {step} return {ep_ret:.1f}")
            obs, _ = env.reset()
            ep_ret, ep_len = 0.0, 0

    agent.save(os.path.join(run_dir, "model.pt"))
    logger.close()
    print(f"Bitti. Sonuçlar: {run_dir}/metrics.csv")


if __name__ == "__main__":
    main()
