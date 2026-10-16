"""Otonom keşif ortamı (Explore-v0). SAHİBİ: Kişi 1.

Önce docs/design_doc.md içinde gözlem, aksiyon, ödül ve bitiş koşulunu ekipçe kararlaştırın,
sonra burayı doldurun. Aşağıdaki iskelet sadece Gymnasium arayüzünün şeklini gösterir.
Ortam 8 Kasım'da dondurulacak: sonrasında değişiklik ancak ortak kararla.
"""
import gymnasium as gym


class ExploreEnv(gym.Env):
    metadata = {"render_modes": ["rgb_array"]}

    def __init__(self, map_size: int = 20, max_steps: int = 500, render_mode=None):
        super().__init__()
        self.map_size = map_size
        self.max_steps = max_steps
        self.render_mode = render_mode
        # TODO (Kişi 1): self.observation_space ve self.action_space tanımla
        #   Öneri aksiyon: Discrete(4)  -> ileri, sol, sağ, bekle
        #   Öneri gözlem: lidar ışın mesafeleri + yerel keşif haritası kesiti

    def reset(self, *, seed=None, options=None):
        super().reset(seed=seed)
        # TODO: seed'e göre harita üret, ajanı yerleştir, ilk gözlemi döndür
        raise NotImplementedError

    def step(self, action):
        # TODO: hareket, sensör güncelle, ödül hesapla, bitiş koşullarını kontrol et
        raise NotImplementedError

    def render(self):
        # TODO: Matplotlib/NumPy ile rgb_array döndür (GIF için)
        raise NotImplementedError
