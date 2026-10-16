from abc import ABC, abstractmethod
from typing import Any, Dict


class Agent(ABC):
    """Tüm algoritmaların uyması gereken ortak arayüz.

    Eğitim döngüsü (scripts/train.py) her adımda sırayla şunu yapar:
        action = agent.act(obs)
        next_obs, reward, terminated, truncated, info = env.step(action)
        agent.observe(obs, action, reward, next_obs, terminated, truncated)
        metrics = agent.update()   # off-policy: her adım; on-policy: buffer dolunca, yoksa {} döner
    """

    def __init__(self, observation_space, action_space, cfg: Dict[str, Any], seed: int = 0):
        self.observation_space = observation_space
        self.action_space = action_space
        self.cfg = cfg
        self.seed = seed

    @abstractmethod
    def act(self, obs, explore: bool = True):
        """Gözlemden aksiyon seçer. Değerlendirmede explore=False çağrılır."""

    def observe(self, obs, action, reward, next_obs, terminated: bool, truncated: bool) -> None:
        """Geçişi buffer'a kaydeder. Öğrenmeyen ajanlar boş bırakabilir."""

    def update(self) -> Dict[str, float]:
        """Bir öğrenme adımı yapar, loglanacak metrikleri döndürür (ör. {'loss': 0.3})."""
        return {}

    def save(self, path: str) -> None:
        """Model ağırlıklarını kaydeder."""

    def load(self, path: str) -> None:
        """Model ağırlıklarını yükler."""
