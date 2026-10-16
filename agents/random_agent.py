from agents.base import Agent


class RandomAgent(Agent):
    """Alt sınır baseline'ı: rastgele aksiyon."""

    def act(self, obs, explore: bool = True):
        return self.action_space.sample()
