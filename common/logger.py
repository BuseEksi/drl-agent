import csv
import os


class CSVLogger:
    """Her bölüm (episode) sonunda bir satır yazar. Tüm algoritmalar aynı formatı kullanır."""

    FIELDS = ["episode", "env_steps", "return", "length"]

    def __init__(self, out_dir: str):
        os.makedirs(out_dir, exist_ok=True)
        self.path = os.path.join(out_dir, "metrics.csv")
        self._f = open(self.path, "w", newline="")
        self._w = csv.DictWriter(self._f, fieldnames=self.FIELDS)
        self._w.writeheader()

    def log_episode(self, episode: int, env_steps: int, ret: float, length: int) -> None:
        self._w.writerow({"episode": episode, "env_steps": env_steps, "return": ret, "length": length})
        self._f.flush()

    def close(self) -> None:
        self._f.close()
