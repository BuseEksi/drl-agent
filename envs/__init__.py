import gymnasium as gym


def make_env(name: str, **kwargs):
    """Ortam fabrikası. Explore-v0 hazır olana kadar CartPole gibi hazır ortamlarla pipeline'ı sınayın."""
    if name == "Explore-v0":
        from envs.explore_env import ExploreEnv
        return ExploreEnv(**kwargs)
    return gym.make(name, **kwargs)
