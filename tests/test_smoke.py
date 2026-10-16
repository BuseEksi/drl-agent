import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from agents import make_agent
from envs import make_env
from scripts.evaluate import evaluate


def test_random_agent_runs_on_cartpole():
    env = make_env("CartPole-v1")
    agent = make_agent("random", env.observation_space, env.action_space)
    rets = evaluate(agent, env, seeds=[1000, 1001])
    assert len(rets) == 2


def test_fixed_seed_gives_same_start():
    env = make_env("CartPole-v1")
    a, _ = env.reset(seed=1000)
    b, _ = env.reset(seed=1000)
    assert (a == b).all()
