from agents.base import Agent
from agents.random_agent import RandomAgent

# Her kişi kendi ajanını yazınca buraya ekler:
#   from agents.ddqn import DoubleDQNAgent   -> "ddqn": DoubleDQNAgent
REGISTRY = {
    "random": RandomAgent,
    # "ddqn": DoubleDQNAgent,   # Kişi 1
    # "a2c": A2CAgent,          # Kişi 2
    # "ppo": PPOAgent,          # Kişi 3
    # "sac": SACAgent,          # Kişi 4
}


def make_agent(name: str, observation_space, action_space, cfg=None, seed: int = 0) -> Agent:
    if name not in REGISTRY:
        raise KeyError(f"Bilinmeyen ajan '{name}'. Kayıtlı olanlar: {list(REGISTRY)}")
    return REGISTRY[name](observation_space, action_space, cfg or {}, seed)
