# RL Keşif Projesi: Kısmi Gözlemlenebilir Ortamda Otonom Keşif

4 farklı RL algoritması (Double DQN, A2C, PPO, SAC) aynı ortamda eğitilip karşılaştırılır.
Baseline'lar: random ve frontier-based keşif.

## Kurulum
```bash
python -m venv .venv
# Windows:  .venv\Scripts\activate
# macOS/Linux:  source .venv/bin/activate
pip install -r requirements.txt
```

## Hızlı test (pipeline çalışıyor mu?)
```bash
pytest -q
python scripts/train.py --agent random --env CartPole-v1 --steps 5000 --seed 0
python scripts/evaluate.py --agent random --env CartPole-v1 --episodes 20
```

## Klasör yapısı
| Klasör | İçerik | Sahibi |
|---|---|---|
| `envs/` | Explore-v0 ortamı, harita üreteci | Kişi 1 |
| `agents/` | Ortak `Agent` arayüzü ve her algoritma | Herkes kendi dosyası |
| `baselines/` | Frontier-based baseline | Kişi 2 |
| `common/` | Seed, loglama | Kişi 3 |
| `configs/` | YAML ayarları | Ortak |
| `scripts/` | `train.py`, `evaluate.py` | Kişi 3 / Kişi 2 |
| `results/` | Eğitim çıktıları (repoya girmez) | |
| `report/` | Rapor ve grafikler | Kişi 4 |
| `docs/` | Ortam tasarım dokümanı | Ortak |

## Yeni ajan ekleme
1. `agents/<isim>.py` içinde `Agent` sınıfından türet (`act`, `observe`, `update`, `save`, `load`).
2. `agents/__init__.py` içindeki `REGISTRY`'ye ekle.
3. `configs/default.yaml` altında `agents.<isim>` bölümüne hyperparameter'ları yaz.
4. Önce CartPole'da, sonra Explore-v0'da dene.

Çalışma kuralları için `CONTRIBUTING.md`'ye bakın.
